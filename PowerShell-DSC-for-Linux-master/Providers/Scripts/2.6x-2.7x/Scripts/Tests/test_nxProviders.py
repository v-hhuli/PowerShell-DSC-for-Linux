#!/usr/bin/env python
#============================================================================
# Copyright (c) Microsoft Corporation. All rights reserved. See license.txt for license information.
#============================================================================
import time
import os
import sys
import hashlib
import grp
import imp
import subprocess
import base64
import platform
import pwd
import codecs
import ctypes
import re
import inspect
import copy
import fnmatch
import hashlib
import base64
import cPickle as pickle
from contextlib import contextmanager

@contextmanager
def opened_w_error(filename, mode="r"):
    """
    This context ensures the file is closed.
    """
    try:
        f = codecs.open(filename, encoding='utf-8' , mode=mode)
    except IOError, err:
        yield None, err
    else:
        try:
            yield f, None
        finally:
            f.close()

try:
    import unittest2
except:
    os.system('tar -zxf ./unittest2-0.5.1.tar.gz')
    sys.path.append(os.path.realpath('./unittest2-0.5.1'))
    import unittest2

def ParseMOF(mof_file):
    srch_list_elem=r'(=[ ]+)({)(.*?)(})([ ]?;)'
    repl_list_elem = r'\1[\3]\5'
    srch_instance=r'(?P<instance>instance)[ ,\n]+of[ ,\n]+(?!OMI)(?P<inst_type>.*?)[ ,\n]+as[ ,\n]+(?P<inst_value>.*?)[ ,\n]?{([ ,\n]+)?(?P<inst_text>.*?)}[ ,\n]?;'
    value_srch_str=r'([ ,\n]+)?(?P<name>.*?)([ ]+)?=([ ]+)?(?P<value>.*?)([ ]+)?;'
    instance_srch_str=r'([ ,\n]+)?ResourceID([ ]+)?=([ ]+)?"\[(?P<module>.*?)\](?P<ResourceID>.*?)"([ ]+)?;'
    list_elem=re.compile(srch_list_elem,re.M|re.S)
    instance=re.compile(srch_instance,re.M|re.S)
    value_srch=re.compile(value_srch_str,re.M|re.S)
    instance_srch=re.compile(instance_srch_str,re.M|re.S)
    mof_text=open(mof_file,'r').read()
    mof_text=list_elem.sub(repl_list_elem,mof_text)
    matches=instance.finditer(mof_text)
    d={}
    d.clear()
    curinst=''
    for match in matches:
        values=match.group('inst_text')
        values=re.sub('(/[*].*?[*]/)','',values)
        i=instance_srch.search(values)
        curinst='['+i.group('module')+']'+i.group('ResourceID').strip('"')
        d[curinst]={}
        v=value_srch.finditer(values)
        for pair in v:
            name=pair.group('name')
            value=pair.group('value')
            if value.lower().strip() == 'false':
                value='False'
            if value.lower().strip() == 'true':
                value='True'
            d[curinst][name]=eval(value)
    d[curinst].pop('ResourceID')
    d[curinst].pop('ModuleName')
    d[curinst].pop('ModuleVersion')
    if 'DependsOn' in d[curinst].keys():
        d[curinst].pop('DependsOn')
    the_module = globals ()[i.group('module')]
    argspec=inspect.getargspec(the_module.__dict__['Set_Marshall'])
    if type(argspec) == tuple :
        args=argspec[0]
    else :
        args=argspec.args
    for arg in args:
        if arg not in d[curinst].keys():
            d[curinst][arg]=None
    return d[curinst]

def check_values(s,d):
    if s is None and d is None:
        return True
    elif s is None or d is None:
        return False
    if s[0] != d[0]:
        return False
    sd=s[1]
    dd=d[1]
    for k in sd.keys():
        if sd[k] == None or dd[k] == None:
            continue
        if sd[k].value==None or dd[k].value==None:
            continue
        if type(sd[k].value) == ctypes.c_bool:
            if sd[k].value.value==None or dd[k].value.value==None:
                continue
            if sd[k].value.value != dd[k].value.value:
                print k+': '+str(sd[k].value.value)+' != '+str(dd[k].value.value)+'\n'
                return False
            continue
        if type(sd[k].value) == ctypes.c_uint or type(sd[k].value) == ctypes.c_ushort :
            if sd[k].value.value==None or dd[k].value.value==None:
                continue
            if sd[k].value.value != dd[k].value.value:
                print k+': '+str(sd[k].value.value)+' != '+str(dd[k].value.value)+'\n'
                return False
            continue
        if not deep_compare(sd[k].value, dd[k].value):  
            print k+': '+str(sd[k].value)+' != '+str(dd[k].value)+'\n'
            return False
    return True

def deep_compare(obj1, obj2):
    if type(obj1) == unicode:
        obj1 = obj1.decode('utf-8').encode('ascii', 'ignore')
    if type(obj2) == unicode:
        obj1 = obj2.decode('utf-8').encode('ascii', 'ignore')
    t1 = type(obj1)
    t2 = type(obj2)
    if t1 != t2:
        return False
    
    if t1 == list and len(obj1) == len(obj2):
        for i in range(len(obj1)):
            if not deep_compare(obj1[i], obj2[i]):
                return False
        return True

    if t1 == dict and len(obj1) == len(obj2):
        for k in obj1.keys():
            if not deep_compare(obj1[k], obj2[k]):
                return False
        return True

    try:
        if obj1 == obj2:
            return True
        if obj1.value == obj2.value:
            return True
    except:
        return False

    return False

sys.path.append('.')
sys.path.append(os.path.realpath('./Scripts'))
os.chdir('../..')
nxUser=imp.load_source('nxUser','./Scripts/nxUser.py') 
nxGroup=imp.load_source('nxGroup','./Scripts/nxGroup.py') 
nxFile=imp.load_source('nxFile','./Scripts/nxFile.py') 
nxScript=imp.load_source('nxScript','./Scripts/nxScript.py') 
nxService=imp.load_source('nxService','./Scripts/nxService.py') 
nxPackage=imp.load_source('nxPackage','./Scripts/nxPackage.py') 
nxSshAuthorizedKeys=imp.load_source('nxSshAuthorizedKeys','./Scripts/nxSshAuthorizedKeys.py')
nxEnvironment=imp.load_source('nxEnvironment','./Scripts/nxEnvironment.py')
nxFirewall=imp.load_source('nxFirewall','./Scripts/nxFirewall.py')
nxIPAddress=imp.load_source('nxIPAddress', './Scripts/nxIPAddress.py')
nxComputer=imp.load_source('nxComputer', './Scripts/nxComputer.py')
nxDNSServerAddress=imp.load_source('nxDNSServerAddress', './Scripts/nxDNSServerAddress.py')
nxFileLine=imp.load_source('nxFileLine', './Scripts/nxFileLine.py')
nxArchive=imp.load_source('nxArchive', './Scripts/nxArchive.py')
nxMySqlUser=imp.load_source('nxMySqlUser', './Scripts/nxMySqlUser.py')
nxMySqlGrant=imp.load_source('nxMySqlGrant', './Scripts/nxMySqlGrant.py')
nxMySqlDatabase=imp.load_source('nxMySqlDatabase', './Scripts/nxMySqlDatabase.py')
nxFileInventory=imp.load_source('nxFileInventory', './Scripts/nxFileInventory.py')

class nxUserTestCases(unittest2.TestCase):
    """
    Test cases for nxUser.py
    """
    def setUp(self):
        """
        Setup test resources
        """
        if not os.system('grep -q jojoma /etc/passwd'):
            os.system('userdel -r jojoma 2> /dev/null')
        if not os.system('grep -q jojoma /etc/group'):
            os.system('groupdel jojoma 2> /dev/null')
        time.sleep(1)
        nxUser.SetShowMof(True)
        print self.id() + '\n'
        
    def tearDown(self):
        """
        Remove test resources.
        """
        if not os.system('grep -q jojoma /etc/passwd'):
            os.system('userdel -r jojoma 2> /dev/null')
        if not os.system('grep -q jojoma /etc/group'):
            os.system('groupdel jojoma 2> /dev/null')
        time.sleep(1)

    def pswd_hash(self,pswd):
        salt=(subprocess.Popen("openssl rand -base64 3", shell=True, bufsize=100, stdout=subprocess.PIPE).stdout).readline().rstrip()
        m = hashlib.sha1()
        m.update(pswd+salt)
        return base64.b64encode(m.digest()+salt)

    def CheckInventory(self, UserName, FullName, Description, Inventory):
        if len(Inventory['__Inventory'].value) < 1:
            return False
        for i in Inventory['__Inventory'].value:
            if UserName != None and len(UserName) and not fnmatch.fnmatch(i['UserName'].value,UserName):
                print 'UserName:' + UserName + ' != ' + i['UserName'].value
                return False
            if FullName != None and len(FullName) and not fnmatch.fnmatch(i['FullName'].value,FullName):
                print 'FullName:' + FullName + ' != ' + i['FullName'].value
                return False
            if Description != None and len(Description) and not fnmatch.fnmatch(i['Description'].value,Description):
                print 'Description:' + Description + ' != ' + i['Description'].value
                return False
        return True

    def make_MI(self,retval,UserName, Ensure, FullName, Description, Password, Disabled, PasswordChangeRequired, HomeDirectory, GroupID, UserID):
        d=dict();
        if UserName == None :
            d['UserName'] = None
        else :
            d['UserName'] = nxUser.protocol.MI_String(UserName)
        if Ensure == None :
            d['Ensure'] = None
        else :
            d['Ensure'] = nxUser.protocol.MI_String(Ensure)
        if FullName == None :
            d['FullName'] = None
        else :
            d['FullName'] = nxUser.protocol.MI_String(FullName)
        if PasswordChangeRequired == None :
            d['PasswordChangeRequired'] = None
        else :
            d['PasswordChangeRequired'] = nxUser.protocol.MI_Boolean(PasswordChangeRequired)
        if Disabled == None :
            d['Disabled'] = None
        else :
            d['Disabled'] = nxUser.protocol.MI_Boolean(Disabled)
        if Description == None :
            d['Description'] = None
        else :
            d['Description'] = nxUser.protocol.MI_String(Description)
        if Password == None :
            d['Password'] = None
        else :
            d['Password'] = nxUser.protocol.MI_String(Password)
        if HomeDirectory == None :
            d['HomeDirectory'] = None
        else :
            d['HomeDirectory'] = nxUser.protocol.MI_String(HomeDirectory)
        if GroupID == None :
            d['GroupID'] = None
        else :
            d['GroupID'] = nxUser.protocol.MI_String(GroupID)
        if UserID == None :
            d['UserID'] = None
        else :
            d['UserID'] = nxUser.protocol.MI_String(UserID)
        return retval,d
    
    def testSetUserAbsentError(self):
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Absent", "", "", "", "", "", "", "" )!=
                        [0],'Set("jojoma", "Absent", "", "", "", "", "", "", "" ) should return !=[0]')

    def testSetUserPresent(self):
        pswd=self.pswd_hash('jojoma')
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, False, False, "/home/jojoma", "mail" )==
                        [0],'Set("jojoma", "Present", "JO JO MA", "JOJOMA", '+pswd+', False, False, "/home/jojoma", "mail" ) should return == [0]')

    def testGetUserAbsent(self):
        assert check_values(nxUser.Get_Marshall("jojoma", "absent", "", "", "", "", "", "", "" ), \
                self.make_MI(0,"jojoma", "absent", "", "", "", False, False, "", "", None))  ==  True, \
                'Get("jojoma", "", "", "", "", "", "", "", "" )[:3] should return ==[0,"jojoma","absent"]'

    def testGetUserPresent(self):
        """
        Note - GroupID is currently returned as the string representation of a number, eg - '27'
        """
        pswd=self.pswd_hash('jojoma')
        grpid=str(grp.getgrnam('mail')[2])
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, False, False, "/home/jojoma", grpid )==  [0],'Set("jojoma", "Present", "JO JO MA", "JOJOMA", '+pswd+', False, False, "/home/jojoma", "8" ) should return == [0]')
        self.assertTrue(check_values(nxUser.Get_Marshall \
        ("jojoma", "", "", "", "", "", "", "", "" ),self.make_MI(0,"jojoma","present", \
        "JO JO MA", "JOJOMA", None, False, False, "/home/jojoma",grpid, None)), \
        'Get("jojoma", "", "", "", "", "", "", "", "" )[:3] should return ==[0,"jojoma","present", "JO JO MA", "JOJOMA", ' \
        +pswd+', False, False, "/home/jojoma", "'+grpid+'"]')
        
    def testTestUserAbsent(self):
        self.assertTrue(nxUser.Test_Marshall("jojoma", "Absent", "", "", "", "", "", "", "" ) ==
                        [0],'Test("jojoma", "Absent", "", "", "", "", "", "", "" ) should return ==[0]')

    def testTestUserAbsentError(self):
        self.assertTrue(nxUser.Test_Marshall("root", "Absent", "", "", "", "", "", "", "" )==
                        [-1],'Test("root", "", "", "", "", "", "", "", "" ) should return ==[-1]')
        
    def testTestUserPresent(self):
        self.assertTrue(nxUser.Test_Marshall("root", "Present", "", "", "", "", "", "", "" )==
                        [0],'Test("root", "Present", "", "", "", "", "", "", "" ) should return ==[0]')

    def testTestUserPresentError(self):
        self.assertTrue(nxUser.Test_Marshall("jojoma", "Present", "", "", "", "", "", "", "" )==
                        [-1],'Test("jojoma", "Present", "", "", "", "", "", "", "" ) should return ==[-1]')

    def testTestUserFullName(self):
        pswd=self.pswd_hash('jojoma')
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "JO JO MA", "", pswd, False, False, "/home/jojoma", "mail" )==
                        [0],'Set("jojoma", "Present", "JO JO MA", "", '+pswd+', False, False, "/home/jojoma", "mail" ) should return == [0]')
        self.assertTrue(nxUser.Test_Marshall("jojoma", "Present", "JO JO MA", "", "", "", "", "", "" )==
                        [0],'Test("jojoma", "Present", "JO JO MA", "", "", "", "", "", "" ) should return ==[0]')

    def testTestUserDescription(self):
        pswd=self.pswd_hash('jojoma')
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "", "JOJOMA", pswd, False, False, "/home/jojoma", "mail" )==
                        [0],'Set("jojoma", "Present", "", "JOJOMA", '+pswd+', False, False, "/home/jojoma", "mail" ) should return == [0]')
        self.assertTrue(nxUser.Test_Marshall("jojoma", "Present", "", "JOJOMA", "", "", "", "", "" )==
                        [0],'Test("jojoma", "Present", "", "JOJOMA", "", "", "", "", "" ) should return ==[0]')

    def testTestUserHomeDirectory(self):
        pswd=self.pswd_hash('jojoma')
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "", "", pswd, False, False, "/home/jojoma", "mail" )==
                        [0],'Set("jojoma", "Present", "", "", '+pswd+', False, False, "/home/jojoma", "mail" ) should return == [0]')
        self.assertTrue(nxUser.Test_Marshall("jojoma", "Present", "", "", "", False, False, "/home/jojoma", "" )==
                        [0],'Test("jojoma", "Present", "", "", "", False, False, "/home/jojoma", "" ) should return ==[0]')

    def testTestUserGroupID(self):
        pswd=self.pswd_hash('jojoma')
        grpid=str(grp.getgrnam('mail')[2])
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, False, False, "/home/jojoma", "mail" )==
                        [0],'Set("jojoma", "Present", "JO JO MA", "JOJOMA", '+pswd+', False, False, "/home/jojoma", "mail" ) should return == [0]')
        self.assertTrue(nxUser.Test_Marshall("jojoma", "Present", "", "", "", "", "", "", grpid )==
                        [0],'Test("jojoma", "Present", "", "", "", "", "", "", "'+ grpid+ '" ) should return ==[0]')
        
    def testTestUserPassword(self):
        pswd=self.pswd_hash('jojoma')
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, False, False, "/home/jojoma", "mail" )==
                        [0],'Set("jojoma", "Present", "JO JO MA", "JOJOMA", '+pswd+', False, False, "/home/jojoma", "mail" ) should return == [0]')
        self.assertTrue(nxUser.Test_Marshall("jojoma", "Present", "", "", "", pswd, "", "", "" )==
                        [0],'Test("jojoma", "Present", "", "", "", '+pswd+', "", "", "" ) should return ==[0]')

    def testTestUserFullNameError(self):
        pswd=self.pswd_hash('jojoma')
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "JO JO MA", "", pswd, False, False, "/home/jojoma", "mail" )==
                        [0],'Set("jojoma", "Present", "JO JO MA", "", '+pswd+', False, False, "/home/jojoma", "mail" ) should return == [0]')
        self.assertTrue(nxUser.Test_Marshall("jojoma", "Present", "JO JO MAMA", "", "", "", "", "", "" )==
                        [-1],'Test("jojoma", "Present", "JO JO MAMA", "", "", "", "", "", "" ) should return ==[-1]')

    def testTestUserDescriptionError(self):
        pswd=self.pswd_hash('jojoma')
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "", "JOJOMA", pswd, False, False, "/home/jojoma", "mail" )==
                        [0],'Set("jojoma", "Present", "", "JOJOMA", '+pswd+', False, False, "/home/jojoma", "mail" ) should return == [0]')
        self.assertTrue(nxUser.Test_Marshall("jojoma", "Present", "", "NOTJOJOMA", "", "", "", "", "" )==
                        [-1],'Test("jojoma", "Present", "", "NOTJOJOMA", "", "", "", "", "" ) should return ==[-1]')

    def testTestUserHomeDirectoryError(self):
        pswd=self.pswd_hash('jojoma')
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "", "", pswd, False, False, "/home/jojoma", "mail" )==
                        [0],'Set("jojoma", "Present", "", "", '+pswd+', False, False, "/home/jojoma", "mail" ) should return == [0]')
        self.assertTrue(nxUser.Test_Marshall("jojoma", "Present", "", "", "", "", "", "/home/ojoma", "" )==
                        [-1],'Test("jojoma", "Present", "", "", "", "", "", "/home/ojoma", "" ) should return ==[-1]')

    def testTestUserGroupIDError(self):
        pswd=self.pswd_hash('jojoma')
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "", "", pswd, False, False, "/home/jojoma", "mail" )==
                        [0],'Set("jojoma", "Present", "", "", '+pswd+', False, False, "/home/jojoma", "mail" ) should return == [0]')
        self.assertTrue(nxUser.Test_Marshall("jojoma", "Present", "", "", "", "", "", "", '1200' )==
                        [-1],'Test("jojoma", "Present", "", "", "", "", "", "", 1200 ) should return ==[-1]')

    def testTestUserPasswordError(self):
        pswd=self.pswd_hash('jojoma')
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "", "", pswd, False, False, "/home/jojoma", "mail" )==
                        [0],'Set("jojoma", "Present", "", "", '+pswd+', False, False, "/home/jojoma", "mail" ) should return == [0]')
        pswd=self.pswd_hash('jojomama')
        self.assertTrue(nxUser.Test_Marshall("jojoma", "Present", "", "", pswd , "", "", "", "" )==
                        [-1],'Test("jojoma", "Present", "", "", "'+pswd+'", "", "", "", "" ) should return ==[-1]')

    def testSetUserDisabled(self):
        pswd=self.pswd_hash('jojoma')
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, True, False, "/home/jojoma", "" )==
                        [0],'Set("jojoma", "Present", "JO JO MA", "JOJOMA", '+pswd+', True, False, "/home/jojoma", "" ) should return == [0]')
        self.assertTrue(nxUser.Test_Marshall("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, True, False, "/home/jojoma", "" )==
                        [0],'Test("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, True, False, "/home/jojoma", "" ) should return ==[0]')
        

    def testSetUserDisabledError(self):
        pswd=self.pswd_hash('jojoma')
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, False, False, "/home/jojoma", "" )==
                        [0],'Set("jojoma", "Present", "JO JO MA", "JOJOMA", '+pswd+', False, False, "/home/jojoma", "" ) should return == [0]')
        self.assertTrue(nxUser.Test_Marshall("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, True, False, "/home/jojoma", "" )==
                        [-1],'Test("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, True, False, "/home/jojoma", "" ) should return ==[-1]')

    def testSetUserExpired(self):
        pswd=self.pswd_hash('jojoma')
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, False, True, "/home/jojoma", "" )==
                        [0],'Set("jojoma", "Present", "JO JO MA", "JOJOMA", '+pswd+', False, True, "/home/jojoma", "" ) should return == [0]')
        self.assertTrue(nxUser.Test_Marshall("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, False, True, "/home/jojoma", "" )==
                        [0],'Test("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, False, True, "/home/jojoma", "" ) should return ==[0]')

    def testSetUserExpiredError(self):
        pswd=self.pswd_hash('jojoma')
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, False, False, "/home/jojoma", "" )==
                        [0],'Set("jojoma", "Present", "JO JO MA", "JOJOMA", '+pswd+', False, False, "/home/jojoma", "" ) should return == [0]')
        self.assertTrue(nxUser.Test_Marshall("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, False, True, "/home/jojoma", "" )==
                        [-1],'Test("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, False, True, "/home/jojoma", "" ) should return ==[-1]')

    def testSetUserNotExpiredError(self):
        pswd=self.pswd_hash('jojoma')
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, False, True, "/home/jojoma", "" )==
 [0],'Set("jojoma", "Present", "JO JO MA", "JOJOMA", '+pswd+', False, True, "/home/jojoma", "" ) should return == [0]')
        self.assertTrue(nxUser.Test_Marshall("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, False, False, "/home/jojoma", "" )==
 [-1],'Test("jojoma", "Present", "JO JO MA", "JOJOMA", '+pswd+', False, False, "/home/jojoma", "" ) should return == [-1]')

    def testUserInventoryMarshal(self):
        d=nxUser.Inventory_Marshall("", "", "", "", "", False, False, "", "" )
        self.assertTrue(d[0] == 0,'Inventory_Marshall("", "", "", "", "", False, False, "", "" ) should return == [0]')

    def testInventoryMarshallUser(self):
        pswd=self.pswd_hash('jojoma')
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, False, False, "/home/jojoma", "mail" )==
                        [0],'Set("jojoma", "Present", "JO JO MA", "JOJOMA", '+pswd+', False, False, "/home/jojoma", "mail" ) should return == [0]')
        r=nxUser.Inventory_Marshall("jojoma", "Present", "JO JO MA", "JOJOMA", "", False, False, "", "" )
        self.assertTrue(self.CheckInventory("jojoma", "JO JO MA", "JOJOMA", r[1]) == True, \
                        'CheckInventory("jojoma", "JO JO MA", "JOJOMA", r[1]) should == True')

    def testInventoryMarshallUserFilterUserName(self):
        pswd=self.pswd_hash('jojoma')
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, False, False, "/home/jojoma", "mail" )==
                        [0],'Set("jojoma", "Present", "JO JO MA", "JOJOMA", '+pswd+', False, False, "/home/jojoma", "mail" ) should return == [0]')
        r=nxUser.Inventory_Marshall("joj*", "", "", "", "", False, False, "", "" )
        self.assertTrue(self.CheckInventory("joj*", None, None, r[1]) == True, \
                        'CheckInventory("joj*", None, None, r[1]) should == True')

    def testInventoryMarshallUserFilterFullName(self):
        pswd=self.pswd_hash('jojoma')
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, False, False, "/home/jojoma", "mail" )==
                        [0],'Set("jojoma", "Present", "JO JO MA", "JOJOMA", '+pswd+', False, False, "/home/jojoma", "mail" ) should return == [0]')
        r=nxUser.Inventory_Marshall("", "", "JO*", "", "", False, False, "", "" )
        self.assertTrue(self.CheckInventory("", "JO*", None, r[1]) == True, \
                        'CheckInventory("", "JO*", None, r[1]) should == True')

    def testInventoryMarshallUserFilterDescription(self):
        pswd=self.pswd_hash('jojoma')
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, False, False, "/home/jojoma", "mail" )==
                        [0],'Set("jojoma", "Present", "JO JO MA", "JOJOMA", '+pswd+', False, False, "/home/jojoma", "mail" ) should return == [0]')
        r=nxUser.Inventory_Marshall("", "", "", "JO*", "", False, False, "", "" )
        self.assertTrue(self.CheckInventory("", None, "JO*", r[1]) == True, \
                        'CheckInventory("", None, "JO*", r[1]) should == True')

    def testInventoryMarshallUserFilterUserNameError(self):
        pswd=self.pswd_hash('jojoma')
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, False, False, "/home/jojoma", "mail" )==
                        [0],'Set("jojoma", "Present", "JO JO MA", "JOJOMA", '+pswd+', False, False, "/home/jojoma", "mail" ) should return == [0]')
        r=nxUser.Inventory_Marshall("yoj*", "", "", "", "", False, False, "", "" )
        self.assertTrue(self.CheckInventory("yoj*", None, None, r[1]) == False, \
                        'CheckInventory("yoj*", None, None, r[1]) should == False')

    def testInventoryMarshallUserFilterFullNameError(self):
        pswd=self.pswd_hash('jojoma')
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, False, False, "/home/jojoma", "mail" )==
                        [0],'Set("jojoma", "Present", "JO JO MA", "JOJOMA", '+pswd+', False, False, "/home/jojoma", "mail" ) should return == [0]')
        r=nxUser.Inventory_Marshall("", "", "JO*", "", "", False, False, "", "" )
        self.assertTrue(self.CheckInventory("", "YO*", None, r[1]) == False, \
                        'CheckInventory("", "YO*", None, r[1]) should == False')

    def testInventoryMarshallUserFilterDescriptionError(self):
        pswd=self.pswd_hash('jojoma')
        self.assertTrue(nxUser.Set_Marshall("jojoma", "Present", "JO JO MA", "JOJOMA", pswd, False, False, "/home/jojoma", "mail" )==
                        [0],'Set("jojoma", "Present", "JO JO MA", "JOJOMA", '+pswd+', False, False, "/home/jojoma", "mail" ) should return == [0]')
        r=nxUser.Inventory_Marshall("", "", "", "YO*", "", False, False, "", "" )
        self.assertTrue(self.CheckInventory("", None, "YO*", r[1]) == False, \
                        'CheckInventory("", None, "YO*", r[1]) should == False')

