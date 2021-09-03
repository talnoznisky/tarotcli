import itertools
import sys
import time

from data.spreads import spreads
from classes import Spread

from simple_term_menu import TerminalMenu


BEGIN_TEXT =    'BEGIN DIVINATION...'
END_TEXT =      '...END DIVINATION.'


def _handle_dashes(spread: str):
    options = ["-"," "]
    add = options["-" in spread]
    remove = options["-" not in spread]
 
    return spread.replace(remove, add)


def spinner():
    spinner = itertools.cycle(['|','/','-','\\'])
    
    for _ in range(30):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')


def get_spread():
    spread_names = [_handle_dashes(spread) for spread in spreads]

    terminal_menu = TerminalMenu(spread_names)
    menu_entry_index = terminal_menu.show()
    selection = spread_names[menu_entry_index]

    spread_dict_key = _handle_dashes(selection)
    spread = Spread(spread_dict_key).spread

    return selection, spread    


def output(selection, spread):
    sys.stdout.write('\n')
    sys.stdout.write(f'YOU HAVE SELECTED: {selection}\n')
    time.sleep(0.3)
    sys.stdout.write(f'🔮✨OK, HOLD UP, DOING TAROT✨🔮 ')
    spinner()
    sys.stdout.write('\n')

    sys.stdout.write('\n')
    sys.stdout.write(BEGIN_TEXT+'\n')
    sys.stdout.write('\n')

    for card in spread:
        sys.stdout.write(f'{card["position"].upper()}: {card["name"] +" (REVERSED)" if card["reversed"] else card["name"]}'+'\n')
        sys.stdout.write(card["description"]+'\n')     
        sys.stdout.write('\n')
    
    sys.stdout.write(END_TEXT)
    sys.stdout.write('\n\n')

if __name__ == "__main__":
    selection, spread = get_spread()
    output(selection, spread)
