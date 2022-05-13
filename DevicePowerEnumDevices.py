import ctypes
from ctypes import windll
from ctypes import sizeof
from ctypes import create_string_buffer
from ctypes import POINTER,byref
from ctypes import wintypes


PowrProf = windll.LoadLibrary('PowrProf.dll')
Kernel32 = windll.LoadLibrary('Kernel32.dll')


QueryIndex = 0
QueryInterpretationFlags = 0x08000000
QueryFlags = 0x00000001|0x00000002

pReturnBuffer = create_string_buffer(b'\000'*32)
print("pReturnBuffer = ",pReturnBuffer)

pBufferSize = byref(pReturnBuffer)
print("pBufferSize = ",pBufferSize)

pReturnBuffer = Kernel32.LocalAlloc(0x0040, pBufferSize)

result = PowrProf.DevicePowerEnumDevices(
                                QueryIndex,
                                QueryInterpretationFlags,
                                QueryFlags,
                                pReturnBuffer,
                                pBufferSize,
                                )
print(result)
