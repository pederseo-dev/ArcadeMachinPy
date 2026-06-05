arcade_machine/
│
├── main.py                      # Punto de entrada, inicializa pygame y el menú
├── requirements.txt             # Dependencias (pygame, etc.)
├── README.md                    # Documentación del proyecto
│
├── games/                       # Un paquete por juego
│   ├── snake/
│   │   ├── __init__.py
│   │   ├── game.py              # Lógica principal de Snake
│   │   ├── sprites.py           # Sprites: serpiente, comida
│   │   └── levels.py            # Configuración de niveles
│   │
│   └── space_invaders/
│       ├── __init__.py
│       ├── game.py              # Lógica principal de Space Invaders
│       ├── enemies.py           # Comportamiento de enemigos
│       └── bullets.py           # Manejo de disparos
│
├── core/                        # Lógica central compartida
│   ├── __init__.py
│   ├── game_loop.py             # Loop principal del juego
│   ├── input_handler.py         # Input de teclado / joystick
│   └── score.py                 # Sistema de puntaje y high scores
│
├── assets/                      # Recursos estáticos
│   ├── images/                  # Sprites e imágenes
│   ├── sounds/                  # Efectos de sonido y música
│   └── fonts/                   # Fuentes tipográficas
│
├── data/                        # Persistencia de datos
│   ├── high_scores.json         # Tabla de puntajes máximos
│   └── settings.json            # Configuración (volumen, controles, etc.)
│
└── ui/                          # Interfaz y pantallas del sistema
    ├── __init__.py
    ├── main_menu.py             # Menú de selección de juegos
    ├── hud.py                   # HUD: puntaje, vidas, tiempo
    └── game_over.py             # Pantalla de game over / pausa