import math

PI:     float = math.pi
TWO_PI: float = 2.0 * math.pi

WIN_W:     int = 1100
WIN_H:     int = 700
WIN_TITLE: bytes = b"Hierarchical Solar System Simulator"

# Sphere resolution
SPHERE_SLICES: int = 36
SPHERE_STACKS: int = 18

# Orbit ring resolution
ORBIT_SEGMENTS: int = 120

# Orthographic projection
ORTHO_BASE_HALF: float = 28.0

# Depth range
ORTHO_NEAR: float = -60.0
ORTHO_FAR:  float = 60.0

# Initial view
INIT_ROT_X: float = 20.0
INIT_ROT_Y: float = 0.0
INIT_ZOOM:  float = 1.0

# Zoom limits
ZOOM_MIN:  float = 0.15
ZOOM_MAX:  float = 8.0
ZOOM_STEP: float = 1.05

# Mouse controls
MOUSE_SENSITIVITY: float = 0.4
ROT_X_CLAMP:       float = 89.0

# Simulation timing
TIMER_MS:        int = 16
DT_CAP:          float = 0.1
INIT_TIME_SCALE: float = 1.0
TIME_SCALE_STEP: float = 1.5
TIME_SCALE_MAX:  float = 64.0
TIME_SCALE_MIN:  float = 0.1

# OpenGL state
BG_COLOR: tuple = (0.02, 0.02, 0.08, 1.0)

# Sun
SUN_RADIUS:     float = 1.8
SUN_COLOR:      tuple = (1.0, 0.95, 0.20)
SUN_GLOW_COLOR: tuple = (1.0, 0.70, 0.10)
SUN_GLOW_INNER: float = 1.85
SUN_GLOW_OUTER: float = 2.5
SUN_GLOW_SEGS:  int = 80

# Orbit ring
ORBIT_RING_COLOR: tuple = (0.22, 0.22, 0.30)

# Saturn ring
SATURN_INDEX:             int = 5
SATURN_RING_COLOR:        tuple = (0.88, 0.82, 0.65, 0.6)
SATURN_RING_TILT:         float = 27.0
SATURN_RING_INNER_FACTOR: float = 1.25
SATURN_RING_OUTER_FACTOR: float = 2.10
SATURN_RING_SEGMENTS:     int = 80

# Planet scale limits
PLANET_SCALE_MIN:  float = 0.2
PLANET_SCALE_MAX:  float = 5.0
PLANET_SCALE_DOWN: float = 0.85
PLANET_SCALE_UP:   float = 1.15
