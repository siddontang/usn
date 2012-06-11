#coding:utf-8
#tangliu@kingsoft.com


import ctypes

from win32kernel import *

MAX_PATH = 256

def getFileSystemName(volumeName):    
    sysNameBuf = ctypes.create_unicode_buffer(MAX_PATH + 1)

    volName = volumeName.upper() + ":\\"
    ret = GetVolumeInformationW(
        ctypes.c_wchar_p(volName),
        None,
        0,
        None,
        None,
        None,
        sysNameBuf,
        len(sysNameBuf))

    if ret != 0:
        return sysNameBuf.value
    else:
        return ''
    
def checkNtfs(path):
    name = getFileSystemName(path)
    if name == 'NTFS':
        return True

    return False

def getVolumeHandle(volumeName):
    volumeName = volumeName.upper()
    name = "\\\\.\\" + volumeName + ":"
    hHandle = CreateFileW(ctypes.c_wchar_p(name),
                              FILE_GENERIC_READ,
                              FILE_SHARE_READ | FILE_SHARE_WRITE,
                              None,
                              OPEN_EXISTING,
                              FILE_ATTRIBUTE_READONLY,
                              None)
    return hHandle

def initUsnJournal(hVolHandle):
    br = DWORD()
    cujd = CREATE_USN_JOURNAL_DATA()
    cujd.MaximumSize = 0
    cujd.AllocationDelta = 0

    
    status = DeviceIoControl(hVolHandle,
                             FSCTL_CREATE_USN_JOURNAL,
                             ctypes.byref(cujd),
                             ctypes.sizeof(cujd),
                             None,
                             0,
                             ctypes.byref(br),
                             None)

    if status != 0:
        return True
    else:
        return GetLastError()

def getUsnJournal(hVolHandle):
    br = DWORD()
    usnData = USN_JOURNAL_DATA()
    ret = DeviceIoControl(hVolHandle,
                          FSCTL_QUERY_USN_JOURNAL,
                          None,
                          0,
                          ctypes.byref(usnData),
                          ctypes.sizeof(usnData),
                          ctypes.byref(br),
                          None)
    return usnData if ret == True else None

def enumUsnJournal(hVolHandle, usnData):
    med = MFT_ENUM_DATA()
    med.StartFileReferenceNumber = 0
    med.LowUsn = 0
    med.HighUsn = usnData.NextUsn

    bufLen = 4096
    buf = ctypes.create_string_buffer(bufLen)
    usnDataSize = DWORD()
    while True:
        ret = DeviceIoControl(hVolHandle,
                               FSCTL_ENUM_USN_DATA,
                               ctypes.byref(med),
                               ctypes.sizeof(med),
                               buf,
                               bufLen,
                               ctypes.byref(usnDataSize),
                               None)
        if ret != True:
            print 'FALSE'
            break

        dwRetBytes = usnDataSize.value - ctypes.sizeof(USN)
        offset = 0

        while dwRetBytes > 0:
            usnRecord = ctypes.cast(ctypes.byref(buf, ctypes.sizeof(USN) + offset), LPUSN_RECORD)[0]
            
            dealUsnRecord(usnRecord)
            
            recordLen = usnRecord.RecordLength
            dwRetBytes -= recordLen
            offset += recordLen

        med.StartFileReferenceNumber = ctypes.cast(ctypes.byref(buf), LPUSN)[0]
            
def dealUsnRecord(usnRecord):
    ptr = ctypes.addressof(usnRecord) + USN_RECORD.FileName.offset
    fileName = ctypes.string_at(ptr, usnRecord.FileNameLength)
    fileReferecnNumber = usnRecord.FileReferenceNumber
    parentReferenceNumber = usnRecord.ParentFileReferenceNumber
    reason = usnRecord.Reason

    
    pass

def testMain():
    if not checkNtfs("c"):
        return
    handle = getVolumeHandle("c")
    print initUsnJournal(handle)
    data =  getUsnJournal(handle)
    
    if data:
        enumUsnJournal(handle, data)
    
if __name__ == '__main__':
    testMain()
