from termcolor import colored, cprint
from random import randint, choice

class Pokemon:
    def __init__(self, name: str, health = randint(100, 150), attack = randint(10, 20)) -> None:
        self.name = name

        if isinstance(health, int):
            self.health = health
        else:
            self.health = randint(100, 150)

        if isinstance(attack, int):
            self.attack = attack
        else:
            self.attack = randint(10, 20)

    def __str__(self) -> str:
        pokemon_name = colored(f"{self.name}", "white", attrs=["bold"])
        pokemon_health = colored(f"{self.health}", "yellow", attrs=["bold", "dark"])
        pokemon_attack = colored(f"{self.attack}", "red", attrs=["bold", "dark"])

        return f"{pokemon_name} (HP: {pokemon_health}, ATK: {pokemon_attack})"
    
    def get_health(self) -> int:
        return self.health
    
    def get_attack(self) -> int:
        return self.attack
    
    def decrease_health(self, attack: int) -> None:
        self.health = self.health - attack

    # def attack(self, opponent: Pokemon) -> None:
    #     opponent.decrease_health(self.attack)

    



    