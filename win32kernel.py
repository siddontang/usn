#coding:utf-8
#tangliu@kingsoft.com

import ctypes

_kernel = ctypes.windll.kernel32

# Win32 API => ctypes type mapping
LPCTSTR = ctypes.c_wchar_p
LPTSTR = LPCTSTR
WORD = ctypes.c_ushort
DWORD = ctypes.c_uint # hmm.. actually unsigned long
LPDWORD = ctypes.POINTER(DWORD)
DWORDLONG = ctypes.c_ulonglong
LPDWORDLONG = ctypes.POINTER(DWORDLONG)
HANDLE = ctypes.c_void_p # Notes: actually represented as int in python
LPCVOID = ctypes.c_void_p
LPVOID = LPCVOID
HANDLE = LPVOID
BOOL = ctypes.c_uint
LARGE_INTEGER = ctypes.c_longlong
PLARGE_INTEGER = ctypes.POINTER(LARGE_INTEGER)
ULONG_PTR = LPVOID
LONG_PTR = LPVOID
va_list = ctypes.c_char_p
va_list_p = ctypes.POINTER(va_list)
USN = ctypes.c_longlong
LPUSN = ctypes.POINTER(USN)

class SECURITY_ATTRIBUTES(ctypes.Structure):
    _fields_ = [ ('nLength', DWORD),
                 ('lpSecurityDescriptor', LPVOID),
                 ('bInheritHandle', BOOL) ]
LPSECURITY_ATTRIBUTES = ctypes.POINTER(SECURITY_ATTRIBUTES)

class OVERLAPPED(ctypes.Structure):
    _fields_ = [ ('Internal', ULONG_PTR),
                 ('InternalHigh', ULONG_PTR),
                 ('Offset', DWORD),
                 ('OffsetHigh', DWORD),
                 ('hEvent', HANDLE) ]
LPOVERLAPPED = ctypes.POINTER(OVERLAPPED)

INVALID_HANDLE_VALUE = HANDLE( -1 )
INVALID_FILE_SIZE = DWORD( 0xFFFFFFFF )
INVALID_SET_FILE_POINTER = DWORD( -1 )
INVALID_FILE_ATTRIBUTES = DWORD( -1 )

FILE_BEGIN = DWORD(0)
FILE_CURRENT = DWORD(1)
FILE_END = DWORD(2)

DELETE = (0x00010000)
READ_CONTROL = (0x00020000)
WRITE_DAC = (0x00040000)
WRITE_OWNER = (0x00080000)
SYNCHRONIZE = (0x00100000)

# The following are masks for the predefined standard access types
STANDARD_RIGHTS_REQUIRED = (0x000F0000)

STANDARD_RIGHTS_READ = (READ_CONTROL)
STANDARD_RIGHTS_WRITE = (READ_CONTROL)
STANDARD_RIGHTS_EXECUTE = (READ_CONTROL)

STANDARD_RIGHTS_ALL = (0x001F0000)

SPECIFIC_RIGHTS_ALL = (0x0000FFFF)

# AccessSystemAcl access type
ACCESS_SYSTEM_SECURITY = (0x01000000)

# MaximumAllowed access type
MAXIMUM_ALLOWED = (0x02000000)



FILE_READ_DATA = ( 0x0001 ) #  file & pipe
FILE_LIST_DIRECTORY = ( 0x0001 ) #  directory

FILE_WRITE_DATA = ( 0x0002 ) #  file & pipe
FILE_ADD_FILE = ( 0x0002 ) #  directory

FILE_APPEND_DATA = ( 0x0004 ) #  file
FILE_ADD_SUBDIRECTORY = ( 0x0004 ) #  directory
FILE_CREATE_PIPE_INSTANCE = ( 0x0004 ) #  named pipe


FILE_READ_EA = ( 0x0008 ) #  file & directory

FILE_WRITE_EA = ( 0x0010 ) #  file & directory

FILE_EXECUTE = ( 0x0020 ) #  file
FILE_TRAVERSE = ( 0x0020 ) #  directory

FILE_DELETE_CHILD = ( 0x0040 ) #  directory

FILE_READ_ATTRIBUTES = ( 0x0080 ) #  all

FILE_WRITE_ATTRIBUTES = ( 0x0100 ) #  all

FILE_ALL_ACCESS = (STANDARD_RIGHTS_REQUIRED | SYNCHRONIZE | 0x1FF)

FILE_GENERIC_READ = (STANDARD_RIGHTS_READ     |
                     FILE_READ_DATA           |
                     FILE_READ_ATTRIBUTES     |
                     FILE_READ_EA             |
                     SYNCHRONIZE)


