from constants import STATUS
import random
import copy 

bubble_clean = 2
bubble_happyiness = 2

places = ["by the fire", "under the table", "behind the car", 
        "behind a tree",  "behind the tent", "on the street", "inside a cave"]

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

    def play_hide_and_seek(self):
        adadachi_places = copy.copy(places)
        player_starting_place = random.choice(places) 
        adadachi_places.remove(player_starting_place)
        adadachi_hiding_place = random.choice(adadachi_places)
        print(player_starting_place)
        print(adadachi_hiding_place)
        
        guesses = 0 
        guessed_places =[]

        while guesses < len(places):
            this_round_of_guess = input("Guess a hiding spot: ")
            if this_round_of_guess != adadachi_hiding_place: 
                guesses += 1 
                guessed_places.append(this_round_of_guess)
                print(f"Your adadachi is not here, please try again! you have guessed {guessed_places}")
                if guesses > len(places)// 2:
                    adadachi_hiding_place = random.choice(places)
                    if adadachi_hiding_place == player_starting_place: 
                        print(f"Your adadachi has returned to the homebase {player_starting_place}. You have lost!")
                        print("Your adadachi is super happy that they returned back to your starting place without being found!")
                        self.adadachi.happiness += 5
                        break
                    else: 
                        print("keep searching for your adadachi! Your adadachi has changed their spot!")
                        print(adadachi_hiding_place)
            else: 
                answer = input("You found your adadachi! Would you like to play again, yes or no?")
                if answer == "yes": 
                    print("Let's play again!")
                elif answer == "no": 
                    print("Your adadachi wish they weren't found. but they are happy that they got to play!")
                    self.adadachi.happiness += 2
                    break
        else: 
            print(f"You didn't find your adadachi after {len(places)} tries! Your adadachi is {adadachi_hiding_place}!")
            print("Your adadachi is happy that they were never found!")
            self.adadachi.happiness += 3

        self.adadachi.hunger += 1
