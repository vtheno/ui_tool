import sys
import ctypes
from typing import Any


if sys.platform == "win32":
    user32 = ctypes.windll.user32
    imm32 = ctypes.windll.imm32

    def set_window_layered(hwnd: Any):
        GWL_EXSTYLE = -20
        WS_EX_LAYERED = 0x00080000
        WS_EX_TRANSPARENT = 0x00000020
        user32.SetWindowLongA(hwnd, GWL_EXSTYLE, WS_EX_LAYERED | WS_EX_TRANSPARENT)

    def unset_window_layered(hwnd: Any):
        GWL_EXSTYLE = -20
        WS_EX_LAYERED = 0x00080000
        user32.SetWindowLongA(hwnd, GWL_EXSTYLE, WS_EX_LAYERED)

    class POINT(ctypes.Structure):
        _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

    class RECT(ctypes.Structure):
        _fields_ = [
            ("left", ctypes.c_long),
            ("top", ctypes.c_long),
            ("right", ctypes.c_long),
            ("bottom", ctypes.c_long),
        ]

    class COMPOSITIONFORM(ctypes.Structure):
        _fields_ = [
            ("dwStyle", ctypes.c_ulong),
            ("ptCurrentPos", POINT),
            ("rcArea", RECT),
        ]

    def set_ime_position(hwnd: Any, x: int, y: int) -> None:
        # hwnd = ctypes.windll.user32.GetForegroundWindow()
        # ctypes.windll.user32.CreateCaret(hwnd, None, 5, 12)
        # ctypes.windll.user32.SetCaretPos(x, y)
        # ctypes.windll.user32.SetCaretBlinkTime(1000)
        # ctypes.windll.user32.ShowCaret(hwnd)
        hIMC = imm32.ImmGetContext(hwnd)
        CFS_POINT = 0x0002
        composition = COMPOSITIONFORM(dwStyle=CFS_POINT, ptCurrentPos=POINT(x, y))
        imm32.ImmSetCompositionWindow(hIMC, ctypes.byref(composition))
        imm32.ImmReleaseContext(hwnd, hIMC)
