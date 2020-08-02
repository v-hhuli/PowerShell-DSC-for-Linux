#!/usr/bin/env python3
# ====================================
#  Copyright (c) Microsoft Corporation. All rights reserved.
# ====================================
"""Runtime module. Contains runtime base class and language specific runtime classes."""

import signal
import subprocess
import sys
import time
import os

import serializerfactory
import subprocessfactory
import tracer
from runbook import *
from workerexception import *

json = serializerfactory.get_serializer(sys.version_info)


def find_executable(executable, path=None):
    """Tries to find 'executable' in the directories listed in 'path'.
    A string listing directories separated by 'os.pathsep'; defaults to
    os.environ['PATH'].  Returns the complete filename or None if not found.
    """
    _, ext = os.path.splitext(executable)
    if (sys.platform == 'win32') and (ext != '.exe'):
        executable = executable + '.exe'

    if os.path.isfile(executable):
        return executable

    if path is None:
        path = os.environ.get('PATH', None)
        if path is None:
            try:
                path = os.confstr("CS_PATH")
            except (AttributeError, ValueError):
                # os.confstr() or CS_PATH is not available
                path = os.defpath
        # bpo-35755: Don't use os.defpath if the PATH environment variable is
        # set to an empty string

    # PATH='' doesn't match, whereas PATH=':' looks in the current directory
    if not path:
        return None

    paths = path.split(os.pathsep)
    for p in paths:
        f = os.path.join(p, executable)
        if os.path.isfile(f):
            # the file exists, we have a shot at spawn working
            return f
    return None

class Runtime(object):
    """Runtime base class."""

    def __init__(self, job_data, runbook):
        """
        :type job_data  : jrdsclient.JobData"
        :type runbook   : Runbook
        """
        # should be overwritten by language runtime
        self.execution_alias = None
        self.base_cmd = None

        # used for actual runtime
        self.runbook = runbook
        self.runbook_subprocess = None
        self.job_data = job_data

    def initialize(self):
        self.runbook.write_to_disk()

    def start_runbook_subprocess(self):
        """Creates the runbook subprocess based on the script language and using properties set by the derived class.

        Requires self.base_cmd & self.runbook_file_path to be set by derived class.
        """
        cmd = self.base_cmd + [self.runbook.runbook_file_path]
        job_parameters = self.job_data.parameters
        if job_parameters is not None and len(job_parameters) > 0:
            for parameter in job_parameters:
                tracer.log_debug_trace("Parameter is: \n" + str(parameter))
                if self.runbook.definition_kind_str == "PowerShell" and parameter["Name"]:
                    # Handle named parameters for PowerShell arriving out of order
                    cmd += ["-%s" % parameter["Name"]]
                cmd += [str(json.loads(parameter["Value"]))]

        # Do not copy current process env var to the sandbox process
        env = os.environ.copy()
        env.update({"AUTOMATION_JOB_ID": str(self.job_data.job_id),
                    "AUTOMATION_ACTIVITY_ID": str(tracer.u_activity_id),
                    "PYTHONPATH": str(configuration.get_source_directory_path()),
                    "HOME": str(os.getcwd())})  # windows env have to be str (not unicode)
        self.runbook_subprocess = subprocessfactory.create_subprocess(cmd=cmd,
                                                                      env=env,
                                                                      stdout=subprocess.PIPE,
                                                                      stderr=subprocess.PIPE)

    def kill_runbook_subprocess(self):
        """Attempts to kill the runbook subprocess.

        This method will attempt to kill the runbook subprocess [max_attempt_count] and will return if successful.

        Throws:
            SandboxRuntimeException : If runbook subprocess is still alive after [max_attempt_count].
        """
        attempt_count = 0
        max_attempt_count = 3
        while attempt_count < max_attempt_count:
            if self.runbook_subprocess is not None and self.runbook_subprocess.poll() is None:
                os.kill(self.runbook_subprocess.pid, signal.SIGTERM)
                runbook_proc_is_alive = self.is_process_alive(self.runbook_subprocess)
                if runbook_proc_is_alive is False:
                    return
                attempt_count += 1
                time.sleep(attempt_count)
            else:
                return
        raise SandboxRuntimeException()

    @staticmethod
    def is_process_alive(process):
        """Checks if the given process is still alive.

        Returns:
            boolean : True if the process [pid] is alive, False otherwise.
        """
        if process.poll() is None:
            return True
        else:
            return False

    def is_runtime_supported(self):
        """Validates that the OS supports the language runtime by testing the executable file path.

        Returns:
            True    : If executable exist.
            False   : Otherwise.
        """
        if find_executable(self.execution_alias) is None:
            return False
        else:
            return True


class PowerShellRuntime(Runtime):
    """PowerShell runtime derived class."""

    def __init__(self, job_data, runbook):
        Runtime.__init__(self, job_data, runbook)

        self.execution_alias = "pwsh"
        if linuxutil.is_posix_host() is False:
            self.execution_alias = "powershell"
            
        self.base_cmd = [self.execution_alias, "-File"]


class Python2Runtime(Runtime):
    """Python 2 runtime derived class."""

    def __init__(self, job_data, runbook):
        Runtime.__init__(self, job_data, runbook)
        self.execution_alias = "python2"

        if get_default_python_interpreter_major_version() == 2:
            self.execution_alias = "python"

        self.base_cmd = [self.execution_alias]


class Python3Runtime(Runtime):
    """Python 3 runtime derived class."""

    def __init__(self, job_data, runbook):
        Runtime.__init__(self, job_data, runbook)
        self.execution_alias = "python3"

        if get_default_python_interpreter_major_version() == 3:
            self.execution_alias = "python3"

        self.base_cmd = [self.execution_alias]


class BashRuntime(Runtime):
    """Bash runtime derived class."""

    def __init__(self, job_data, runbook):
        Runtime.__init__(self, job_data, runbook)
        self.execution_alias = "bash"

        self.base_cmd = [self.execution_alias]


def get_default_python_interpreter_major_version():
    """Return the default "python" alias interpreter version.

    Returns:
        int, the interpreter major version
        None, if the default interpreter version cannot be detected
    """
    cmd = ["python3", "-c", "import sys;print(sys.version[0])"]  # need to use print() for python3 compatibility
    p = subprocessfactory.create_subprocess(cmd=cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    default_interpreter_version, error = p.communicate()
    if p.returncode == 0:
        return int(default_interpreter_version.decode().strip())
    else:
        return None
