# Coding sprint

# TODO: Refactor this into a Player class

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []       # inventory
        self.health = 100         # health
        self.score = 0            # points

    def status(self):
        print(f"{self.name}'s Status")
        print(f"Health: {self.health}")
        print(f"Score: {self.score}")
        print(f"Inventory: {self.inventory if self.inventory else 'Empty'}")
        print("--------------------------")



# TODO: Add an inventory system
# Example: player_inventory = []

# TODO: Add a health/points system to track player progress
# Example: player_health = 100, player_score = 0

player = Player(input("Enter your name: "))
player.status()
player_health =100
player_score = 0
    
def explore():
    print("You walk into a dark forest.")
    print("A wild creature appears!")
    action = input("Do you [fight] or [run]? ")
    if action.lower() == "fight":
        print("You bravely fight and win!")
        # TODO: Award points or add loot to inventory
     
        player.inventory.append("Loot")
    
        print("You gain 10 points and some loot, but lose 10 health.")
        # TODO: Decrease health if the player takes damage
    elif action.lower() == "run":
        print("You escape safely, but miss out on treasure. no score gained")
      

        # TODO: Maybe reduce score for running away
    else:
        print("You hesitate and the creature vanishes.")
        # TODO: Add more consequences for indecision
        player.health -= 5 
print("Type 'explore', 'cave', 'village', 'castle', 'random', or 'quit'.")


# TODO: Add more locations (e.g., cave, village, castle) with unique events
# TODO: Create a function for random encounters (monsters, treasures, allies)

def random_encounter():
    import random
    encounters = [explore, cave, village, castle]
    random.choice(encounters)()

def cave():
    print("You enter a dark cave and find some loot")

def village():
    print("You are now at the peaceful village.")

def castle():
    print("You go to the grand castle.")


def main():
    while True:
        command = input("> ")
        if command.lower() == "explore":
            explore()
        elif command.lower() == "cave":
            cave()
        elif command.lower() == "village":
            village()
        elif command.lower() == "castle":
            castle()
        elif command.lower() == "random":
            random_encounter()
        elif command.lower() == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command. Try: explore, cave, village, castle, random, quit.")

if __name__ == "__main__":
    main()