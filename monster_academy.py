class Room:
    def __init__(self, name):
        self.name = name

class MainEntrance(Room):
    def __init__(self):
        super().__init__("Main Entrance")

class Library(Room):
    def __init__(self):
        super().__init__("Library")

class EnchantedGarden(Room):
    def __init__(self):
        super().__init__("Enchanted Garden")

class Dungeon(Room):
    def __init__(self):
        super().__init__("Dungeon")

class TreasureRoom(Room):
    def __init__(self):
        super().__init__("Treasure Room")

class MonsterAcademyAdventure:
    def __init__(self):
        self.current_room = MainEntrance()

    def start_game(self):
        print("Welcome to the Monster Academy Adventure!")

    def handle_choice(self, choice):
        if choice == "1":
            self.current_room = Library()
        elif choice == "2":
            self.current_room = EnchantedGarden()
        else:
            print("Invalid choice. Please try again.")

    def play(self):
        self.start_game()
        print("You are at the", self.current_room.name)
        choice = input("Do you choose door 1 or door 2? ")
        self.handle_choice(choice)

# Instantiate the game and start playing
game = MonsterAcademyAdventure()
game.play()