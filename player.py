from constants import STATUS
import random

bubble_clean = 2
bubble_happyiness = 2

class Player:
    def __init__(self):
        self.adadachi = None
        self.inventory = {
            "games": ["hide-n-seek", "tag", "go fish", "red rover"],
            "foods": ["lemon cream pie", "sushi", "wonton", "crepes", "steak", "black cherry ice cream", "strawberries", "rice"],
        }
    def set_adadachi(self, adadachi): 
        self.adadachi = adadachi
    
    def get_adadachi_fav_food(self): 
        return self.inventory["foods"][self.adadachi.personality["fav_food"]]

    def get_happiness_level(self): 
        return self.adadachi.happiness

    def get_status(self): 
        print(STATUS)
        adadachi_name = self.adadachi.name
        hunger_level = self.adadachi.hunger
        poop_level = self.adadachi.poop_lvl
        clean_level = self.adadachi.clean_level
        hates_food = self.inventory["foods"][self.adadachi.personality["hates_food"]]
        fav_game = self.inventory["games"][self.adadachi.personality["fav_game"]]
        hates_game = self.inventory["games"][self.adadachi.personality["hates_game"]]
        
        print(
            f"""Hello! My name is {adadachi_name}. 
            My hunger level is {hunger_level}.
            My happiness level is {self.get_happiness_level()}.
            My fav food is {self.get_adadachi_fav_food()}.
            My least fav food is {hates_food}.
            My fav game is {fav_game}.
            My least fav game is {hates_game}.
            My poop level is {poop_level}.
            My clean level is {clean_level}."""
            )
            
    def clean(self): 
        self.adadachi.clean_level += bubble_clean
        self.adadachi.happiness += bubble_happyiness

        print("Your adadachi has been given a bubble bath!")
    
    def feed(self, food): 
        if food == self.get_adadachi_fav_food():
            self.adadachi.happiness += 2
        elif food == hates_food:
            self.adadachi.happiness -= 1 
        else: 
            self.adadachi.happiness +=1 
        
        hunger_level = 0
        print(f"Your adadachi has been fed {food} and it's happy level is {self.adadachi.happiness}.")

    def play_with_adadachi(self, adadachi):
        pass