FILE_GENERIC_WRITE = (STANDARD_RIGHTS_WRITE    |
                      FILE_WRITE_DATA          |
                      FILE_WRITE_ATTRIBUTES    |
                      FILE_WRITE_EA            |
                      FILE_APPEND_DATA         |
                      SYNCHRONIZE)

FILE_GENERIC_EXECUTE = (STANDARD_RIGHTS_EXECUTE  |
                        FILE_READ_ATTRIBUTES     |
                        FILE_EXECUTE             |
                        SYNCHRONIZE)


FILE_SHARE_READ = 0x00000001  
FILE_SHARE_WRITE = 0x00000002  
FILE_SHARE_DELETE = 0x00000004  
FILE_ATTRIBUTE_READONLY = 0x00000001  
FILE_ATTRIBUTE_HIDDEN = 0x00000002  
FILE_ATTRIBUTE_SYSTEM = 0x00000004  
FILE_ATTRIBUTE_DIRECTORY = 0x00000010  
FILE_ATTRIBUTE_ARCHIVE = 0x00000020  
FILE_ATTRIBUTE_DEVICE = 0x00000040  
FILE_ATTRIBUTE_NORMAL = 0x00000080  
FILE_ATTRIBUTE_TEMPORARY = 0x00000100  
FILE_ATTRIBUTE_SPARSE_FILE = 0x00000200  
FILE_ATTRIBUTE_REPARSE_POINT = 0x00000400  
FILE_ATTRIBUTE_COMPRESSED = 0x00000800  
FILE_ATTRIBUTE_OFFLINE = 0x00001000  
FILE_ATTRIBUTE_NOT_CONTENT_INDEXED = 0x00002000  
FILE_ATTRIBUTE_ENCRYPTED = 0x00004000  
FILE_ATTRIBUTE_VIRTUAL = 0x00010000  
FILE_NOTIFY_CHANGE_FILE_NAME = 0x00000001   
FILE_NOTIFY_CHANGE_DIR_NAME = 0x00000002   
FILE_NOTIFY_CHANGE_ATTRIBUTES = 0x00000004   
FILE_NOTIFY_CHANGE_SIZE = 0x00000008   
FILE_NOTIFY_CHANGE_LAST_WRITE = 0x00000010   
FILE_NOTIFY_CHANGE_LAST_ACCESS = 0x00000020   
FILE_NOTIFY_CHANGE_CREATION = 0x00000040   
FILE_NOTIFY_CHANGE_SECURITY = 0x00000100   
FILE_ACTION_ADDED = 0x00000001   
FILE_ACTION_REMOVED = 0x00000002   
FILE_ACTION_MODIFIED = 0x00000003   
FILE_ACTION_RENAMED_OLD_NAME = 0x00000004   
FILE_ACTION_RENAMED_NEW_NAME = 0x00000005   
MAILSLOT_NO_MESSAGE = DWORD(-1)
MAILSLOT_WAIT_FOREVER = DWORD(-1)
FILE_CASE_SENSITIVE_SEARCH = 0x00000001  
FILE_CASE_PRESERVED_NAMES = 0x00000002  
FILE_UNICODE_ON_DISK = 0x00000004  
FILE_PERSISTENT_ACLS = 0x00000008  
FILE_FILE_COMPRESSION = 0x00000010  
FILE_VOLUME_QUOTAS = 0x00000020  
FILE_SUPPORTS_SPARSE_FILES = 0x00000040  
FILE_SUPPORTS_REPARSE_POINTS = 0x00000080  
FILE_SUPPORTS_REMOTE_STORAGE = 0x00000100  
FILE_VOLUME_IS_COMPRESSED = 0x00008000  
FILE_SUPPORTS_OBJECT_IDS = 0x00010000  
FILE_SUPPORTS_ENCRYPTION = 0x00020000  
FILE_NAMED_STREAMS = 0x00040000  
FILE_READ_ONLY_VOLUME = 0x00080000  
FILE_SEQUENTIAL_WRITE_ONCE = 0x00100000  
FILE_SUPPORTS_TRANSACTIONS = 0x00200000  

CREATE_NEW         = 1
CREATE_ALWAYS      = 2
OPEN_EXISTING      = 3
OPEN_ALWAYS        = 4
TRUNCATE_EXISTING  = 5

ERROR_HANDLE_EOF = 38

FORMAT_MESSAGE_ALLOCATE_BUFFER = 0x00000100
FORMAT_MESSAGE_IGNORE_INSERTS = 0x00000200
FORMAT_MESSAGE_FROM_STRING = 0x00000400
FORMAT_MESSAGE_FROM_HMODULE = 0x00000800
FORMAT_MESSAGE_FROM_SYSTEM = 0x00001000
FORMAT_MESSAGE_ARGUMENT_ARRAY = 0x00002000
FORMAT_MESSAGE_MAX_WIDTH_MASK = 0x000000FF

