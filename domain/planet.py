from dataclasses import dataclass, field


@dataclass
class Planet:

    name: str
    color:      tuple
    radius:     float
    user_scale: float = 1.0
    orbit_radius: float = 0.0
    orbit_speed:  float = 0.0
    orbit_angle:  float = 0.0
    axis_speed:  float = 0.0
    axis_angle:  float = 0.0
    orbit_tilt:  float = 0.0
    has_moon:          bool = False
    moon_color:        tuple = field(default_factory=lambda: (0.8, 0.8, 0.8))
    moon_radius:       float = 0.0
    moon_orbit_radius: float = 0.0
    moon_orbit_speed:  float = 0.0
    moon_orbit_angle:  float = 0.0
    moon_axis_angle:   float = 0.0

PLANETS: list[Planet] = [

    # 0 Mercury
    Planet(
        name="Mercury",
        color=(0.72, 0.70, 0.67), radius=0.35,
        orbit_radius=2.8,  orbit_speed=87.97, orbit_tilt=7.0,
        axis_speed=0.30,
    ),

    # 1 Venus
    Planet(
        name="Venus",
        color=(0.93, 0.83, 0.50), radius=0.60,
        orbit_radius=4.2,  orbit_speed=36.00, orbit_tilt=3.4,
        axis_speed=0.05,
    ),

    # 2 Earth (Moon)
    Planet(
        name="Earth",
        color=(0.25, 0.55, 0.85), radius=0.65,
        orbit_radius=5.8,  orbit_speed=22.50, orbit_tilt=0.0,
        axis_speed=1.50,
        has_moon=True,
        moon_color=(0.80, 0.80, 0.80), moon_radius=0.18,
        moon_orbit_radius=1.10, moon_orbit_speed=120.0,
    ),

    # 3 Mars
    Planet(
        name="Mars",
        color=(0.85, 0.35, 0.20), radius=0.45,
        orbit_radius=7.5,  orbit_speed=12.00, orbit_tilt=1.9,
        axis_speed=1.45,
    ),

    # 4 Jupiter (Moon)
    Planet(
        name="Jupiter",
        color=(0.88, 0.72, 0.55), radius=1.10,
        orbit_radius=10.5, orbit_speed=3.80,  orbit_tilt=1.3,
        axis_speed=5.50,
        has_moon=True,
        moon_color=(0.70, 0.65, 0.55), moon_radius=0.22,
        moon_orbit_radius=1.60, moon_orbit_speed=60.0,
    ),

    # 5 Saturn
    Planet(
        name="Saturn",
        color=(0.92, 0.85, 0.60), radius=0.90,
        orbit_radius=14.0, orbit_speed=1.90,  orbit_tilt=2.5,
        axis_speed=3.80,
    ),

    # 6 Uranus
    Planet(
        name="Uranus",
        color=(0.55, 0.82, 0.90), radius=0.70,
        orbit_radius=17.5, orbit_speed=0.96,  orbit_tilt=82.0,
        axis_speed=2.40,
    ),

    # 7 Neptune
    Planet(
        name="Neptune",
        color=(0.25, 0.40, 0.85), radius=0.65,
        orbit_radius=21.0, orbit_speed=0.48,  orbit_tilt=1.8,
        axis_speed=2.60,
    ),
]
