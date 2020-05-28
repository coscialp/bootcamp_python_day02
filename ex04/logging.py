import time
import os


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
