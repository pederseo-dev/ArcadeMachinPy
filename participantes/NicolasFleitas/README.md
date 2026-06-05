arcade_machine/
│
├── main.py                  # Punto de entrada único
│
├── core/                    # El motor de la máquina arcade
│   ├── __init__.py
│   ├── display.py           # Utilidades visuales (colores, limpiar pantalla)
│   ├── loader.py            # Descubre y carga los juegos dinámente
│   └── menu.py              # Bucle principal del menú de selección
│
├── games/                   # Carpeta de juegos 
│   ├── __init__.py
│   ├── snake/               # Ejemplo de juego 1
│   │   ├── __init__.py
│   │   └── game.py          # Debe contener TITLE y run()
│   └── adivina/             # Ejemplo de juego 2
│       ├── __init__.py
│       └── game.py          # Debe contener TITLE y run()
│
└── assets/                  # Recursos estáticos
    └── banner.txt           # Arte ASCII para el título principal