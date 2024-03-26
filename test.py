import os
import time
import random

DELAY = int(os.getenv('DELAY', 0))
ERROR_PROBABILITY = float(os.getenv('ERROR_PROBABILITY', 0))

def introduce_error(prob):
    if random.random() < prob:
        raise RuntimeError("Error introduced with probability {:.2f}".format(prob))

def delay_execution(delay):
    time.sleep(delay/1000)

introduce_error(ERROR_PROBABILITY)
delay_execution(DELAY)

print(f'DELAY: {DELAY}')
print(f'ERROR_PROBABILITY: {ERROR_PROBABILITY}')
print('Hello, World!')
