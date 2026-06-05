import os
import importlib

def discover_games():
    """Escanea la carpeta 'games' y retorna una lista de módulos de juego."""
    games_list = []
    games_dir = os.path.join(os.path.dirname(__file__), '..', 'games')
    
    for item in os.listdir(games_dir):
        item_path = os.path.join(games_dir, item)
        # Ignorar archivos __init__.py o carpetas no válidas
        if os.path.isdir(item_path) and not item.startswith('__'):
            game_file = os.path.join(item_path, 'game.py')
            if os.path.exists(game_file):
                # Importación dinámica: games.snake.game
                module_name = f"games.{item}.game"
                try:
                    module = importlib.import_module(module_name)
                    if hasattr(module, 'TITLE') and hasattr(module, 'run'):
                        games_list.append(module)
                except Exception as e:
                    print(f"Error cargando {item}: {e}")
                    
    return games_list