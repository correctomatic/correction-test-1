import time
import random
import string
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
    response_type = configuration.get('RESPONSE_TYPE', 'json')

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

def generate_random_text(num_lines = random.randint(0, 10), line_length = random.randint(2, 50)):
    random_text = []
    for _ in range(num_lines):
        line = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation + ' ', k=line_length))
        random_text.append(line)
    return '\n'.join(random_text)

def generate_response_with_separators(json_text):
    START_SEPARATOR = '-----BEGIN CORRECTOMATIC RESPONSE-----'
    END_SEPARATOR = '-----END CORRECTOMATIC RESPONSE-----'

    response = [ generate_random_text() ]
    response.append(START_SEPARATOR)
    response.append(json_text)
    response.append(END_SEPARATOR)
    response.append(generate_random_text())

    return '\n'.join(response)

def generate_response_text(response, type='json'):
    json_text = json.dumps(response)
    if type == 'json':
        return json_text
    else:
        return generate_response_with_separators(json_text)


completed_response = complete_length(response, response_size)
print(generate_response_text(completed_response, response_type))
