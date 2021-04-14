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

    def get_adadachi_fav_game(self): 
        return self.inventory["games"][self.adadachi.personality["fav_game"]]
    
    def get_adadachi_hates_food(self): 
        return self.inventory["foods"][self.adadachi.personality["hates_food"]]
    
    def get_adadachi_hates_game(self): 
        return self.inventory["games"][self.adadachi.personality["hates_game"]]

    def get_happiness_level(self): 
        return self.adadachi.happiness

    def get_status(self): 
        print(STATUS)
            
        print(
            f"""Hello! My name is {self.adadachi.name}. 
            My hunger level is {self.adadachi.hunger}.
            My happiness level is {self.get_happiness_level()}.
            My fav food is {self.get_adadachi_fav_food()}.
            My least fav food is {self.get_adadachi_hates_food()}.
            My fav game is {self.get_adadachi_fav_game()}.
            My least fav game is {self.get_adadachi_hates_game()}.
            My poop level is {self.adadachi.poop_lvl}.
            My clean level is {self.adadachi.clean_level}."""
            )
            
    def clean(self): 
        self.adadachi.clean_level += bubble_clean
        self.adadachi.happiness += bubble_happyiness

        print(f"Your adadachi has been given a bubble bath! Its happy level is {self.adadachi.happiness} and its clean level is {self.adadachi.clean_level}.")
    
    def feed(self, food): 
        if food == self.get_adadachi_fav_food():
            self.adadachi.happiness += 2
        elif food == self.get_adadachi_hates_food():
            self.adadachi.happiness += 0 
        else: 
            self.adadachi.happiness +=1 
        
        self.adadachi.hunger = 0
        print(f"Your adadachi has been fed {food}. Its happy level is {self.adadachi.happiness} and its hunger level is {self.adadachi.hunger}.")

    def play_with_adadachi(self, adadachi):
        pass

