import json
from pprint import pprint

# - - - - - - INITIAL VALUES - - - - - -


#   #  INPUT THE DICTIONARY FROM dictionary.txt AS A STRING
#   inputFile = open('dictionary.txt')
#   #  USE ast.literal_eval() TO CONVERT THE STRING INPUT TO A DICTIONARY AND STORE THE DICTIONARY IN recipe
#   recipe = ast.literal_eval(inputFile.read())
#   #  WRITE THE DICTIONARY IN recipe TO A JSON FILE
#   data = json.dumps(recipe)
#   with open("dictionary.json", 'w') as d:
#     d.write(data)

inputJSON = open('dictionary.json')
recipe = json.loads(inputJSON.read())

# - - - - - - FUNCTIONS - - - - - -


def print_recipe(n: str):
    print('\nHere\'s a recipe we found for', recipe[n]['name'])
    print('Cooking Time: ', recipe[n]['time'], 'minutes')
    print('Ingredient List: ', recipe[n]['ingredients'])
    print('Cooking Instructions: \n', recipe[n]['instructions'])


def print_recipe(n: int):
    n = str(n)
    print('\nHere\'s a recipe we found for', recipe[n]['name'])
    print('Cooking Time: ', recipe[n]['time'], 'minutes')
    print('Ingredient List: ', recipe[n]['ingredients'])
    print('Cooking Instructions: \n', recipe[n]['instructions'])


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
    print_recipe('3')


main()
