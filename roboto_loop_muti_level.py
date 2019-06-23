import random
import time


from actors import Hacker, Creature, Pawns, FBI, FBIsnitch, Pawnscum, RightHand


def main():
    print_headera()
    game_loopa()
    print_headerb()
    game_loopb()


def print_headera():
    print('---------------------------------------')
    print('          MR.ROBOTO & LE Smith')
    print('---------------------------------------')
    print()
    print("     Today I met you, Yes, you!!!!!!!!! "
          "I finally have a friend to talk to. You "
          "remind me of someone. I just cant put my"
          " finger on it yet.")
    print()


def game_loopa():
    creatures = [
        Pawns(' THe LOw level Security', 4),
        Creature('Sharleen', 30),
        Pawns('The whITE-ARmy', 6),
        FBI('FBI', 18, 25, True),
        Hacker('BLACK Violet', 404)
    ]

    hero = Hacker('LE', 187)

    while True:

        active_creature = random.choice(creatures)
        print('{} of cmd stats {} creeps from the silicon of the DarkWeb!!!'
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [Hack]Attack, MR[roboto], or Reading[white papers]? ')
        if cmd == 'Hack':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("LE Hacks time, reset his own history.............")
                time.sleep(5)
                print("LE Flashes back into existence!")
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
            print("MR.Roboto has destructed HELLcORP!!! We never Forget, We know no limits, We will find you. "
                  " Game over Clowns!!!")
            print()
            print()
            print()
            print()
            print("Bonsoir LE, hope to catch up with you next level!!!!!!!!!!!!!!!!!!!!!!")
            break

        print()


def print_headerb():
    print('--------------------------------------------------')
    print('          MR.ROBOTO & LEs tide of change!!!')
    print('--------------------------------------------------')
    print()
    print("    I just Don't trust anything you might have to say."
          "You Don't exist. The world is not able to deal with the"
          "aftermath of 9/5. I just let everyone die for nothing."
          "I have to Stop Black Violet And THe whITE-ARmy........")
    print()


def game_loopb():
    creatures = [
        Pawns(' THe LOw level Security', 4),
        Creature('SHa', 5),
        Creature('Sharleen', 30),
        Pawns('The whITE-ARmy', 6),
        FBI('FBI', 18, 25, True),
        FBIsnitch('Nesto', 4, 12, False),
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
                print("LEs vision comes into focus............")
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
