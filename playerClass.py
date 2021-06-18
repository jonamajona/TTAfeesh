import deckClass as Decks
from math import ceil


class Player():
    def __init__(self):
        self.military_hand = []
        self.civil_hand = []
        self.blue_cubes = 16
        self.yellow_bank = 18
        self.idle_workers = 1
        self.government = Decks.Despotism
        self.CA = self.government.CA
        self.MA = self.government.MA
        self.happy_faces = 0
        self.rocks = 0
        self.food = 0
        self.science = 0
        self.culture = 0
        self.production = [Decks.Agriculture, Decks.Bronze]
        self.urban = [Decks.Philosophy, Decks.Religion]
        self.military_tech = [Decks.Warriors]

    def get_food_cost(self):
        if self.yellow_bank > 16:
            return 2
        elif self.yellow_bank > 12:
            return 3
        elif self.yellow_bank > 8:
            return 4
        elif self.yellow_bank > 4:
            return 5
        else:
            return 7

    def get_consumption(self):
        if self.yellow_bank > 16:
            return 0
        elif self.yellow_bank > 12:
            return 1
        elif self.yellow_bank > 8:
            return 2
        elif self.yellow_bank > 4:
            return 3
        elif self.yellow_bank > 0:
            return 4
        else:
            return 6

    def get_corruption(self):
        if self.blue_cubes > 10:
            return 0
        elif self.blue_cubes > 5:
            return 2
        elif self.blue_cubes > 0:
            return 4
        else:
            return 6

    def get_food_prod(self):
        food_prod = 0
        for card in self.farms:
            food_prod += card.prod * card.yellow_tokens
        return food_prod

    def get_rock_prod(self):
        rock_prod = 0
        for card in self.mines:
            rock_prod += card.prod * card.yellow_tokens
        return rock_prod

    def lose_food(self, food):
        food_to_lose = food
        food_taken = 0
        for card in self.production:
            if card.type == 'farm':
                while food_to_lose > 0 and card.blue_cubes > 0:
                    food_taken += card.prod
                    food_to_lose -= card.prod
                    card.blue_cubes -= 1
                    self.food -= card.prod
                    self.blue_cubes += 1
                    print(
                        f"Blue cube taken from {card.name}. {food_taken} food taken so far.")
        left_over = food_taken - food
        print(f"There is {left_over} food left over.")
        for card in reversed(self.production):
            if card.type == 'farm':
                while left_over >= card.prod:
                    card.blue_cubes += 1
                    self.food += card.prod
                    self.blue_cubes -= 1
                    left_over -= card.prod
                    print(
                        f"Blue cube added to {card.name}. There is {left_over} food left to add")
        if left_over < 0:
            self.culture += left_over * 4
            print(
                f"Your people are starving! You lost {left_over * -4} culture points")

    def lose_rocks(self, rocks):
        rocks_to_lose = rocks
        rocks_taken = 0
        for card in self.production:
            if card.type == 'mine':
                while rocks_to_lose > 0 and card.blue_cubes > 0:
                    rocks_taken += card.prod
                    rocks_to_lose -= card.prod
                    card.blue_cubes -= 1
                    self.rocks -= card.prod
                    self.blue_cubes += 1
                    print(
                        f"Blue cube taken from {card.name}. {rocks_taken} rocks taken so far.")
        left_over = rocks_taken - rocks
        print(f"There are {left_over} rocks left over.")
        for card in reversed(self.production):
            if card.type == 'mine':
                while left_over >= card.prod:
                    card.blue_cubes += 1
                    self.rocks += card.prod
                    self.blue_cubes -= 1
                    left_over -= card.prod
                    print(
                        f"Blue cube added to {card.name}. There are {left_over} rocks left to add")
        if left_over < 0:
            self.lose_food(left_over*-1)
            print(f"You lost {left_over*-1} food ")

    def produce_food(self):
        food_added = 0
        for card in reversed(self.production):
            if card.type == 'farm':
                remaining_blue_cubes = card.yellow_tokens
                while self.blue_cubes > 0 and remaining_blue_cubes > 0:
                    self.blue_cubes -= 1
                    card.blue_cubes += 1
                    remaining_blue_cubes -= 1
                    food_added += card.prod
                if remaining_blue_cubes > 0:
                    print(f"No more blue cubes left, some food lost")
        self.food += food_added
        print(f"You produced {food_added} food in total")

    def produce_rocks(self):
        rocks_added = 0
        for card in reversed(self.production):
            if card.type == 'mine':
                remaining_blue_cubes = card.yellow_tokens
                while self.blue_cubes > 0 and remaining_blue_cubes > 0:
                    self.blue_cubes -= 1
                    card.blue_cubes += 1
                    remaining_blue_cubes -= 1
                    rocks_added += card.prod
                if remaining_blue_cubes > 0:
                    print(f"No more blue cubes left, some resources lost")
        self.rocks += rocks_added
        print(f"You produced {rocks_added} resources in total")

    # military cards discarded = number of military cards in hand minus number of MA
    # military cards drawn = left over MA after turn (max of 3)
    # TODO account for wonder which allows you to hold 1 extra military card?
    def discard_military_cards(self, MA):
        while len(self.military_hand) > MA:
            cards_to_discard = len(self.military_hand) - MA
            print(
                f"You must discard {cards_to_discard} military cards. \nYour military cards are:")
            for index, card in enumerate(self.military_hand):
                print(f"{index+1}: {card.name}")
            proceed = False
            while proceed == False:
                try:
                    discard_index = int(
                        input("Which card would you like to discard?"))
                    if discard_index <= len(self.military_hand) and discard_index > 0:
                        proceed = True
                    else:
                        raise ValueError()
                except ValueError:
                    print("Please enter a valid number")
                    proceed = False
            Decks.discarded_military_cards.append(
                self.military_hand.pop(discard_index-1))

    def score_science(self):
        for card in self.urban:
            self.science += card.science_prod * card.yellow_tokens

    def score_culture(self):
        for card in self.urban:
            self.culture += card.culture_prod * card.yellow_tokens

    def draw_military_cards(self, remaining_MA):
        if remaining_MA >= 3:
            remaining_MA = 3
        while remaining_MA > 0:
            new_military_card = Decks.draw_military_card()
            self.military_hand.append(new_military_card)
            remaining_MA -= 1

    def calculate_discontent_workers(self):
        if self.yellow_bank > 16:
            discontent = 0
        elif self.yellow_bank > 12:
            discontent = 1 - self.happy_faces
        else:
            discontent = ceil((15 - self.yellow_bank)/2) - self.happy_faces
        if discontent < 0:
            return 0
        else:
            return discontent

    def check_for_uprising(self):
        if self.idle_workers > self.calculate_discontent_workers():
            return False
        else:
            return True

    def start_of_turn(self):
        pass

    def end_of_turn(self):
        self.discard_military_cards(self.MA)
        if not self.check_for_uprising():
            self.score_science()
            self.score_culture()
            self.lose_rocks(self.get_corruption())
            self.produce_food()
            self.lose_food(self.get_consumption())
            self.produce_rocks()
        else:
            print("You have an uprising! Production Phase skipped")
        self.draw_military_cards(self.MA)
