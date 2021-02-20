'''
This module organises navigation in json file
'''
import json
import pprint
import sys

def reading(path: str) -> dict:
    '''
    Reads json file and returns its content
    If path is not str returns None
    >>> reading(1)

    '''
    if not isinstance(path, str):
        return None
    file = open (path, 'r', encoding='UTF-8')
    data = json.load(file)
    return data


def navigating (data):
    '''
    Organises all navigation
    '''
    if isinstance (data, list):
        while True:
            print('On this stage you can choose number from 1 to', len(data), '(it will naviget you\
 to it)')
            print('One more option - print curent element (type print)')
            print('You also can return to parent element (type parent)')
            print('If you want to kill the program type exit.')
            answer = input()
            if answer == 'exit':
                sys.exit()
            elif answer == 'print':
                pprint.pprint(data)
                print('Maybe now you want to choose?')

            elif answer == 'parent':
                return 'parent'

            elif answer in list(map(str, list(range(1, len(data) + 1)))):
                navigating(data[int(answer) - 1])
            else:
                print('Incorrect input, try again')

    elif isinstance (data, dict):
        while True:
            print('On this stage you can choose key from given (it will navigate you to its value)')
            print('Available keys:')

            for key in data:
                print(key)

            print('One more option - print curent element (type print)')
            print('you also can return to parent element (type parent)')
            print('If you want to kill the program type exit.')
            answer = input()
            if answer == 'exit':
                sys.exit()
            elif answer == 'print':
                pprint.pprint(data)
                print('Maybe now you want to choose?')

            elif answer == 'parent':
                return 'parent'

            elif answer in data:
                navigating(data[answer])
            else:
                print('Incorrect input, try again')
    else:
        while True:
            print('On this stage you can print curent element (type print)')
            print('You also can return to parent element (type parent)')
            print('If you want to kill the program type exit.')
            answer = input()
            if answer == 'exit':
                sys.exit()
            elif answer == 'print':
                pprint.pprint(data)

            elif answer == 'parent':
                return 'parent'

            else:
                print('Incorrect input, try again')



if __name__ == '__main__':
    to_read = input('Enter a path to json in which you want to realize navigation: ')
    encoded_json = reading(to_read)
    print('Now we are ready to navigate you through json!')
    while True:
        if navigating(encoded_json) == 'parent':
            print('You have reached the document root already. Choose something else.')
