import sys
import os

# Asegurar que la carpeta raíz esté en el path para importar 'core' y 'games'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.menu import main_menu

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nSaliendo de la Arcade...")
        sys.exit(0)