FSCTL_CREATE_USN_JOURNAL = 0x000900E7
FSCTL_QUERY_USN_JOURNAL = 0x000900F4
FSCTL_ENUM_USN_DATA = 0x000900B3
FSCTL_READ_USN_JOURNAL = 0x000900BB


def MAKELANGID(p, s):
    return DWORD( (s << 10) | p )

def PRIMARYLANGID(lgid):
    return DWORD( lgid & 0x3ff )
    
def SUBLANGID(lgid):
    return DWORD( lgid >> 10 )

LANG_NEUTRAL = 0x00
SUBLANG_DEFAULT = 0x01    # user default

def make_windows_error( exc_class=WindowsError ):
    'Raise WindowsError exception using GetLastError message.'
    win_error_id = GetLastError();
    flags = DWORD( FORMAT_MESSAGE_FROM_SYSTEM |
                   FORMAT_MESSAGE_IGNORE_INSERTS )
    msg_buffer = ctypes.create_unicode_buffer( 512 )
    lang_id = MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT)
    length = FormatMessageW( flags, LPCVOID(), win_error_id, 
        lang_id, msg_buffer, len(msg_buffer), va_list_p() )
    error = exc_class( msg_buffer.value )
    error.errno = 0
    error.winerror = win_error_id
    error.strerror = msg_buffer.value
    return error

def check_valid_handle( handle, exc_class=WindowsError ):
    if handle.value == INVALID_HANDLE_VALUE:
        raise make_windows_error( exc_class )

def check_succeed( c_bool_value ):
    if not c_bool_value:
        raise make_windows_error()

def check_io_succeed( c_bool_value ):
    if not c_bool_value:
        raise make_windows_error( IOError )


class CREATE_USN_JOURNAL_DATA(ctypes.Structure):
    _fields_ = [ ('MaximumSize', DWORDLONG),
                 ('AllocationDelta', DWORDLONG) ]
LPCREATE_USN_JOURNAL_DATA = ctypes.POINTER(CREATE_USN_JOURNAL_DATA)

class USN_JOURNAL_DATA(ctypes.Structure):
    _fields_ = [ ('UsnJournalID', DWORDLONG),
                 ('FirstUsn', USN),
                 ('NextUsn', USN),
                 ('LowestValidUsn', USN),
                 ('MaxUsn', USN),
                 ('MaximumSize', DWORDLONG),
                 ('AllocationDelta', DWORDLONG)]
LPUSN_JOURNAL_DATA = ctypes.POINTER(USN_JOURNAL_DATA)

class USN_RECORD(ctypes.Structure):
    _fields_ = [ ('RecordLength', DWORD),
                 ('MajorVersion', WORD),
                 ('MinorVersion', WORD),
                 ('FileReferenceNumber', DWORDLONG),
                 ('ParentFileReferenceNumber', DWORDLONG),
                 ('Usn', USN),
                 ('TimeStamp', LARGE_INTEGER),
                 ('Reason', DWORD),
                 ('SourceInfo', DWORD),
                 ('SecurityId', DWORD),
                 ('FileAttribute', DWORD),
                 ('FileNameLength', WORD),
                 ('FileNameOffset', WORD),
                 ('FileName', ctypes.c_wchar * 1)]
LPUSN_RECORD = ctypes.POINTER(USN_RECORD)

class MFT_ENUM_DATA(ctypes.Structure):
    _fields_ = [ ('StartFileReferenceNumber', DWORDLONG),
                 ('LowUsn', USN),
                 ('HighUsn', USN)]
LPMFT_ENUM_DATA = ctypes.POINTER(MFT_ENUM_DATA)

class READ_USN_JOURNAL_DATA(ctypes.Structure):
    _fields_ = [ ('StartUsn', USN),
                 ('ReasonMask', DWORD),
                 ('ReturnOnlyOnClose', DWORD),
                 ('Timeout', DWORDLONG),
                 ('BytesToWaitFor', DWORDLONG),
                 ('UsnJournalID', DWORDLONG)]
LPREAD_USN_JOURNAL_DATA = ctypes.POINTER(READ_USN_JOURNAL_DATA)

_kernel.GetStdHandle.argtypes= [DWORD]
_kernel.GetStdHandle.restype=HANDLE
_kernel.GetStdHandle.__doc__="HANDLE GetStdHandle(__in DWORD nStdHandle)"

