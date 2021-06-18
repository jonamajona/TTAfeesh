class Card:
    def __init__(self, name, age, num_2P, num_3P, num_4P):
        self.name = name
        self.age = age
        self.num_2P = num_2P
        self.num_3P = num_3P
        self.num_4P = num_4P
        self.is_active = False
        self.is_expansion = False

    def __str__(self):
        return f"{self.name} ({self.age})"


class Government(Card):
    def __init__(self, name, age, num_2P, num_3P, num_4P, CA, MA, urban_limit, science_cost, revolution_cost):
        super().__init__(name, age, num_2P, num_3P, num_4P)
        self.CA = CA
        self.MA = MA
        self.urban_limit = urban_limit
        self.science_cost = science_cost
        self.revolution_cost = revolution_cost
        self.science_prod = 0
        self.happy_faces = 0
        self.might = 0
        self.culture_prod = 0
        self.rock_prod = 0


class Production(Card):
    def __init__(self, name, age, num_2P, num_3P, num_4P, type, prod, science_cost, rock_cost):
        super().__init__(name, age, num_2P, num_3P, num_4P)
        self.type = type
        self.prod = prod
        self.science_cost = science_cost
        self.rock_cost = rock_cost
        self.yellow_tokens = 0
        self.blue_cubes = 0


class Urban(Card):
    def __init__(self, name, age, num_2P, num_3P, num_4P, type, science_prod, culture_prod, might, happy_faces, science_cost, rock_cost):
        super().__init__(name, age, num_2P, num_3P, num_4P)
        self.type = type
        self.science_prod = science_prod
        self.culture_prod = culture_prod
        self.might = might
        self.happy_faces = happy_faces
        self.yellow_tokens = 0
        self.science_cost = science_cost
        self.rock_cost = rock_cost


class Military(Card):
    def __init__(self, name, age, num_2P, num_3P, num_4P, type, might, science_cost, rock_cost):
        super().__init__(name, age, num_2P, num_3P, num_4P)
        self.type = type
        self.might = might
        self.science_cost = science_cost
        self.rock_cost = rock_cost
        self.yellow_tokens = 0


class Action(Card):
    def __init__(self, name, age, num_2P, num_3P, num_4P):
        super().__init__(name, age, num_2P, num_3P, num_4P)


class Technology(Card):
    def __init__(self, name, age, num_2P, num_3P, num_4P, type, CA, MA, might, colonisation, wonder_steps, urban_discount, science_cost):
        super().__init__(name, age, num_2P, num_3P, num_4P)
        self.type = type
        self.CA = CA
        self.MA = MA
        self.colonisation = colonisation
        self.wonder_steps = wonder_steps
        self.urban_discount = urban_discount
        self.science_cost = science_cost
        self.blue_cubes = 0


class Leader(Card):
    def __init__(self, name, age, num_2P, num_3P, num_4P, is_expansion):
        super().__init__(name, age, num_2P, num_3P, num_4P)


class Wonder(Card):
    def __init__(self, name, age, num_2P, num_3P, num_4P, is_expansion):
        super().__init__(name, age, num_2P, num_3P, num_4P)


class Event(Card):
    def __init__(self, name, age, num_2P, num_3P, num_4P):
        super().__init__(name, age, num_2P, num_3P, num_4P)


class Pact(Card):
    def __init__(self, name, age, num_2P, num_3P, num_4P):
        super().__init__(name, age, num_2P, num_3P, num_4P)


class Colony(Event):
    def __init__(self, name, age, num_2P, num_3P, num_4P):
        super().__init__(name, age, num_2P, num_3P, num_4P)


class Impact(Event):
    def __init__(self, name, age, num_2P, num_3P, num_4P):
        super().__init__(name, age, num_2P, num_3P, num_4P)


class Aggression(Card):
    def __init__(self, name, age, num_2P, num_3P, num_4P):
        super().__init__(name, age, num_2P, num_3P, num_4P)


class War(Card):
    def __init__(self, name, age, num_2P, num_3P, num_4P):
        super().__init__(name, age, num_2P, num_3P, num_4P)


class Bonus(Card):
    def __init__(self, name, age, num_2P, num_3P, num_4P):
        super().__init__(name, age, num_2P, num_3P, num_4P)


class Tactic(Card):
    def __init__(self, name, age, num_2P, num_3P, num_4P):
        super().__init__(name, age, num_2P, num_3P, num_4P)
