from app.solar_system_app import SolarSystemApp
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

def main() -> None:
    app = SolarSystemApp()
    app.run()

if __name__ == "__main__":
    main()
