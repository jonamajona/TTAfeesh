from enum import Enum
from random import shuffle
from math import ceil

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
        
class Decks:
    #cards cards to auto-discard on card row
    
    full_civil_deck = []
    full_military_deck = []
    partial_civil_deck = []
    partial_military_deck = []
    card_row = []

    age_A_civil_deck = []
    age_A_leaders = []
    age_A_wonders = []
    age_I_civil_deck = []
    age_I_leaders = []
    age_I_wonders = []
    age_II_civil_deck = []
    age_II_leaders = []
    age_II_wonders = []
    age_III_civil_deck = []
    age_III_leaders = []
    age_III_wonders = []

    age_A_military_deck = []
    age_I_military_deck = []
    age_II_military_deck = []
    age_III_military_deck = []

    discarded_military_cards = []
    discarded_civil_cards = []

    #Age A Government
    Despotism = Government('Despotism', 'A', 0, 0, 0, 4, 2, 2, None, None)

    #Age I Government
    Monarchy = Government('Monarchy', 'I', 1, 2, 2, 5, 3, 3, 8, 2)
    Theocracy = Government('Theocracy', 'I', 1, 1, 1, 4, 3, 3, 6, 1)
    Theocracy.happy_faces = 1
    Theocracy.culture_prod = 1
    Theocracy.might = 1

    #Age II Government
    Republic = Government('Republic', 'II', 1, 2, 2, 7, 2, 3, 11, 2)
    Conmon = Government('Constitutional Monarchy', 'II', 1, 2, 2, 6, 4, 3, 12, 6)

    #Age III Government
    Communism = Government('Communism', 'III', 1, 1, 1, 7, 5, 4, 18, 1)
    Communism.happy_faces = -1
    Communism.rock_prod = 1
    Democracy = Government('Democracy', 'III', 1, 2, 2, 7, 3, 4, 17, 9)
    Democracy.culture_prod = 3
    Fundamentalism = Government('Fundamentalism', 'III', 1, 1, 1, 6, 5, 4, 16, 5)
    Fundamentalism.science_prod = -2
    Fundamentalism.might = 6

    #Age A Production Cards
    Bronze = Production('Bronze', 'A', 0, 0, 0, 'mine', 1, None, 2)
    Bronze.is_active = True
    Bronze.yellow_tokens = 2
    Agriculture = Production('Agriculture', 'A', 0, 0, 0, 'farm', 1, None, 2)
    Agriculture.is_active = True
    Agriculture.yellow_tokens = 2

    #Age I Production Cards
    Iron = Production('Iron', 'I', 2, 2, 3, 'mine', 2, 5, 5)
    Irrigation = Production('Irrigation', 'I', 2, 2, 2, 'farm', 2, 3, 4)

    #Age II Production Cards
    Coal = Production('Coal', 'II', 1, 2, 2, 'mine', 3, 7, 8)
    Selective_Breeding = Production('Selective_Breeding', 'II', 1, 2, 3, 'farm', 3, 5, 6)

    #Age III Production Cards
    Oil = Production('Oil', 'III', 1, 2, 2, 'mine', 5, 9, 11)
    Mechanized_Agriculture = Production('Mechanized Agriculture', 'III', 1, 2, 2, 'farm', 5, 7, 8)

    #Age A Urban Buildings
    Religion = Urban('Religion', 'A', 0, 0, 0, 'temple', 0, 1, 0, 1, None, 3)
    Religion.is_active = True
    Philosophy = Urban('Philosophy', 'A', 0, 0, 0, 'lab', 1, 0, 0, 0, None, 3)
    Philosophy.is_active = True
    Philosophy.yellow_tokens = 1

    #Age I Urban Buildings
    Theology = Urban('Theology', 'I', 1, 2, 2, 'temple', 0, 1, 0, 2, 2, 5)
    Alchemy = Urban('Alchemy', 'I', 2, 2, 3, 'lab', 2, 0, 0, 0, 4, 6)
    Printing_Press = Urban('Printing Press', 'I', 2, 2, 2, 'library', 1, 1, 0, 0, 3, 3)
    Bread_and_Circuses = Urban('Bread and Circuses', 'I', 1, 2, 2, 'arena', 0, 0, 1, 2, 3, 3)
    Drama = Urban('Drama', 'I', 1, 2, 2, 'theatre', 0, 2, 0, 1, 3, 4)

    #Age II Urban Buildings
    Organized_Religion = Urban('Organized Religion', 'II', 2, 2, 2, 'temple', 0, 1, 0, 3, 4, 7)
    Scientific_Method = Urban('Scientific Method', 'II', 2, 2, 2, 'lab', 3, 0, 0, 0, 6, 8)
    Journalism = Urban('Journalism', 'II', 1, 2, 2, 'library', 2, 2, 0, 0, 6, 8)
    Team_Sports = Urban('Team Sports', 'II', 1, 1, 1, 'arena', 0, 0, 2, 3, 5, 5)
    Opera = Urban('Opera', 'II', 2, 2, 2, 'theatre', 0, 3, 0, 1, 7, 8)

    #Age III Urban Buildings
    Computers = Urban('Computers', 'III', 2, 2, 2, 'lab', 5, 0, 0, 0, 8, 11)
    Multimedia = Urban('Multimedia', 'III', 2, 2, 2, 'library', 3, 3, 0, 0, 9, 11)
    Professional_Sports = Urban('Professional Sports', 'III', 1, 2, 2, 'arena', 0, 0, 4, 4, 7, 7)
    Movies = Urban('Movies', 'III', 2, 2, 2, 'theatre', 0, 4, 0, 1, 10, 11)

    #Age A Military
    Warriors = Military('Warriors', 'A', 0, 0, 0, 'infantry', 1, None, 2)
    Warriors.is_active = True

    #Age I Military
    Swordsmen = Military('Swordsmen', 'I', 2, 2, 2, 'infantry', 2, 4, 3)
    Knights = Military('Knights', 'I', 2, 2, 3, 'cavalry', 2, 5, 3)

    #Age II Military
    Riflemen = Military('Riflemen', 'II', 2, 2, 2, 'infantry', 3, 6, 5)
    Cavalrymen = Military('Cavalrymen', 'II', 1, 2, 2, 'cavalry', 3, 6, 5)
    Cannon = Military('Cannon', 'II', 2, 2, 3, 'artillery', 3, 6, 5)

    #Age III Military
    Modern_Infantry = Military('Modern Infantry', 'III', 1, 2, 2, 'infantry', 5, 10, 7)
    Tanks = Military('Tanks', 'III', 1, 2, 2, 'cavalry', 5, 9, 7)
    Rockets = Military('Rockets', 'III', 1, 2, 2, 'artillery', 5, 8, 7)
    Air_Forces = Military('Air Forces', 'III', 2, 2, 3, 'air forces', 5, 12, 7)
    
    #Age A Action Cards
    Rich_Land_A = Action('Rich Land', 'A', 2, 2, 2)
    Engineering_Genius_A = Action('Engineering Genius', 'A', 1, 1, 1)
    Patriotism_A = Action('Patriotism', 'A', 1, 1, 1)
    Frugality_A = Action('Frugality', 'A', 2, 2, 2)
    Urban_Growth_A = Action('Urban Growth', 'A', 2, 2, 2)
    Cultural_Heritage_A = Action('Cultural Heritage', 'A', 1, 1, 1)
    Stock_Pile = Action('Stock_Pile', 'A', 1, 1, 1)

    #Age I Action Cards
    Rich_Land_I = Action('Rich Land', 'I', 2, 3, 3)
    Engineering_Genius_I = Action('Engineering Genius', 'I', 1, 1, 1)
    Patriotism_I = Action('Patriotism', 'I', 1, 1, 1)
    Frugality_I = Action('Frugality', 'I', 2, 2, 2)
    Breakthrough_I = Action('Breakthrough', 'I', 2, 2, 2)
    Urban_Growth_I = Action('Urban Growth', 'I', 2, 2, 2)
    Cultural_Heritage_I = Action('Cultural Heritage', 'I', 1, 1, 1)
    Reserves_I = Action('Reserves', 'I', 2, 2, 2)

    #Age II Action Cards
    Rich_Land_II = Action('Rich Land', 'II', 1, 1, 1)
    Engineering_Genius_II = Action('Engineering Genius', 'II', 1, 1, 1)
    Revolutionary_Idea_II = Action('Revolutionary Idea', 'II', 1, 1, 1)
    Patriotism_II = Action('Patriotism', 'II', 1, 1, 1)
    Frugality_II = Action('Frugality', 'II', 1, 2, 2)
    Breakthrough_II = Action('Breakthrough', 'II', 2, 2, 2)
    Efficient_Upgrade_II = Action('Efficient Upgrade', 'II', 2, 2, 2)
    Wave_of_Nationalism = Action('Wave of Nationalism', 'II', 1, 1, 1)
    Urban_Growth_II = Action('Urban Growth', 'II', 1, 2, 2)
    Reserves_II = Action('Reserves', 'II', 2, 2, 2)

    #Age III Action Cards
    Engineering_Genius_III = Action('Engineering Genius', 'III', 1, 1, 1)
    Revolutionary_Idea_III = Action('Revolutionary Idea', 'III', 2, 3, 3)
    Patriotism_III = Action('Patriotism', 'III', 1, 2, 2)
    Efficient_Upgrade_III = Action('Efficient Upgrade', 'III', 2, 2, 2)
    Endowment_for_the_Arts = Action('Endowment for the Arts', 'III', 1, 1, 1)
    Military_Build_Up = Action('Military Build Up', 'III', 1, 1, 1)
    Urban_Growth_III = Action('Urban Growth', 'III', 2, 2, 2)
    Reserves_III = Action('Reserves', 'III', 3, 4, 4)

    #Age I Technologies
    Cartography = Technology('Cartography', 'I', 1, 1, 1, 'exploration', 0, 0, 1, 2, 0, 0, 4)
    Warfare = Technology('Warfare', 'I', 1, 2, 2, 'warfare', 0, 1, 1, 0, 0, 0, 5)   
    Code_of_Laws = Technology('Code of Laws', 'I', 1, 2, 2, 'law', 1, 0, 0, 0, 0, 0, 6)   
    Masonry = Technology('Masonry', 'I', 1, 1, 1, 'construction', 0, 0, 0, 0, 2, [1,1,1], 3)

    #Age II Technologies
    Navigation = Technology('Navigation', 'II', 1, 1, 1, 'exploration', 0, 0, 2, 3, 0, 0, 6)
    Strategy = Technology('Strategy', 'II', 1, 1, 1, 'warfare', 0, 2, 3, 0, 0, 0, 8)   
    Justice_System = Technology('Justice System', 'II', 1, 1, 1, 'law', 1, 0, 0, 0, 0, 0, 7)
    Justice_System.blue_cubes = 3 
    Architecture = Technology('Architecture', 'II', 1, 2, 2, 'construction', 0, 0, 0, 0, 3, [1,2,2], 6)
    

    #Age III Technologies
    Satellites = Technology('Satellites', 'III', 1, 1, 1, 'exploration', 0, 0, 3, 4, 0, 0, 8)
    Military_Theory = Technology('Military Theory', 'III', 1, 2, 2, 'warfare', 0, 3, 5, 0, 0, 0, 11)   
    Civil_Service = Technology('Civil Service', 'III', 1, 1, 1, 'law', 2, 0, 0, 0, 0, 0, 10)
    Civil_Service.blue_cubes = 3   
    Engineering = Technology('Engineering', 'III', 1, 1, 1, 'construction', 0, 0, 0, 0, 4, [1,2,3], 9)

    #Age A Base Leaders
    Hammurabi = Leader('Hammurabi', 'A', 0, 0, 0, False)
    Caesar = Leader('Julius Caesar', 'A', 0, 0, 0, False)
    Alexander = Leader('Alexander the Great', 'A', 0, 0, 0, False)
    Aristotle = Leader('Aristotle', 'A', 0, 0, 0, False)
    Moses = Leader('Moses', 'A', 0, 0, 0, False)
    Homer = Leader('Homer', 'A', 0, 0, 0, False)
    
    #Age A Expansion Leaders
    Boudica = Leader('Boudica', 'A', 0, 0, 0, True)
    Cleopatra = Leader('Cleopatra', 'A', 0, 0, 0, True)
    Hippocrates = Leader('Hippocrates', 'A', 0, 0, 0, True)
    Confucius = Leader('Confucius', 'A', 0, 0, 0, True)
    Sun_Tzu = Leader('Sun Tzu', 'A', 0, 0, 0, True)
    Ashoka = Leader('Ashoka', 'A', 0, 0, 0, True)

    #Age I Base Leaders
    Genghis_Khan = Leader('Genghis Khan', 'I', 0, 0, 0, False)
    Barbarossa = Leader('Frederick Barbarossa', 'I', 0, 0, 0, False) 
    Columbus = Leader('Christopher Columbus', 'I', 0, 0, 0, False) 
    Da_Vinci = Leader('Leonardo Da Vinci', 'I', 0, 0, 0, False) 
    Michelangelo = Leader('Michelangelo', 'I', 0, 0, 0, False) 
    Joan_of_Arc = Leader('Joan of Arc', 'I', 0, 0, 0, False)

    #Age I Expansion Leaders
    Isabella = Leader('Isabella of Castile', 'I', 0, 0, 0, True)
    Eleanor = Leader('Eleanor of Aquitane', 'I', 0, 0, 0, True)
    Zizka = Leader('Jan Zizka', 'I', 0, 0, 0, True)
    Nostradamus = Leader('Nostradamus', 'I', 0, 0, 0, True)
    Gutenbeast = Leader('Johannes Gutenberg', 'I', 0, 0, 0, True)
    Saladin = Leader('Saladin', 'I', 0, 0, 0, True)

    #Age II Base Leaders
    Napoleon = Leader('Napoleon Bonaparte', 'II', 0, 0, 0, False)
    Shakespeare = Leader('William Shakespeare', 'II', 0, 0, 0, False) 
    Newton = Leader('Isaac Newton', 'II', 0, 0, 0, False) 
    Robespierre = Leader('Maximilien Robespierre', 'II', 0, 0, 0, False) 
    Cook = Leader('James Cook', 'II', 0, 0, 0, False) 
    Bach = Leader('Johann Sebastian Bach', 'II', 0, 0, 0, False)

    #Age II Expansion Leaders
    Catherine = Leader('Catherine the Great', 'II', 0, 0, 0, True)
    Maria_Theresa = Leader('Maria Theresa', 'II', 0, 0, 0, True)
    Watt = Leader('James Watt', 'II', 0, 0, 0, True)
    Nobel = Leader('Alfred Nobel', 'II', 0, 0, 0, True)
    Gaudi = Leader('Anton Gaudi', 'II', 0, 0, 0, True)
    Darwin = Leader('Charles Darwin', 'II', 0, 0, 0, True)

    #Age III Base Leaders
    Ghandi = Leader('Ghandi', 'III', 0, 0, 0, False)
    Bill_Gates = Leader('Bill Gates', 'III', 0, 0, 0, False) 
    Sid_Meier = Leader('Sid Meier', 'III', 0, 0, 0, False) 
    Churchill = Leader('Winston Churchill', 'III', 0, 0, 0, False) 
    Einstein = Leader('Albert Einstein', 'III', 0, 0, 0, False) 
    Chaplin = Leader('Charlie Chaplin', 'III', 0, 0, 0, False)

    #Age III Expansion Leaders
    Marie_Curie = Leader('Marie Curie Sklodowska', 'III', 0, 0, 0, True)
    Marlene = Leader('Marlene Dietrich', 'III', 0, 0, 0, True)
    Steve_Jobs = Leader('Steve Jobs', 'III', 0, 0, 0, True)
    Mandela = Leader('Nelson Mandela', 'III', 0, 0, 0, True)
    Pierre_de_Coubertin = Leader('Pierre de Coubertin', 'III', 0, 0, 0, True)
    Ian_Fleming = Leader('Ian_Fleming', 'III', 0, 0, 0, True)

    #Age A Base Wonders
    Pyramids = Wonder('Pyramids', 'A', 0, 0, 0, False)
    Hanging_Gardens = Wonder('Hanging Gardens', 'A', 0, 0, 0, False)
    Library_of_Alexandria = Wonder('Library of Alexandria', 'A', 0, 0, 0, False)
    Colossus = Wonder('Colossus ', 'A', 0, 0, 0, False)

    #Age A Expansion Wonders
    Colosseum = Wonder('Colosseum', 'A', 0, 0, 0, True)
    Roman_Roads = Wonder('Roman Roads', 'A', 0, 0, 0, True)
    Stonehenge = Wonder('Stonehenge', 'A', 0, 0, 0, True)
    Acropolis = Wonder('Acropolis', 'A', 0, 0, 0, True)

    #Age I Base Wonders
    Great_Wall = Wonder('Great Wall', 'I', 0, 0, 0, False)
    Universitas = Wonder('Universitas Carolina', 'I', 0, 0, 0, False)
    Taj_Mahal = Wonder('Taj Mahal', 'I', 0, 0, 0, False)
    St_Petes = Wonder('St Peters Basilica', 'I', 0, 0, 0, False)

    #Age I Expansion Wonders
    Machu_Picchu = Wonder('Machu Picchu', 'I', 0, 0, 0, True)
    Himeji_Castle = Wonder('Himeji Castle', 'I', 0, 0, 0, True)
    Forbidden_City = Wonder('Forbidden City', 'I', 0, 0, 0, True)
    Silk_Road = Wonder('Silk Road', 'I', 0, 0, 0, True)

    #Age II Base Wonders
    Railroad = Wonder('Transcontinental Railroad', 'II', 0, 0, 0, False)
    Ocean_Liner = Wonder('Ocean Liner Service', 'II', 0, 0, 0, False)
    Eiffel_Tower = Wonder('Eiffel Tower', 'II', 0, 0, 0, False)
    Kremlin = Wonder('Kremlin', 'II', 0, 0, 0, False)

    #Age II Expansion Wonders
    Harvard = Wonder('Harvard College', 'II', 0, 0, 0, True)
    Statue_of_Liberty = Wonder('Statue of Liberty', 'II', 0, 0, 0, True)
    Louvre = Wonder('Louvre Museum', 'II', 0, 0, 0, True)
    Suez_Canal = Wonder('Suez Canal', 'II', 0, 0, 0, True)

    #Age III Base Wonders
    Fast_Food_Chains = Wonder('Fast Food Chains', 'III', 0, 0, 0, False)
    Space_Flight = Wonder('Space Flight', 'III', 0, 0, 0, False)
    Hollywood = Wonder('Hollywood', 'III', 0, 0, 0, False)
    Internet = Wonder('Internet', 'III', 0, 0, 0, False)

    #Age III Expansion Wonders
    Empire_State = Wonder('Empire State Building', 'III', 0, 0, 0, True)
    United_Nations = Wonder('United Nations', 'III', 0, 0, 0, True)
    Red_Cross = Wonder('International Red Cross', 'III', 0, 0, 0, True)
    Manhattan_Project = Wonder('Manhattan Project', 'III', 0, 0, 0, True)

    ###########
    #Military Cards
    ###########

    #Age A Events
    D_of_Settlement = Event('Development of Settlement', 'A', 1, 1, 1)
    D_of_Science = Event('Development of Science', 'A', 1, 1, 1)
    D_of_Crafts = Event('Development of Crafts', 'A', 1, 1, 1)
    D_of_Agriculture = Event('Development of Agriculture', 'A', 1, 1, 1)
    D_of_Warfare = Event('Development of Warfare', 'A', 1, 1, 1)
    D_of_Religion = Event('Development of Religion', 'A', 1, 1, 1)
    D_of_Politics = Event('Development of Politics', 'A', 1, 1, 1)
    D_of_Markets = Event('Development of Markets', 'A', 1, 1, 1)
    D_of_Trade_Routes = Event('Development of Trade Routes', 'A', 1, 1, 1)
    D_of_Civil_Life = Event('Development of Civil Life', 'A', 1, 1, 1)
    D_of_Planning = Event('Development of Planning', 'A', 1, 1, 1)
    D_of_Planning.is_expansion = True

    #Age I Events
    Rats = Event('Rats', 'I', 1, 1, 1)
    Pestilence = Event('Pestilence', 'I', 1, 1, 1)
    Raiders = Event('Raiders', 'I', 1, 1, 1)
    Barbarians = Event('Barbarians', 'I', 1, 1, 1)
    Foray = Event('Foray', 'I', 1, 1, 1)
    Reign_of_Terror = Event('Reign of Terror', 'I', 1, 1, 1)
    Immigration = Event('Immigration', 'I', 1, 1, 1)
    Uncertain_Borders = Event('Uncertain Borders', 'I', 1, 1, 1)
    Border_Conflict = Event('Border Conflict', 'I', 1, 1, 1)
    Crusades = Event('Crusades', 'I', 1, 1, 1)
    Rebellion = Event('Rebellion', 'I', 1, 1, 1)
    Scientific_Breakthrough = Event('Scientific Breakthrough', 'I', 1, 1, 1)
    Good_Harvest = Event('Good Harvest', 'I', 1, 1, 1)
    New_Deposits = Event('New Deposits', 'I', 1, 1, 1)
    Cultural_Influence = Event('Cultural Influence', 'I', 1, 1, 1)
    Dark_Ages = Event('Dark Ages', 'I', 1, 1, 1)
    Dark_Ages.is_expansion = True
    Call_to_Arms = Event('Call to Arms', 'I', 1, 1, 1)
    Call_to_Arms.is_expansion = True
    Knowledge_of_the_Ancients= Event('Knowledge of the Ancients', 'I', 1, 1, 1)
    Knowledge_of_the_Ancients.is_expansion = True

    #Age II Events
    Iconoclasm = Event('Iconoclasm', 'II', 1, 1, 1)
    Ravages_of_Time = Event('Ravages of Time', 'II', 1, 1, 1)
    Terrorism = Event('Terrorism', 'II', 1, 1, 1)
    Civil_Unrest = Event('Civil Unrest', 'II', 1, 1, 1)
    National_Pride = Event('National Pride', 'II', 1, 1, 1)
    Crime_Wave = Event('Crime Wave', 'II', 1, 1, 1)
    Independence_Declaration = Event('Independence Declaration', 'II', 1, 1, 1)
    Emigration = Event('Emigration', 'II', 1, 1, 1)
    Cold_War = Event('Cold War', 'II', 1, 1, 1)
    Refugees = Event('Refugees', 'II', 1, 1, 1)
    International_Agreement = Event('International Agreement', 'II', 1, 1, 1)
    Economic_Progress = Event('Economic Progress', 'II', 1, 1, 1)
    Popularization_of_Science = Event('Popularization of Science', 'II', 1, 1, 1)
    Politics_of_strength = Event('Politics of Strength', 'II', 1, 1, 1)
    Prosperity = Event('Prosperity', 'II', 1, 1, 1)
    Freedom_of_Movement = Event('Freedom of Movement', 'II', 1, 1, 1)
    Freedom_of_Movement.is_expansion = True
    International_Negotiations = Event('International Negotiations', 'II', 1, 1, 1)
    International_Negotiations.is_expansion = True
    Arms_Industry = Event('Arms Industry', 'II', 1, 1, 1)
    Arms_Industry.is_expansion = True
    
    #Age I Colonies
    Vast_Territory_I = Colony('Vast Territory', 'I', 1, 1, 1)
    Wealthy_Territory_I = Colony('Wealthy Territory', 'I', 1, 1, 1)
    Inhabited_Territory_I = Colony('Inhabited Territory', 'I', 1, 1, 1)
    Strategic_Territory_I = Colony('Strategic Territory', 'I', 1, 1, 1)
    Historic_Territory_I = Colony('Historic Territory', 'I', 1, 1, 1)
    Developed_Territory_I = Colony('Developed Territory', 'I', 1, 1, 1)

    #Age II Colonies
    Vast_Territory_II = Colony('Vast Territory', 'II', 1, 1, 1)
    Wealthy_Territory_II = Colony('Wealthy Territory', 'II', 1, 1, 1)
    Inhabited_Territory_II = Colony('Inhabited Territory', 'II', 1, 1, 1)
    Strategic_Territory_II = Colony('Strategic Territory', 'II', 1, 1, 1)
    Historic_Territory_II = Colony('Historic Territory', 'II', 1, 1, 1)
    Developed_Territory_II = Colony('Developed Territory', 'II', 1, 1, 1)
    Autonomous_Territory = Colony('Autonomous Territory', 'II', 1, 1, 1)
    Autonomous_Territory.is_expansion = True

    #Age I Bonus Cards
    Bonus_I = Bonus('Military Bonus', 'I', 7, 7, 7)

    #Age II Bonus Cards
    Bonus_II = Bonus('Military Bonus', 'II', 7, 7, 7)

    #Age III Bonus Cards
    Bonus_III = Bonus('Military Bonus', 'III', 7, 7, 7)

    #Age I Tactics
    Fighting_Band = Tactic('Fighting Band', 'I', 2, 2, 2)
    Legion = Tactic('Legion', 'I', 2, 2, 2)
    Phalanx = Tactic('Phalanx', 'I', 2, 2, 2)
    Heavy_Cavalry = Tactic('Heavy Cavalry', 'I', 2, 2, 2)
    Medieval_Army = Tactic('Medieval Army', 'I', 2, 2, 2)

    #Age II Tactics
    Napoleonic_Army = Tactic('Napoleonic Army', 'II', 1, 1, 1)
    Defensive_Army = Tactic('Defensive Army', 'II', 1, 1, 1)
    Conquistadors = Tactic('Conquistadors', 'II', 1, 1, 1)
    Fortifications = Tactic('Fortifications', 'II', 1, 1, 1)
    Classic_Army = Tactic('Classic Army', 'II', 1, 1, 1)
    Mobile_Artillery = Tactic('Mobile Artillery', 'II', 1, 1, 1)
    Hussars = Tactic('Hussars', 'II', 1, 1, 1)
    Hussars.is_expansion = True

    #Age III Tactics
    Entrenchments = Tactic('Entrenchments', 'III', 1, 1, 1)
    Modern_Army = Tactic('Modern Army', 'III', 2, 2, 2)
    Mechanized_Army = Tactic('Mechanized Army', 'III', 2, 2, 2)
    Shock_Troops = Tactic('Shock Troops', 'III', 1, 1, 1)
    Positional_Army = Tactic('Positional Army', 'III', 1, 1, 1)
    Positional_Army.is_expansion = True

    #Age I Aggressions
    Raid_I = Aggression('Aggression: Raid', 'I', 1, 2, 2)
    Plunder_I = Aggression('Aggression: Plunder', 'I', 2, 2, 2)
    Enslave = Aggression('Aggression: Enslave', 'I', 2, 2, 2)
    Kidnap = Aggression('Aggression: Kidnap', 'I', 1, 1, 1)
    Kidnap.is_expansion = True

    #Age II Aggressions
    Raid_II = Aggression('Aggression: Raid', 'II', 2, 2, 2)
    Plunder_II = Aggression('Aggression: Plunder', 'II', 2, 2, 2)
    Spy = Aggression('Aggression: Spy', 'II', 2, 2, 2)
    Annex = Aggression('Aggression: Annex', 'II', 1, 1, 1)
    Infiltrate = Aggression('Aggression: Infiltrate', 'II', 2, 2, 2)

    #Age III Aggressions
    Raid_III = Aggression('Aggression: Raid', 'III', 2, 2, 2)
    Plunder_III = Aggression('Aggression: Plunder', 'III', 2, 2, 2)
    Armed_Intervention = Aggression('Aggression: Armed Intervention', 'III', 4, 4, 4)
    Occupy = Aggression('Aggression: Occupy', 'III', 1, 1, 1)
    Occupy.is_expansion = True

    #Age I Pacts
    Open_Borders = Pact('Open Borders Agreement', 'I', 0, 1, 1)
    Trade_Routes = Pact('Trade Routes Agreement', 'I', 0, 1, 1)
    Naval_Trade = Pact('Naval Trade Agreement', 'I', 0, 1, 1)
    Naval_Trade.is_expansion = True

    #Age II Pacts
    Supremacy = Pact('Acceptance of Supremacy', 'II', 0, 1, 1)
    Scientific_Cooperation = Pact('Scientific Cooperation', 'II', 0, 1, 1)
    International_Trade = Pact('International Trade Agreement', 'II', 0, 1, 1)
    International_Trade.is_expansion = True
    Military_Protection = Pact('Promise of Military Protection', 'II', 0, 1, 1)
    Military_Protection.is_expansion = True

    #Age III Pacts
    Military_Alliance = Pact('Military Alliance', 'III', 0, 1, 1)
    Peace_Treaty = Pact('Peace Treaty', 'III', 0, 1, 1)
    Tourism = Pact('International Tourism', 'III', 0, 1, 1)
    Tourism.is_expansion = True
    Loss_of_Sovereignty = Pact('Loss of Sovereignty', 'III', 0, 1, 1)
    Loss_of_Sovereignty.is_expansion = True

    #Age II Wars
    War_over_Territory = War('War over Territory', 'II', 2, 2, 2)
    War_over_Technology = War('War over Technology', 'II', 2, 2, 2)

    #Age III Wars
    War_over_Culture = War('War over Culture', 'III', 6, 6, 6)
    Hybrid_War = War('Hybrid War', 'III', 1, 1, 1)
    Hybrid_War.is_expansion = True

    #Age III Impacts
    Impact_of_Industry = Impact('Iconoclasm', 'III', 1, 1, 1)
    Impact_of_Agriculture = Impact('Ravages of Time', 'III', 1, 1, 1)
    Impact_of_Competition = Impact('Impact of Competition', 'III', 1, 1, 1)
    Impact_of_Progress = Impact('Impact of Progress', 'III', 1, 1, 1)
    Impact_of_Wonders = Impact('Impact of Wonders', 'III', 1, 1, 1)
    Impact_of_Population = Impact('Impact of Population', 'III', 1, 1, 1)
    Impact_of_Colonies = Impact('Impact of Colonies', 'III', 1, 1, 1)
    Impact_of_Government = Impact('Impact of Government', 'III', 1, 1, 1)
    Impact_of_Architecture = Impact('Impact of Architecture', 'III', 1, 1, 1)
    Impact_of_Strength = Impact('Impact of Strength', 'III', 1, 1, 1)
    Impact_of_Happiness = Impact('Impact of Happiness', 'III', 1, 1, 1)
    Impact_of_Science = Impact('Impact of Science', 'III', 1, 1, 1)
    Impact_of_Technology = Impact('Impact of Technology', 'III', 1, 1, 1)
    Impact_of_Balance = Impact('Impact of Balance', 'III', 1, 1, 1)
    Impact_of_Variety = Impact('Impact of Variety', 'III', 1, 1, 1)
    Impact_of_Harmony = Impact('Impact of Harmony', 'III', 1, 1, 1)
    Impact_of_Harmony.is_expansion = True
    Impact_of_Culture = Impact('Impact of Culture', 'III', 1, 1, 1)
    Impact_of_Culture.is_expansion = True

    civil_card = [Bronze, Agriculture, Religion, Philosophy, Warriors, Rich_Land_A, Engineering_Genius_A, Patriotism_A, Frugality_A, Urban_Growth_A, Cultural_Heritage_A, \
        Stock_Pile, Hammurabi, Caesar, Alexander, Aristotle, Moses, Homer, Boudica, Cleopatra, Hippocrates, Confucius, Sun_Tzu, Ashoka, Pyramids, Hanging_Gardens, \
        Library_of_Alexandria, Colossus, Colosseum, Roman_Roads, Stonehenge, Acropolis, Rich_Land_I, Engineering_Genius_I, Patriotism_I, Frugality_I, \
        Breakthrough_I, Urban_Growth_I, Cultural_Heritage_I, Reserves_I, Iron, Irrigation, Theology, Alchemy, Printing_Press, Bread_and_Circuses, Drama, \
        Cartography, Warfare, Code_of_Laws, Masonry, Swordsmen, Knights, Monarchy, Theocracy, Genghis_Khan, Barbarossa, Columbus, Da_Vinci, Michelangelo, \
        Joan_of_Arc, Isabella, Eleanor, Zizka, Nostradamus, Gutenbeast, Saladin, Great_Wall, Universitas, Taj_Mahal, St_Petes, Machu_Picchu, Himeji_Castle, \
        Forbidden_City, Silk_Road, Rich_Land_II, Engineering_Genius_II, Revolutionary_Idea_II, Patriotism_II, Frugality_II, Breakthrough_II, Efficient_Upgrade_II, \
        Wave_of_Nationalism, Urban_Growth_II, Reserves_II, Coal, Selective_Breeding, Organized_Religion, Scientific_Method, Journalism, Team_Sports, Opera, \
        Navigation, Strategy, Justice_System, Architecture, Riflemen, Cavalrymen, Cannon, Republic, Conmon, Napoleon, Shakespeare, Newton, Robespierre, Cook, \
        Bach, Catherine, Maria_Theresa, Watt, Nobel, Gaudi, Darwin, Railroad, Ocean_Liner, Eiffel_Tower, Kremlin, Harvard, Statue_of_Liberty, Louvre, Suez_Canal, \
        Engineering_Genius_III, Revolutionary_Idea_III, Patriotism_III, Efficient_Upgrade_III, Endowment_for_the_Arts, Military_Build_Up, Urban_Growth_III, Reserves_III, \
        Oil, Mechanized_Agriculture, Computers, Multimedia, Movies, Satellites, Military_Theory, Civil_Service, Engineering, Modern_Infantry, Tanks, Rockets, \
        Air_Forces, Communism, Fundamentalism, Democracy, Ghandi, Bill_Gates, Sid_Meier, Churchill, Einstein, Chaplin, Marie_Curie, Marlene, Steve_Jobs, Mandela, \
        Pierre_de_Coubertin, Ian_Fleming, Fast_Food_Chains, Space_Flight, Hollywood, Internet, Empire_State, United_Nations, Red_Cross, Manhattan_Project]

    military_card = [D_of_Settlement, D_of_Science, D_of_Crafts, D_of_Agriculture, D_of_Warfare, D_of_Warfare, D_of_Religion, D_of_Politics, D_of_Markets, \
        D_of_Trade_Routes, D_of_Civil_Life, D_of_Planning, Rats, Pestilence, Raiders, Barbarians, Foray, Reign_of_Terror, Immigration, Uncertain_Borders, \
        Border_Conflict, Crusades, Rebellion, Scientific_Breakthrough, Good_Harvest, New_Deposits, Cultural_Influence, Dark_Ages, Call_to_Arms, Knowledge_of_the_Ancients, \
        Vast_Territory_I, Wealthy_Territory_I, Inhabited_Territory_I, Strategic_Territory_I, Historic_Territory_I, Developed_Territory_I, Bonus_I, Fighting_Band, \
        Legion, Phalanx, Heavy_Cavalry, Medieval_Army, Raid_I, Plunder_I, Enslave, Kidnap, Open_Borders, Trade_Routes, Naval_Trade, Iconoclasm, Ravages_of_Time, Terrorism, Civil_Unrest, National_Pride, \
        Crime_Wave, Independence_Declaration, Emigration, Cold_War, Refugees, International_Agreement, Economic_Progress, Popularization_of_Science, Politics_of_strength, \
        Prosperity, Freedom_of_Movement, International_Negotiations, Arms_Industry, Vast_Territory_II, Wealthy_Territory_II, Inhabited_Territory_II, \
        Strategic_Territory_II, Historic_Territory_II, Developed_Territory_II, Autonomous_Territory, Bonus_II, Napoleonic_Army, Defensive_Army, Conquistadors, \
        Fortifications, Classic_Army, Mobile_Artillery, Hussars, Raid_II, Plunder_II, Spy, Annex, Infiltrate, War_over_Territory, War_over_Technology, \
        Supremacy, Scientific_Cooperation, International_Trade, Military_Protection, \
        Impact_of_Industry, Impact_of_Agriculture, Impact_of_Competition, Impact_of_Progress, Impact_of_Wonders, Impact_of_Population, Impact_of_Colonies, \
        Impact_of_Government, Impact_of_Architecture, Impact_of_Strength, Impact_of_Happiness, Impact_of_Science, Impact_of_Technology, Impact_of_Balance, \
        Impact_of_Variety, Impact_of_Harmony, Impact_of_Culture, Bonus_III, Entrenchments, Modern_Infantry, Mechanized_Army, Shock_Troops, Positional_Army, \
        Raid_III, Plunder_III, Armed_Intervention, Occupy, War_over_Culture, Hybrid_War, Military_Alliance, Peace_Treaty, Tourism, Loss_of_Sovereignty]

    def __init__(self, num_players):
        self.num_players = num_players
        if num_players == 2:
            self.auto_discard = 3
        elif num_players == 3:
            self.auto_discard = 2
        elif players == 4:
            self.auto_discard = 1

    def build_civil_deck(self):
        for card in self.civil_card:
            num = 0
            if self.num_players == 2:
                num = card.num_2P
            elif self.num_players == 3:
                num = card.num_3P
            elif self.num_players == 4:
                num = card.num_4P
            if card.age == 'A':
                #age A leaders
                if isinstance(card, Leader):
                    self.age_A_leaders.append(card)
                #age A wonders
                if isinstance(card, Wonder):
                    self.age_A_wonders.append(card)
                #rest of age A civil cards
                i = 0
                while num > i:
                    self.age_A_civil_deck.append(card)
                    i += 1
            if card.age == 'I':
                #age I leaders
                if isinstance(card, Leader):
                    self.age_I_leaders.append(card)
                #age I wonders
                if isinstance(card, Wonder):
                    self.age_I_wonders.append(card)
                #rest of age I civil cards
                i = 0
                while num > i:
                    self.age_I_civil_deck.append(card)
                    i += 1
            if card.age == 'II':
                #age II leaders
                if isinstance(card, Leader):
                    self.age_II_leaders.append(card)
                #age II wonders
                if isinstance(card, Wonder):
                    self.age_II_wonders.append(card)
                #rest of age II civil cards
                i = 0
                while num > i:
                    self.age_II_civil_deck.append(card)
                    i += 1
            if card.age == 'III':
                #age III leaders
                if isinstance(card, Leader):
                    self.age_III_leaders.append(card)
                #age III wonders
                if isinstance(card, Wonder):
                    self.age_III_wonders.append(card)
                #rest of age III civil cards
                i = 0
                while num > i:
                    self.age_III_civil_deck.append(card)
                    i += 1
        #construct leader and wonder decks
        if self.num_players == 2:
            num_leaders = 6
            num_wonders = 4
        else:
            num_leaders = 7
            num_wonders = 5
        #shuffle age A leaders and wonders and add into civil deck
        shuffle(self.age_A_leaders)
        self.age_A_leaders = self.age_A_leaders[:num_leaders]
        shuffle(self.age_A_wonders)
        self.age_A_wonders = self.age_A_wonders[:num_wonders]
        self.age_A_civil_deck += self.age_A_leaders + self.age_A_wonders
        shuffle(self.age_A_civil_deck)

        #shuffle age I leaders and wonders and add into civil deck
        shuffle(self.age_I_leaders)
        self.age_I_leaders = self.age_I_leaders[:num_leaders]
        shuffle(self.age_I_wonders)
        self.age_I_wonders = self.age_I_wonders[:num_wonders]
        self.age_I_civil_deck += self.age_I_leaders + self.age_I_wonders
        shuffle(self.age_I_civil_deck)

        #shuffle age II leaders and wonders and add into civil deck
        shuffle(self.age_II_leaders)
        self.age_II_leaders = self.age_II_leaders[:num_leaders]
        shuffle(self.age_II_wonders)
        self.age_II_wonders = self.age_II_wonders[:num_wonders]
        self.age_II_civil_deck += self.age_II_leaders + self.age_II_wonders
        shuffle(self.age_II_civil_deck)

        #shuffle age III leaders and wonders and add into civil deck
        shuffle(self.age_III_leaders)
        self.age_III_leaders = self.age_III_leaders[:num_leaders]
        shuffle(self.age_III_wonders)
        self.age_III_wonders = self.age_III_wonders[:num_wonders]
        self.age_III_civil_deck += self.age_III_leaders + self.age_III_wonders
        shuffle(self.age_III_civil_deck)

        self.full_civil_deck = self.age_A_civil_deck + self.age_I_civil_deck + self.age_II_civil_deck + self.age_III_civil_deck
        self.partial_civil_deck = list(self.full_civil_deck)

    def build_military_deck(self):
        for card in self.military_card:
            num = 0
            if self.num_players == 2:
                num = card.num_2P
            elif self.num_players == 3:
                num = card.num_3P
            elif self.num_players == 4:
                num = card.num_4P
            if card.age == 'A':
                i = 0
                while num > i:
                    self.age_A_military_deck.append(card)
                    i += 1
            if card.age == 'I':
                i = 0
                while num > i:
                    self.age_I_military_deck.append(card)
                    i += 1
            if card.age == 'II':
                i = 0
                while num > i:
                    self.age_II_military_deck.append(card)
                    i += 1
            if card.age == 'III':
                i = 0
                while num > i:
                    self.age_III_military_deck.append(card)
                    i += 1
        #shuffle military decks
        shuffle(self.age_A_military_deck)
        self.age_A_military_deck = self.age_A_military_deck[:self.num_players+2]
        shuffle(self.age_A_military_deck)
        shuffle(self.age_I_military_deck)
        shuffle(self.age_II_military_deck)
        shuffle(self.age_III_military_deck)
        self.full_military_deck = self.age_A_military_deck + self.age_I_military_deck + self.age_II_military_deck + self.age_III_military_deck
        self.partial_military_deck = list(self.full_military_deck)


    def draw_civil_card(self):
        card_drawn = self.partial_civil_deck.pop(0)
        return card_drawn
    
    def discard_civil_card(self, index):
        if not self.card_row[index] == None:
            self.discarded_civil_cards.append(self.card_row.pop(index))
        else:
            self.card_row.pop(index)

    def draw_military_card(self):
        card_drawn = self.partial_military_deck.pop(0)
        return card_drawn

    def initialise_card_row(self):
        for i in range(13):
            card_drawn = self.draw_civil_card()
            self.card_row.append(card_drawn)
    
    def take_card(self, card_index):
        card_taken = self.card_row.pop(card_index)
        self.card_row.insert(card_index, None)
        return card_taken

    def replenish_card_row(self):
        for i in range(self.auto_discard):
            self.discard_civil_card(0)
        self.card_row = list(filter(lambda card: card != None, self.card_row))
        while len(self.card_row) < 13:
            new_card = self.draw_civil_card()
            self.card_row.append(new_card)

    def new_game(self):
        self.build_civil_deck()
        self.build_military_deck()
        self.initialise_card_row()


