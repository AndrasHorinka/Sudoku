# main game methods
import file_manager
import ui


def start_module(game_map):
    """ Loads the selected map (default if none given)
    Arguments: 
        game_map: a list in list with the selected map
    Returns:
        None, it just prints the map """
    step_push = []
    while True:
        ui.print_table(game_map)

    # create a list of coordinates of the win condition zones
    
    pass


def define_coords_of_win_condition(game_map):
    win_zones = ""
    for pos, line in enumerate(game_map):
        for char, row in enumaret(line):    
            win_zones += char
    return win_zones

    """ Define the zones of win condition (winzones);
    Argument: 

    game_map: list in list of the original game map

    Returns: tuple/list of the coordinates of the winzones
     """
    

    


def define_current_position(game_map):
    
    """ Define the position of the Player in given map
    Arguments:
        table: list in list - current map
        
    Return: 
        coordinates of player as list [y, x] where y is the first list coordinate, x is the list in list coordinate  """
    
    pass
    # Geri 


def check_win_condition(game_map, win_zones):
    # 1. read the game_map
    # 2. crosscheck if coordinates of boxes in table == to win_zones coordinates
    #       if yes --> return win --
    # (3. sys.exit() --> step back 3 stacks)

    pass
    # Geri


def select_level():
    pass


def save_game():
    pass


def load_game():
    pass
