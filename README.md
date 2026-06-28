# Hierarchical Solar System Simulator

## Course
Computer Graphics (SITE CG) Capstone Project

## Group Members

| Name | ID |
|------|-----|
| Wengelle Yohannes | UGR/2568/16 |
| Hemen Mengistu | UGR/2373/16 |
| Ezana Mulatu | UGR/5768/16 |
| Samuel Abraham | UGR/0041/16 |
| Natnael Habteselassie | UGR/5666/16 |

## Project Description

A real-time pseudo-3D solar system simulator built using Python and PyOpenGL that demonstrates:

- Hierarchical transformations using matrix stacks (`glPushMatrix()` and `glPopMatrix()`)
- Time-based animation using delta time
- Affine transformations (translation, rotation, and scaling)
- Interactive camera controls
- Planet and moon orbital systems

## Features

- Sun and 8 planets rendered programmatically
- Hierarchical moon orbit system
- Planet self-rotation and orbital motion
- Saturn ring rendering
- Interactive zoom and camera rotation
- Time speed control
- Reverse simulation
- Pause/Resume
- Interactive planet scaling
- Window resizing with aspect ratio preservation
- On-screen simulation information (HUD)

## Controls

| Key | Action |
|-----|---------|
| `+` / `=` | Speed up simulation |
| `-` | Slow down simulation |
| `R` | Reverse time |
| `P` | Pause/Resume |
| `1-8` | Select planet |
| `[` | Scale down selected planet |
| `]` | Scale up selected planet |
| `0` | Reset selected planet scale |
| Left Mouse Drag | Rotate camera |
| Mouse Wheel | Zoom |
| `ESC` / `Q` | Quit |

## Technologies Used

- Python 3.x
- PyOpenGL
- GLUT (FreeGLUT)
- OpenGL Fixed-Function Pipeline

## Project Structure

```text
solar_system/
├── app/
│   └── solar_system_app.py
├── config/
│   └── constants.py
├── core/
│   └── context.py
├── domain/
│   └── planet.py
├── rendering/
│   └── renderer.py
├── main.py
└── README.md