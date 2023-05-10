import ast
import json
from pprint import pprint

# - - - - - - INITIAL VALUES - - - - - -


inputFile = open('dictionary.txt')
testFile = open('example.txt')

recipe = ast.literal_eval(inputFile.read())


data = json.dumps(recipe)
with open('dictionary.json', 'w') as dictionary:
    dictionary.write(data)

# - - - - - - FUNCTIONS - - - - - -


def add_recipe():
    pass


def del_recipe():
    pass


def search_recipe():
    pass

# - - - - - - MAIN EVENT LOOP - - - - - -


def main():
    pprint(recipe[1])
    print(type(recipe))


main()
