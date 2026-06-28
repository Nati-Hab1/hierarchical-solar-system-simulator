import math

from OpenGL.GL import *
from OpenGL.GLUT import *

from config.constants import (
    PI, TWO_PI,
    SPHERE_SLICES, SPHERE_STACKS,
    ORBIT_SEGMENTS,
    ORTHO_BASE_HALF, ORTHO_NEAR, ORTHO_FAR,
    BG_COLOR,
    SUN_RADIUS, SUN_COLOR, SUN_GLOW_COLOR,
    SUN_GLOW_INNER, SUN_GLOW_OUTER, SUN_GLOW_SEGS,
    ORBIT_RING_COLOR,
    SATURN_INDEX,
    SATURN_RING_COLOR, SATURN_RING_TILT,
    SATURN_RING_INNER_FACTOR, SATURN_RING_OUTER_FACTOR, SATURN_RING_SEGMENTS,
)


def init_gl() -> None:
    glClearColor(*BG_COLOR)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)     
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)


def draw_sphere(radius: float,
                slices: int = SPHERE_SLICES,
                stacks: int = SPHERE_STACKS) -> None:
    for i in range(stacks):
        lat0 = PI * (-0.5 + i / stacks)
        lat1 = PI * (-0.5 + (i + 1) / stacks)
        sin0, cos0 = math.sin(lat0), math.cos(lat0)
        sin1, cos1 = math.sin(lat1), math.cos(lat1)

        glBegin(GL_QUAD_STRIP)
        for j in range(slices + 1):
            lng = TWO_PI * j / slices
            sl, cl = math.sin(lng), math.cos(lng)

            x0, y0, z0 = cos0 * cl, sin0, cos0 * sl
            glNormal3f(x0, y0, z0)
            glVertex3f(x0 * radius, y0 * radius, z0 * radius)

            x1, y1, z1 = cos1 * cl, sin1, cos1 * sl
            glNormal3f(x1, y1, z1)
            glVertex3f(x1 * radius, y1 * radius, z1 * radius)
        glEnd()


def draw_orbit_ring(radius: float,
                    segments: int = ORBIT_SEGMENTS) -> None:
    glBegin(GL_LINE_LOOP)
    for i in range(segments):
        angle = TWO_PI * i / segments
        glVertex3f(math.cos(angle) * radius, 0.0, math.sin(angle) * radius)
    glEnd()


def draw_ring_disk(inner_r: float, outer_r: float,
                   segments: int = 80) -> None:
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(segments + 1):
        angle = TWO_PI * i / segments
        ca, sa = math.cos(angle), math.sin(angle)
        glVertex3f(ca * outer_r, 0.0, sa * outer_r)
        glVertex3f(ca * inner_r, 0.0, sa * inner_r)
    glEnd()


def draw_text_2d(x: float, y: float, text: str) -> None:
    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(GLUT_BITMAP_8_BY_13, ord(ch))


def draw_planet(p, is_saturn: bool = False) -> None:
    glPushMatrix()

    glRotatef(p.orbit_tilt, 0.0, 0.0, 1.0)

    glRotatef(p.orbit_angle, 0.0, 1.0, 0.0)

    glTranslatef(p.orbit_radius, 0.0, 0.0)

    if p.has_moon:
        glPushMatrix()

        glRotatef(p.moon_orbit_angle, 0.0, 1.0, 0.0)
        glTranslatef(p.moon_orbit_radius, 0.0, 0.0)

        glRotatef(p.moon_axis_angle, 0.0, 1.0, 0.0) 
        glColor3f(*p.moon_color)
        draw_sphere(p.moon_radius, 20, 10)

        glPopMatrix()

    glRotatef(p.axis_angle, 0.0, 1.0, 0.0)

    glScalef(p.user_scale, p.user_scale, p.user_scale)

    glColor3f(*p.color)
    draw_sphere(p.radius)

    if is_saturn:
        glColor4f(*SATURN_RING_COLOR)

        glRotatef(-p.axis_angle, 0.0, 1.0, 0.0)
        glRotatef(SATURN_RING_TILT, 1.0, 0.0, 0.0)

        draw_ring_disk(
            p.radius * SATURN_RING_INNER_FACTOR,
            p.radius * SATURN_RING_OUTER_FACTOR,
            SATURN_RING_SEGMENTS,
        )

    glPopMatrix()


def render_frame(context) -> None:
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    win_w = glutGet(GLUT_WINDOW_WIDTH)
    win_h = glutGet(GLUT_WINDOW_HEIGHT) or 1   

    aspect = win_w / win_h
    half = ORTHO_BASE_HALF / context.zoom

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(
        -half * aspect,
        +half * aspect,
        -half,
        +half,
        ORTHO_NEAR,
        ORTHO_FAR,
    )

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glRotatef(context.rot_x, 1.0, 0.0, 0.0)
    glRotatef(context.rot_y, 0.0, 1.0, 0.0)

    glColor3f(*ORBIT_RING_COLOR)
    for p in context.planets:
        glPushMatrix()
        glRotatef(p.orbit_tilt, 0.0, 0.0, 1.0)
        draw_orbit_ring(p.orbit_radius)
        glPopMatrix()

    glColor3f(*SUN_COLOR)
    draw_sphere(SUN_RADIUS)

    glColor3f(*SUN_GLOW_COLOR)
    glPushMatrix()
    glRotatef(90.0, 1.0, 0.0, 0.0) 
    draw_ring_disk(SUN_GLOW_INNER, SUN_GLOW_OUTER, SUN_GLOW_SEGS)
    glPopMatrix()

    for idx, p in enumerate(context.planets):
        draw_planet(p, is_saturn=(idx == SATURN_INDEX))

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, win_w, 0, win_h, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glDisable(GL_DEPTH_TEST)

    hx = 10.0
    hy = float(win_h - 20)
    step = 15.0

    glColor3f(1.0, 1.0, 1.0)
    draw_text_2d(hx, hy, "HIERARCHICAL SOLAR SYSTEM SIMULATOR")
    hy -= step

    glColor3f(0.80, 0.80, 0.80)
    paused_tag = "  [PAUSED]" if context.paused else ""

    draw_text_2d(
        hx,
        hy,
        f"Time scale : {abs(context.time_scale):.2f}x{paused_tag}"
    )
    hy -= step

    direction = "Reverse" if context.time_scale < 0 else "Forward"
    draw_text_2d(hx, hy, f"Direction  : {direction}")
    hy -= step

    if context.selected_planet > 0:
        draw_text_2d(
            hx,
            hy,
            f"Selected   : {context.selected_planet_name}"
            f"  (scale {context.selected_planet_scale:.2f})"
        )
    else:
        draw_text_2d(hx, hy, "Selected   : none")
    hy -= step

    draw_text_2d(
        hx,
        hy,
        f"Ortho zoom : {context.zoom:.2f}x  "
        f"(half-extent {ORTHO_BASE_HALF / context.zoom:.1f} wu)"
    )
    hy -= step

    hy -= 5
    glColor3f(0.60, 0.90, 0.60)
    draw_text_2d(hx, hy, "Controls:")
    hy -= step

    glColor3f(0.70, 0.70, 0.70)
    for line in [
        " +/=  Speed up     -  Slow down",
        " r    Reverse      p  Pause/Resume",
        " 1-8  Select planet   [ ] Scale",
        " 0    Reset scale    ESC  Quit",
        " Mouse: Left-drag to rotate, scroll to zoom",
    ]:
        draw_text_2d(hx, hy, line)
        hy -= step

    glEnable(GL_DEPTH_TEST)

    glutSwapBuffers()