class nxGroupTestCases(unittest2.TestCase):
    """
    Test cases for nxGroup.py
    """
    def setUp(self):
        """
        Setup test resources
        """
        if not os.system('grep -q jojomamas /etc/group'):
            os.system('groupdel jojomamas 2> /dev/null')
        if os.system('grep -q jojoma /etc/passwd'):
            os.system('useradd -m jojoma 2> /dev/null')
        time.sleep(1)
        nxGroup.SetShowMof(False)
        print self.id() + '\n'
        
    def tearDown(self):
        """
        Remove test resources.
        """
        os.system('userdel -r jojoma 2> /dev/null')
        os.system('groupdel jojomamas 2> /dev/null')
        time.sleep(1)
        nxGroup.SetShowMof(False)
        print self.id() + '\n'

    def pswd_hash(self,pswd):
        import subprocess,hashlib,base64
        salt=(subprocess.Popen("openssl rand -base64 3", shell=True, bufsize=100, stdout=subprocess.PIPE).stdout).readline().rstrip()
        m = hashlib.sha1()
        m.update(pswd+salt)
        return base64.b64encode(m.digest()+salt)

    def CheckInventory(self, GroupName, Inventory):
        if len(Inventory['__Inventory'].value) < 1:
            return False
        for i in Inventory['__Inventory'].value:
            if GroupName != None and len(GroupName) and not fnmatch.fnmatch(i['GroupName'].value,GroupName):
                print 'GroupName:' + GroupName + ' != ' + i['GroupName'].value
                return False
        return True

    def make_MI(self,retval,GroupName, Ensure, Members, MembersToInclude, MembersToExclude, PreferredGroupID, GroupID):
        d=dict();
        if GroupName == None :
            d['GroupName'] = None
        else :
            d['GroupName'] = nxGroup.protocol.MI_String(GroupName)
        if Ensure == None :
            d['Ensure'] = None
        else :
            d['Ensure'] = nxGroup.protocol.MI_String(Ensure)
        if Members == None :
            d['Members'] = None
        else :
            d['Members'] = nxGroup.protocol.MI_StringA(Members)
        if MembersToInclude == None :
            d['MembersToInclude'] = None
        else :
            d['MembersToInclude'] = nxGroup.protocol.MI_StringA(MembersToInclude)
        if MembersToExclude == None :
            d['MembersToExclude'] = None
        else :
            d['MembersToExclude'] = nxGroup.protocol.MI_StringA(MembersToExclude)
        if PreferredGroupID == None :
            d['PreferredGroupID'] = None
        else :
            d['PreferredGroupID'] = nxGroup.protocol.MI_String(PreferredGroupID)
        if GroupID == None :
            d['GroupID'] = None
        else :
            d['GroupID'] = nxGroup.protocol.MI_String(GroupID)
        return retval,d

    def testSetGroupPresent(self):
        self.assertTrue(nxGroup.Set_Marshall("jojomamas", "Present", ["jojoma"], "", "", "1101" ) ==
                        [0],'Set("jojomamas", "Present", ["jojoma"], "", "", "1101" ) should return == [0]')

    def testSetGroupAbsent(self):
        self.assertTrue(nxGroup.Set_Marshall("jojomamas", "Present", ["jojoma"], "", "", "1101" ) ==
                        [0],'Set("jojomamas", "Present", ["jojoma"], "", "", "1101" ) should return == [0]')
        time.sleep(1)
        self.assertTrue(nxGroup.Set_Marshall("jojomamas", "Absent", ["jojoma"], "", "", "1101" ) ==
                        [0],'Set("jojomamas", "Absent", ["jojoma"], "", "", "1101" ) should return == [0]')

    def testGetGroupAbsent(self):
        self.assertTrue(check_values(nxGroup.Get_Marshall \
        ("jojomamas", "Absent", "", "", "", ""),self.make_MI(0,"jojomamas","absent",None ,None ,None ,None ,None )), \
        'Get("jojomamas", "", "", "", "", "")[:3] should return ==[0,"jojomamas","absent"]')

    def testGetGroupPresent(self):
        self.assertTrue(nxGroup.Set_Marshall("jojomamas", "Present", ["jojoma"], "", "", "1101" ) ==
                        [0],'Set("jojomamas", "Present", ["jojoma"], "", "", "1101" ) should return == [0]')
        
        self.assertTrue(check_values(nxGroup.Get_Marshall("jojomamas", "Present", ['jojoma'], "", "", "1101"), \
        self.make_MI(0,"jojomamas","present", ['jojoma'],None ,None , "1101" ,None )), \
                        'Get("jojomamas", "", "", "", "", "1101")[:6] should return ==[0,"jojomamas","present", "", "", "1101"]')

    def testTestGroupAbsent(self):
        self.assertTrue(nxGroup.Test_Marshall("jojomamas", "Absent", "", "", "", "") ==
                        [0],'Test("jojomamas", "Absent", "", "", "", "") should return ==[0]')

    def testTestGroupAbsentError(self):
        self.assertTrue(nxGroup.Test_Marshall("mail", "Absent", "", "", "", "")==
                        [-1],'Test("mail", "Absent", "", "", "", "") should return ==[-1]')

    def testTestGroupPresent(self):
        self.assertTrue(nxGroup.Test_Marshall("mail", "Present", "", "", "", "")==
                        [0],'Test("mail", "Present", "", "", "", "") should return ==[0]')

    def testTestGroupPresentError(self):
        self.assertTrue(nxGroup.Test_Marshall("jojomamas", "Present", "", "", "", "")==
                        [-1],'Test("jojomamas", "Present", "", "", "", "") should return ==[-1]')

    def testSetGroupPresentMembers(self):
        self.assertTrue(nxGroup.Set_Marshall("jojomamas", "Present", ("jojoma","root"), "", "", "1101" ) ==
                        [0],'Set("jojomamas", "Present", ["jojoma","root"], "", "", "1101" ) should return == [0]')
        self.assertTrue(nxGroup.Test_Marshall("jojomamas", "Present", ("jojoma","root"), "", "", "1101")==
                        [0],'Test("jojomamas", "Present", ["jojoma","root"], "", "", "1101") should return ==[0]')

    def testSetGroupPresentMembersInclude(self):
        self.assertTrue(nxGroup.Set_Marshall("jojomamas", "Present", "", "", "", "1101" ) ==
                        [0],'Set("jojomamas", "Present", "", "", "", "1101" ) should return == [0]')
        self.assertTrue(nxGroup.Set_Marshall("jojomamas", "Present", "", ["jojoma"], "", "1101" ) ==
                        [0],'Set("jojomamas", "Present", "", ["jojoma"], "", "1101" ) should return == [0]')
        self.assertTrue(nxGroup.Test_Marshall("jojomamas", "Present", ["jojoma"], "", "", "1101")==
                        [0],'Test("jojomamas", "Present", ["jojoma"], "", "", "1101") should return ==[0]')

    def testSetGroupPresentMembersExclude(self):
        self.assertTrue(nxGroup.Set_Marshall("jojomamas", "Present", ["jojoma","root"], "", "", "1101" ) ==
                        [0],'Set("jojomamas", "Present", ("jojoma","root"), "", "", "1101" ) should return == [0]')
        # Below is a bug in nxGroup ?
        self.assertTrue(nxGroup.Set_Marshall("jojomamas", "Present", "", "", ["jojoma"], "1101" ) ==
                        [0],'Set("jojomamas", "Present", "", "", ("jojoma"), "1101" ) should return == [0]')
        self.assertTrue(nxGroup.Test_Marshall("jojomamas", "Present", ["root"], "", "", "1101")==
                        [0],'Test("jojomamas", "Present", "root", "", "", "1101") should return ==[0]')

    def testSetGroupPresentPreferredGroupIDInUseError(self):
        self.assertTrue(nxGroup.Set_Marshall("jojomamas", "Present", "", "", "", "0" ) ==
                        [0],'Set("jojomamas", "Present", "", "", "", "0" ) should return == [0]')
        self.assertTrue(nxGroup.Test_Marshall("jojomamas", "Present", "", "", "", "0")==
                        [-1],'Test("jojomamas", "Present", , "", "", "0") should return ==[-1]')

    def testInventory_Marshall(self):
        d=nxGroup.Inventory_Marshall("*", "", "", "", "", "")

    def testSetInventory_MarshallFilterGroup(self):
        self.assertTrue(nxGroup.Set_Marshall("jojomamas", "Present", "", "", "", "1101" ) ==
                        [0],'Set("jojomamas", "Present", "", "", "", "1101" ) should return == [0]')
        d=nxGroup.Inventory_Marshall("*mama*", "", "", "", "", "")
        self.assertTrue(self.CheckInventory("*mama*",d[1]) == True, 'self.CheckInventory("*mama*",d[1]) should == True')

    def testSetInventory_MarshallFilterGroupError(self):
        self.assertTrue(nxGroup.Set_Marshall("jojomamas", "Present", "", "", "", "1101" ) ==
                        [0],'Set("jojomamas", "Present", "", "", "", "1101" ) should return == [0]')
        d=nxGroup.Inventory_Marshall("*jama*", "", "", "", "", "")
        self.assertTrue(self.CheckInventory("*jama*",d[1]) == False, \
                        'self.CheckInventory("*mama*",d[1]) should == False')


class nxScriptTestCases(unittest2.TestCase):
    """
    Test cases for nxScript.py
    """
    def setUp(self):
        """
        Setup test resources
        """
        os.system('useradd -m jojoma  2> /dev/null')
        time.sleep(1)
        self.get_script='#!/bin/bash \ncat /tmp/testfile\n'
        self.test_script='#!/bin/bash \ngrep  "set script successfull" /tmp/testfile\n'
        self.set_script='#!/bin/bash \necho "set script successfull" > /tmp/testfile\n'
        
    def tearDown(self):
        """
        Remove test resources.
        """
        os.system('userdel -r jojoma  2> /dev/null')
        os.system('rm /tmp/testfile 2> /dev/null')
        time.sleep(1)
    
    def make_MI(self,retval,GetScript, SetScript, TestScript, User, Group, Result):
        d=dict();
        if GetScript == None :
            d['GetScript'] = None
        else :
            d['GetScript'] = nxScript.protocol.MI_String(GetScript)
        if SetScript == None :
            d['SetScript'] = None
        else :
            d['SetScript'] = nxScript.protocol.MI_String(SetScript)
        if TestScript == None :
            d['TestScript'] = None
        else :
            d['TestScript'] = nxScript.protocol.MI_String(TestScript)
        if User == None :
            d['User'] = None
        else :
            d['User'] = nxScript.protocol.MI_String(User)
        if Group == None :
            d['Group'] = None
        else :
            d['Group'] = nxScript.protocol.MI_String(Group)
        if Result == None :
            d['Result'] = None
        else :
            d['Result'] = nxScript.protocol.MI_String(Result)
        return retval,d

    def testGetScriptUser(self):
        nxScript.Set_Marshall(self.get_script,self.set_script,self.test_script, "jojoma", "" )
        r=nxScript.Get_Marshall(self.get_script,self.set_script,self.test_script, "jojoma", "" )
        self.assertTrue(check_values(r,self.make_MI(0,self.get_script,self.set_script,self.test_script, "jojoma", "", "set script successfull\n" )) == True,'nxScript.Get_Marshall(self.get_script,self.set_script,self.test_script, "jojoma", "" )[0] should return == 0')

    def testTestScriptUser(self):
        nxScript.Set_Marshall(self.get_script,self.set_script,self.test_script, "jojoma", "" )
        r=nxScript.Test_Marshall(self.get_script,self.set_script,self.test_script, "jojoma", "" )
        self.assertTrue(r == [0],'nxScript.Test_Marshall(self.get_script,self.set_script,self.test_script, "jojoma", "" )[0] should return == 0')

    def testSetScriptUser(self):
        r=nxScript.Set_Marshall(self.get_script,self.set_script,self.test_script, "jojoma", "" )
        self.assertTrue(r[0] == 0,'nxScript.Set_Marshall(self.get_script,self.set_script,self.test_script, "jojoma", "" )[0] should return == 0')

    def testGetScriptGroup(self):
        nxScript.Set_Marshall(self.get_script,self.set_script,self.test_script, "", "mail" )
        r=nxScript.Get_Marshall(self.get_script,self.set_script,self.test_script, "", "mail" )
        self.assertTrue(check_values(r,self.make_MI(0,self.get_script,self.set_script,self.test_script, "", "mail", "set script successfull\n" )) == True,'nxScript.Get_Marshall(self.get_script,self.set_script,self.test_script, "", "mail" )[0] should return == 0')

    def testTestScriptGroup(self):
        nxScript.Set_Marshall(self.get_script,self.set_script,self.test_script, "", "mail" )
        r=nxScript.Test_Marshall(self.get_script,self.set_script,self.test_script, "", "mail" )
        self.assertTrue(r == [0],'nxScript.Test_Marshall(self.get_script,self.set_script,self.test_script, "", "mail" )[0] should return == 0')

    def testSetScriptGroup(self):
        r=nxScript.Set_Marshall(self.get_script,self.set_script,self.test_script, "", "mail" )
        self.assertTrue(r[0] == 0,'nxScript.Set_Marshall(self.get_script,self.set_script,self.test_script, "", "mail" )[0] should return == 0')

    def testGetScriptUserError(self):
        nxScript.Set_Marshall(self.get_script,self.set_script,self.test_script, "jojoma", "" )
        r=nxScript.Get_Marshall(self.get_script,self.set_script,self.test_script, "ojoma", "" )
        self.assertTrue(check_values(r,self.make_MI(0,self.get_script,self.set_script,self.test_script, "ojoma", "", "set script successfull\n") ) == False,'nxScript.Get_Marshall(self.get_script,self.set_script,self.test_script, "ojoma", "" )[-1] should return == -1')

    def testTestScriptUserError(self):
        nxScript.Set_Marshall(self.get_script,self.set_script,self.test_script, "jojoma", "" )
        r=nxScript.Test_Marshall(self.get_script,self.set_script,self.test_script, "ojoma", "" )
        self.assertTrue(r == [-1],'nxScript.Test_Marshall(self.get_script,self.set_script,self.test_script, "ojoma", "" )[-1] should return == -1')

    def testSetScriptUserError(self):
        r=nxScript.Set_Marshall(self.get_script,self.set_script,self.test_script, "ojoma", "" )
        self.assertTrue(r[0] == -1,'nxScript.Set_Marshall(self.get_script,self.set_script,self.test_script, "ojoma", "" )[-1] should return == -1')

    def testGetScriptGroupError(self):
        nxScript.Set_Marshall(self.get_script,self.set_script,self.test_script, "", "ojoma" )
        r=nxScript.Get_Marshall(self.get_script,self.set_script,self.test_script, "", "ojoma" )
        self.assertTrue(check_values(r,self.make_MI(0,self.get_script,self.set_script,self.test_script, "", "ojoma" , "set script successfull\n")) == False,'nxScript.Get_Marshall(self.get_script,self.set_script,self.test_script, "", "ojoma" )[-1] should return == -1')

    def testTestScriptGroupError(self):
        nxScript.Set_Marshall(self.get_script,self.set_script,self.test_script, "", "ojoma" )
        r=nxScript.Test_Marshall(self.get_script,self.set_script,self.test_script, "", "ojoma" )
        self.assertTrue(r == [-1],'nxScript.Test_Marshall(self.get_script,self.set_script,self.test_script, "", "ojoma" )[-1] should return == -1')

    def testSetScriptGroupError(self):
        r=nxScript.Set_Marshall(self.get_script,self.set_script,self.test_script, "", "ojoma" )
        self.assertTrue(r[0] == -1,'nxScript.Set_Marshall(self.get_script,self.set_script,self.test_script, "", "ojoma" )[-1] should return == -1')


