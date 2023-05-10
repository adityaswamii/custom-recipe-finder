import ast
import json
from pprint import pprint

# - - - - - - INITIAL VALUES - - - - - -


inputFile = open('dictionary.txt')
inputJSON = open('dictionary.json')
testFile = open('example.txt')

#  recipe = ast.literal_eval(inputFile.read())
recipe = json.loads(inputJSON.read())

# - - - - - - FUNCTIONS - - - - - -


def add_recipe():
    pass


def del_recipe():
    pass


def search_recipe():
    pass

# - - - - - - MAIN EVENT LOOP - - - - - -


def main():
    print(type(recipe))
    pprint(recipe['1'])


main()
