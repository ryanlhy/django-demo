# services.py
import requests
import re


def remove_special_characters(string):
    # Regular expression pattern to match special characters
    pattern = '[^a-zA-Z0-9\s]+'
    # Replace special characters with a space
    return re.sub(pattern, ' ', string)

def extract_text(string):
    items = string.split()
    # print(items)
    new_string = [item for item in items if not item.isdigit()]
    return new_string if new_string else None 

def extract_numbers(string):
    # Split the string into a list of words
    words = string.split()
    # Filter the list to return only the numbers
    numbers = [word for word in words if word.isdigit()]
    return numbers if numbers else None

def convert_params(key, list):
    list = [str(x) for x in list]
    modified_list = []
    for i, val in enumerate(list):
        if i == len(list) - 1:
            modified_list.append(f'{key}:"*{val}*"')
        else:
            modified_list.append(f'{key}:"*{val}*" OR ')
    string = ''.join(modified_list)
    return f'({string})'

def build_query_string(param_text, param_numbers):
    query_string = ""
    if param_text is not None:
        query_string = f'({convert_params("name", param_text)} OR {convert_params("set.name", param_text)}) '
    if param_numbers is not None:
        query_string += f'({convert_params("number", param_numbers)} OR {convert_params("set.printedTotal", param_numbers)})'
    return query_string

def get_data_from_api(param):
    param = remove_special_characters(param)
    # split param in strings, and numbers
    param_text = extract_text(param)
    param_numbers = extract_numbers(param)
    query_string = build_query_string(param_text, param_numbers)

    # url = f"https://api.pokemontcg.io/v2/cards?q=set.id:{set_name}&page=1&pageSize=10"
    # url = f'https://api.pokemontcg.io/v2/cards?q=name:"*{param}*"&page=1&pageSize=10'
    url_new = f'https://api.pokemontcg.io/v2/cards?q={query_string}&page=1&pageSize=10'
    # print(url_new)
    response = requests.get(url_new)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("API request failed with status code: ", response.status_code)


