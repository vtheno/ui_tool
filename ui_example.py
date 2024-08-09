import glfw
from OpenGL.GL import *

from ui_window import Event, EventKind, Window
from ui_enum import PRESS, KEY_ENTER, KEY_ESCAPE, KEY_F11


class ExampleWindow(Window):
    def __init__(
        self, title: str, width: int, height: int, major: int = 4, minor: int = 5
    ) -> None:
        super().__init__(title, width, height, major, minor)

    def before_rendererloop(self):
        return

    def renderer(self):
        glViewport(0, 0, self.properties.width, self.properties.height)
        glClearColor(0.2, 0.3, 0.3, 0.3)
        glClear(GL_COLOR_BUFFER_BIT)

        return

    def dispatch(self, ev: Event):
        super().dispatch(ev)
        if (
            ev.kind == EventKind.KeyButton
            and ev.button == KEY_ENTER
            and ev.action == PRESS
        ):
            self.set_typing(not self._typing)
        elif (
            ev.kind == EventKind.KeyButton
            and ev.button == KEY_F11
            and ev.action == PRESS
        ):
            self.layered()
            self.fullscreen()
        elif (
            ev.kind == EventKind.KeyButton
            and ev.button == KEY_ESCAPE
            and ev.action == PRESS
        ):
            self.close()

    def before_mainloop(self):
        self.iconify()
        self.restore()
        return


def main():
    window = ExampleWindow("Title", 800, 600)

    window.run()


if __name__ == "__main__":
    main()
