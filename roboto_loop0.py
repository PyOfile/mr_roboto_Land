import random
import time


from actors import Hacker, Creature, Pawns, FBI


def main():
    print_header()
    game_loop()


def print_header():
    print('---------------------------------------')
    print('          MR.ROBOTO & LE Smith')
    print('---------------------------------------')
    print()
    print("     Today I met you, Yes, you!!!!!!!!! "
          "I finally have a friend to talk to. You "
          "remind me of someone. I just cant put my"
          " finger on it yet.")
    print()


def game_loop():
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


if __name__ == '__main__':
    main()