_kernel.CreateFileW.argtypes= [LPCTSTR, DWORD, DWORD, LPSECURITY_ATTRIBUTES, DWORD, DWORD, HANDLE]
_kernel.CreateFileW.restype=HANDLE
_kernel.CreateFileW.__doc__="HANDLE CreateFile(__in LPCTSTR lpFileName, __in DWORD dwDesiredAccess, __in DWORD dwShareMode, __in LPSECURITY_ATTRIBUTES lpSecurityAttributes, __in DWORD dwCreationDisposition, __in DWORD dwFlagsAndAttributes, __in HANDLE hTemplateFile)"

_kernel.WriteFile.argtypes= [HANDLE, LPCVOID, DWORD, LPDWORD, LPOVERLAPPED]
_kernel.WriteFile.restype=BOOL
_kernel.WriteFile.__doc__="BOOL WriteFile(__in HANDLE hFile, __in LPCVOID lpBuffer, __in DWORD nNumberOfBytesToWrite, __out LPDWORD lpNumberOfBytesWritten, __in LPOVERLAPPED lpOverlapped)"

_kernel.ReadFile.argtypes= [HANDLE, LPVOID, DWORD, LPDWORD, LPOVERLAPPED]
_kernel.ReadFile.restype=BOOL
_kernel.ReadFile.__doc__="BOOL ReadFile(__in HANDLE hFile, __out LPVOID lpBuffer, __in DWORD nNumberOfBytesToRead, __out LPDWORD lpNumberOfBytesRead, __in LPOVERLAPPED lpOverlapped)"

_kernel.GetLastError.argtypes= []
_kernel.GetLastError.restype=DWORD
_kernel.GetLastError.__doc__="DWORD GetLastError()"

_kernel.FormatMessageW.argtypes= [DWORD, LPCVOID, DWORD, DWORD, LPTSTR, DWORD, va_list_p]
_kernel.FormatMessageW.restype=DWORD
_kernel.FormatMessageW.__doc__="DWORD FormatMessage(__in DWORD dwFlags, __in LPCVOID lpSource, __in DWORD dwMessageId, __in DWORD dwLanguageId, __out LPTSTR lpBuffer, __in DWORD nSize, __in va_list_p Arguments)"

_kernel.SetFilePointerEx.argtypes= [HANDLE, LARGE_INTEGER, PLARGE_INTEGER, DWORD]
_kernel.SetFilePointerEx.restype=BOOL
_kernel.SetFilePointerEx.__doc__="BOOL SetFilePointerEx(__in HANDLE hFile, __in LARGE_INTEGER liDistanceToMove, __out_opt PLARGE_INTEGER lpNewFilePointer, __in DWORD dwMoveMethod)"

_kernel.GetFileSizeEx.argtypes= [HANDLE, PLARGE_INTEGER]
_kernel.GetFileSizeEx.restype=BOOL
_kernel.GetFileSizeEx.__doc__="BOOL GetFileSizeEx(__in HANDLE hFile, __out PLARGE_INTEGER lpFileSize)"

_kernel.FlushFileBuffers.argtypes= [HANDLE]
_kernel.FlushFileBuffers.restype=BOOL
_kernel.FlushFileBuffers.__doc__="BOOL FlushFileBuffers(__in HANDLE hFile)"

_kernel.SetEndOfFile.argtypes= [HANDLE]
_kernel.SetEndOfFile.restype=BOOL
_kernel.SetEndOfFile.__doc__="BOOL SetEndOfFile(__in HANDLE hFile)"

_kernel.CloseHandle.argtypes= [HANDLE]
_kernel.CloseHandle.restype=BOOL
_kernel.CloseHandle.__doc__="BOOL CloseHandle(__in HANDLE hObject)"

_kernel.GetVolumeInformationW.argtypes=[LPCTSTR, LPTSTR, DWORD, LPDWORD, LPDWORD, LPDWORD, LPTSTR, DWORD]
_kernel.GetVolumeInformationW.restype=BOOL

_kernel.DeviceIoControl.argtypes = [HANDLE, DWORD, LPVOID, DWORD, LPVOID, DWORD, LPDWORD, LPOVERLAPPED]
_kernel.DeviceIoControl.restype = BOOL

GetStdHandle = _kernel.GetStdHandle
CreateFileW = _kernel.CreateFileW
WriteFile = _kernel.WriteFile
ReadFile = _kernel.ReadFile
GetLastError = _kernel.GetLastError
FormatMessageW = _kernel.FormatMessageW
SetFilePointerEx = _kernel.SetFilePointerEx
GetFileSizeEx = _kernel.GetFileSizeEx
FlushFileBuffers = _kernel.FlushFileBuffers
SetEndOfFile = _kernel.SetEndOfFile
CloseHandle = _kernel.CloseHandle
GetVolumeInformationW = _kernel.GetVolumeInformationW
DeviceIoControl = _kernel.DeviceIoControl
