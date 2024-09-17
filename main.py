from Pokemon import Pokemon

from termcolor import colored
from simple_term_menu import TerminalMenu

class PokemonApp:
    def __init__(self) -> None:
        # https://pokemondb.net/pokedex/all
        self._pokemon_list = [
            ["Pikachu", 35, 55], 
            ["Bulbasaur", 45, 49],
            ["Ivysaur", 60, 62],
            ["Venusaur", 80, 100],
            ["Charmander", 39, 52],
        ]

        self._pokemons = []
        self._player = None
        self._opponent = None

        self.create_pokemons()
    
    def create_pokemons(self):
        for i, pokemon in enumerate(self._pokemon_list):
            self.add_pokemon(pokemon[0], pokemon[1], pokemon[2])
    
    def list_pokemons(self, has_output:bool = False, skip:int = -1):
        pokemons = []
        for i, pokemon in enumerate(self._pokemons):
            if (i != skip):
                pokemons.append(pokemon)
                if (has_output == True):
                    print(pokemon)
        return pokemons

    def add_pokemon(self, name, health, attack):
        self._pokemons.append(Pokemon(name, health, attack))

    def get_pokemon_by_id(self, pokemon_id) -> Pokemon:
        return self._pokemons[pokemon_id]

    def choose_pokemon(self, pokemon, is_opponent=False):
        if (is_opponent):
            self._opponent = pokemon
        else:
            self._player = pokemon

    def fight(self, attacker:Pokemon, receiver:Pokemon, is_receiving:bool =True) -> None:
        receiver.decrease_health(attacker.get_attack())
        direction = colored(f">", "green", attrs=["bold"])

        if (is_receiving == False):
            direction = colored(f"<", "red", attrs=["bold"])
    
        attacker_name = attacker.get_name() if is_receiving == True else receiver.get_name()
        receiver_name = receiver.get_name() if is_receiving == True else attacker.get_name()

        obituary = ""
        if (receiver.get_health() < 0):
            obituary = f"; {receiver.get_name()} died honorably."
        print(f"{attacker_name} {direction} {receiver_name}; {receiver.get_name()} down to {receiver.get_health()}{obituary}")
    
    def init_attack_sequence(self):
        # Choose opponent

        # Get Player & Opponent Pokémons
        player = self.get_pokemon_by_id(self._player)
        opponent = self.get_pokemon_by_id(self._opponent)

        # Initiate turns
        turn = 1

        print(player)
        print("-- fights against --")
        print(opponent)
        while (player.get_health() > 0 and opponent.get_health() > 0):
            turn_title = colored(f"Turn {turn}", "white", attrs=["bold"])
            print(f"\n{turn_title}")
            self.fight(player, opponent)
            self.fight(opponent, player, False)
            turn = turn + 1

            
def main():
    pokemonApp = PokemonApp()

    main_menu_title = "Pokémon Main Menu • Press Q or Esc to quit \n"
    main_menu_options = ["List Pokémons", "Add Pokémon", "Choose Pokémon", "Initiate Fighting Sequence", "", "Exit"]
    terminal_menu = TerminalMenu(main_menu_options, title=main_menu_title, skip_empty_entries=True, clear_screen=True)
    menu_entry_index = terminal_menu.show();
    print(f"You have selected {main_menu_options[menu_entry_index]}\n")

    # pokemonApp.list_pokemons(True)

    pokemonApp.choose_pokemon(0, False)
    pokemonApp.choose_pokemon(3, True)
    pokemonApp.init_attack_sequence()

if __name__ == "__main__":
    main()