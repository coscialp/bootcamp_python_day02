import time
import os
from random import randint


def log(function):

    def logger_function(*param, **param2):
        file = open('machine.log', "a")
        file.write('({})Running: '.format(os.environ.get('USER')))
        name = function.__name__
        name = name.replace('_', ' ')
        file.write("{:20}".format(name.title()))
        t1 = time.time()
        ret = function(*param, **param2)
        t2 = time.time()
        final_time = t2 - t1
        units = 's'
        if final_time < 1:
            final_time *= 1000
            units = 'ms'
        file.write('[ exec-time = {:.3f} {:2} ]'.format(final_time, units))
        file.write('\n')
        file.close()
        return ret

    return logger_function


class CoffeeMachine:

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
