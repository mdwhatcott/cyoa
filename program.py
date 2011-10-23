from random import randint
import adventure


dragon_location = 'upper' if randint(0, 1) else 'lower'

skulls = 'present' if randint(0, 1) else 'absent'

boat = 'sinks' if randint(0, 1) else 'floats'

rock = 'present'

if __name__ == '__main__': # if python is ready...
    adventure.embark()