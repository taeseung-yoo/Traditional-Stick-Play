import ctypes


def gotoxy(x, y):  # x, y 값을 받아서 커서를 해당 위치로 이동
    return ctypes.windll.kernel32.SetConsoleCursorPosition(
        ctypes.windll.kernel32.GetStdHandle(-11),
        (((y & 0xFFFF) << 0x10) | (x & 0xFFFF)),
    )


class CUSTOM_CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
    _fields_ = [
        ("dwSize", ctypes.c_uint),
        ("dwCursorPosition", ctypes.c_uint),
        ("wAttributes", ctypes.c_ushort),
        ("srWindow", ctypes.c_ulonglong),
        ("dwMaximumWindowSize", ctypes.c_uint),
    ]


def GetConsoleCursorPos():  # 현재 커서의 위치를 반환
    ccsbi = CUSTOM_CONSOLE_SCREEN_BUFFER_INFO()
    ccsbi.dwSize = 0x16
    ctypes.windll.kernel32.GetConsoleScreenBufferInfo(
        ctypes.windll.kernel32.GetStdHandle(-11), ctypes.byref(ccsbi)
    )
    pos = ccsbi.dwCursorPosition
    return (pos & 0xFFFF), ((pos >> 0x10) & 0xFFFF)