class nxPackageTestCases(unittest2.TestCase):
    """
    Test cases for nxPackage
    """
    def setUp(self):
        """
        Setup test resources
        """
        time.sleep(4)
        self.pkg = 'nano'
        if platform.dist()[0].lower() == 'suse':
            self.pkg = 'gvim'
        if os.system('which dpkg') == 0 :
            os.system('dpkg -r ' + self.pkg + ' 2> /dev/null')
            if os.path.exists('/usr/bin/dummy.sh'):
                os.system('dpkg -r dummy 2> /dev/null')
            self.package_path='./Scripts/Tests/dummy-1.0.deb'
        else :
            os.system('rpm -e ' + self.pkg + ' 2> /dev/null')
            if os.path.exists('/usr/bin/dummy.sh'):
                os.system('rpm -e dummy 2> /dev/null')
            self.package_path='./Scripts/Tests/dummy-1.0-1.x86_64.rpm'
        time.sleep(3)
        print self.id() + '\n'
        
    def tearDown(self):
        """
        Remove test resources.
        """
        time.sleep(4)
        if os.system('which dpkg') == 0 :
            os.system('dpkg -r ' + self.pkg + ' 2> /dev/null')
            if os.path.exists('/usr/bin/dummy.sh'):
                os.system('dpkg -r dummy 2> /dev/null')
        else :
            os.system('rpm -e ' + self.pkg + ' 2> /dev/null')
            if os.path.exists('/usr/bin/dummy.sh'):
                os.system('rpm -e dummy 2> /dev/null')
        time.sleep(3)

    def CheckInventory(self, Name, Inventory):
        if len(Inventory['__Inventory'].value) < 1:
            return False
        for i in Inventory['__Inventory'].value:
            if Name != None and len(Name) and not fnmatch.fnmatch(i['Name'].value,Name):
                print 'Name:' + Name + ' != ' + i['Name'].value
                return False
        return True

    def make_MI(self, retval, Ensure, PackageManager, Name, FilePath, PackageGroup, Arguments,
                ReturnCode,PackageDescription,Publisher,InstalledOn,Size,Version,Installed, Architecture):
        d=dict();
        if Ensure == None :
            d['Ensure'] = None
        else :
            d['Ensure'] = nxPackage.protocol.MI_String(Ensure)
        if PackageManager == None :
            d['PackageManager'] = None
        else :
            d['PackageManager'] = nxPackage.protocol.MI_String(PackageManager)
        if Name == None :
            d['Name'] = None
        else :
            d['Name'] = nxPackage.protocol.MI_String(Name)
        if FilePath == None :
            d['FilePath'] = None
        else :
            d['FilePath'] = nxPackage.protocol.MI_String(FilePath)
        if PackageGroup == None :
            d['PackageGroup'] = None
        else :
            d['PackageGroup'] = nxPackage.protocol.MI_Boolean(PackageGroup)
        if Arguments == None :
            d['Arguments'] = None
        else :
            d['Arguments'] = nxPackage.protocol.MI_String(Arguments)
        if ReturnCode == None :
            d['ReturnCode'] = None
        else :
            d['ReturnCode'] = nxPackage.protocol.MI_Uint32(ReturnCode)
        if PackageDescription == None :
            d['PackageDescription'] = None
        else:
            d['PackageDescription'] = nxPackage.protocol.MI_String(PackageDescription)
        if Publisher == None:
            d['Publisher'] = None
        else:
            d['Publisher'] = nxPackage.protocol.MI_String(Publisher)
        if InstalledOn == None:
            d['InstalledOn'] = None
        else:
            d['InstalledOn'] = nxPackage.protocol.MI_String(InstalledOn)
        if Size == None:
            d['Size'] = None
        else:
            d['Size'] = nxPackage.protocol.MI_Uint32(int(Size))
        if Version == None:
            d['Version'] = None
        else:
            d['Version'] = nxPackage.protocol.MI_String(Version)
        if Installed == None:
            d['Installed'] = None
        else:
            d['Installed'] = nxPackage.protocol.MI_Boolean(Installed)
        if Architecture == None:
            d['Architecture'] = None
        else:
            d['Architecture'] = nxPackage.protocol.MI_Boolean(Architecture)
        return retval,d
    
    def testSetEnableNameDefaultProviderArguments(self):
        """
        use the appropriate argument to try-out a package
        with no installation, then test that the package is not installed.
        """
        dryrun={}
        dryrun['zypper']='--dry-run'
        dryrun['apt']='--dry-run'
        dryrun['yum']='-v' # no dry run in yum...
        dryrun['dpkg']='--dry-run'
        dryrun['rpm']='--test'
        pm=nxPackage.GetPackageManager()
        args=dryrun[pm]
        if pm == 'zypper':
            args='|'+args
        self.assertTrue(nxPackage.Set_Marshall('Present','',self.pkg,'',False,args,0)==
                        [0],"nxPackage.Set_Marshall('Present','','" + self.pkg + "','',False,'',True,0) should return ==[0]")
        
    def testSetEnablePathAndNameDefaultProvider(self):
        """
        Test that when Path and Name are set, Path is used.
        """
        self.assertTrue(nxPackage.Set_Marshall('Present','',self.pkg,self.package_path,False,'',0)==
                        [0],"nxPackage.Set_Marshall('Present','dummy','','"+ self.package_path +"',False,'',0) should return ==[0]")

    def testSetEnableNameDefaultProvider(self):
        self.assertTrue(nxPackage.Set_Marshall('Present','',self.pkg,'',False,'',0)==
                        [0],"nxPackage.Set_Marshall('Present','','" + self.pkg + "','',False,'',0) should return ==[0]")

    def testSetEnableNameExplicitProvider(self):
        pm=nxPackage.GetPackageManager()
        self.assertTrue(nxPackage.Set_Marshall('Present',pm,self.pkg,'',False,'',0)==
                        [0],"nxPackage.Set_Marshall('Present','"+pm+"','" + self.pkg + "','',False,'',0) should return ==[0]")
 
    def testSetEnableNameBadExplicitProviderError(self):
        pm=nxPackage.GetPackageManager()
        for b in ('zypper','yum','apt-get'):
            if b != pm:
                break
        self.assertTrue(nxPackage.Set_Marshall('Present',b,self.pkg,'',False,'',0)==
                        [-1],"nxPackage.Set_Marshall('Present','"+b+"','" + self.pkg + "','',False,'',0) should return ==[-1]")

    def testSetEnableNameDefaultProviderBadReturnCodeError(self):
        self.assertTrue(nxPackage.Set_Marshall('Present','',self.pkg,'',False,'',6)==
                        [-1],"nxPackage.Set_Marshall('Present','','" + self.pkg + "','',False,'',0) should return ==[-1]")

    def testGetEnableNameDefaultProvider(self):
        self.assertTrue(nxPackage.Set_Marshall('Present','',self.pkg,'',False,'',0)==
                        [0],"nxPackage.Set_Marshall('Present','','" + self.pkg + "','',False,'',0) should return ==[0]")
        r=nxPackage.Get_Marshall('Present','',self.pkg,'',False,'',0)


        self.assertTrue(check_values(r,self.make_MI(0,'present', None,self.pkg,'',False,'',0,  None, None, None, None, None, None, None )) == True
                        ,"nxPackage.Get_Marshall('Present','','" + self.pkg + "','',False,'',0)[0] should return == 0")

    def testTestEnableNameDefaultProviderBadReturnCodeError(self):
        self.assertTrue(nxPackage.Set_Marshall('Present','',self.pkg,'',False,'',0)==
                        [0],"nxPackage.Set_Marshall('Present','','" + self.pkg + "','',False,'',0) should return ==[0]")


        self.assertTrue(nxPackage.Test_Marshall('Present','',self.pkg,'',False,'',6)==
                        [-1],"nxPackage.Test_Marshall('Present','','" + self.pkg + "','',False,'',True,6) should return == [-1]")

    def testGetEnableNameDefaultProviderBadReturnCodeError(self):
        self.assertTrue(nxPackage.Set_Marshall('Present','',self.pkg,'',False,'',0)==
                        [0],"nxPackage.Set_Marshall('Present','','" + self.pkg + "','',False,'',0) should return ==[0]")
        r=nxPackage.Get_Marshall('Present','',self.pkg,'',False,'',6)

        self.assertTrue(check_values(r,self.make_MI(0,'present', None,self.pkg,'',False,'',6,  None, None, None, None, None, None, None )) == True
                        ,"nxPackage.Get_Marshall('Present','','" + self.pkg + "','',False,'',True,6)[0] should return == 0")

    def testTestEnableNameDefaultProvider(self):
        self.assertTrue(nxPackage.Set_Marshall('Present','',self.pkg,'',False,'',0)==
                        [0],"nxPackage.Set_Marshall('Present','','" + self.pkg + "','',False,'',0) should return ==[0]")


        self.assertTrue(nxPackage.Test_Marshall('Present','',self.pkg,'',False,'',0)==
                        [0],"nxPackage.Test_Marshall('Present','','" + self.pkg + "','',False,'',0) should return == [0]")

    @unittest2.skipUnless(os.system('which yum') ==
                          0,'groupmode is not implemented.')
    def testSetEnableGroupDefaultProvider(self):
        self.assertTrue(nxPackage.Set_Marshall('Present','','Remote Desktop Clients','',True,'',0)==
                        [0],"nxPackage.Set_Marshall('Present','','" + self.pkg + "','',True,'',0) should return ==[0]")
            
    def testSetEnablePathDefaultProvider(self):
        self.assertTrue(nxPackage.Set_Marshall('Present','','',self.package_path,False,'',0)==
        [0],"nxPackage.Set_Marshall('Present','','','"+ self.package_path +"',False,'',0) should return ==[0]")

    def testSetDisableNameDefaultProvider(self):
        self.assertTrue(nxPackage.Set_Marshall('Present','',self.pkg,'',False,'',0)==
                        [0],"nxPackage.Set_Marshall('Present','','" + self.pkg + "','',False,'',0) should return ==[0]")
        time.sleep(4)
        self.assertTrue(nxPackage.Set_Marshall('Absent','',self.pkg,'',False,'',0)==
                        [0],"nxPackage.Set_Marshall('Absent','','" + self.pkg + "','',False,'',0) should return ==[0]")

    def testGetDisableNameDefaultProvider(self):
        self.assertTrue(nxPackage.Set_Marshall('Present','',self.pkg,'',False,'',0)==
                        [0],"nxPackage.Set_Marshall('Present','','" + self.pkg + "','',False,'',0) should return ==[0]")
        time.sleep(4)
        self.assertTrue(nxPackage.Set_Marshall('Absent','',self.pkg,'',False,'',0)==
                        [0],"nxPackage.Set_Marshall('Absent','','" + self.pkg + "','',False,'',0) should return ==[0]")
        time.sleep(4)
        r=nxPackage.Get_Marshall('Absent','',self.pkg,'',False,'',0)

        self.assertTrue(check_values(r,self.make_MI(0,'absent', None,self.pkg,'',False,'',0, None, None, None, None, None, None, None )) == True
                        ,"nxPackage.Get_Marshall('Absent','','" + self.pkg + "','',False,'',0)[0] should return == 0")

    def testTestDisableNameDefaultProvider(self):
        self.assertTrue(nxPackage.Set_Marshall('Present','',self.pkg,'',False,'',0)==
                        [0],"nxPackage.Set_Marshall('Present','','" + self.pkg + "','',False,'',0) should return ==[0]")
        time.sleep(4)
        self.assertTrue(nxPackage.Set_Marshall('Absent','',self.pkg,'',False,'',0)==
                        [0],"nxPackage.Set_Marshall('Absent','','" + self.pkg + "','',False,'',0) should return ==[0]")
        time.sleep(4)


        self.assertTrue(nxPackage.Test_Marshall('Absent','',self.pkg,'',False,'',0)==
                        [0],"nxPackage.Test_Marshall('Absent','','" + self.pkg + "','',False,'',0) should return == [0]")

    @unittest2.skipUnless(os.system('which yum') ==
                          0,'groupmode is not implemented.')
    def testSetDisableGroupDefaultProvider(self):
        self.assertTrue(nxPackage.Set_Marshall('Present','','Remote Desktop Clients','',True,'',0)==
                        [0],"nxPackage.Set_Marshall('Present','','" + self.pkg + "','',True,'',0) should return ==[0]")
        time.sleep(4)
        self.assertTrue(nxPackage.Set_Marshall('Absent','','Remote Desktop Clients','',True,'',0)==
                        [0],"nxPackage.Set_Marshall('Absent','','" + self.pkg + "','',True,'',0) should return ==[0]")
            
    def testSetDisablePathDefaultProvider(self):
        self.assertTrue(nxPackage.Set_Marshall('Absent','','',self.package_path,False,'',0)==
                        [0],"nxPackage.Set_Marshall('Present','','','"+ self.package_path +"',False,'',0) should return == [0]")

    def testSetEnableBadNameDefaultProvider(self):
        self.assertTrue(nxPackage.Set_Marshall('Present','','nanoo','',False,'',0)==
                        [-1],"nxPackage.Set_Marshall('Present','','nanoo','',False,'',0) should return == [-1]")

    def testGetEnableBadNameDefaultProvider(self):
        r=nxPackage.Get_Marshall('Present','','nanoo','',False,'',0)

        self.assertTrue(check_values(r,self.make_MI(0,'present', None,'nanoo','',False,'',0, None, None, None, None, None, None, None )) == True
                        ,"nxPackage.Get_Marshall('Present','','nanoo','',False,'',0)[-1] should return == 0")

    def testTestEnableBadNameDefaultProvider(self):
        self.assertTrue(nxPackage.Test_Marshall('Present','','nanoo','',False,'',0)==
                        [-1],"nxPackage.Test_Marshall('Present','','nanoo','',False,'',0) should return == [-1]")

    def testSetEnableBadPathDefaultProvider(self):
        self.assertTrue(nxPackage.Set_Marshall('Present','','','BADPATH'+self.package_path,False,'',0)==
                        [-1],"nxPackage.Set_Marshall('Present','','','"+ 'BADPATH'+ self.package_path +"',False,'',0) should return ==[-1]")

    def testSetDisableBadNameDefaultProvider(self):
        self.assertTrue(nxPackage.Set_Marshall('Absent','','nanoo','',False,'',0)==
                        [0],"nxPackage.Set_Marshall('Absent','','nanoo','',False,'',0) should return ==[0]")

    def testGetDisableBadNameDefaultProvider(self):
        r=nxPackage.Get_Marshall('Absent','','nanoo','',False,'',0)

        self.assertTrue(check_values(r,self.make_MI(0,'absent', None,'nanoo','',False,'',0, None, None, None, None, None, None, None )) == True
                        ,"nxPackage.Get_Marshall('Absent','','nanoo','',False,'',0)[0] should return == 0")

    def testTestDisableBadNameDefaultProvider(self):
        self.assertTrue(nxPackage.Test_Marshall('Absent','','nanoo','',False,'',0)==
                        [0],"nxPackage.Test_Marshall('Absent','','nanoo','',False,'',0) should return == [0]")

    def testSetDisableBadPathDefaultProvider(self):
        self.assertTrue(nxPackage.Set_Marshall('Absent','','', 'BADPATH'+ self.package_path,False,'',0)==
                        [0],"nxPackage.Set_Marshall('Absent','','','"+  'BADPATH'+ self.package_path +"',False,'',0) should return == [0]")

    def testInventoryMarshall(self):
        r=nxPackage.Inventory_Marshall('','','*','',False,'',0)
        self.assertTrue(r[0] == 0,"Inventory_Marshall('','','*','',False,'',0)  should return == [0]")


    def testInventoryMarshallFilterName(self):
        self.assertTrue(nxPackage.Set_Marshall('Present','',self.pkg,'',False,'',0)==
                        [0],"nxPackage.Set_Marshall('Present','','" + self.pkg + "','',False,'',0) should return ==[0]")
        r=nxPackage.Inventory_Marshall('', '', self.pkg, '', False, '', 0)
        self.assertTrue(self.CheckInventory(self.pkg, r[1]) == True, \
                        'CheckInventory(self.pkg, r[1]) should == True')
        pkg = self.pkg[:3]
        pkg += '*'
        r=nxPackage.Inventory_Marshall('', '',  pkg, '', False, '', 0)
        self.assertTrue(self.CheckInventory(pkg, r[1]) == True, \
                        'CheckInventory('+ pkg + ', r[1]) should == True')

    def testInventoryMarshallFilterNameError(self):
        self.assertTrue(nxPackage.Set_Marshall('Present','',self.pkg,'',False,'',0)==
                        [0],"nxPackage.Set_Marshall('Present','','" + self.pkg + "','',False,'',0) should return ==[0]")
        r=nxPackage.Inventory_Marshall('', '', self.pkg[2:], '', False, '', 0)
        self.assertTrue(self.CheckInventory(self.pkg[2:], r[1]) == False, \
                        'CheckInventory(self.pkg, r[1]) should == False')

    def testInventoryMarshallCmdlineError(self):
        os.system('cp  ./Scripts/nxPackage.py /tmp/nxPackageBroken.py')
        os.system(r'sed -i "s/\((f).*\)[0-9]/\120/" /tmp/nxPackageBroken.py')
        nxPackageBroken = imp.load_source('nxPackageBroken','/tmp/nxPackageBroken.py') 
        r=nxPackageBroken.Inventory_Marshall('','','*','',False,'',0)
        os.system('rm /tmp/nxPackageBroken.py')
        self.assertTrue(len(r[1]['__Inventory'].value) == 0,"nxPackageBroken.Inventory_Marshall('','','*','',False,'',0)  should return empty MI_INSTANCEA.")



