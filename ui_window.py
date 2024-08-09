from __future__ import annotations
import sys
from typing import Any, Callable, Optional
from threading import Thread
from enum import Enum

import glfw

from ui_enum import (
    action_mappings,
    key_buttons_mappings,
    mouse_buttons_mappings,
)
from ui_tool import set_ime_position, set_window_layered, unset_window_layered

"""
REFERENCES:
https://learnopengl.com
https://www.glfw.org/
https://pypi.org/project/glfw/
https://docs.python.org/3/library/ctypes.html

https://learn.microsoft.com/en-us/answers/questions/1167835/how-can-i-move-the-ime-window-to-a-specific-positi
https://docs.pingcode.com/ask/ask-ask/176003.html
https://learn.microsoft.com/zh-cn/windows/win32/api/winuser/nf-winuser-setlayeredwindowattributes
"""


class WindowInitException(Exception):
    pass


class EventKind(Enum):
    KeyButton = 0
    KeyTyping = 1
    MouseButton = 2
    MouseScroll = 3
    DropIn = 4


class Event:
    def __init__(
        self,
        kind: EventKind,
        button: Optional[int] = None,
        action: Optional[int] = None,
        mods: Optional[int] = None,
        dx: Optional[float] = None,
        dy: Optional[float] = None,
        codepoint: Optional[int] = None,
        pathes: Optional[list[str]] = None,
    ) -> None:
        self.kind: EventKind = kind
        self.button: Optional[int] = button
        self.action: Optional[int] = action
        self.mods: Optional[int] = mods
        self.dx: Optional[float] = dx
        self.dy: Optional[float] = dy
        self.codepoint: Optional[int] = codepoint
        self.pathes = pathes

    def __repr__(self) -> str:
        kind = self.kind
        if kind in (EventKind.KeyButton, EventKind.MouseButton):
            if kind == EventKind.KeyButton:
                mappings = key_buttons_mappings
            else:
                mappings = mouse_buttons_mappings
            button = mappings[self.button]
            action = action_mappings[self.action]
            mods = self.mods
            return f"Event({kind=}, {button=}, {action=}, {mods=})"
        else:
            if kind == EventKind.MouseScroll:
                dx = self.dx
                dy = self.dy
                return f"Event({kind=}, {dx=}, {dy=})"
            elif kind == EventKind.KeyTyping:
                codepoint = self.codepoint
                return f"Event({kind=}, {codepoint=})"
            else:
                pathes = self.pathes
                return f"Event({kind=}, {pathes=})"


class WindowProperties:
    def __init__(self, window: Window) -> None:
        self.window = window

        self._window_focused = True
        self._window_width, self._window_height = self.window.window_size
        self._window_x, self._window_y = self.window.window_pos
        self._mouse_x, self._mouse_y = self.window.mouse_pos
        self._mouse_entered = False

    @property
    def title(self) -> str:
        return self.window.window_title

    @property
    def visible(self) -> bool:
        return self.window.window_visible

    @property
    def iconified(self) -> bool:
        return self.window.window_iconified

    @property
    def maximized(self) -> bool:
        return self.window.window_maximized

    @property
    def hovered(self) -> bool:
        return self.window.window_hovered

    @property
    def resizeable(self) -> bool:
        return self.window.window_resizeable

    @property
    def decorated(self) -> bool:
        return self.window.window_decorated

    @property
    def auto_iconify(self) -> bool:
        return self.window.window_auto_iconify

    @property
    def floating(self) -> bool:
        return self.window.window_floating

    @property
    def focused(self) -> bool:
        return self._window_focused

    @property
    def width(self) -> int:
        return self._window_width

    @property
    def height(self) -> int:
        return self._window_height

    @property
    def x(self) -> int:
        return self._window_x

    @property
    def y(self) -> int:
        return self._window_y

    @property
    def mx(self):
        return self._mouse_x

    @property
    def my(self):
        return self._mouse_y

    @property
    def mentered(self):
        return self._mouse_entered


