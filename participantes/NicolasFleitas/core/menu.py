from . import display
from . import loader

def show_banner():
    """Muestra un banner ASCII simple."""
    display.clear_screen()
    banner = [
        " █████╗ ██████╗  ██████╗██╗  ██╗███████╗██████╗ ",
        "██╔══██╗██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗",
        "███████║██████╔╝██║     ███████║█████╗  ██████╔╝",
        "██╔══██║██╔══██╗██║     ██╔══██║██╔══╝  ██╔══██╗",
        "██║  ██║██║  ██║╚██████╗██║  ██║███████╗██║  ██║",
        "╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝"
    ]
    for line in banner:
        display.print_centered(line, "CYAN")
    display.print_centered("--- MÁQUINA ARCADE PYTHON ---\n", "BOLD")

def main_menu():
    """Bucle principal del menú."""
    games = loader.discover_games()
    
    while True:
        show_banner()
        display.print_centered("SELECCIONA UN JUEGO:", "GREEN")
        print()
        
        # Mostrar opciones
        for i, game in enumerate(games, 1):
            display.print_centered(f"{i}. {game.TITLE}", "BLUE")
            
        display.print_centered(f"{len(games) + 1}. SALIR", "RED")
        print()
        
        choice = input("  > Tu elección: ").strip()
        
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(games):
                selected_game = games[choice - 1]
                _run_game(selected_game)
            elif choice == len(games) + 1:
                display.clear_screen()
                display.print_centered("¡Gracias por jugar! Hasta pronto.", "GREEN")
                break
            else:
                display.print_centered("Opción no válida.", "RED")
                display.press_enter_to_continue()
        else:
            display.press_enter_to_continue()

def _run_game(game_module):
    """Ejecuta un juego y maneja el retorno al menú."""
    try:
        display.clear_screen()
        game_module.run()
    except KeyboardInterrupt:
        pass # Permitir salir con Ctrl+C de forma limpia
    finally:
        display.press_enter_to_continue()