class nxFileTestCases(unittest2.TestCase):
    """
    Test cases for nxFile
    """
    def setUp(self):
        """
        Setup test resources
        """
        os.system('rm -rf /tmp/*pp* 2> /dev/null')
        os.system('rm -rf /tmp/Python-2.4.6.tgz 2> /dev/null')
        nxFile.SetShowMof(False)
        print self.id() + '\n'
        
    def tearDown(self):
        """
        Remove test resources.
        """
        os.system('rm -rf /tmp/*pp* 2> /dev/null')
        os.system('rm -rf /tmp/Python-2.4.6.tgz 2> /dev/null')

    def make_MI(self,retval,DestinationPath, SourcePath, Ensure, Type, Force, Contents, Checksum, Recurse, Links, Owner, Group, Mode, ModifiedDate):
        d=dict();
        if DestinationPath == None :
            d['DestinationPath'] = None
        else :
            d['DestinationPath'] = nxFile.protocol.MI_String(DestinationPath)
        if SourcePath == None :
            d['SourcePath'] = None
        else :
            d['SourcePath'] = nxFile.protocol.MI_String(SourcePath)
        if Ensure == None :
            d['Ensure'] = None
        else :
            d['Ensure'] = nxFile.protocol.MI_String(Ensure)
        if Type == None :
            d['Type'] = None
        else :
            d['Type'] = nxFile.protocol.MI_String(Type)
        if Force == None :
            d['Force'] = None
        else :
            d['Force'] = nxFile.protocol.MI_Boolean(Force)
        if Contents == None :
            d['Contents'] = None
        else :
            d['Contents'] = nxFile.protocol.MI_String(Contents)
        if Checksum == None :
            d['Checksum'] = None
        else :
            d['Checksum'] = nxFile.protocol.MI_String(Checksum)
        if Recurse == None :
            d['Recurse'] = None
        else :
            d['Recurse'] = nxFile.protocol.MI_Boolean(Recurse)
        if Links == None :
            d['Links'] = None
        else :
            d['Links'] = nxFile.protocol.MI_String(Links)
        if Owner == None :
            d['Owner'] = None
        else :
            d['Owner'] = nxFile.protocol.MI_String(Owner)
        if Group == None :
            d['Group'] = None
        else :
            d['Group'] = nxFile.protocol.MI_String(Group)
        if Mode == None :
            d['Mode'] = None
        else :
            d['Mode'] = nxFile.protocol.MI_String(Mode)
        if ModifiedDate == None :
            d['ModifiedDate'] = None
        else :
            d['ModifiedDate'] = nxFile.protocol.MI_Timestamp.from_time(ModifiedDate)
        return retval,d

    def testSetFileAbsent(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/1.pp", "", "Absent", "File", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/1.pp", "", "Absent", "File", "", "", "md5", "", "", "", "", "") should return [0]')

    def testSetFileAbsentError(self):
        self.assertTrue(nxFile.Set_Marshall("/tp/1.pp", "", "Absent", "File", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tp/1.pp", "", "Absent", "File", "", "", "md5", "", "", "", "", "") should return [0]')

    def testSetFileData(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "These are the contents of 1.pp", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "These are the contents of 1.pp", "md5", "", "", "", "", "") should return [0]')
        d,e=nxFile.ReadFile('/tmp/1.pp')
        self.assertTrue(d==
                        "These are the contents of 1.pp","File contents mismatch:"+d)

    def testSetFileDataError(self):
        self.assertTrue(nxFile.Set_Marshall("/tp/1.pp", "", "Present", "File", "", "These are the contents of 1.pp", "md5", "", "", "", "", "")==
                        [-1],'nxFile.Set_Marshall("/tp/1.pp", "", "Present", "File", "", "These are the contents of 1.pp", "md5", "", "", "", "", "") should return [-1]')

    def testSetFileNoData(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "", "md5", "", "", "", "", "") should return [0]')
        d,e=nxFile.ReadFile('/tmp/1.pp')
        self.assertTrue(len(d)==
                        0,"The contents of 1.pp should be empty.  File contents mismatch:"+d)

    def testTestCompareFilesMD5Same(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "These are the contents of 1.pp", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "These are the contents of 1.pp", "md5", "", "", "", "", "") should return [0]')
        self.assertTrue(nxFile.Set_Marshall("/tmp/12.pp", "/tmp/1.pp", "", "", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/12.pp", "/tmp/1.pp", "", "", "", "", "md5", "", "", "", "", "") should return [0]')
        self.assertTrue(nxFile.Test_Marshall("/tmp/12.pp", "/tmp/1.pp", "", "", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Test_Marshall("/tmp/12.pp", "/tmp/1.pp", "", "", "", "", "md5", "", "", "", "", "") should return [0]')
        
    def testTestCompareFilesMD5Different(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "These are the contents of 1.pp", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "These are the contents of 1.pp", "md5", "", "", "", "", "") should return [0]')
        self.assertTrue(nxFile.Set_Marshall("/tmp/12.pp", "/tmp/1.pp", "", "", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/12.pp", "/tmp/1.pp", "", "", "", "", "md5", "", "", "", "", "") should return [0]')
        self.assertTrue(nxFile.Test_Marshall("/tmp/12.pp", "/tmp/1.pp", "", "", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Test_Marshall("/tmp/12.pp", "/tmp/1.pp", "", "", "", "", "md5", "", "", "", "", "") should return [0]')
        
    def testTestCompareFilesMD5Error(self):
        self.assertTrue(nxFile.Test_Marshall("/tmp/12.pp", "/tmp/1.pp", "", "", "", "", "md5", "", "", "", "", "")==
                        [-1],'nxFile.Test_Marshall("/tmp/12.pp", "/tmp/1.pp", "", "", "", "", "md5", "", "", "", "", "") should return [-1]')

    def testSetFileCopy(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "These are the contents of 1.pp", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "These are the contents of 1.pp", "md5", "", "", "", "", "") should return [0]')
        self.assertTrue(nxFile.Set_Marshall("/tmp/12.pp", "/tmp/1.pp", "", "", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/12.pp", "/tmp/1.pp", "", "", "", "", "md5", "", "", "", "", "") should return [0]')
        d,e=nxFile.ReadFile('/tmp/12.pp')
        self.assertTrue(d==
                        "These are the contents of 1.pp","File contents mismatch:"+d)

    def testSetDirectoryPresent(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "") should return [0]')
        self.assertTrue(os.path.isdir('/tmp/pp') ==
                        True,'Directory /tmp/pp is missing.')

    def testSetDirectoryAbsent(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "") should return [0]')
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp", "", "Absent", "Directory", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/1.pp", "", "Absent", "Directory", "", "", "md5", "", "", "", "", "") should return [0]')
        self.assertTrue(os.path.isdir('/tmp/pp') ==
                        False,'Directory /tmp/pp is present.')

    def testSetDirectoryAbsentError(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp", "", "Absent", "Directory", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/1.pp", "", "Absent", "Directory", "", "", "md5", "", "", "", "", "") should return [0]')

    def testSetCopyDirectoryToNew(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "") should return [0]')
        self.assertTrue(os.path.isdir('/tmp/pp') ==
                        True,'Directory /tmp/pp is missing.')
        self.assertTrue(nxFile.Set_Marshall("/tmp/ppp", "/tmp/pp", "Present", "Directory", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "") should return [0]')
        self.assertTrue(os.path.isdir('/tmp/ppp') ==
                        True,'Directory /tmp/ppp is missing.')
        
    def testSetCopyDirectoryToExistingForce(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "") should return [0]')
        self.assertTrue(os.path.isdir('/tmp/pp') ==
                        True,'Directory /tmp/pp is missing.')
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp/1.pp", "", "Present", "File", "", "These are the contents of 1.pp", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/pp/1.pp", "", "Present", "File", "", "These are the contents of 1.pp", "md5", "", "", "", "", "") should return [0]')
        d,e=nxFile.ReadFile('/tmp/pp/1.pp')
        self.assertTrue(d==
                        "These are the contents of 1.pp","File contents mismatch:"+d)
        self.assertTrue(nxFile.Set_Marshall("/tmp/ppp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "") should return [0]')
        self.assertTrue(os.path.isdir('/tmp/ppp') ==
                        True,'Directory /tmp/ppp is missing.')
        self.assertTrue(nxFile.Set_Marshall("/tmp/ppp/1.pp", "", "Present", "File", "", "These are the contents of 1.pp", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/ppp/1.pp", "", "Present", "File", "", "These are the contents of 1.pp", "md5", "", "", "", "", "") should return [0]')
        d,e=nxFile.ReadFile('/tmp/ppp/1.pp')
        self.assertTrue(d==
                        "These are the contents of 1.pp","File contents mismatch:"+d)
        self.assertTrue(nxFile.Set_Marshall("/tmp/ppp", "/tmp/pp", "Present", "Directory", "Force", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "") should return [0]')

    def testSetModeRecursive(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "") should return [0]')
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp/1.pp", "", "Present", "File", "", "These are the contents of 1.pp", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/pp/1.pp", "", "Present", "File", "", "These are the contents of 1.pp", "md5", "", "", "", "", "") should return [0]')
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp/12.pp", "", "Present", "File", "", "These are the contents of 12.pp", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/pp/12.pp", "", "Present", "File", "", "These are the contents of 12.pp", "md5", "", "", "", "", "") should return [0]')
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "", "", '755')==
                        [0],'nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "", "", 755) should return [0]')
        self.assertTrue((nxFile.StatFile('/tmp/pp/1.pp').st_mode & 0755 ) ==
                        0755 and (nxFile.StatFile('/tmp/pp/12.pp').st_mode & 0755) == 0755,'Mode of /tmp/pp/1.pp and /tmp/pp/12.pp should be 755')

    def testSetOwnerRecursive(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "") should return [0]')
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp/1.pp", "", "Present", "File", "", "These are the contents of 1.pp", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/pp/1.pp", "", "Present", "File", "", "These are the contents of 1.pp", "md5", "", "", "", "", "") should return [0]')
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp/12.pp", "", "Present", "File", "", "These are the contents of 12.pp", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/pp/12.pp", "", "Present", "File", "", "These are the contents of 12.pp", "md5", "", "", "", "", "") should return [0]')
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "", "mail", "")==
                        [0],'nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "", "mail", "") should return [0]')
        self.assertTrue(nxFile.StatFile('/tmp/pp/1.pp').st_gid ==
                        grp.getgrnam('mail')[2]  and nxFile.StatFile('/tmp/pp/12.pp').st_gid == grp.getgrnam('mail')[2] ,'Group of /tmp/pp/1.pp and /tmp/pp/12.pp should be mail')

    def testTestNoDestPathError(self):
        self.assertTrue(nxFile.Test_Marshall("", "", "Present", "File", "", "", "md5", "", "", "", "", "")==
                        [-1],'nxFile.Test_Marshall("/tmp/1.pp", "", "Present", "File", "", "", "md5", "", "", "", "", "") should return [-1]')

    def testTestFilePresentError(self):
        self.assertTrue(nxFile.Test_Marshall("/tp/1.pp", "", "Present", "File", "", "", "md5", "", "", "", "", "")==
                        [-1],'nxFile.Test_Marshall("/tp/1.pp", "", "Present", "File", "", "", "md5", "", "", "", "", "") should return [-1]')

    def testTestFilePresent(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "", "md5", "", "", "", "", "") should return [0]')
        self.assertTrue(nxFile.Test_Marshall("/tmp/1.pp", "", "Present", "File", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Test_Marshall("/tmp/1.pp", "", "Present", "File", "", "", "md5", "", "", "", "", "") should return [0]')

    def testTestFileAbsentError(self):
        self.assertTrue(nxFile.Test_Marshall("/tp/1.pp", "", "Absent", "File", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Test_Marshall("/tp/1.pp", "", "Absent", "File", "", "", "md5", "", "", "", "", "") should return [0]')

    def testTestFileAbsent(self):
        self.assertTrue(nxFile.Test_Marshall("/tp/1.pp", "", "Absent", "File", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Test_Marshall("/tp/1.pp", "", "Absent", "File", "", "", "md5", "", "", "", "", "") should return [0]')

    def testTestDirectoryRecurseCheckOwnerError(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "", "", "") should return [0]')
        self.assertTrue(nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "", "md5", "", "", "", "", "") should return [0]')
        self.assertTrue(nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "udos", "", "")==
                        [-1],'nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "udos", "", "") should return [-1]')

    def testTestDirectoryRecurseCheckGroupError(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "", "mail", "")==
                        [0],'nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "", "mail", "") should return [0]')
        self.assertTrue(nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "", "md5", "", "", "", "", "") should return [0]')
        self.assertTrue(nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "", "udos", "")==
                        [-1],'nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "", "udos", "") should return [-1]')

    def testTestDirectoryRecurseCheckModeError(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "", "", '755')==
                        [0],'nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "", "", 755) should return [0]')
        self.assertTrue(nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "", "md5", "", "", "", "", '755')==
                        [0],'nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "", "md5", "", "", "", "", 755) should return [0]')
        self.assertTrue(nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "", "", '744')==
                        [-1],'nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "", "", 744) should return [-1]')

    def testTestDirectoryRecurseCheckOwner(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "", "", "") should return [0]')
        self.assertTrue(nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "", "md5", "", "", "", "", "") should return [0]')
        me =  pwd.getpwuid(os.getuid()).pw_name
        self.assertTrue(nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", me, "", "")==
                        [0],'nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "'+me+'", "", "") should return [0]')

    def testTestDirectoryRecurseCheckGroup(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "", "mail", "") should return [0]')
        self.assertTrue(nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "", "md5", "", "", "", "", "") should return [0]')
        me = grp.getgrgid(os.getgid()).gr_name
        self.assertTrue(nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "", me, "")==
                        [0],'nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "'+me+'", "", "") should return [0]')

    def testTestDirectoryRecurseCheckMode(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "", "", '755')==
                        [0],'nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "", "", 755) should return [0]')
        self.assertTrue(nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "", "md5", "", "", "", "", '755')==
                        [0],'nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "", "md5", "", "", "", "", 755) should return [0]')
        self.assertTrue(nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "", "", '755')==
                        [0],'nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", True, "", "", "", 755) should return [0]')

    def testGetNoDestPathError(self):
        r=nxFile.Get_Marshall("", "", "Present", "File", "", "", "md5", "", "", "", "", "")
        self.assertTrue(check_values(r,self.make_MI(0,"", "", "present", "file", False, None, "md5", False, "", "", "", "",None)) == False
                        ,'nxFile.Get_Marshall("", "", "Present", "File", "", "", "md5", "", "", "", "", "") should return [-1]')

    def testGetFilePresent(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "", "md5", "", "", "", "", "")[0]==
                        0,'nxFile.Set_Marshall("/tmp/1.pp", "", "Present", "File", "", "", "md5", "", "", "", "", "") should return [0]')
        r=nxFile.Get_Marshall("/tmp/1.pp", "", "present", "file", "", "", "md5", "", "", "", "", "")
        self.assertTrue(check_values(r,self.make_MI(0,"/tmp/1.pp", "", "present", "file", False, None, "md5", False, "", None, None, None, None)) == True
                        ,'nxFile.Get_Marshall("/tmp/1.pp", "", "present", "file", "", "", "md5", "", "", "", "", "") should return [0]')

    def testGetDirectoryPresent(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "")[0]==
                        0,'nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "") should return [0]')
        self.assertTrue(nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "","", "")==
                        [0],'nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "") should return [0]')
        r=nxFile.Get_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "")
        self.assertTrue(check_values(r,self.make_MI(0,"/tmp/pp", "", "present", "directory",  \
                        False, None, "md5", False, "", None, None, None, None)) == True
                        ,'nxFile.Get_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "") should return [0]')

    def testTestDirectoryCheckOwnerError(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "") should return [0]')
        self.assertTrue(nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "udos", "", "")==
                        [-1],'nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "udos", "", "") should return [-1]')

    def testTestDirectoryCheckGroupError(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "mail", "")==
                        [0],'nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "mail", "") should return [0]')
        self.assertTrue(nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "udos", "")==
                        [-1],'nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "udos", "") should return [-1]')

    def testTestDirectoryCheckOwner(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "") should return [0]')
        me =  pwd.getpwuid(os.getuid()).pw_name
        self.assertTrue(nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", me, "", "")==
                        [0],'nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "'+me+'", "", "") should return [0]')

    def testTestDirectoryCheckGroup(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", "")==
                        [0],'nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "mail", "") should return [0]')
        me = grp.getgrgid(os.getgid()).gr_name
        self.assertTrue(nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", me, "")==
                        [0],'nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "'+me+'", "", "") should return [0]')

    def testTestDirectoryCheckMode(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", '776')==
                        [0],'nxFile.Set_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", 776) should return [0]')
        self.assertTrue(nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", '776')==
                        [0],'nxFile.Test_Marshall("/tmp/pp", "", "Present", "Directory", "", "", "md5", "", "", "", "", 776) should return [0]')

    def testRemoteFilePass(self):
        self.assertTrue(nxFile.Test_Marshall("/tmp/Python-2.4.6.tgz",\
               "https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "ctime", "", "", "", "", '776') ==
               [-1],'nxFile.Test(_Marshall("/tmp/Python-2.4.6.tgz",'+\
               '"https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "ctime", "", "", "", "", 776) should return [-1]')
        self.assertTrue(nxFile.Set_Marshall("/tmp/Python-2.4.6.tgz",\
               "https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "ctime", "", "", "", "", '776') ==
               [0],'nxFile.Set(_Marshall("/tmp/Python-2.4.6.tgz",'+\
               '"https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "ctime", "", "", "", "", 776) should return [0]')
        self.assertTrue(nxFile.Test_Marshall("/tmp/Python-2.4.6.tgz",\
               "https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "ctime", "", "", "", "", '776') ==
               [0],'nxFile.Test(_Marshall("/tmp/Python-2.4.6.tgz",'+\
               '"https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "ctime", "", "", "", "", 776) should return [0]')
                                                                                             

    def testRemoteFileMtimePass(self):
        self.assertTrue(nxFile.Test_Marshall("/tmp/Python-2.4.6.tgz",\
               "https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "mtime", "", "", "", "", '776') ==
               [-1],'nxFile.Test(_Marshall("/tmp/Python-2.4.6.tgz",'+\
               '"https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "mtime", "", "", "", "", 776) should return [-1]')
        self.assertTrue(nxFile.Set_Marshall("/tmp/Python-2.4.6.tgz",\
               "https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "mtime", "", "", "", "", '776') ==
               [0],'nxFile.Set(_Marshall("/tmp/Python-2.4.6.tgz",'+\
               '"https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "mtime", "", "", "", "", 776) should return [0]')
        self.assertTrue(nxFile.Test_Marshall("/tmp/Python-2.4.6.tgz",\
               "https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "mtime", "", "", "", "", '776') ==
               [0],'nxFile.Test(_Marshall("/tmp/Python-2.4.6.tgz",'+\
               '"https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "mtime", "", "", "", "", 776) should return [0]')


    def testRemoteFileMD5Pass(self):
        self.assertTrue(nxFile.Test_Marshall("/tmp/Python-2.4.6.tgz",\
               "https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "md5", "", "", "", "", '776') ==
               [-1],'nxFile.Test(_Marshall("/tmp/Python-2.4.6.tgz",'+\
               '"https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "md5", "", "", "", "", 776) should return [-1]')
        self.assertTrue(nxFile.Set_Marshall("/tmp/Python-2.4.6.tgz",\
               "https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "md5", "", "", "", "", '776') ==
               [0],'nxFile.Set(_Marshall("/tmp/Python-2.4.6.tgz",'+\
               '"https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "md5", "", "", "", "", 776) should return [0]')
        self.assertTrue(nxFile.Test_Marshall("/tmp/Python-2.4.6.tgz",\
               "https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "md5", "", "", "", "", '776') ==
               [0],'nxFile.Test(_Marshall("/tmp/Python-2.4.6.tgz",'+\
               '"https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "md5", "", "", "", "", 776) should return [0]')

    def testRemoteFileMtimeFail(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/Python-2.4.6.tgz",\
               "https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "mtime", "", "", "", "", '776') ==
               [0],'nxFile.Set(_Marshall("/tmp/Python-2.4.6.tgz",'+\
               '"https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "mtime", "", "", "", "", 776) should return [-1]')
        os.utime('/tmp/Python-2.4.6.tgz',(0,0))
        self.assertTrue(nxFile.Test_Marshall("/tmp/Python-2.4.6.tgz",\
               "https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "mtime", "", "", "", "", '776') ==
               [-1],'nxFile.Test(_Marshall("/tmp/Python-2.4.6.tgz",'+\
               '"https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "mtime", "", "", "", "", 776) should return [-1]')


    def testRemoteFileMD5Fail(self):
        self.assertTrue(nxFile.Set_Marshall("/tmp/Python-2.4.6.tgz",\
               "https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "md5", "", "", "", "", '776') ==
                [0],'nxFile.Set(_Marshall("/tmp/Python-2.4.6.tgz",'+\
               '"https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "md5", "", "", "", "", 776) should return [0]')
        os.system('ls >> /tmp/Python-2.4.6.tgz')
        self.assertTrue(nxFile.Test_Marshall("/tmp/Python-2.4.6.tgz",\
               "https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "md5", "", "", "", "", '776') ==
               [-1],'nxFile.Test(_Marshall("/tmp/Python-2.4.6.tgz",'+\
               '"https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "md5", "", "", "", "", 776) should return [-1]')

    def testRemoteFileBadUrl(self):
        self.assertTrue(nxFile.Test_Marshall("/tmp/Python-2.4.6.tgz",\
               "https://www.python.org/ftp/python/2.4.6/Python-2.4.6.nope", "Present", "File", "", "", "md5", "", "", "", "", '776') ==
               [-1],'nxFile.Test(_Marshall("/tmp/Python-2.4.6.tgz",'+\
               '"https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz", "Present", "File", "", "", "md5", "", "", "", "", 776) should return [-1]')

dummy_service_file=r"""#!/usr/bin/env python
from __future__ import with_statement

import time
import os

with open('/var/run/dummy_service.pid','w') as F: 
        F.write(str(os.getpid()) + "\n")
        F.flush()
        F.close()
while True:
    time.sleep(5)
    with open('/tmp/dummy_service.log','a') as F: 
        F.write('dummy_service is running at '+time.asctime()+'\n')
        F.flush()
        F.close()
"""

#sample init files for testing
upstart_etc_default="""# To disable , set DUMMY_SERVICE_ENABLED=0
DUMMY_SERVICE_ENABLED=1
"""

upstart_init_conf="""description "dummy_service"
author "Eric Gable"
export PATH=$PATH:/usr/local/bin
start on mounted MOUNTPOINT=/
stop on runlevel [!2345]

pre-start script

    [ -r /etc/default/dummy_service ] && . /etc/default/dummy_service

    if [ "$DUMMY_SERVICE_ENABLED" != "1" ]; then
        stop ; exit 0
    fi

    if [ ! -x /usr/sbin/dummy_service.py ]; then
        stop ; exit 0
    fi

    #Load the udf module
    modprobe -b udf

end script

exec /usr/sbin/dummy_service.py -daemon
"""

upstart_init_d_file = """#!/bin/sh -e
# upstart-job
#
# Symlink target for initscripts that have been converted to Upstart.

set -e

UPSTART_JOB_CONF="/etc/default/upstart-job"
INITSCRIPT="$(basename "$0")"
JOB="${INITSCRIPT%.sh}"

if [ "$JOB" = "upstart-job" ]; then
    if [ -z "$1" ]; then
        echo "Usage: upstart-job JOB COMMAND" 1>&2
	exit 1
    fi

    JOB="$1"
    INITSCRIPT="$1"
    shift
else
    if [ -z "$1" ]; then
        echo "Usage: $0 COMMAND" 1>&2
	exit 1
    fi
fi

COMMAND="$1"
shift

ECHO=echo
ECHO_ERROR=echo
if [ -e "$UPSTART_JOB_CONF" ]; then
	. "$UPSTART_JOB_CONF"
fi
if [ -n "$DPKG_MAINTSCRIPT_PACKAGE" ]; then
	ECHO=:
	ECHO_ERROR=:
fi

$ECHO "Rather than invoking init scripts through /etc/init.d, use the service(8)"
$ECHO "utility, e.g. service $INITSCRIPT $COMMAND"

# Only check if jobs are disabled if the currently _running_ version of
# Upstart (which may be older than the latest _installed_ version)
# supports such a query.
#
# This check is necessary to handle the scenario when upgrading from a
# release without the 'show-config' command (introduced in
# Upstart for Ubuntu version 0.9.7) since without this check, all
# installed packages with associated Upstart jobs would be considered
# disabled.
#
# Once Upstart can maintain state on re-exec, this change can be
# dropped (since the currently running version of Upstart will always
# match the latest installed version).

UPSTART_VERSION_RUNNING=$(initctl version|awk '{print $3}'|tr -d ')')

if dpkg --compare-versions "$UPSTART_VERSION_RUNNING" ge 0.9.7
then
    initctl show-config -e "$JOB"|grep -q '^  start on' || DISABLED=1
fi

case $COMMAND in
status)
    $ECHO
    $ECHO "Since the script you are attempting to invoke has been converted to an"
    $ECHO "Upstart job, you may also use the $COMMAND(8) utility, e.g. $COMMAND $JOB"
    $COMMAND "$JOB"
    ;;
start|stop)
    $ECHO
    $ECHO "Since the script you are attempting to invoke has been converted to an"
    $ECHO "Upstart job, you may also use the $COMMAND(8) utility, e.g. $COMMAND $JOB"
    if status "$JOB" 2>/dev/null | grep -q ' start/'; then
        RUNNING=1
    fi
    if [ -z "$RUNNING" ] && [ "$COMMAND" = "stop" ]; then
        exit 0
    elif [ -n "$RUNNING" ] && [ "$COMMAND" = "start" ]; then
        exit 0
    elif [ -n "$DISABLED" ] && [ "$COMMAND" = "start" ]; then
        exit 0
    fi
    $COMMAND "$JOB"
    ;;
restart)
    $ECHO
    $ECHO "Since the script you are attempting to invoke has been converted to an"
    $ECHO "Upstart job, you may also use the stop(8) and then start(8) utilities,"
    $ECHO "e.g. stop $JOB ; start $JOB. The restart(8) utility is also available."
    if status "$JOB" 2>/dev/null | grep -q ' start/'; then
        RUNNING=1
    fi
    if [ -n "$RUNNING" ] ; then
        stop "$JOB"
    fi
    # If the job is disabled and is not currently running, the job is
    # not restarted. However, if the job is disabled but has been forced into the
    # running state, we *do* stop and restart it since this is expected behaviour
    # for the admin who forced the start.
    if [ -n "$DISABLED" ] && [ -z "$RUNNING" ]; then
        exit 0
    fi
    start "$JOB"
    ;;
reload|force-reload)
    $ECHO
    $ECHO "Since the script you are attempting to invoke has been converted to an"
    $ECHO "Upstart job, you may also use the reload(8) utility, e.g. reload $JOB"
    reload "$JOB"
    ;;
*)
    $ECHO_ERROR
    $ECHO_ERROR "The script you are attempting to invoke has been converted to an Upstart" 1>&2
    $ECHO_ERROR "job, but $COMMAND is not supported for Upstart jobs." 1>&2
    exit 1
esac
"""

debian_init_file = """#!/bin/sh
### BEGIN INIT INFO
# Provides:          dummy_service
# Required-Start:    $network $syslog
# Required-Stop:     $network $syslog
# Should-Start:      $network $syslog
# Should-Stop:       $network $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: dummy_service
# Description:       dummy_service
### END INIT INFO

. /lib/lsb/init-functions

OPTIONS="-daemon"
WAZD_BIN=/usr/sbin/dummy_service.py
WAZD_PID=/var/run/dummy_service.pid

case "$1" in
    start)
        log_begin_msg "Starting dummy_service..."
        pid=$( pidofproc -p $WAZD_PID $WAZD_BIN)
        if [ -n "$pid" ] ; then
              log_begin_msg "Already running."
              log_end_msg 0
              exit 0
        fi
        start-stop-daemon --start --quiet --oknodo --background --exec $WAZD_BIN -- $OPTIONS
        log_end_msg $?
        ;;

    stop)
        log_begin_msg "Stopping dummy_service..."
        start-stop-daemon --stop --quiet --oknodo --pidfile $WAZD_PID
        ret=$?
        rm -f $WAZD_PID
        log_end_msg $ret
        ;;
    force-reload)
        $0 restart
        ;;
    restart)
        $0 stop
        $0 start
        ;;
    status)
	status_of_proc -p $WAZD_PID $WAZD_BIN && exit 0 || exit $?
        ;;
    *)
        log_success_msg "Usage: /etc/init.d/dummy_service {start|stop|force-reload|restart|status}"
        exit 1
        ;;
esac

exit 0
"""

suse_init_file = """#! /bin/sh
#
#
# /etc/init.d/dummy_service
#
#  and symbolic link
#
# /usr/sbin/rcdummy_service
#
# System startup script for the dummy_service 
#
### BEGIN INIT INFO
# Provides: dummy_service
# Required-Start: $network sshd
# Required-Stop: $network sshd
# Default-Start: 3 5
# Default-Stop: 0 1 2 6
# Description: Start the dummy_service
### END INIT INFO

PYTHON=/usr/bin/python
WAZD_BIN=/usr/sbin/dummy_service.py
WAZD_PIDFILE=/var/run/dummy_service.pid

test -x "$WAZD_BIN" || { echo "$WAZD_BIN not installed"; exit 5; }

. /etc/rc.status

# First reset status of this service
rc_reset

# Return values acc. to LSB for all commands but status:
# 0 - success
# 1 - misc error
# 2 - invalid or excess args
# 3 - unimplemented feature (e.g. reload)
# 4 - insufficient privilege
# 5 - program not installed
# 6 - program not configured
#
# Note that starting an already running service, stopping
# or restarting a not-running service as well as the restart
# with force-reload (in case signalling is not supported) are
# considered a success.

case "$1" in
    start)
        echo -n "Starting dummy_service"
        ## Start daemon with startproc(8). If this fails
        ## the echo return value is set appropriate.
        startproc -f ${PYTHON} ${WAZD_BIN} -daemon
        rc_status -v
        ;;
    stop)
        echo -n "Shutting down dummy_service"
        ## Stop daemon with killproc(8) and if this fails
        ## set echo the echo return value.
        killproc -p ${WAZD_PIDFILE} ${PYTHON} ${WAZD_BIN}
        rc_status -v
        ;;
    try-restart)
        ## Stop the service and if this succeeds (i.e. the
        ## service was running before), start it again.
        $0 status >/dev/null && $0 restart
        rc_status
        ;;
    restart)
        ## Stop the service and regardless of whether it was
        ## running or not, start it again.
        $0 stop
        sleep 1
        $0 start
        rc_status
        ;;
    force-reload|reload)
        rc_status
        ;;
    status)
        echo -n "Checking for service dummy_service "
        ## Check status with checkproc(8), if process is running
        ## checkproc will return with exit status 0.

        checkproc -p ${WAZD_PIDFILE} ${PYTHON} ${WAZD_BIN}
        rc_status -v
        ;;
    probe)
        ;;
    *)
        echo "Usage: $0 {start|stop|status|try-restart|restart|force-reload|reload}"
        exit 1
        ;;
esac
rc_exit
"""

redhat_init_file= """#!/bin/bash
#
# Init file for dummy_service.
#
# chkconfig: 2345 60 80
# description: dummy_service
# pidfile: /var/run/dummy_service.pid
# processname dummy_service.py
# source function library
. /etc/rc.d/init.d/functions

RETVAL=0
FriendlyName="dummy_service"
WAZD_BIN=/usr/sbin/dummy_service.py

start()
{
    echo -n $"Starting $FriendlyName: "
    $WAZD_BIN &
}

stop()
{
    echo -n $"Stopping $FriendlyName: "
    killproc -p /var/run/dummy_service.pid $WAZD_BIN
    RETVAL=$?
    echo
    return $RETVAL
}

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        stop
        start
        ;;
    reload)
        ;;
    report)
        ;;
    status)
        status $FriendlyName
        RETVAL=$?
        ;;
    *)
        echo $"Usage: $0 {start|stop|restart|status}"
        RETVAL=1
esac
exit $RETVAL
"""

ubuntu_systemd_init_file="""
[Unit]
Description=Dummy Service
After=network.target
[Service]
Type=simple
PIDFile=/var/run/dummy_service.pid
ExecStart=/usr/bin/python /usr/sbin/dummy_service.py
ExecStop=rm -f /var/run/dummy_service.pid
KillMode=process
KillSignal=SIGKILL
TimeoutStartSec=10

[Install]
WantedBy=multi-user.target
"""


class nxServiceTestCases(unittest2.TestCase):
    """
    Test cases for nxService
    """
    def setUp(self):
        """
        Setup test resources
        """
        self.controller = None
        nxService.SetShowMof(True)
        print self.id() + '\n'
        dist=platform.dist()[0].lower()
        init_file=''
        if 'suse' in dist:
            init_file=suse_init_file
        elif 'ubuntu' in dist:
            if nxService.SystemdExists():
                init_file=ubuntu_systemd_init_file
        elif 'redhat' in dist:
            init_file=redhat_init_file
        elif 'cent' in dist:
            init_file=redhat_init_file
            if nxService.SystemdExists():
                init_file=ubuntu_systemd_init_file
        elif 'debian' in dist:
            init_file=debian_init_file
        if nxService.SystemdExists():
            self.controller='systemd'
            try:
                if 'ubuntu' in dist or 'cent' in dist:
                    nxService.WriteFile('/lib/systemd/system/dummy_service.service',init_file)
                    os.chmod('/lib/systemd/system/dummy_service.service',0744)
                else:
                    nxService.WriteFile('/etc/rc.d/dummy_service',init_file)
                    os.chmod('/etc/rc.d/dummy_service',0744)
                nxService.WriteFile('/usr/sbin/dummy_service.py',dummy_service_file)
                os.chmod('/usr/sbin/dummy_service.py',0744)
            except:
                print repr(sys.exc_info())
            os.system('systemctl --system daemon-reload 2> /dev/null')
        elif nxService.UpstartExists():
            self.controller='upstart'
            try:
                nxService.WriteFile('/etc/default/dummy_service',upstart_etc_default)
                os.chmod('/etc/default/dummy_service',0744)
                nxService.WriteFile('/etc/init/dummy_service.conf',upstart_init_conf)
                nxService.WriteFile('/etc/init.d/dummy_service',upstart_init_d_file)
                os.chmod('/etc/init.d/dummy_service',0744)
                nxService.WriteFile('/usr/sbin/dummy_service.py',dummy_service_file)
                os.chmod('/usr/sbin/dummy_service.py',0744)
            except:
                print repr(sys.exc_info())

        elif nxService.InitExists():
            self.controller='init'
            try:
                nxService.WriteFile('/etc/init.d/dummy_service',init_file)
                os.chmod('/etc/init.d/dummy_service',0744)
                nxService.WriteFile('/usr/sbin/dummy_service.py',dummy_service_file)
                os.chmod('/usr/sbin/dummy_service.py',0744)
            except:
                print repr(sys.exc_info())
            

    def tearDown(self):
        """
        Remove test resources.
        """
        dist=platform.dist()[0].lower()
        if nxService.SystemdExists():
            os.system('systemctl disable dummy_service 2> /dev/null')
            if 'ubuntu' in dist or 'debian' in dist  or 'cent' in dist:
                os.system('rm /usr/sbin/dummy_service.py /lib/systemd/system/dummy_service.' + \
                          'service /etc/systemd/system/multi-user.target.wants/dummy_service.service 2> /dev/null')
            else:
                os.system('rm /usr/sbin/dummy_service.py /etc/rc.d/dummy_service 2> /dev/null')
            os.system('systemctl --system daemon-reload 2> /dev/null')
        elif nxService.UpstartExists():
            os.system('update-rc.d -f dummy_service remove 2> /dev/null')
            os.system('rm /usr/sbin/dummy_service.py /etc/init/dummy_service.conf /etc/init.d/dummy_service /etc/default/dummy_service 2> /dev/null')
        elif nxService.InitExists():
            os.system('chkconfig --del dummy_service 2> /dev/null')
            os.system('rm /usr/sbin/dummy_service.py /etc/init.d/dummy_service 2> /dev/null')
            
        time.sleep(1)
        os.system("ps -ef | grep -v grep | grep dummy_service | awk '{print $2}' | xargs -L1 kill 2> /dev/null")

    def CheckInventory(self, Name, Controller, Enabled, State, Inventory):
        if len(Inventory['__Inventory'].value) < 1:
            return False
        for i in Inventory['__Inventory'].value:
            if Name != None and len(Name) and not fnmatch.fnmatch(i['Name'].value,Name):
                print 'Name:' + Name + ' != ' + i['Name'].value
                return False
            if Enabled is not None and Enabled != i['Enabled'].value.value:
                print 'Enabled:' + repr(Enabled) + ' != ' + repr(i['Enabled'].value.value)
                return False
            if State != None and len(State) and not fnmatch.fnmatch(i['State'].value,State):
                print 'State:' + State + ' != ' + i['State'].value
                return False
        return True

    def make_MI(self,retval, Name, Controller, Enabled, State, Path, Description, Runlevels):
        d=dict();
        if Name == None :
            d['Name'] = None
        else :
            d['Name'] = nxService.protocol.MI_String(Name)
        if Controller == None :
            d['Controller'] = None
        else :
            d['Controller'] = nxService.protocol.MI_String(Controller)
        if Enabled == None :
            d['Enabled'] = None
        else :
            d['Enabled'] = nxService.protocol.MI_Boolean(Enabled)
        if State == None :
            d['State'] = None
        else :
            d['State'] = nxService.protocol.MI_String(State)
        if Path == None :
            d['Path'] = None
        else :
            d['Path'] = nxService.protocol.MI_String(Path)
        if Description == None :
            d['Description'] = None
        else :
            d['Description'] = nxService.protocol.MI_String(Description)
        if Runlevels == None :
            d['Runlevels'] = None
        else :
            d['Runlevels'] = nxService.protocol.MI_String(Runlevels)
        return retval,d

    def testSetEnable(self):
        controller=self.controller
        self.assertTrue(nxService.Set_Marshall("dummy_service", controller, True, "running")==
                        [0],'nxService.Set_Marshall("dummy_service", "'+controller+'", True, "running") should return ==[0]')

    def testSetDisable(self):
        controller=self.controller
        self.assertTrue(nxService.Set_Marshall("dummy_service", controller, True, "running")==
                        [0],'nxService.Set_Marshall("dummy_service", "'+controller+'", True, "running") should return ==[0]')
        self.assertTrue(nxService.Set_Marshall("dummy_service", controller, False, "stopped")==
                        [0],'nxService.Set_Marshall("dummy_service", "'+controller+'", False, "stopped") should return ==[0]')

    def testSetEnableError(self):
        controller=self.controller
        self.assertTrue(nxService.Set_Marshall("yummyservice", controller, True, "running")==
                        [-1],'nxService.Set_Marshall("yummyservice", "'+controller+'", True, "running") should return ==[-1]')

    def testSetDisableError(self):
        controller=self.controller
        self.assertTrue(nxService.Set_Marshall("yummyservice", controller, False, "stopped")==
                        [-1],'nxService.Set_Marshall("yummyservice", "'+controller+'", False, "stopped") should return ==[-1]')

    def testGetEnable(self):
        controller=self.controller
        self.assertTrue(nxService.Set_Marshall("dummy_service", controller, True, "running")==
                        [0],'nxService.Set_Marshall("dummy_service", "'+controller+'", True, "running") should return ==[0]')
        r=nxService.Get_Marshall("dummy_service", controller, True, "running")

        self.assertTrue(check_values(r,self.make_MI(0,"dummy_service", controller, True, "running",None,None,None)) == True
                        ,'nxService.Get_Marshall("dummy_service", "'+controller+'", True, "running") should return ==[0]')

    def testGetDisable(self):
        controller=self.controller
        self.assertTrue(nxService.Set_Marshall("dummy_service", controller, True, "running")==
                        [0],'nxService.Set_Marshall("dummy_service", "'+controller+'", True, "running") should return ==[0]')
        self.assertTrue(nxService.Set_Marshall("dummy_service", controller, False, "stopped")==
                        [0],'nxService.Set_Marshall("dummy_service", "'+controller+'", False, "stopped") should return ==[0]')
        r=nxService.Get_Marshall("dummy_service", controller, False, "stopped")

        self.assertTrue(check_values(r,self.make_MI(0,"dummy_service", controller, False, "stopped", None, None, None)) == True
                        ,'nxService.Get_Marshall("dummy_service", "'+controller+'", False, "stopped") should return ==[0,"dummy_service", controller, False, "stopped"]')

    def testGetEnableError(self):
        controller=self.controller
        self.assertTrue(nxService.Set_Marshall("yummyservice", controller, True, "running")==
                        [-1],'nxService.Set_Marshall("yummyservice", "'+controller+'", True, "running") should return ==[-1]')
        r=nxService.Get_Marshall("yummyservice", controller, True, "running")

        self.assertTrue(check_values(r,self.make_MI(0,"yummyservice", controller, True, "running", None, None, None)) == False
                        ,'nxService.Get_Marshall("yummyservice", "'+controller+'", True, "running")[0:5] should return ==[-1,"yummyservice", controller, True, "running"]')

    def testGetDisableError(self):
        controller=self.controller
        self.assertTrue(nxService.Set_Marshall("yummyservice", controller, False, "stopped")==
                        [-1],'nxService.Set_Marshall("yummyservice", "'+controller+'", False, "stopped") should return ==[-1]')
        r=nxService.Get_Marshall("yummyservice", controller, False, "stopped")

        self.assertTrue(check_values(r,self.make_MI(0,"yummyservice", controller, False, "stopped", None, None, None)) == False
                        ,'nxService.Get_Marshall("yummyservice", "'+controller+'", False, "stopped")[0:5] should return ==[-1,"yummyservice", controller, False, "stopped"]')

    def testInventoryMarshall(self):
        r=nxService.Inventory_Marshall('*', self.controller, None,'')
        self.assertTrue(r[0] == 0,"Inventory_Marshall('*', " + self.controller + ", None,'')  should return == 0")


    def testInventoryMarshallCmdlineError(self):
        os.system('cp  ./Scripts/nxService.py /tmp/nxServiceBroken.py')
        os.system('sed -i "s/cmd =  initd_service + \' --status-all \'/cmd =  initd_service + \' --atus-all \'/" /tmp/nxServiceBroken.py')
        os.system('sed -i "s/cmd = initd_chkconfig + \' --list \'/cmd = initd_chkconfig + \' --ist \'/" /tmp/nxServiceBroken.py')
        os.system('sed -i "s/cmd = \'initctl list\'/cmd = \'initctl ist\'/" /tmp/nxServiceBroken.py')
        os.system('sed -i "s/cmd = \'systemctl -a list-unit-files \'/cmd = \'systemctl -a ist-unit-files \'/" /tmp/nxServiceBroken.py')
        nxServiceBroken = imp.load_source('nxServiceBroken','/tmp/nxServiceBroken.py') 
        r=nxServiceBroken.Inventory_Marshall('*', self.controller, None,'')
        os.system('rm /tmp/nxServiceBroken.py')
        self.assertTrue(r[0] == -1,"nxServiceBroken.Inventory_Marshall('*', " + self.controller + ", None,'')  should return == -1")


    def testInventoryMarshallControllerWildcard(self):
        r=nxService.Inventory_Marshall('*', '*', None,'')
        self.assertTrue(r[0] == 0,"Inventory_Marshall('*', '*', None,'')  should return == 0")


    def testInventoryMarshallControllerError(self):
        controllers = ['systemd', 'upstart', 'init']
        controllers.remove(self.controller)
        r=nxService.Inventory_Marshall('*', controllers[0], None,'')
        self.assertTrue(r[0] == -1,"Inventory_Marshall('*', " + self.controller + ", None,'')  should return == -1")


    def testInventoryMarshallDummyService(self):
        self.assertTrue(nxService.Set_Marshall("dummy_service", self.controller, True, "running")==
                        [0],'nxService.Set_Marshall("dummy_service", "'+self.controller+'", True, "running") should return ==[0]')
        r=nxService.Inventory_Marshall('dummy_service', self.controller, None,'')
        self.assertTrue(r[0] == 0,"Inventory_Marshall('dummy_service', " + self.controller + ", None,'')  should return == 0")
        self.assertTrue(self.CheckInventory('dummy_service', self.controller, None, '', r[1]) == True, \
                        'CheckInventory("dummy_service", self.controller, None, "", r[1]) should == True')

    def testInventoryMarshallDummyServiceFilterName(self):
        self.assertTrue(nxService.Set_Marshall("dummy_service", self.controller, True, "running")==
                        [0],'nxService.Set_Marshall("dummy_service", "'+self.controller+'", True, "running") should return ==[0]')
        r=nxService.Inventory_Marshall('dummy?*ice', self.controller, None,'')
        self.assertTrue(r[0] == 0,"Inventory_Marshall('dummy?*ice', " + self.controller + ", None,'')  should return == 0")
        self.assertTrue(self.CheckInventory('dummy?*ice', self.controller, None, '', r[1]) == True, \
                        'CheckInventory("dummy?*ice", ' + self.controller + ', None, "", r[1]) should == True')

    @unittest2.skipIf(nxService.UpstartExists() == True,'Not implemented in upstart')
    def testInventoryMarshallDummyServiceFilterEnabled(self):
        self.assertTrue(nxService.Set_Marshall("dummy_service", self.controller, True, "running")==
                        [0],'nxService.Set_Marshall("dummy_service", "'+self.controller+'", True, "running") should return ==[0]')
        r=nxService.Inventory_Marshall('dummy?*ice', self.controller, True,'')
        self.assertTrue(r[0] == 0,"Inventory_Marshall('dummy?*ice', " + self.controller + ", True,'')  should return == 0")
        self.assertTrue(self.CheckInventory('dummy?*ice', self.controller, True, '', r[1]) == True, \
                        'CheckInventory("dummy?*ice", ' + self.controller + ', True, "", r[1]) should == True')

#     def testInventoryMarshallDummyServiceFilterState(self):
#         # This test inconsistantly fails on slower systems.  The sleep here reduces these failures.
#         time.sleep(3)
#         self.assertTrue(nxService.Set_Marshall("dummy_service", self.controller, True, "running")==
#                         [0],'nxService.Set_Marshall("dummy_service", "'+self.controller+'", True, "running") should return ==[0]')
#         r=nxService.Inventory_Marshall('dummy?*ice', self.controller, None,'running')
#         self.assertTrue(r[0] == 0,"Inventory_Marshall('dummy?*ice', " + self.controller + ", None,'running')  should return == 0")
#         self.assertTrue(self.CheckInventory('dummy?*ice', self.controller, None, 'running', r[1]) == True, \
#                         'CheckInventory("dummy?*ice", ' + self.controller + ', None, "running", r[1]) should == True')

    def testInventoryMarshallDummyServiceFilterNameError(self):
        # This test inconsistantly fails on slower systems.  The sleep here reduces these failures.
        time.sleep(3)
        self.assertTrue(nxService.Set_Marshall("dummy_service", self.controller, True, "running")==
                        [0],'nxService.Set_Marshall("dummy_service", "'+self.controller+'", True, "running") should return ==[0]')
        r=nxService.Inventory_Marshall('Gummy_service', self.controller, None,'')
        self.assertTrue(r[0] == 0, "Inventory_Marshall('Gummy_service', " + self.controller + ", None,'')  should return == 0")
        self.assertTrue(self.CheckInventory('Gummy_service', self.controller, None, '', r[1]) == False, \
                        'CheckInventory("Gummy_service", self.controller, None, "", r[1]) should == False')

    def testInventoryMarshallDummyServiceFilterEnabledError(self):
        # This test inconsistantly fails on slower systems.  The sleep here reduces these failures.
        time.sleep(3)
        self.assertTrue(nxService.Set_Marshall("dummy_service", self.controller, True, "running")==
                        [0],'nxService.Set_Marshall("dummy_service", "'+self.controller+'", True, "running") should return ==[0]')
        r=nxService.Inventory_Marshall('dummy?*ice', self.controller, False,'')
        self.assertTrue(r[0] == 0,"Inventory_Marshall('dummy?*ice', " + self.controller + ", False,'')  should return == 0")
        self.assertTrue(self.CheckInventory('dummy?*ice', self.controller, False, '', r[1]) == False, \
                        'CheckInventory("dummy?*ice", ' + self.controller + ', False, "", r[1]) should == False')

    def testInventoryMarshallDummyServiceFilterStateError(self):
        # This test inconsistantly fails on slower systems.  The sleep here reduces these failures.
        time.sleep(3)
        self.assertTrue(nxService.Set_Marshall("dummy_service", self.controller, True, "running")==
                        [0],'nxService.Set_Marshall("dummy_service", "'+self.controller+'", True, "running") should return ==[0]')
        r=nxService.Inventory_Marshall('dummy?*ice', self.controller, None,'stopped')
        self.assertTrue(r[0] == 0,"Inventory_Marshall('dummy?*ice', " + self.controller + ", None,'stopped')  should return == 0")
        self.assertTrue(self.CheckInventory('dummy?*ice', self.controller, None, 'stopped', r[1]) == False, \
                        'CheckInventory("dummy?*ice", ' + self.controller + ', None, "stopped", r[1]) should == False')

    def testInventoryMarshallNoStderr(self):
        code, out = nxService.RunGetOutputNoStderr('ls -l /tmp/bad/path', False, True)
        self.assertTrue(code !=0 and len(out) == 0, "code, out = nxService.RunGetOutputNoStderr('ls -l /tmp/bad/path', False, True) \
        should be code !=0 and len(out) == 0")

 
class nxSshAuthorizedKeysTestCases(unittest2.TestCase):
    """
    Test cases for nxSshAuthorizedKeys.py
    """
    def setUp(self):
        """
        Setup test resources
        """
        self.mykey='MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDLXp6PkCtbpV+P1gwFQWH6Ez0U83uEmS8IGnpeI8Fk8rY/vHOZzZZaxRCw+loyc342qCDIQheMOCNm5Fkevz06q757/oooiLR3yryYGKiKG1IZIiplmtsC95oKrzUSKk60wuI1mbgpMUP5LKi/Tvxes5PmkUtXfimz2qgkeUcPpQIDAQAB'
        if os.system('grep -q jojoma /etc/passwd'):
            nxUser.Set_Marshall("jojoma", "Present", "JO JO MA", "JOJOMA", 'badpass', False, False, "/home/jojoma", "mail" )    
        path='/home/jojoma/.ssh/authorized_keys'
        if not os.path.isfile(path):
            os.system('echo '+ self.mykey + ' > ' + path +' ; echo ' + self.mykey +' >> ' + path )
        os.system('cp -p ' + path + ' /tmp/')
        nxSshAuthorizedKeys.SetShowMof(True)
        print self.id() + '\n'

    def tearDown(self):
        """
        Remove test resources.
        """
        path='/home/jojoma/.ssh/authorized_keys'
        os.system('rm -rf ' + path + ' 2> /dev/null')

    def make_MI(self,retval, KeyComment, Ensure, UserName, Key):
        d=dict();
        if KeyComment == None :
            d['KeyComment'] = None
        else :
            d['KeyComment'] = nxSshAuthorizedKeys.protocol.MI_String(KeyComment)
        if Ensure == None :
            d['Ensure'] = None
        else :
            d['Ensure'] = nxSshAuthorizedKeys.protocol.MI_String(Ensure)
        if UserName == None :
            d['UserName'] = None
        else :
            d['UserName'] = nxSshAuthorizedKeys.protocol.MI_String(UserName)
        if Key == None :
            d['Key'] = None
        else :
            d['Key'] = nxSshAuthorizedKeys.protocol.MI_String(Key)
        return retval,d

    def testSetKeyPresentTwice(self):
        self.assertTrue(nxSshAuthorizedKeys.Set_Marshall('MyKey','Present','jojoma',self.mykey) ==
                        [0],"assert nxSshAuthorizedKeys.Set_Marshall('MyKey','Present','jojoma',key) should be == [0]")
        # do this twice to prove there is no error if the same key already exists
        self.assertTrue(nxSshAuthorizedKeys.Set_Marshall('MyKey','Present','jojoma',self.mykey) ==
                        [0],"assert nxSshAuthorizedKeys.Set_Marshall('MyKey','Present','jojoma',key) should be == [0]")

    def testSetKeyAbsentTwice(self):
        self.assertTrue(nxSshAuthorizedKeys.Set_Marshall('MyKey','Present','jojoma',self.mykey) ==
                        [0],"assert nxSshAuthorizedKeys.Set_Marshall('MyKey','Present','jojoma',key) should be == [0]")
        self.assertTrue(nxSshAuthorizedKeys.Set_Marshall('MyKey','Absent','jojoma',self.mykey) ==
                        [0],"assert nxSshAuthorizedKeys.Set_Marshall('MyKey','Absent','jojoma',key) should be == [0]")
        self.assertTrue(nxSshAuthorizedKeys.Set_Marshall('MyKey','Absent','jojoma',self.mykey) ==
                        [0],"assert nxSshAuthorizedKeys.Set_Marshall('MyKey','Absent','jojoma',key) should be == [0]")

    def testTestKeyPresent(self):
        self.assertTrue(nxSshAuthorizedKeys.Set_Marshall('MyKey','Present','jojoma',self.mykey) ==
                        [0],"assert nxSshAuthorizedKeys.Set_Marshall('MyKey','Present','jojoma',key) should be == [0]")
        self.assertTrue(nxSshAuthorizedKeys.Test_Marshall('MyKey','Present','jojoma',self.mykey) ==
                        [0],"assert nxSshAuthorizedKeys.Test_Marshall('MyKey','Present','jojoma',key) should be == [0]")
        
    def testTestKeyPresentError(self):
        self.assertTrue(nxSshAuthorizedKeys.Test_Marshall('MyKey','Present','jojoma',self.mykey) ==
                        [-1],"assert nxSshAuthorizedKeys.Test_Marshall('MyKey','Present','jojoma',key) should be == [-1]")
        
    def testGetKeyPresent(self):
        self.assertTrue(nxSshAuthorizedKeys.Set_Marshall('MyKey','Present','jojoma',self.mykey) ==
                        [0],"assert nxSshAuthorizedKeys.Set_Marshall('MyKey','Present','jojoma',key) should be == [0]")
        r=nxSshAuthorizedKeys.Get_Marshall('MyKey','Present','jojoma',self.mykey)
        self.assertTrue(check_values(r,self.make_MI(0,'MyKey','present','jojoma',self.mykey)) == True
                        ,"assert nxSshAuthorizedKeys.Get_Marshall('MyKey','Present','jojoma',key)[0] should be == 0")
        
    def testTestKeyPresentBadUser(self):
        self.assertTrue(nxSshAuthorizedKeys.Test_Marshall('MyKey','Present','jojoma',self.mykey) ==
                        [-1],"assert nxSshAuthorizedKeys.Test_Marshall('MyKey','Present','jojoma',key) should be == [-1]")

    def testSetKeyPresentMissingKeyComment(self):
        self.assertTrue(nxSshAuthorizedKeys.Set_Marshall('','Present','jojoma',self.mykey) ==
                        [-1],"assert nxSshAuthorizedKeys.Set_Marshall('','Present','jojoma',key) should be == [-1]")
        
    def testSetKeyPresentMissingEnsure(self):
        self.assertTrue(nxSshAuthorizedKeys.Set_Marshall('MyKey','','jojoma',self.mykey) ==
                        [0],"assert nxSshAuthorizedKeys.Set_Marshall('MyKey','','jojoma',key) should be == [0]")
        
    def testSetKeyPresentMissingUserName(self):
        self.assertTrue(nxSshAuthorizedKeys.Set_Marshall('MyKey','Present','',self.mykey) ==
                        [-1],"assert nxSshAuthorizedKeys.Set_Marshall('MyKey','Present','',key) should be == [-1]")
        
    def testSetKeyPresentMissingKey(self):
        self.assertTrue(nxSshAuthorizedKeys.Set_Marshall('MyKey','Present','jojoma','') ==
                        [0],"assert nxSshAuthorizedKeys.Set_Marshall('MyKey','Present','jojoma','') should be == [0]")


class nxEnvironmentTestCases(unittest2.TestCase):
    """
    Test cases for nxEnvironment.py
    """
    
    def setUp(self):
        """
        Setup test resources
        """
        os.system('rm /tmp/environment /tmp/DSCEnvironment.sh 2> /dev/null')
        path='/etc/environment'
        if os.path.isfile(path) :
            os.system('cp -p ' + path + ' /tmp/')

        path='/etc/profile.d/DSCEnvironment.sh'
        if os.path.isfile(path) :
            os.system('cp -p ' + path + ' /tmp/')
        nxEnvironment.SetShowMof(True)
        print self.id() + '\n'
        
    def tearDown(self):
        """
        Remove test resources.
        """
        path='/etc/environment'
        if os.path.isfile('/tmp/environment') :
            os.system('mv ' + ' /tmp/environment ' + path)
        path='/etc/profile.d/DSCEnvironment.sh'
        if os.path.isfile('/tmp/DSCEnvironment.sh') :
            os.system('mv ' + ' /tmp/DSCEnvironment.sh ' + path)
            
    def make_MI(self, retval, Name, Value, Ensure, Path):
        d=dict();
        if Name == None :
            d['Name'] = None
        else :
            d['Name'] = nxEnvironment.protocol.MI_String(Name)
        if Value == None :
            d['Value'] = None
        else :
            d['Value'] = nxEnvironment.protocol.MI_String(Value)
        if Ensure == None :
            d['Ensure'] = None
        else :
            d['Ensure'] = nxEnvironment.protocol.MI_String(Ensure)
        if Path == None :
            d['Path'] = None
        else :
            d['Path'] = nxEnvironment.protocol.MI_Boolean(Path)
        return retval,d

    def testSetVarPresentTwice(self):
        self.assertTrue(nxEnvironment.Set_Marshall('MYVAR','/tmp','Present',False) ==
                        [0],"self.assertTrue(nxEnvironment.Set_Marshall('MYVAR','/tmp','Present',False) should == [0]")
        # do this twice to prove there is no error if the same path already exists
        self.assertTrue(nxEnvironment.Set_Marshall('MYVAR','/tmp','Present',False) ==
                        [0],"assert nxEnvironment.Set_Marshall('MYVAR','/tmp','Present',False) should == [0]")

    def testSetVarPresentTwoValues(self):
        self.assertTrue(nxEnvironment.Set_Marshall('MYVAR','/tmp','Present',False) ==
                        [0],"self.assertTrue(nxEnvironment.Set_Marshall('MYVAR','/tmp','Present',False) should == [0]")
        # do this twice to prove there is no error if the same path already exists
        self.assertTrue(nxEnvironment.Set_Marshall('MYVAR2','/tmp','Present',False) ==
                        [0],"assert nxEnvironment.Set_Marshall('MYVAR','/tmp','Present',False) should == [0]")
        r=nxEnvironment.Get_Marshall('MYVAR','/tmp','Present',False)
        self.assertTrue(check_values(r,self.make_MI(0,'MYVAR','/tmp','present',False)) == True
                        ,"assert nxEnvironment.Get_Marshall('MYVAR','/tmp','Present',False)[0] should == [0]")
        r=nxEnvironment.Get_Marshall('MYVAR2','/tmp','Present',False)
        self.assertTrue(check_values(r,self.make_MI(0,'MYVAR2','/tmp','present',False)) == True
                        ,"assert nxEnvironment.Get_Marshall('MYVAR2','/tmp','Present',False)[0] should == [0]")

    def testSetVarAbsentTwice(self):
        self.assertTrue(nxEnvironment.Set_Marshall('MYVAR','/tmp','Present',False) ==
                        [0],"assert nxEnvironment.Set_Marshall('MYVAR','/tmp','Present',False) should == [0]")
        self.assertTrue(nxEnvironment.Set_Marshall('MYVAR','/tmp','Absent',False) ==
                        [0],"assert nxEnvironment.Set_Marshall('MYVAR','/tmp','Absent',False) should == [0]")
        self.assertTrue(nxEnvironment.Set_Marshall('MYVAR','/tmp','Absent',False) ==
                        [0],"assert nxEnvironment.Set_Marshall('MYVAR','/tmp','Absent',False) should == [0]")

    def testTestVarPresent(self):
        self.assertTrue(nxEnvironment.Set_Marshall('MYVAR','/tmp','Present',False) ==
                        [0],"assert nxEnvironment.Set_Marshall('MYVAR','/tmp','Present',False) should == [0]")
        self.assertTrue(nxEnvironment.Test_Marshall('MYVAR','/tmp','Present',False) ==
                        [0],"assert nxEnvironment.Test_Marshall('MYVAR','/tmp','Present',False) should == [0]")
        
    def testTestVarPresentError(self):
        self.assertTrue(nxEnvironment.Test_Marshall('MYVAR','/tp','Present',False) ==
                        [-1],"assert nxEnvironment.Test_Marshall('MYVAR','/tmp','Present',False) should == [-1]")

    def testGetVarPresent(self):
        self.assertTrue(nxEnvironment.Set_Marshall('MYVAR','/tmp','Present',False) ==
                        [0],"assert nxEnvironment.Set_Marshall('MYVAR','/tmp','Present',False) should == [0]")
        r=nxEnvironment.Get_Marshall('MYVAR','/tmp','Present',False)

        self.assertTrue(check_values(r,self.make_MI(0,'MYVAR','/tmp','present',False)) == True
                        ,"assert nxEnvironment.Get_Marshall('MYVAR','/tmp','Present',False)[0] should == [0]")
        
    def testSetPathPresentTwice(self):
        self.assertTrue(nxEnvironment.Set_Marshall('','/tmp','Present',True) ==
                        [0],"assert nxEnvironment.Set_Marshall('','/tmp','Present',True) should == [0]")
        # do this twice to prove there is no error if the same path already exists
        self.assertTrue(nxEnvironment.Set_Marshall('','/tmp','Present',True) ==
                        [0],"assert nxEnvironment.Set_Marshall('','/tmp','Present',True) should == [0]")

    def testSetPathAbsentTwice(self):
        self.assertTrue(nxEnvironment.Set_Marshall('','/tmp','Present',True) ==
                        [0],"assert nxEnvironment.Set_Marshall('','/tmp','Present',True) should == [0]")
        self.assertTrue(nxEnvironment.Set_Marshall('','/tmp','Absent',True) ==
                        [0],"assert nxEnvironment.Set_Marshall('','/tmp','Absent',True) should == [0]")
        self.assertTrue(nxEnvironment.Set_Marshall('','/tmp','Absent',True) ==
                        [0],"assert nxEnvironment.Set_Marshall('','/tmp','Absent',True) should == [0]")

    def testTestPathPresent(self):
        self.assertTrue(nxEnvironment.Set_Marshall('','/tmp','Present',True) ==
                        [0],"assert nxEnvironment.Set_Marshall('','/tmp','Present',True) should == [0]")
        self.assertTrue(nxEnvironment.Test_Marshall('','/tmp','Present',True) ==
                        [0],"assert nxEnvironment.Test_Marshall('','/tmp','Present',True) should == [0]")

    def testTestPathPresentTwoValues(self):
        self.assertTrue(nxEnvironment.Set_Marshall('','/tmp','Present',True) ==
                        [0],"assert nxEnvironment.Set_Marshall('','/tmp','Present',True) should == [0]")
        self.assertTrue(nxEnvironment.Set_Marshall('','/tmp2','Present',True) ==
                        [0],"assert nxEnvironment.Set_Marshall('','/tmp2','Present',True) should == [0]")
        self.assertTrue(nxEnvironment.Test_Marshall('','/tmp','Present',True) ==
                        [0],"assert nxEnvironment.Test_Marshall('','/tmp','Present',True) should == [0]")
        self.assertTrue(nxEnvironment.Test_Marshall('','/tmp2','Present',True) ==
                        [0],"assert nxEnvironment.Test_Marshall('','/tmp2','Present',True) should == [0]")
        
    def testTestPathPresentError(self):
        self.assertTrue(nxEnvironment.Test_Marshall('','/tp','Present',True) ==
                        [-1],"assert nxEnvironment.Test_Marshall('','/tmp','Present',True) should == [-1]")

    def testGetPathPresent(self):
        self.assertTrue(nxEnvironment.Set_Marshall('','/tmp','Present',True) ==
                        [0],"assert nxEnvironment.Set_Marshall('','/tmp','Present',True) should == [0]")
        r=nxEnvironment.Get_Marshall('','/tmp','Present',True)

        self.assertTrue(check_values(r,self.make_MI(0,'','/tmp','present',True)) == True
                        ,"assert nxEnvironment.Get_Marshall('','/tmp','Present',True) should == [0]")
        
    def testGetPathPresentError(self):
        r=nxEnvironment.Get_Marshall('','/tp','Present',True)

        self.assertTrue(check_values(r,self.make_MI(0,'','/tp','present',True)) == False
                        ,"assert nxEnvironment.Get_Marshall('','/tmp','Present',True)[0] should == [-1]")

        
    def testSetPathPresentMissingEnsure(self):
        self.assertTrue(nxEnvironment.Set_Marshall('MYVAR','/tmp','',False) ==
                        [0],"assert nxEnvironment.Set_Marshall('MYVAR','/tmp','Present',False) should == [-1]")

        
    def testSetPathPresentMissingNamePathFalse(self):
        self.assertTrue(nxEnvironment.Set_Marshall('','/tmp','Present',False) ==
                        [-1],"assert nxEnvironment.Set_Marshall('MYVAR','/tmp','Present',False) should == [-1]")

    def testSetPathPresentMissingValue(self):
        self.assertTrue(nxEnvironment.Set_Marshall('MYVAR','','Present',False) ==
                        [0],"assert nxEnvironment.Set_Marshall('MYVAR','/tmp','Present',False) should == [-1]")


class tBag(object):
    def __init__(self,Name, FirewallType, Protocol, Ensure,
    AddressFamily, Access, State,  Direction, Position, SourceHost,
    SourcePort, DestinationHost, DestinationPort) :
        self.Name = Name
        self.FirewallType = FirewallType
        self.Protocol = Protocol
        self.Ensure = Ensure
        self.AddressFamily =AddressFamily 
        self.Access = Access
        self.State = State
        self.Direction = Direction
        self.Position = Position
        self.SourceHost = SourceHost
        self.SourcePort = SourcePort
        self.DestinationHost = DestinationHost
        self.DestinationPort = DestinationPort
 
def FirewallTypeIs():
    t=['ufw','SuSEfirewall2','firewalld','iptables']
    for f in t:
        if os.system('which ' + f) == 0:
            return f
    return 'nothing'

def IsFirewallRunning():
    if FirewallTypeIs() == 'iptables':
        return True
    cmd='ps -ef | grep -v grep | grep ' + FirewallTypeIs()
    if FirewallTypeIs() == 'SuSEfirewall2':
        cmd='rcSuSEfirewall2 status | grep running'
    return os.system(cmd)

def StartFirewall(firewall):
    if firewall == 'iptables':
        return
    t={}
    t['ufw']='yes | ufw enable '
    t['SuSEfirewall2']='SuSEfirewall2 start'
    t['firewalld']='service firewalld start'
    os.system(t[firewall] + ' 2> /dev/null')

def StopFirewall(firewall):
    if firewall == 'iptables':
        return
    t={}
    t['ufw']='ufw disable'
    t['SuSEfirewall2']='SuSEfirewall2 stop'
    t['firewalld']='service firewalld stop'
    os.system(t[firewall] + ' 2> /dev/null')


@unittest2.skipUnless(FirewallTypeIs() != 
                     'nothing','Skipping nxFirewallTestCases.  No supported firewall installed.')
class nxFirewallTestCases(unittest2.TestCase):
    """
    Test cases for nxFirewall.py
    """

    @classmethod    
    def setUpClass(cls):
        StartFirewall(FirewallTypeIs())

    @classmethod
    def tearDownClass(cls):
        StopFirewall(FirewallTypeIs())
    
    def setUp(self):
        """
        Setup test resources
        """
        print self.id() + '\n'
        self.FirewallType=FirewallTypeIs()
        self.min_rule={}
        self.min_rule['Name'] = "rule1"
        self.min_rule['InterfaceName'] = "eth1"
        self.min_rule['FirewallType'] = self.FirewallType
        self.min_rule['Protocol'] = ""
        self.min_rule['Ensure'] = "Present"
        self.min_rule['AddressFamily'] = ""
        self.min_rule['Access'] = "Allow"
        self.min_rule['State'] = ""
        self.min_rule['Direction'] = "INPUT"
        self.min_rule['Position'] = ""
        self.min_rule['SourceHost'] = ""
        self.min_rule['SourcePort'] = "22"
        self.min_rule['DestinationHost'] = ""
        self.min_rule['DestinationPort'] = ""
        self.max_rule={}
        self.max_rule['Name'] = "rule1"
        self.max_rule['InterfaceName'] = "eth1"
        self.max_rule['FirewallType'] = self.FirewallType
        self.max_rule['Protocol'] = "tcp"
        self.max_rule['Ensure'] = "Present"
        self.max_rule['AddressFamily'] = "IPv4"
        self.max_rule['Access'] = "Allow"
        self.max_rule['State'] = ["NEW" , "RELATED"]
        self.max_rule['Direction'] = "INPUT"
        self.max_rule['Position'] = "top"
        self.max_rule['SourceHost'] = "0.0.0.0"
        self.max_rule['SourcePort'] = "22"
        self.max_rule['DestinationHost'] = "0.0.0.1"
        self.max_rule['DestinationPort'] = "22"

    def tearDown(self):
        """
        Remove test resources.
        """
        self.max_rule['Ensure'] = "Absent"
        nxFirewall.Set_Marshall(**self.max_rule)
        self.min_rule['Ensure'] = "Absent"
        nxFirewall.Set_Marshall(**self.min_rule)
        
    def make_MI(self,retval,Name, InterfaceName, FirewallType, Protocol, Ensure, AddressFamily,
                Access, State,  Direction, Position, SourceHost, SourcePort,
                DestinationHost, DestinationPort):
        d=dict();
        if Name == None :
            d['Name'] = None
        else :
            d['Name'] = nxFirewall.protocol.MI_String(Name)
        if InterfaceName == None :
            d['InterfaceName'] = None
        else :
            d['InterfaceName'] = nxFirewall.protocol.MI_String(InterfaceName)
        if FirewallType == None :
            d['FirewallType'] = None
        else :
            d['FirewallType'] = nxFirewall.protocol.MI_String(FirewallType)
        if Protocol == None :
            d['Protocol'] = None
        else :
            d['Protocol'] = nxFirewall.protocol.MI_String(Protocol)
        if Ensure == None :
            d['Ensure'] = None
        else :
            d['Ensure'] = nxFirewall.protocol.MI_String(Ensure)
        if AddressFamily == None :
            d['AddressFamily'] = None
        else :
            d['AddressFamily'] = nxFirewall.protocol.MI_String(AddressFamily)
        if Access == None :
            d['Access'] = None
        else :
            d['Access'] = nxFirewall.protocol.MI_String(Access)
        if State == None :
            d['State'] = None
        else :
            d['State'] = nxFirewall.protocol.MI_StringA(State)
        if Direction == None :
            d['Direction'] = None
        else :
            d['Direction'] = nxFirewall.protocol.MI_String(Direction)
        if Position == None :
            d['Position'] = None
        else :
            d['Position'] = nxFirewall.protocol.MI_String(Position)
        if SourceHost == None :
            d['SourceHost'] = None
        else :
            d['SourceHost'] = nxFirewall.protocol.MI_String(SourceHost)
        if SourcePort == None :
            d['SourcePort'] = None
        else :
            d['SourcePort'] = nxFirewall.protocol.MI_String(SourcePort)
        if DestinationHost == None :
            d['DestinationHost'] = None
        else :
            d['DestinationHost'] = nxFirewall.protocol.MI_String(DestinationHost)
        if DestinationPort == None :
            d['DestinationPort'] = None
        else :
            d['DestinationPort'] = nxFirewall.protocol.MI_String(DestinationPort)
        return retval,d

    def testTestPassMaxArgs(self):
        nxFirewall.Set_Marshall(**self.max_rule)
        self.assertTrue(nxFirewall.Test_Marshall(**self.max_rule) ==
        [0],"self.assertTrue(nxFirewall.Test_Marshall(" + repr(self.max_rule) + ") should == [0]")
        
    def testTestFailMaxArgs(self):
        nxFirewall.Set_Marshall(**self.max_rule)
        self.bag=dict(self.max_rule)
        self.bag['Direction'] = 'output'
        self.assertTrue(nxFirewall.Test_Marshall(**self.bag) ==
        [-1],"self.assertTrue(nxFirewall.Test_Marshall(" + repr(self.bag) + ") should == [-1]")

    def testTestPassMinArgs(self):
        nxFirewall.Set_Marshall(**self.min_rule)
        self.bag=dict(self.min_rule)
        self.assertTrue(nxFirewall.Test_Marshall(**self.bag) ==
        [0],"self.assertTrue(nxFirewall.Test_Marshall(" + repr(self.bag) + ") should == [0]")

    def testTestFailMinArgs(self):
        nxFirewall.Set_Marshall(**self.min_rule)
        self.bag=dict(self.min_rule)
        self.bag['Direction'] = 'output'
        self.assertTrue(nxFirewall.Test_Marshall(**self.bag) ==
                        [-1],"self.assertTrue(nxFirewall.Test_Marshall(" + repr(self.bag) + ") should == [-1]")
        

class nxIPAddressTestCases(unittest2.TestCase):
    """
    Test cases for nxIPAddress.py
    """
    def setUp(self):
        """
        Setup test resources
        """
        pass
    
    def tearDown(self):
        """
        Remove test resources.
        """
        pass
    
    def make_MI(self,retval,IPAddress,InterfaceName,BootProtocol,DefaultGateway,Ensure,PrefixLength,AddressFamily):
        d=dict()
        d.clear()
        if IPAddress == None :
            d['IPAddress'] = None
        else :
            d['IPAddress'] = nxIPAddress.protocol.MI_String(IPAddress)
        if InterfaceName == None :
            d['InterfaceName'] = None
        else :
            d['InterfaceName'] = nxIPAddress.protocol.MI_String(InterfaceName)
        if BootProtocol == None :
            d['BootProtocol'] = None
        else :
            d['BootProtocol'] = nxIPAddress.protocol.MI_String(BootProtocol)
        if DefaultGateway == None :
            d['DefaultGateway'] = None
        else :
            d['DefaultGateway'] = nxIPAddress.protocol.MI_String(DefaultGateway)
        if Ensure == None :
            d['Ensure'] = None
        else :
            d['Ensure'] = nxIPAddress.protocol.MI_String(Ensure)
        if PrefixLength == None :
            d['PrefixLength'] = None
        else :
            d['PrefixLength'] = nxIPAddress.protocol.MI_Uint32(PrefixLength)
        if AddressFamily == None :
            d['AddressFamily'] = None
        else :
            d['AddressFamily'] = nxIPAddress.protocol.MI_String(AddressFamily)
        return retval,d
    
    def testSetIPAddressV4Dynamic(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxIPAddress_eth1_V4_dynamic.mof')
        self.assertTrue(nxIPAddress.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]') 

    def testGetIPAddressV4Dynamic(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxIPAddress_eth1_V4_dynamic.mof')
        self.assertTrue(nxIPAddress.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]')
        self.assertTrue(check_values(nxIPAddress.Get_Marshall(**d), \
        self.make_MI(0,**d))  ==  True, \
        'Get('+repr(d)+' should return ==['+repr(d)+']')

    def testSetIPAddressV4Static(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxIPAddress_eth1_V4_static.mof')
        self.assertTrue(nxIPAddress.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]') 

    def testGetIPAddressV4Static(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxIPAddress_eth1_V4_static.mof')
        self.assertTrue(nxIPAddress.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]')
        self.assertTrue(check_values(nxIPAddress.Get_Marshall(**d), \
        self.make_MI(0,**d))  ==  True, \
        'Get('+repr(d)+' should return ==['+repr(d)+']')

    def testSetIPAddressV6Dynamic(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxIPAddress_eth1_V6_dynamic.mof')
        self.assertTrue(nxIPAddress.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]') 

    def testGetIPAddressV6Dynamic(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxIPAddress_eth1_V6_dynamic.mof')
        self.assertTrue(nxIPAddress.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]')
        self.assertTrue(check_values(nxIPAddress.Get_Marshall(**d), \
        self.make_MI(0,**d))  ==  True, \
        'Get('+repr(d)+' should return ==['+repr(d)+']')

    def testSetIPAddressV6Static(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxIPAddress_eth1_V6_static.mof')
        self.assertTrue(nxIPAddress.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]') 

    def testGetIPAddressV6Static(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxIPAddress_eth1_V6_static.mof')
        self.assertTrue(nxIPAddress.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]')
        self.assertTrue(check_values(nxIPAddress.Get_Marshall(**d), \
        self.make_MI(0,**d))  ==  True, \
        'Get('+repr(d)+' should return ==['+repr(d)+']')


class nxComputerTestCases(unittest2.TestCase):
    """
    Test cases for nxComputer.py
    """
    def setUp(self):
        """
        Setup test resources
        """
        os.system('cp /etc/localtime /etc/localtime.bak;'+
                  'date +%Z > /etc/lastdate;' +
                  'cp /etc/hostname /etc/hostname.bak;' +
                  'cp /etc/hosts /etc/hosts.bak')
        
    def tearDown(self):
        """
        Remove test resources.
        """
        os.system('mv /etc/localtime.bak /etc/localtime')
        os.environ['TZ'] = open('/etc/lastdate').read()
        time.tzset()
        os.system('mv /etc/hostname.bak /etc/hostname;' +
                  'mv /etc/hosts.bak /etc/hosts')
        os.system('cat /etc/hostname | xargs hostname')
        time.sleep(1)
        
    def make_MI(self,retval,Name, DNSDomainName, TimeZoneName, AlternateTimeZoneName):
        d=dict()
        d.clear()
        if Name == None :
            d['Name'] = None
        else :
            d['Name'] = nxComputer.protocol.MI_String(Name)
        if DNSDomainName == None :
            d['DNSDomainName'] = None
        else :
            d['DNSDomainName'] = nxComputer.protocol.MI_String(DNSDomainName)
        if TimeZoneName == None :
            d['TimeZoneName'] = None
        else :
            d['TimeZoneName'] = nxComputer.protocol.MI_String(TimeZoneName)
        if AlternateTimeZoneName == None :
            d['AlternateTimeZoneName'] = None
        else :
            d['AlternateTimeZoneName'] = nxComputer.protocol.MI_String(AlternateTimeZoneName)
        return retval,d
    
    def testSetComputerNameTimeZone(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxComputer.mof')
        self.assertTrue(nxComputer.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]') 

    def testGetComputerNameTimeZone(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxComputer.mof')
        self.assertTrue(nxComputer.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]')
        d['AlternateTimeZoneName']=''
        self.assertTrue(check_values(nxComputer.Get_Marshall(**d), \
        self.make_MI(0,**d))  ==  True, \
        'Get('+repr(d)+' should return ==['+repr(d)+']')


class nxDNSServerAddressTestCases(unittest2.TestCase):
    """
    Test cases for nxDNSServerAddress.py
    """
    def setUp(self):
        """
        Setup test resources
        """
        print self.id() + '\n'
        dist=nxDNSServerAddress.GetMyDistro()
        os.system('cp ' + dist.file + ' ' + dist.file + '.bak')

    def tearDown(self):
        """
        Remove test resources.
        """
        dist=nxDNSServerAddress.GetMyDistro()
        os.system('mv ' + dist.file + '.bak' + ' ' + dist.file)

    def make_MI(self,retval,Address,Ensure,AddressFamily):
        d=dict();
        d.clear()
        if Address == None :
            d['Address'] = None
        else :
            d['Address'] = nxDNSServerAddress.protocol.MI_StringA(Address)
        if Ensure == None :
            d['Ensure'] = None
        else :
            d['Ensure'] = nxDNSServerAddress.protocol.MI_String(Ensure)
        if AddressFamily == None :
            d['AddressFamily'] = None
        else :
            d['AddressFamily'] = nxDNSServerAddress.protocol.MI_String(AddressFamily)
        return retval,d
    
    def testSetDNSServerAddressPresent(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxDNSServerAddress_add.mof')
        self.assertTrue(nxDNSServerAddress.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]')

    def testGetDNSServerAddressPresent(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxDNSServerAddress_add.mof')
        self.assertTrue(nxDNSServerAddress.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]')

        self.assertTrue(check_values(nxDNSServerAddress.Get_Marshall(**d), \
        self.make_MI(0,**d))  ==  True, \
        'Get('+repr(d)+' should return [0,'+ repr(d) + ']')

    def testGetDNSServerAddressAbsent(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxDNSServerAddress_add.mof')
        self.assertTrue(nxDNSServerAddress.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]')
        d['Ensure']='Absent'
        self.assertTrue(nxDNSServerAddress.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]')
        self.assertTrue(check_values(nxDNSServerAddress.Get_Marshall(**d), \
        self.make_MI(0,**d))  ==  True, \
        'Get('+repr(d)+' should return [0,'+ repr(d) + ']')


class nxFileLineTestCases(unittest2.TestCase):
    """
    Test cases for nxFileLine.py
    """
    def setUp(self):
        """
        Setup test resources
        """
        os.system('echo "joe is coolest" >  /tmp/joe.txt') 
        print self.id() + '\n'
        
    def tearDown(self):
        """
        Remove test resources.
        """
        pass

    def make_MI(self,retval,FilePath, DoesNotContainPattern, ContainsLine):
        d=dict()
        d.clear()
        if FilePath == None :
            d['FilePath'] = None
        else :
            d['FilePath'] = nxFileLine.protocol.MI_String(FilePath)
        if DoesNotContainPattern == None :
            d['DoesNotContainPattern'] = None
        else :
            d['DoesNotContainPattern'] = nxFileLine.protocol.MI_String(DoesNotContainPattern)
        if ContainsLine == None :
            d['ContainsLine'] = None
        else :
            d['ContainsLine'] = nxFileLine.protocol.MI_String(ContainsLine)
        return retval,d
    
    def testSetFileLinePresent(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxFileLine_add.mof')
        self.assertTrue(nxFileLine.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]')

    def testGetFileLine(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxFileLine_add.mof')
        self.assertTrue(nxFileLine.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]')
        self.assertTrue(check_values(nxFileLine.Get_Marshall(**d), \
        self.make_MI(0,**d))  ==  True, \
        'Get('+repr(d)+' should return [0,'+ repr(d) + ']')


class nxArchiveTestCases(unittest2.TestCase):
    """
    Test cases for nxArchive.py
    """
    def setUp(self):
        """
        Setup test resources
        """
        if not os.path.exists('/tmp/src.tar.gz') or not os.path.exists('/tmp/src.zip'):
            os.system('cp ./Scripts/Tests/test_mofs/src* /tmp/') 
        print self.id() + '\n'
        
    def tearDown(self):
        """
        Remove test resources.
        """
        pass

    def make_MI(self,retval,DestinationPath, SourcePath, Ensure, Force, Checksum):
        d=dict();
        
        if DestinationPath == None :
            d['DestinationPath'] = None
        else :
            d['DestinationPath'] = nxArchive.protocol.MI_String(DestinationPath)
        if SourcePath == None :
            d['SourcePath'] = None
        else :
            d['SourcePath'] = nxArchive.protocol.MI_String(SourcePath)
        if Ensure == None :
            d['Ensure'] = None
        else :
            d['Ensure'] = nxArchive.protocol.MI_String(Ensure)
        if Force == None :
            d['Force'] = None
        else :
            d['Force'] = nxArchive.protocol.MI_Boolean(Force)
        if Checksum == None :
            d['Checksum'] = None
        else :
            d['Checksum'] = nxArchive.protocol.MI_String(Checksum)
        return retval,d

    def testSetTarArchivePresent(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxArchive_tar_ctime_test.mof')
        self.assertTrue(nxArchive.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]')

    def testSetZipArchivePresent(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxArchive_zip_ctime_test.mof')
        self.assertTrue(nxArchive.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]')


@unittest2.skipUnless(os.system('ps -ef | grep -v grep | grep -q mysqld') ==
                      0,'Skipping nxMySqlUserTestCases.   mysqld is not running.')
class nxMySqlUserTestCases(unittest2.TestCase):
    """
    Test cases for nxMySqlUser.py
    """
    def drop(self):
        Name = 'jojoma'
        cmd = "DROP USER " + Name + ";"
        cmd='mysql -u root -e "' + cmd + ' FLUSH PRIVILEGES;"'
        os.environ['MYSQL_PWD'] = 'root'
        os.system(cmd + ' 2> /dev/null')
        os.environ['MYSQL_PWD'] = ''

    def setUp(self):
        """
        Setup test resources
        """
        self.drop()
        
    def tearDown(self):
        """
        Remove test resources.
        """
        self.drop()

        
    def make_MI(self,retval,Name, Credential,  ConnectionCredential, Ensure):
        d=dict()
        d.clear()
        if Name == None :
            d['Name'] = None
        else :
            d['Name'] = nxMySqlUser.protocol.MI_String(Name)
        if Credential == None :
            d['Credential'] = None
        else :
            d['Credential'] = nxMySqlUser.protocol.MI_String(Credential)
        if ConnectionCredential == None :
            d['ConnectionCredential'] = None
        else :
            d['ConnectionCredential'] = nxMySqlUser.protocol.MI_String(ConnectionCredential)
        if Ensure == None :
            d['Ensure'] = None
        else :
            d['Ensure'] = nxMySqlUser.protocol.MI_String(Ensure)
        return retval,d
    
    def testSetMySqlUser_add(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxMySqlUser_add.mof')
        self.assertTrue(nxMySqlUser.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]') 

    def testGetMySqlUser_add(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxMySqlUser_add.mof')
        self.assertTrue(nxMySqlUser.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]')
        self.assertTrue(check_values(nxMySqlUser.Get_Marshall(**d), \
        self.make_MI(0,**d))  ==  True, \
        'Get('+repr(d)+' should return ==['+repr(d)+']')

    def testSetMySqlUser_del(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxMySqlUser_del.mof')
        self.assertTrue(nxMySqlUser.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]') 

    def testGetMySqlUser_del(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxMySqlUser_del.mof')
        self.assertTrue(nxMySqlUser.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]')
        self.assertTrue(check_values(nxMySqlUser.Get_Marshall(**d), \
        self.make_MI(0,**d))  ==  True, \
        'Get('+repr(d)+' should return ==['+repr(d)+']')

    def testSetMySqlUser_upd(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxMySqlUser_upd.mof')
        self.assertTrue(nxMySqlUser.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]') 

    def testGetMySqlUser_upd(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxMySqlUser_upd.mof')
        self.assertTrue(nxMySqlUser.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]')
        self.assertTrue(check_values(nxMySqlUser.Get_Marshall(**d), \
        self.make_MI(0,**d))  ==  True, \
        'Get('+repr(d)+' should return ==['+repr(d)+']')


@unittest2.skipUnless(os.system('ps -ef | grep -v grep | grep -q mysqld') ==
                      0,'Skipping nxMySqlDatabaseTestCases.   mysqld is not running.')
class nxMySqlDatabaseTestCases(unittest2.TestCase):
    """
    Test cases for nxMySqlDatabase.py
    """

    def drop(self):
        Name = 'jojoma'
        cmd = "DROP DATABASE " + Name + ";"
        cmd='mysql -u root -e "' + cmd + '"'
        os.environ['MYSQL_PWD'] = 'root'
        os.system(cmd + ' 2> /dev/null')
        os.environ['MYSQL_PWD'] = ''

    def setUp(self):
        """
        Setup test resources
        """
        self.drop()
        
    def tearDown(self):
        """
        Remove test resources.
        """
        self.drop()
        
    def make_MI(self,retval,Name, ConnectionCredential, Ensure):
        d=dict()
        d.clear()
        if Name == None :
            d['Name'] = None
        else :
            d['Name'] = nxMySqlDatabase.protocol.MI_String(Name)
        if ConnectionCredential == None :
            d['ConnectionCredential'] = None
        else :
            d['ConnectionCredential'] = nxMySqlDatabase.protocol.MI_String(ConnectionCredential)
        if Ensure == None :
            d['Ensure'] = None
        else :
            d['Ensure'] = nxMySqlDatabase.protocol.MI_String(Ensure)
        return retval,d
    
    def testSetMySqlDatabase_add(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxMySqlDatabase_add.mof')
        self.assertTrue(nxMySqlDatabase.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]') 

    def testGetMySqlDatabase_add(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxMySqlDatabase_add.mof')
        self.assertTrue(nxMySqlDatabase.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]')
        self.assertTrue(check_values(nxMySqlDatabase.Get_Marshall(**d), \
        self.make_MI(0,**d))  ==  True, \
        'Get('+repr(d)+' should return ==['+repr(d)+']')

    def testSetMySqlDatabase_del(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxMySqlDatabase_del.mof')
        self.assertTrue(nxMySqlDatabase.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]') 

    def testGetMySqlDatabase_del(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxMySqlDatabase_del.mof')
        self.assertTrue(nxMySqlDatabase.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]')
        self.assertTrue(check_values(nxMySqlDatabase.Get_Marshall(**d), \
        self.make_MI(0,**d))  ==  True, \
        'Get('+repr(d)+' should return ==['+repr(d)+']')


@unittest2.skipUnless(os.system('ps -ef | grep -v grep | grep -q mysqld') ==
                      0,'Skipping nxMySqlGrantTestCases.   mysqld is not running.')
class nxMySqlGrantTestCases(unittest2.TestCase):
    """
    Test cases for nxMySqlGrant.py
    """
    def revoke(self):
        UserName="jojoma"
        Host="127.0.0.1"
        DatabaseName = "jojoma"
        PermissionType = "ALL PRIVILEGES"
        cmd = "REVOKE "+ PermissionType + " ON " + DatabaseName + ".* FROM '" + UserName+"'@'" + Host  + "';"
        cmd='mysql -u root -e "' + cmd + ' FLUSH PRIVILEGES;"'
        os.environ['MYSQL_PWD'] = 'root'
        os.system(cmd + ' 2> /dev/null')
        os.environ['MYSQL_PWD'] = ''

    def setUp(self):
        """
        Setup test resources
        """
        d=ParseMOF('./Scripts/Tests/test_mofs/nxMySqlDatabase_add.mof')
        nxMySqlDatabase.Set_Marshall(**d)
        d=ParseMOF('./Scripts/Tests/test_mofs/nxMySqlUser_add.mof')
        nxMySqlUser.Set_Marshall(**d)
        self.revoke()
        
    def tearDown(self):
        """
        Remove test resources.
        """
        self.revoke()
        d=ParseMOF('./Scripts/Tests/test_mofs/nxMySqlDatabase_del.mof')
        nxMySqlDatabase.Set_Marshall(**d)
        d=ParseMOF('./Scripts/Tests/test_mofs/nxMySqlUser_del.mof')
        nxMySqlUser.Set_Marshall(**d)
        
    def make_MI(self,retval,UserName, DatabaseName, ConnectionCredential, PermissionType, Ensure):
        d=dict()
        d.clear()
        if UserName == None :
            d['UserName'] = None
        else :
            d['UserName'] = nxMySqlGrant.protocol.MI_String(UserName)
        if UserName == None :
            d['DatabaseName'] = None
        else :
            d['DatabaseName'] = nxMySqlGrant.protocol.MI_String(DatabaseName)
        if ConnectionCredential == None :
            d['ConnectionCredential'] = None
        else :
            d['ConnectionCredential'] = nxMySqlGrant.protocol.MI_String(ConnectionCredential)
        if Ensure == None :
            d['Ensure'] = None
        else :
            d['Ensure'] = nxMySqlGrant.protocol.MI_String(Ensure)
        if PermissionType == None :
            d['PermissionType'] = None
        else :
            d['PermissionType'] = nxMySqlGrant.protocol.MI_String(PermissionType)
        return retval,d
    
    def testSetMySqlGrant_add(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxMySqlGrant_add.mof')
        self.assertTrue(nxMySqlGrant.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]') 

    def testGetMySqlGrant_add(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxMySqlGrant_add.mof')
        self.assertTrue(nxMySqlGrant.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]')
        self.assertTrue(check_values(nxMySqlGrant.Get_Marshall(**d), \
        self.make_MI(0,**d))  ==  True, \
        'Get('+repr(d)+' should return ==['+repr(d)+']')

    def testSetMySqlGrant_del(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxMySqlGrant_del.mof')
        self.assertTrue(nxMySqlGrant.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]') 

    def testGetMySqlGrant_del(self):
        d=ParseMOF('./Scripts/Tests/test_mofs/nxMySqlGrant_del.mof')
        self.assertTrue(nxMySqlGrant.Set_Marshall(**d) == [0],'Set('+repr(d)+') should return == [0]')
        self.assertTrue(check_values(nxMySqlGrant.Get_Marshall(**d), \
        self.make_MI(0,**d))  ==  True, \
        'Get('+repr(d)+' should return ==['+repr(d)+']')

    

class nxFileInventoryTestCases(unittest2.TestCase):
    """
    Test cases for nxFileInventory.py
    """
    @classmethod    
    def setUpClass(cls):
        """
        You should set 'create_files' to True
        to re-create the picked files
        when Inventory_Marshall
        or the tests have changed.
        """
        cls.create_files = False
        cls.linkfarm = '/tmp/linkfarm/'
        os.system('rm -rf ' + cls.linkfarm + ' 2> /dev/null')
        os.makedirs(cls.linkfarm+'joe')
        os.makedirs(cls.linkfarm+'bob')
        open(cls.linkfarm+'joe/linkfarmjoefile1.txt','w+').write(\
            'Contents of linkfarmjoefile1.txt\n')
        open(cls.linkfarm+'joe/linkfarmjoefile2.txt','w+').write(\
            'Contents of linkfarmjoefile2.txt\n')
        open(cls.linkfarm+'bob/linkfarmbobfile1.txt','w+').write(\
            'Contents of linkfarmbobfile1.txt\n')
        open(cls.linkfarm+'bob/linkfarmbobfile2.txt','w+').write(\
            'Contents of linkfarmbobfile2.txt\n')
        cls.basepath = '/tmp/FileInventory/'
        os.system('rm -rf ' + cls.basepath + ' 2> /dev/null')
        os.makedirs(cls.basepath+'joedir0/joedir1/joedir2/')
        open(cls.basepath+'basedirfile1.txt','w+').write(\
            'Contents of basedirfile1.txt\n')
        open(cls.basepath+'omsadmin.conf','w+').write(\
            'Contents of omsadmin.conf\n')
        open(cls.basepath+'basedirfile2.txt','w+').write(\
            'Contents of basedirfile2.txt\n')
        open(cls.basepath+'basedirfile3.bin','wb+').write(\
            '\xff\xff\xfe\x00\xfe\x00\xff\x00\x00\x00')
        os.chown(cls.basepath+'basedirfile3.bin', 7777, 7777)
        open(cls.basepath+'joedir0/joedir0file1.txt','w+').write(\
            'Contents of joedir0file1.txt\n')
        open(cls.basepath+'joedir0/joedir0file2.txt','w+').write(\
            'Contents of joedir0file2.txt\n')
        open(cls.basepath+'joedir0/joedir0file3.bin','wb+').write(\
            '\xff\xff\xfe\x00\xfe\x00\xff\x00\x00\x00')
        os.chown(cls.basepath+'joedir0/joedir0file3.bin', 7777, 7777)
        open(cls.basepath+'joedir0/joedir1/joedir1file1.txt','w+').write(\
            'Contents of joedir1file1.txt\n')
        open(cls.basepath+'joedir0/joedir1/joedir1file2.txt','w+').write(\
            'Contents of joedir1file2.txt\n')
        open(cls.basepath+'joedir0/joedir1/joedir1file3.bin','wb+').write(\
            '\xff\xff\xfe\x00\xfe\x00\xff\x00\x00\x00')
        os.chown(cls.basepath+'joedir0/joedir1/joedir1file3.bin', 7777, 7777)
        open(cls.basepath+'joedir0/joedir1/joedir2/joedir2file1.txt','w+').write(\
            'Contents of joedir2file1.txt\n')
        open(cls.basepath+'joedir0/joedir1/joedir2/joedir2file2.txt','w+').write(\
            'Contents of joedir2file2.txt\n')
        open(cls.basepath+'joedir0/joedir1/joedir2/joedir2file3.bin','wb+').write(\
            '\xff\xff\xfe\x00\xfe\x00\xff\x00\x00\x00')
        os.chown(cls.basepath+'joedir0/joedir1/joedir2/joedir2file3.bin', 7777, 7777)
        os.makedirs(cls.basepath+'bobdir0/bobdir1/bobdir2/')
        open(cls.basepath+'bobdir0/bobdir0file1.txt','w+').write(\
            'Contents of bobdir0file1.txt\n')
        open(cls.basepath+'bobdir0/bobdir0file2.txt','w+').write(\
            'Contents of bobdir0file2.txt\n')
        open(cls.basepath+'bobdir0/bobdir0file3.bin','wb+').write(\
            '\xff\xff\xfe\x00\xfe\x00\xff\x00\x00\x00')
        os.chown(cls.basepath+'bobdir0/bobdir0file3.bin', 7777, 7777)
        open(cls.basepath+'bobdir0/bobdir1/bobdir1file1.txt','w+').write(\
            'Contents of bobdir1file1.txt\n')
        open(cls.basepath+'bobdir0/bobdir1/bobdir1file2.txt','w+').write(\
            'Contents of bobdir1file2.txt\n')
        open(cls.basepath+'bobdir0/bobdir1/bobdir1file3.bin','wb+').write(\
            '\xff\xff\xfe\x00\xfe\x00\xff\x00\x00\x00')
        os.chown(cls.basepath+'bobdir0/bobdir1/bobdir1file3.bin', 7777, 7777)
        open(cls.basepath+'bobdir0/bobdir1/bobdir2/bobdir2file1.txt','w+').write(\
            'Contents of bobdir2file1.txt\n')
        open(cls.basepath+'bobdir0/bobdir1/bobdir2/bobdir2file2.txt','w+').write(\
            'Contents of bobdir2file2.txt\n')
        open(cls.basepath+'bobdir0/bobdir1/bobdir2/bobdir2file3.bin','wb+').write(\
            '\xff\xfe\x00\x00\xff\xfd\x00\x00\x00\x00')
        os.chown(cls.basepath+'bobdir0/bobdir1/bobdir2/bobdir2file3.bin', 7777, 7777)
        os.symlink(cls.basepath+'bobdir0/bobdir0file1.txt', cls.basepath+'basedirfilelink1.txt')
        os.symlink(cls.basepath+'bobdir0/bobdir1', cls.basepath+'basedirdirlink1')
        os.symlink(cls.basepath+'bobdir0/bobdir0file1.txt', cls.basepath+'joedir0/joedir0filelink1.txt')
        os.symlink(cls.linkfarm+'joe', cls.basepath+'joedir0/joedir0dirlink1')
        os.symlink(cls.basepath+'joedir0', cls.basepath+'joedir0/joedir1/joedir1dirlinktojoedir0') # infinite recursion
        os.symlink(cls.basepath+'joedir0/joedir0file1.txt', cls.basepath+'bobdir0/bobdir0filelink1.txt')
        os.symlink(cls.linkfarm+'bob', cls.basepath+'bobdir0/bobdir0dirlink1')
        os.symlink(cls.basepath+'bobdir0', cls.basepath+'bobdir0/bobdir1/bobdir1dirlinktobobdir0') # infinite recursion

    @classmethod    
    def tearDownClass(cls):
        os.system('rm -rf ' + cls.basepath + ' 2> /dev/null')
        os.system('rm -rf ' + cls.linkfarm + ' 2> /dev/null')
    
    def setUp(self):
        """
        Setup test resources
        """
        pass

    
    def tearDown(self):
        """
        Remove test resources.
        """
        pass

    def SerializeInventoryObject(self, fname, ob):
        # Persist the results of correct results for future tests.
        # The pickled results are stored in test_mofs.
        # You should re-create these files if Inventory_Marshall
        # or the the tests have changed.
        l = []
        for d in ob[1]['__Inventory'].value:
            l.append(d['DestinationPath'].value)
        l.sort()
        with open('./Scripts/Tests/test_mofs/' + fname + '.pkl', 'wb') as F:
            pickle.dump(l, F, -1)

    def DeserializeInventoryObject(self, fname):
        with open('./Scripts/Tests/test_mofs/' + fname + '.pkl', 'rb') as F:
            r = pickle.load(F)
        return r
        
    def MakeList(self,ob):
        l = []
        for d in ob[1]['__Inventory'].value:
            l.append(d['DestinationPath'].value)
        l.sort()
        return l
    
    def testFileInventoryInventory_MarshallDir(self):
        d = {'Links': u'ignore', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': False, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath, 'UseSudo': True, 'Type': u'directory'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0')
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallDir',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallDir')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))

    
    def testFileInventoryInventory_MarshallFile(self):
        d = {'Links': u'ignore', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': False, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath, 'UseSudo': True, 'Type': u'file'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0')
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallFile',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallFile')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallSingleFile(self):
        d = {'Links': u'ignore', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': False, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath + 'basedirfile1.txt', 'UseSudo': True, 'Type': u'file'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0')
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallSingleFile',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallSingleFile')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallSingleFile_omsadminconf(self):
        d = {'Links': u'ignore', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': False, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath + 'omsadmin.conf', 'UseSudo': True, 'Type': u'file'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0')
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallSingleFile',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallSingleFile')
        self.assertTrue(l == [], repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallTypeWild(self):
        d = {'Links': u'ignore', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': False, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath, 'UseSudo': True, 'Type': u'*'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallTypeWild',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallTypeWild')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallDirRecurse(self):
        d = {'Links': u'ignore', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': True, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath, 'UseSudo': True, 'Type': u'directory'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallDirRecurse',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallDirRecurse')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallFileRecurse(self):
        d = {'Links': u'ignore', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': True, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath, 'UseSudo': True, 'Type': u'file'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallFileRecurse',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallFileRecurse')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallTypeWildRecurse(self):
        d = {'Links': u'ignore', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': True, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath, 'UseSudo': True, 'Type': u'*'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallTypeWildRecurse',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallTypeWildRecurse')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallWildDir(self):
        d = {'Links': u'ignore', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': False, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath+'*dir*', 'UseSudo': True, 'Type': u'directory'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallWildDir',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallWildDir')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallWildFile(self):
        d = {'Links': u'ignore', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': False, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath+'*/*file*', 'UseSudo': True, 'Type': u'file'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallWildFile',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallWildFile')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallWildTypeWild(self):
        d = {'Links': u'ignore', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': False, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath+'*/*', 'UseSudo': True, 'Type': u'*'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallWildTypeWild',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallWildTypeWild')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallWildDirRecurse(self):
        d = {'Links': u'ignore', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': True, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath+'*/*dir*', 'UseSudo': True, 'Type': u'directory'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallWildDirRecurse',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallWildDirRecurse')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallWildFileRecurse(self):
        d = {'Links': u'ignore', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': True, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath+'*/*file*', 'UseSudo': True, 'Type': u'file'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallWildFileRecurse',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallWildFileRecurse')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallWildTypeWildRecurse(self):
        d = {'Links': u'ignore', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': True, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath+'*/*', 'UseSudo': True, 'Type': u'*'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallWildTypeWildRecurse',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallWildTypeWildRecurse')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallDirFollowLink(self):
        d = {'Links': u'follow', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': False, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath, 'UseSudo': True, 'Type': u'directory'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallDirFollowLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallDirFollowLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallFileFollowLink(self):
        d = {'Links': u'follow', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': False, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath, 'UseSudo': True, 'Type': u'file'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallFileFollowLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallFileFollowLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallTypeWildFollowLink(self):
        d = {'Links': u'follow', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': False, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath, 'UseSudo': True, 'Type': u'*'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallTypeWildFollowLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallTypeWildFollowLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallDirRecurseFollowLink(self):
        d = {'Links': u'follow', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': True, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath, 'UseSudo': True, 'Type': u'directory'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallDirRecurseFollowLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallDirRecurseFollowLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallFileRecurseFollowLink(self):
        d = {'Links': u'follow', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': True, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath, 'UseSudo': True, 'Type': u'file'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallFileRecurseFollowLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallFileRecurseFollowLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallTypeWildRecurseFollowLink(self):
        d = {'Links': u'follow', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': True, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath, 'UseSudo': True, 'Type': u'*'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallTypeWildRecurseFollowLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallTypeWildRecurseFollowLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallWildDirFollowLink(self):
        d = {'Links': u'follow', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': False, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath+'*dir*', 'UseSudo': True, 'Type': u'directory'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallWildDirFollowLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallWildDirFollowLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallWildFileFollowLink(self):
        d = {'Links': u'follow', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': False, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath+'*/*file*', 'UseSudo': True, 'Type': u'file'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallWildFileFollowLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallWildFileFollowLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallWildTypeWildFollowLink(self):
        d = {'Links': u'follow', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': False, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath+'*/*', 'UseSudo': True, 'Type': u'*'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallWildTypeWildFollowLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallWildTypeWildFollowLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallWildDirRecurseFollowLink(self):
        d = {'Links': u'follow', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': True, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath+'*/*dir*', 'UseSudo': True, 'Type': u'directory'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallWildDirRecurseFollowLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallWildDirRecurseFollowLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallWildFileRecurseFollowLink(self):
        d = {'Links': u'follow', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': True, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath+'*/*file*', 'UseSudo': True, 'Type': u'file'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallWildFileRecurseFollowLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallWildFileRecurseFollowLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallWildTypeWildRecurseFollowLink(self):
        d = {'Links': u'follow', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': True, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath+'*/*', 'UseSudo': True, 'Type': u'*'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallWildTypeWildRecurseFollowLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallWildTypeWildRecurseFollowLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']


    def testFileInventoryInventory_MarshallDirManageLink(self):
        d = {'Links': u'manage', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': False, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath, 'UseSudo': True, 'Type': u'directory'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallDirManageLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallDirManageLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallFileManageLink(self):
        d = {'Links': u'manage', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': False, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath, 'UseSudo': True, 'Type': u'file'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallFileManageLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallFileManageLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallTypeWildManageLink(self):
        d = {'Links': u'manage', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': False, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath, 'UseSudo': True, 'Type': u'*'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallTypeWildManageLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallTypeWildManageLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallDirRecurseManageLink(self):
        d = {'Links': u'manage', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': True, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath, 'UseSudo': True, 'Type': u'directory'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallDirRecurseManageLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallDirRecurseManageLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallFileRecurseManageLink(self):
        d = {'Links': u'manage', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': True, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath, 'UseSudo': True, 'Type': u'file'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallFileRecurseManageLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallFileRecurseManageLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallTypeWildRecurseManageLink(self):
        d = {'Links': u'manage', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': True, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath, 'UseSudo': True, 'Type': u'*'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallTypeWildRecurseManageLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallTypeWildRecurseManageLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallWildDirManageLink(self):
        d = {'Links': u'manage', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': False, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath+'*dir*', 'UseSudo': True, 'Type': u'directory'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallWildDirManageLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallWildDirManageLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallWildFileManageLink(self):
        d = {'Links': u'manage', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': False, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath+'*/*file*', 'UseSudo': True, 'Type': u'file'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallWildFileManageLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallWildFileManageLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallWildTypeWildManageLink(self):
        d = {'Links': u'manage', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': False, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath+'*/*', 'UseSudo': True, 'Type': u'*'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallWildTypeWildManageLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallWildTypeWildManageLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallWildDirRecurseManageLink(self):
        d = {'Links': u'manage', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': True, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath+'*/*dir*', 'UseSudo': True, 'Type': u'directory'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallWildDirRecurseManageLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallWildDirRecurseManageLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallWildFileRecurseManageLink(self):
        d = {'Links': u'manage', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': True, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath+'*/*file*', 'UseSudo': True, 'Type': u'file'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallWildFileRecurseManageLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallWildFileRecurseManageLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']

    def testFileInventoryInventory_MarshallWildTypeWildRecurseManageLink(self):
        d = {'Links': u'manage', 'MaxOutputSize': None, \
             'Checksum': u'md5', 'Recurse': True, \
             'MaxContentsReturnable': None, \
             'DestinationPath': self.basepath+'*/*', 'UseSudo': True, 'Type': u'*'}
        r = nxFileInventory.Inventory_Marshall(**d)
        self.assertTrue(r[0] == 0,'Inventory_Marshall('+repr(d)+')[0] should return == 0') 
        if self.create_files:
            self.SerializeInventoryObject('testFileInventoryInventory_MarshallWildTypeWildRecurseManageLink',r)
        l = self.MakeList(r)
        g = self.DeserializeInventoryObject('testFileInventoryInventory_MarshallWildTypeWildRecurseManageLink')
        self.assertTrue(g == l, repr(g) + '\n should be == to \n' + repr(l))
#        for d in r[1]['__Inventory'].value:
#            print d['DestinationPath'], d['Contents']



######################################
if __name__ == '__main__':
    s1=unittest2.TestLoader().loadTestsFromTestCase(nxUserTestCases)
    s2=unittest2.TestLoader().loadTestsFromTestCase(nxGroupTestCases)
    s3=unittest2.TestLoader().loadTestsFromTestCase(nxFileTestCases)
    s4=unittest2.TestLoader().loadTestsFromTestCase(nxScriptTestCases)
    s5=unittest2.TestLoader().loadTestsFromTestCase(nxServiceTestCases)
    s6=unittest2.TestLoader().loadTestsFromTestCase(nxPackageTestCases)
    s7=unittest2.TestLoader().loadTestsFromTestCase(nxSshAuthorizedKeysTestCases)
    s8=unittest2.TestLoader().loadTestsFromTestCase(nxEnvironmentTestCases)
    s9=unittest2.TestLoader().loadTestsFromTestCase(nxFirewallTestCases)
    s10=unittest2.TestLoader().loadTestsFromTestCase(nxArchiveTestCases)
    s11=unittest2.TestLoader().loadTestsFromTestCase(nxFileLineTestCases)
    s12=unittest2.TestLoader().loadTestsFromTestCase(nxDNSServerAddressTestCases)
    s13=unittest2.TestLoader().loadTestsFromTestCase(nxComputerTestCases)
    s14=unittest2.TestLoader().loadTestsFromTestCase(nxIPAddressTestCases)
    s15=unittest2.TestLoader().loadTestsFromTestCase(nxMySqlDatabaseTestCases)
    s16=unittest2.TestLoader().loadTestsFromTestCase(nxMySqlUserTestCases)
    s17=unittest2.TestLoader().loadTestsFromTestCase(nxMySqlGrantTestCases)
    s18=unittest2.TestLoader().loadTestsFromTestCase(nxFileInventoryTestCases)
    alltests = unittest2.TestSuite([s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18])
    if not unittest2.TextTestRunner(stream=sys.stdout,verbosity=0).run(alltests).wasSuccessful():
        sys.exit(1)