class Window:
    def __init__(
        self,
        title: str,
        width: int,
        height: int,
        major: int = 4,
        minor: int = 5,
    ) -> None:
        self._rendering: bool = True
        self._renderer: Optional[Callable] = None
        self._typing: bool = False

        if not glfw.init():
            raise WindowInitException("GLFW Init Failed!")
        glfw.window_hint(glfw.CLIENT_API, glfw.OPENGL_API)  # glfw.OPENGL_ES_API
        glfw.window_hint(glfw.DOUBLEBUFFER, glfw.TRUE)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, major)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, minor)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.window_hint(glfw.TRANSPARENT_FRAMEBUFFER, glfw.TRUE)
        glfw.window_hint(glfw.VISIBLE, glfw.FALSE)

        self._window = glfw.create_window(width, height, title, None, None)
        if not self._window:
            glfw.terminate()
            raise WindowInitException("GLFW Create Window Failed!")

        self.properties = WindowProperties(self)

    # region Renderer
    def renderer(self):
        return

    # endregion
    # region Properties

    @property
    def window_pos(self) -> tuple[int, int]:
        pos = glfw.get_window_pos(self._window)
        return pos

    @property
    def window_size(self) -> tuple[int, int]:
        size = glfw.get_window_size(self._window)
        return size

    @property
    def window_title(self) -> str:
        title = glfw.get_window_title(self._window)
        if title is None:
            return ""
        return title

    @property
    def window_visible(self) -> bool:
        visible = glfw.get_window_attrib(self._window, glfw.VISIBLE)
        return visible

    @property
    def window_iconified(self) -> bool:
        iconified = glfw.get_window_attrib(self._window, glfw.ICONIFIED)
        return iconified

    @property
    def window_maximized(self) -> bool:
        maximized = glfw.get_window_attrib(self._window, glfw.MAXIMIZED)
        return maximized

    @property
    def window_hovered(self) -> bool:
        hovered = glfw.get_window_attrib(self._window, glfw.HOVERED)
        return hovered

    @property
    def window_resizeable(self) -> bool:
        resizeable = glfw.get_window_attrib(self._window, glfw.RESIZABLE)
        return resizeable

    @property
    def window_decorated(self) -> bool:
        decorated = glfw.get_window_attrib(self._window, glfw.DECORATED)
        return decorated

    @property
    def window_auto_iconify(self) -> bool:
        auto_iconify = glfw.get_window_attrib(self._window, glfw.AUTO_ICONIFY)
        return auto_iconify

    @property
    def window_floating(self) -> bool:
        floating = glfw.get_window_attrib(self._window, glfw.FLOATING)
        return floating

    @property
    def mouse_pos(self) -> tuple[float, float]:
        pos = glfw.get_cursor_pos(self._window)
        return pos

    if sys.platform == "win32":

        @property
        def hwnd(self) -> Any:
            hwnd = glfw.get_win32_window(self._window)
            return hwnd

    # endregion
    # region Action
    def set_typing(self, typing: bool = False):
        self._typing = typing

    def set_title(self, title: str):
        glfw.set_window_title(self._window, title)

    def get_clipboard(self, is_global: bool = True) -> str:
        content = glfw.get_clipboard_string(None if is_global else self._window)
        return content

    def set_clipboard(self, content: str, is_global: bool = True):
        glfw.set_clipboard_string(None if is_global else self._window, content)

    def set_size(self, width: int, height: int):
        glfw.set_window_size(self._window, width, height)

    def set_pos(self, x: int, y: int):
        glfw.set_window_pos(self._window, x, y)

    def set_resizeable(self, value: bool = True):
        glfw.set_window_attrib(
            self._window, glfw.RESIZABLE, glfw.TRUE if value else glfw.FALSE
        )

    def set_decorated(self, value: bool = True):
        glfw.set_window_attrib(
            self._window, glfw.DECORATED, glfw.TRUE if value else glfw.FALSE
        )

    def set_auto_iconify(self, value: bool = True):
        glfw.set_window_attrib(
            self._window, glfw.AUTO_ICONIFY, glfw.TRUE if value else glfw.FALSE
        )

    def set_floating(self, value: bool = True):
        glfw.set_window_attrib(
            self._window, glfw.FLOATING, glfw.TRUE if value else glfw.FALSE
        )

    def show(self):
        glfw.show_window(self._window)
        self.request_attention()

    def hide(self):
        glfw.hide_window(self._window)

    def request_attention(self):
        glfw.request_window_attention(self._window)

    def maximize(self):
        glfw.maximize_window(self._window)

    def iconify(self):
        glfw.iconify_window(self._window)

    def restore(self):
        glfw.restore_window(self._window)

    def focus(self):
        glfw.focus_window(self._window)

    def close(self):
        glfw.set_window_should_close(self._window, glfw.TRUE)

    def fullscreen(self):
        monitor = glfw.get_primary_monitor()
        mode = glfw.get_video_mode(monitor)
        size = mode.size
        self.set_decorated(False)
        self.set_floating(True)
        self.set_pos(0, 0)
        self.set_size(size.width, size.height - 1)

    if sys.platform == "win32":

        def layered(self, value: bool = True):
            func = set_window_layered if value else unset_window_layered
            func(self.hwnd)

        def set_ime_pos(self, x: int, y: int):
            set_ime_position(self.hwnd, x, y)

    # endregion
    # region Callbacks
    def _window_focus_cb(self, _, focused: bool):
        self.properties._window_focused = focused

    def _window_size_cb(self, _, width: int, height: int):
        self.properties._window_width = width
        self.properties._window_height = height

    def _window_pos_cb(self, _, x: int, y: int):
        self.properties._window_x = x
        self.properties._window_y = y

    def _window_maximized_cb(self, _, maximized: bool):
        # print(f"{maximized=}")
        return

    def _window_iconified_cb(self, _, iconified: bool):
        # print(f"{iconified=}")
        return

    def _mouse_pos_cb(self, _, x: float, y: float):
        self.properties._mouse_x = x
        self.properties._mouse_y = y

    def _mouse_enter_cb(self, _, entered: bool):
        self.properties._mouse_entered = entered

    def _mouse_scroll_cb(self, _, dx: float, dy: float):
        self.dispatch(Event(kind=EventKind.MouseScroll, dx=dx, dy=dy))

    def _mouse_button_cb(self, _, button: int, action: int, mods: int):
        self.dispatch(
            Event(kind=EventKind.MouseButton, button=button, action=action, mods=mods)
        )

    def _key_button_cb(self, _, button: int, __, action: int, mods: int):
        self.dispatch(
            Event(kind=EventKind.KeyButton, button=button, action=action, mods=mods)
        )

    def _key_typing_cb(self, _, codepoint: int):
        if self._typing:
            self.dispatch(Event(kind=EventKind.KeyTyping, codepoint=codepoint))

    def _dropin_cb(self, _, pathes: list[str]):
        self.dispatch(Event(kind=EventKind.DropIn, pathes=pathes))

    def dispatch(self, ev: Event):
        print("[dispatch]", ev)

    def register_callbacks(self):
        # region Window
        glfw.set_window_focus_callback(self._window, self._window_focus_cb)
        glfw.set_window_size_callback(self._window, self._window_size_cb)
        glfw.set_window_pos_callback(self._window, self._window_pos_cb)
        glfw.set_window_maximize_callback(self._window, self._window_maximized_cb)
        glfw.set_window_iconify_callback(self._window, self._window_iconified_cb)
        # endregion
        # region Mouse
        glfw.set_cursor_pos_callback(self._window, self._mouse_pos_cb)
        glfw.set_cursor_enter_callback(self._window, self._mouse_enter_cb)
        glfw.set_scroll_callback(self._window, self._mouse_scroll_cb)
        glfw.set_mouse_button_callback(self._window, self._mouse_button_cb)
        # endregion
        # region Keyboard
        glfw.set_key_callback(self._window, self._key_button_cb)
        glfw.set_char_callback(self._window, self._key_typing_cb)
        # endregion
        glfw.set_drop_callback(self._window, self._dropin_cb)
        return

    # endregion

    # region RendererLoop
    def before_rendererloop(self):
        glfw.swap_interval(0)

    def after_rendererloop(self):
        return

    def rendererloop(self):
        glfw.make_context_current(self._window)
        self.show()
        self.before_rendererloop()
        while self._rendering:
            self.renderer()
            glfw.swap_buffers(self._window)
        self.after_rendererloop()

    # endregion

    # region MainLoop
    def before_mainloop(self):
        return

    def after_mainloop(self):
        return

    def mainloop(self):
        return

    def run(self):
        glfw.make_context_current(None)
        glfw.set_window_size_limits(
            self._window,
            self.properties.width,
            self.properties.height,
            glfw.DONT_CARE,
            glfw.DONT_CARE,
        )
        self.register_callbacks()
        self.before_mainloop()
        self._rendererThread = Thread(target=self.rendererloop, args=())
        self._rendererThread.start()
        try:
            while not glfw.window_should_close(self._window):
                self.mainloop()
                glfw.poll_events()
        except KeyboardInterrupt:
            pass
        finally:
            self._rendering = False
            self._rendererThread.join()
        print(f"{self._rendererThread.is_alive()=}")
        self.after_mainloop()
        glfw.terminate()

    # endregion
