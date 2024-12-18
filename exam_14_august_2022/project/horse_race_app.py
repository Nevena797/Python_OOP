from typing import List

from project.horse_race import HorseRace
from project.horse_specification.horse import Horse
from project.jockey import Jockey
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred


class HorseRaceApp:
    VALID_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.VALID_TYPES:
            return None
        if self.find_horse_name(horse_name, self.horses):
            raise Exception(f"Horse {horse_name} has been already added!")
        new_horse = self.VALID_TYPES[horse_type](horse_name, horse_speed)
        self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.find_jockey(jockey_name, self.jockeys):
            raise Exception(f"Jockey {jockey_name} has been already added!")
        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if race_type not in HorseRace.RACE_TYPES:
            raise Exception(f"Race {race_type} has been already created!")
        new_horse_race = HorseRace(race_type)
        self.horse_races.append(new_horse_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        current_jokey: Jockey = self.find_jockey(jockey_name, self.jockeys)
        current_horse: Horse = self.find_horse_rase(horse_type, self.horse_races)
        if not current_jokey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not current_horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if current_jokey.horse:
            return f"Jockey {jockey_name} already has a horse."
        current_jokey.horse = current_horse
        current_horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {current_horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        current_jokey: Jockey = self.find_jockey(jockey_name, self.jockeys)
        current_horse: Horse = self.find_horse_rase(horse_type, self.horse_races)
        if not current_horse:


    def start_horse_race(self, race_type: str):
        pass

    @staticmethod
    def find_horse_name(horse_name: str, horses: List):
        for horse in horses:
            if horse_name == horse.name:
                return horse

    @staticmethod
    def find_jockey(jockey_name: str, jockeys: List):
        for jockey in jockeys:
            if jockey_name == jockey.name:
                return jockey

    @staticmethod
    def find_horse_rase(horse_type, horse_races: List):
        for horse in horse_races:
            if horse_type == horse.race_type and not horse.is_taken:
                return horse
