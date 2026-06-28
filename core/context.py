import time

from config.constants import (
    INIT_ROT_X, INIT_ROT_Y, INIT_ZOOM,
    ZOOM_MIN, ZOOM_MAX, ZOOM_STEP,
    MOUSE_SENSITIVITY, ROT_X_CLAMP,
    DT_CAP,
    INIT_TIME_SCALE, TIME_SCALE_STEP, TIME_SCALE_MAX, TIME_SCALE_MIN,
    PLANET_SCALE_MIN, PLANET_SCALE_MAX, PLANET_SCALE_DOWN, PLANET_SCALE_UP,
)
from domain.planet import PLANETS, Planet


class SimulationContext:
    def __init__(self) -> None:
        self.rot_x: float = INIT_ROT_X
        self.rot_y: float = INIT_ROT_Y
        self.zoom:  float = INIT_ZOOM

        self.mouse_down:   bool = False
        self.mouse_last_x: int = 0
        self.mouse_last_y: int = 0

        self.time_scale: float = INIT_TIME_SCALE
        self.paused:     bool = False
        self._last_time: float = time.time()

        self.selected_planet: int = 0

        self.planets: list[Planet] = PLANETS

    def tick(self) -> None:
        now = time.time()
        dt = now - self._last_time
        self._last_time = now

        dt = min(dt, DT_CAP)

        if self.paused:
            return

        scaled_dt = dt * self.time_scale

        for p in self.planets:
            p.orbit_angle = (p.orbit_angle + p.orbit_speed * scaled_dt) % 360.0

            p.axis_angle = (p.axis_angle + p.axis_speed * scaled_dt) % 360.0

            if p.has_moon:
                p.moon_orbit_angle = (
                    p.moon_orbit_angle + p.moon_orbit_speed * scaled_dt
                ) % 360.0

                p.moon_axis_angle = (
                    p.moon_axis_angle + p.moon_orbit_speed * 0.5 * scaled_dt
                ) % 360.0

    def speed_up(self) -> None:
        if self.time_scale > 0:
            self.time_scale = min(
                self.time_scale * TIME_SCALE_STEP, TIME_SCALE_MAX)
        else:
            self.time_scale = max(
                self.time_scale * TIME_SCALE_STEP, -TIME_SCALE_MAX)
        print(f"Time scale: {self.time_scale:.2f}")

    def slow_down(self) -> None:
        if self.time_scale > 0:
            self.time_scale = max(
                self.time_scale / TIME_SCALE_STEP, TIME_SCALE_MIN)
        else:
            self.time_scale = min(
                self.time_scale / TIME_SCALE_STEP, -TIME_SCALE_MIN)
        print(f"Time scale: {self.time_scale:.2f}")

    def reverse_time(self) -> None:
        self.time_scale = -self.time_scale
        print(f"Reversed. Time scale: {self.time_scale:.2f}")

    def toggle_pause(self) -> None:
        self.paused = not self.paused
        print("Simulation", "PAUSED" if self.paused else "RESUMED")

    def select_planet(self, number: int) -> None:
        self.selected_planet = number
        print(f"Selected: {self.planets[number - 1].name}")

    def scale_down_selected(self) -> None:
        if self.selected_planet == 0:
            return
        p = self.planets[self.selected_planet - 1]
        if p.user_scale > PLANET_SCALE_MIN:
            p.user_scale *= PLANET_SCALE_DOWN
        print(f"{p.name} scale: {p.user_scale:.2f}")

    def scale_up_selected(self) -> None:
        if self.selected_planet == 0:
            return
        p = self.planets[self.selected_planet - 1]
        if p.user_scale < PLANET_SCALE_MAX:
            p.user_scale *= PLANET_SCALE_UP
        print(f"{p.name} scale: {p.user_scale:.2f}")

    def reset_selected_scale(self) -> None:
        if self.selected_planet == 0:
            return
        p = self.planets[self.selected_planet - 1]
        p.user_scale = 1.0
        print(f"Reset scale for {p.name}")

    # Zoom
    def zoom_in(self) -> None:
        self.zoom = min(self.zoom * ZOOM_STEP, ZOOM_MAX)

    def zoom_out(self) -> None:
        self.zoom = max(self.zoom / ZOOM_STEP, ZOOM_MIN)

    # Mouse drag
    def begin_drag(self, x: int, y: int) -> None:
        self.mouse_down = True
        self.mouse_last_x = x
        self.mouse_last_y = y

    def end_drag(self) -> None:
        self.mouse_down = False

    def update_drag(self, x: int, y: int) -> None:
        if not self.mouse_down:
            return

        dx = x - self.mouse_last_x
        dy = y - self.mouse_last_y

        self.rot_y += dx * MOUSE_SENSITIVITY
        self.rot_x += dy * MOUSE_SENSITIVITY
        self.rot_x = max(-ROT_X_CLAMP, min(ROT_X_CLAMP, self.rot_x))

        self.mouse_last_x = x
        self.mouse_last_y = y

    @property
    def selected_planet_name(self) -> str:
        if self.selected_planet == 0:
            return "none"
        return self.planets[self.selected_planet - 1].name

    @property
    def selected_planet_scale(self) -> float:
        if self.selected_planet == 0:
            return 1.0
        return self.planets[self.selected_planet - 1].user_scale
