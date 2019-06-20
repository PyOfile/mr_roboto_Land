import random


class Creature:
    def __init__(self, name: object, the_level: object) -> object:
        self.name = name
        self.level = the_level

    def __repr__(self):
        return '{} of cmd level {}'.format(
            self.name, self.level
        )

    def get_defensive_roll(self):
        return random.randint(1, 24) * self.level


class Hacker(Creature):

    def attack(self, creature):
        print("The CMD jockey {} SQL injects {}!".format(
            self.name, creature.name
        ))

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print("You reverse Shell {}...".format(my_roll))
        print("{} SCRIPS {}...".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("LE poisons the base code of {}!!!!!".format(creature.name))
            return True
        else:
            print("LE is in mental brake down!!!!!!")
            return False


class Pawns(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 3
    
# new actor for the new level    
    
class Pawnscum(Creature):
    def __init__(self, name, level, backstab, deception):
        super().__init__(name, level)
        self.backstab = backstab
        self.deception = deception
    
    def get_defensive_roll(self):
            base_roll = super().get_defensive_roll()
            stab_modifier = 7 if self.backstab else 3
            decept_modifier = 9 if self.deception else 3
            
            return base_roll * stab_modifier * decept_modifier


class FBI(Creature):
    def __init__(self, name, level, antivirus, fire_wall):
        super().__init__(name, level)
        self.fire_wall = fire_wall
        self.antivirus = antivirus

    def get_defensive_roll(self):
            base_roll = super().get_defensive_roll()
            fire_modifier = 5 if self.fire_wall else 1
            anti_modifier = self.antivirus / 6

            return base_roll * fire_modifier * anti_modifier
        
 # new actors for the new level          
        
class FBI_snitch(Creature):
    def __init__(self, name, level, fire_wall, blackmail):
        super().__init__(name, level)
        self.fire_wall = fire_wall
        self.blackmail = blackmail

    def get_defensive_roll(self):
            base_roll = super().get_defensive_roll()
            fire_modifier = 5 if self.fire_wall else 1
            black_modifier = self.blackmail / 12

            return base_roll * fire_modifier * black_modifier
        
class RightHand(Creature):
    def __init__(self, name, level, problem_solve, axe_man):
        super().__init__(name, level)
        self.problem_solve = problem_solve
        self.axe_man = axe_man

    def get_defensive_roll(self):
            base_roll = super().get_defensive_roll()
            solve_modifier = 4 if self.problem_solve else 1
            axe_modifier = self.axe_man / 24

            return base_roll * solve_modifier * axe_modifier
