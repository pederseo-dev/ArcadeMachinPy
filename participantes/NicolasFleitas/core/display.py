import os
import time

# Códigos de color ANSI
COLORS = {
    "RESET": "\033[0m",
    "RED": "\033[91m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "BLUE": "\033[94m",
    "CYAN": "\033[96m",
    "BOLD": "\033[1m"
}

def clear_screen():
    """Limpia la terminal de forma multiplataforma."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_centered(text, color="RESET"):
    """Imprime texto centrado con color opcional."""
    cols = os.get_terminal_size().columns
    # Quitamos los códigos de color para calcular el ancho real
    clean_text = text
    for code in COLORS.values():
        clean_text = clean_text.replace(code, "")
    
    padding = (cols - len(clean_text)) // 2
    print(f"{' ' * padding}{COLORS[color]}{text}{COLORS['RESET']}")

def press_enter_to_continue():
    """Pausa creativa con parpadeo simulado."""
    print_centered("\n[Pulsa ENTER para continuar]", "YELLOW")
    input()