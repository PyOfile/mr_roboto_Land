import random
import time


from actors import Hacker, Creature, Pawns, FBI, FBIsnitch, Pawnscum, RightHand


def main():
    print_header()
    game_loop()


def print_header():
    print('--------------------------------------------------')
    print('          MR.ROBOTO & LEs tide of change!!!')
    print('--------------------------------------------------')
    print()
    print("    I just Don't trust anything you might have to say."
          "You Dont exist. The world is not able to deal with the"
          "aftermath of 9/5. I just let everyone die for nothing."
          "I have to Stop Black Violet And THe whITE-ARmy........")
    print()


def game_loop():
    creatures = [
        Pawns(' THe LOw level Security', 4),
        Creature('SHa', 5),
        Creature('Sharleen', 30),
        Pawns('The whITE-ARmy', 6),
        FBI('FBI', 18, 25, True),
        FBIsnitch('Nesto', 4, 12, True),
        Pawnscum('SoulTravler', 16, 20, True),
        RightHand('Cannavale', 20, 40, True),
        Hacker('BLACK Violet', 408),
        Hacker('Rell', 205)
    ]

    hero = Hacker('LE', 300)

    while True:

        active_creature = random.choice(creatures)
        print('{} of Terminal stats {} pulls into focus out of the !!!'
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [Hack]Attack, MR[roboto], or Reading[white papers]? ')
        if cmd == 'Hack':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("LEs vision coms into focus............")
                time.sleep(12)
                print("a moment of clarity!")
        elif cmd == 'roboto':
            print('Mr.Roboto takes control of LE !!!')
        elif cmd == 'white papers':
            print('I {} Time to do some research!!!:'
                  .format(hero.name))
            for c in creatures:
                print(' * {} of level {}'.format(c.name, c.level))
        else:
            print('YOu have Beeeeeeeeeeeen owned............... Late!!')
            break

        if not creatures:
            print("'LE,'No matter what I do, Black Violet Seems to be ahead, as if for seen..... "
                  " What will come of us!!!")
            print()
            print()
            print()
            print()
            print("How Will this un-rap next!!!!!!!!!!!!!!!!!!!!!!")
            break

        print()


if __name__ == '__main__':
    main()
