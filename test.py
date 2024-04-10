import os
import time
import random
import json

DELAY = int(os.getenv('DELAY', 0))
ERROR_PROBABILITY = float(os.getenv('ERROR_PROBABILITY', 0))

def introduce_error(prob):
    if random.random() < prob:
        raise RuntimeError("Error introduced with probability {:.2f}".format(prob))

def delay_execution(delay):
    time.sleep(delay/1000)

response = {}

try:
    introduce_error(ERROR_PROBABILITY)
    delay_execution(DELAY)
except RuntimeError as e:
    response = {
        'success': False,
        'error': str(e)
    }
    print(json.dumps(response))
    exit(1)

response = {
    'success': True,
    'grade': 100,
    'comments': [
        f'DELAY: {DELAY}',
        f'ERROR_PROBABILITY: {ERROR_PROBABILITY}'
    ]
}

print(json.dumps(response))
