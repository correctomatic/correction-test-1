import os
import time
import random
import json

CORRECTION_FILE = '/tmp/exercise'

def load_variables_from_file(file_path):
    variables = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and '=' in line:
                    variable, value = line.split('=')
                    variables[variable.strip()] = value.strip()
    except FileNotFoundError:
        pass
    return variables

def introduce_error(prob):
    if random.random() < prob:
        raise RuntimeError("Error introduced with probability {:.2f}".format(prob))

def delay_execution(delay):
    time.sleep(delay/1000)

response = {}

try:

    configuration = load_variables_from_file(CORRECTION_FILE)
    delay = int(configuration.get('DELAY', 0))
    error_probability = float(configuration.get('ERROR_PROBABILITY', 0))
    response_size = int(configuration.get('RESPONSE_SIZE', 0))

    introduce_error(error_probability)
    delay_execution(delay)
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
        f'DELAY: {delay}',
        f'ERROR_PROBABILITY: {error_probability}'
    ]
}

def complete_length(response, length):
    if length == 0: return response

    # 4 is the length of the comma, the space and the quotes for the
    # new element in the list
    EXTRA_CHARACTERS_FOR_ITEM = 4
    PADDING = (response_size - len(json.dumps(response)) - EXTRA_CHARACTERS_FOR_ITEM)
    new_response = dict(response)
    new_response['comments'].append('*'*PADDING)
    return new_response

completed_response = complete_length(response, response_size)
print(json.dumps(completed_response))
