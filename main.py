import json
import random

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


def print_recipe(n):  # print a specified recipe
    n = str(n)
    print('\nHere\'s a recipe we found for', recipe[n]['name'])
    print('Cooking Time: ', recipe[n]['time'], 'minutes')
    print('Ingredient List: ', recipe[n]['ingredients'])
    print('Cooking Instructions: \n', recipe[n]['instructions'])


def check_recipe(n, k, sv) -> bool:  # check if a search value exists in a given parameter of a specified recipe
    n = str(n)
    if k == 'name':
        return recipe[n][k].lower() == sv.lower()
    elif k == 'ingredients' or k == 'tags':
        return sv.lower() in (i.lower() for i in recipe[n][k])
    elif k == 'time':
        sv = int(sv)
        return recipe[n][k] <= sv
    else:
        print('invalid check parameter in', n, k, sv)
        return False


def search_recipe():
    search_parameters = ['name', 'time', 'ingredients', 'tags']
    print('Search for recipes based on the following parameters', search_parameters)
    k = input('Enter search parameter: ')
    while k.lower() not in search_parameters:
        print('Incorrect search parameter')
        k = input('Enter search parameter: ')
    sv = input('Enter search value: ')
    
    c = 0
    for n in recipe.keys():
        if check_recipe(n, k, sv):
            print_recipe(n)
            c += 1
    if c == 0:
        print('Sorry, we don\'t have any recipes that match your search criteria :(')
        print('Add some recipes of your own by typing /add\n')
        return


def add_recipe():
    pass


def delete_recipe():
    pass

# - - - - - - MAIN EVENT LOOP - - - - - -


def main():
    input_commands = ['/exit', '/search', '/add', '/delete', '/all', '/random', '/help']
    print('\nWelcome to Custom Recipe Finder - a program that lets you find the perfect recipe for you at any time\n')
    print('Enter a command to get started! \nType /help to see the list of valid commands')
    command = ""
    while True:
        command = input('\n_')
        if command == '/exit':
            print('\nThank you for trying out Custom Recipe Finder!')
            return
        elif command == '/help':
            print('Here is the list of valid commands:')
            print('/exit --> Exits the program')
            print('/search --> Search for a suitable recipe from our collection')
            print('/add --> Add your own custom recipe to our collection')
            print('/delete --> Remove a recipe from our collection')
            print('/all --> Prints our entire collection of recipes')
            print('/random --> Picks a random recipe to show you')
            print('/help --> Shows list of valid commands\n')
        elif command == '/search':
            search_recipe()
        elif command == '/add':
            add_recipe()
        elif command == '/delete':
            delete_recipe()
        elif command == '/all':
            for n in recipe.keys():
                print_recipe(n)
        elif command == '/random':
            r = random.choice(list(recipe.keys()))
            print_recipe(r)
        else:
            print('Please enter a valid command')


main()
