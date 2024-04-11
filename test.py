import os
import time
import random
import json

DELAY = int(os.getenv('DELAY', 0))
ERROR_PROBABILITY = float(os.getenv('ERROR_PROBABILITY', 0))
RESPONSE_SIZE = int(os.getenv('RESPONSE_SIZE', 0))

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

def complete_length(response, length):
    if length == 0: return response

    # 4 is the length of the comma, the space and the quotes for the
    # new element in the list
    EXTRA_CHARACTERS_FOR_ITEM = 4
    PADDING = (RESPONSE_SIZE - len(json.dumps(response)) - EXTRA_CHARACTERS_FOR_ITEM)
    new_response = dict(response)
    new_response['comments'].append('*'*PADDING)
    return new_response

completed_response = complete_length(response, RESPONSE_SIZE)
print(json.dumps(completed_response))