class Player():
    def __init__(self):
        self.military_hand = []
        self.civil_hand = []
        self.blue_cubes = 16
        self.yellow_bank = 18
        self.idle_workers = 1
        self.government = decks.Despotism
        self.CA = self.government.CA
        self.MA = self.government.MA
        self.happy_faces = 0
        self.rocks = 0
        self.food = 0
        self.science = 0
        self.culture = 0
        self.production = [decks.Agriculture, decks.Bronze]
        self.urban = [decks.Philosophy, decks.Religion]
        self.military_tech = [decks.Warriors]

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
                    print(f"Blue cube taken from {card.name}. {food_taken} food taken so far.")
        left_over = food_taken - food
        print(f"There is {left_over} food left over.")
        for card in reversed(self.production):
            if card.type == 'farm':
                while left_over >= card.prod:
                    card.blue_cubes += 1
                    self.food += card.prod
                    self.blue_cubes -= 1
                    left_over -= card.prod
                    print(f"Blue cube added to {card.name}. There is {left_over} food left to add")
        if left_over < 0:
            self.culture += left_over * 4
            print(f"Your people are starving! You lost {left_over * -4} culture points")

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
                    print(f"Blue cube taken from {card.name}. {rocks_taken} rocks taken so far.")
        left_over = rocks_taken - rocks
        print(f"There are {left_over} rocks left over.")
        for card in reversed(self.production):
            if card.type == 'mine':
                while left_over >= card.prod:
                    card.blue_cubes += 1
                    self.rocks += card.prod
                    self.blue_cubes -= 1
                    left_over -= card.prod
                    print(f"Blue cube added to {card.name}. There are {left_over} rocks left to add")
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

    #military cards discarded = number of military cards in hand minus number of MA
    #military cards drawn = left over MA after turn (max of 3)   
    def discard_military_cards(self, MA):
        while len(self.military_hand) > MA:
            cards_to_discard = len(self.military_hand) - MA
            print(f"You must discard {cards_to_discard} military cards. \nYour military cards are:")
            for index, card in enumerate(self.military_hand):
                print(f"{index+1}: {card.name}")
            proceed = False
            while proceed == False:
                try: 
                    discard_index = int(input("Which card would you like to discard?"))
                    if discard_index <= len(self.military_hand) and discard_index > 0:
                        proceed = True
                    else:
                        raise ValueError()
                except ValueError:
                    print("Please enter a valid number")
                    proceed = False
            decks.discarded_military_cards.append(self.military_hand.pop(discard_index-1))

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
            new_military_card = decks.draw_military_card()
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

class Game:
    def __init__(self):
        pass


players = int(input("How many players? "))
while players!= 2 and players!=3 and players!=4:
    players = int(input("Please select 2, 3 or 4 players: "))
print(f"There are {players} players\n")

'''for card in decks.card_row:
    print(card)
which_card = int(input("Which card do ya want? "))
card_taken = decks.take_card(which_card)
print("\nThe card you took is " + card_taken.name + "\n")

decks.replenish_card_row()
print("\nThe replenished card row is\n\n")
for card in decks.card_row:
    print(card)


player = Player()
player.draw_military_cards(1)
for card in player.military_hand:
    print(card.name)
'''