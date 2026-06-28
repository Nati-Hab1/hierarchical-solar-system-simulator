import sys

from OpenGL.GLUT import *
from OpenGL.GL import glViewport

from config.constants import (
    WIN_W, WIN_H, WIN_TITLE,
    TIMER_MS,
)
from core.context import SimulationContext
from rendering.renderer import init_gl, render_frame

_SCROLL_UP = 3
_SCROLL_DOWN = 4


class SolarSystemApp:

    def __init__(self) -> None:
        self._context = SimulationContext()

    def run(self) -> None:
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(WIN_W, WIN_H)
        glutInitWindowPosition(100, 100)
        glutCreateWindow(WIN_TITLE)

        init_gl()

        glutDisplayFunc(self._display)
        glutReshapeFunc(self._reshape)
        glutKeyboardFunc(self._keyboard)
        glutMouseFunc(self._mouse_button)
        glutMotionFunc(self._mouse_motion)

        glutTimerFunc(TIMER_MS, self._timer, 0)

        self._print_controls()
        glutMainLoop()

    def _display(self) -> None:
        render_frame(self._context)

    def _reshape(self, width: int, height: int) -> None:
        glViewport(0, 0, width, max(height, 1))

    def _timer(self, value: int) -> None:
        self._context.tick()
        glutPostRedisplay()
        glutTimerFunc(TIMER_MS, self._timer, 0)

    def _keyboard(self, key: bytes, x: int, y: int) -> None:
        ch = key.decode("latin-1") if isinstance(key, bytes) else key

        if ch in ('+', '='):
            self._context.speed_up()
        elif ch == '-':
            self._context.slow_down()
        elif ch in ('r', 'R'):
            self._context.reverse_time()
        elif ch in ('p', 'P'):
            self._context.toggle_pause()
        elif ch in ('1', '2', '3', '4',
                    '5', '6', '7', '8'):
            self._context.select_planet(int(ch))
        elif ch == '0':
            self._context.reset_selected_scale()
        elif ch == '[':
            self._context.scale_down_selected()
        elif ch == ']':
            self._context.scale_up_selected()
        elif ch in ('\x1b', 'q', 'Q'):
            print("Goodbye!")
            sys.exit(0)

    def _mouse_button(self, button: int, state: int,
                      x: int, y: int) -> None:
        if button == GLUT_LEFT_BUTTON:
            if state == GLUT_DOWN:
                self._context.begin_drag(x, y)
            else:
                self._context.end_drag()

        if state == GLUT_DOWN:
            if button == _SCROLL_UP:
                self._context.zoom_in()
            elif button == _SCROLL_DOWN:
                self._context.zoom_out()

    def _mouse_motion(self, x: int, y: int) -> None:
        self._context.update_drag(x, y)

    @staticmethod
    def _print_controls() -> None:
        print("=== Hierarchical Solar System Simulator ===")
        print("Controls:")
        print("  +/=  Speed up  |  -  Slow down  |  r  Reverse  |  p  Pause")
        print("  1-8  Select planet  |  [ ] Scale  |  0  Reset scale")
        print("  Mouse: Left-drag rotate  |  Scroll: Zoom")
        print("  ESC or q: Quit\n")
