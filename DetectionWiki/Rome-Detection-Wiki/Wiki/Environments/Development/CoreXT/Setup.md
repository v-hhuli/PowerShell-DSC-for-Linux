# CoreXT Installation

Open  a command-prompt with Admin privileges and run the below:
1. *\\\reddog\public\build\bootstrap\install.cmd*
2. *\\\reddog\public\Build\GitCredentialManager\Setup.exe* (popup installer will show up, it takes time ~15m) 
3. Set an environment variable: NugetMachineInstallRoot=C:\cxCache
	- Run: SETX NugetMachineInstallRoot "C:\CxCache" /m
	- Run: SETX NugetMachineInstallRoot "C:\CxCache"

----

## Add Repository Root (May 2020)
For the most up to date version of this page, please [visit One Branch offial documentation](https://onebranch.visualstudio.com/Build/_wiki/wikis/Build.wiki/121/Initialize-Working-Directory).
This wiki page is useful in case the above is unavailable

Important: The working dir must be in after the root. e.g. C:\OneRepo

Concept: The "working directory" is the root directory that all of your repositories will be stored in on your machine. 
1. Create a directory you want to use as your working directory (e.g. md c:\OneRepo)
2. Change directory into that directory (e.g. cd c:\OneRepo)
3. Tell repo to initialize that directory with the Azure manifest (NOTE: Use the following URL literally, do not replace it with your repository URL):
`repo init -u http://vstfrd:8080/Azure/One/_git/Manifest`

Shoot your troubles

1. 
    	System.ApplicationException: Could not find Git!. Ensure that 'git.exe' is in a path listed in your PATH environment variable
    	at Repo.Core.GitShell.get_PathToGit() in c:\one\EngSys\DevServices\Repo\Repo.Core\GitShell.cs:line 185
    Possible Fix: If you just installed the chocolatey software in the same command window, close it and re-open a new one then re-run the above command.


2. 
        System.Exception: Call to git.exe return 128   at Repo.Core.GitShell.Run(String arguments, String workingFolder) in c:\one\EngSys\DevServices\Repo\Repo.Core\GitShell.cs:line 34
    Possible Fix: Run repo init -u again.  This time git may prompt for credentials.


3.
         System.ArgumentException: An item with the same key has already been added.
    Possible Fix: Find where repo.exe exists(usually C:\Chocolatey\lib\Repo.x.x.x\tools\Repo.exe). Use repo.exe's fullpath instead of "repo".

Note:  it may be necessary to restart your machine after installing the prerequisites and prior to running repo init.

-----------------

# Using CoreXT

1. Go to the one of the desired CoreXT repository
2. Run: init.cmd no_cache
    - When initiating a repository for the first time, it will take quite some time for coreXT to grab all the dependencies, be patient.
## build
3. Build the project using on of the following cmd commands:
    - Local build: 
        - build
    - Buddy build (building on a remote designated build server, but not signing the files), a link to the build status will be produced:
        - buildreq -b
    - Official build (building on a remote designated build server, producing production ready drop folder), a link to the build status will be produced. 
    *USE WISELY*. 
        - buildreq

## Open Visual Studio
4. Use the following cmd commands (might be a script similar name, if one does not exist):
    - RunVS2017.cmd