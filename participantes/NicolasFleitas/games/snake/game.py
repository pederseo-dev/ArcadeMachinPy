import time
from core import display

# Contrato obligatorio para que el loader lo detecte
TITLE = "🐍 Snake Minimalista"

def run():
    """Lógica principal del juego."""
    display.clear_screen()
    display.print_centered(f"Iniciando: {TITLE}", "GREEN")
    display.print_centered("(Simulación de juego...)", "YELLOW")
    
    # Aquí iría la lógica real del juego (bucle while, input, etc.)
    # Ejemplo creativo simple:
    for i in range(3, 0, -1):
        display.clear_screen()
        display.print_centered(f"Comenzando en {i}...", "RED")
        time.sleep(1)
        
    display.clear_screen()
    display.print_centered("¡Juego terminado! Puntuación: 9999", "CYAN")