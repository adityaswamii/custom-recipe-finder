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

inputJSON = open('dictionary.json')  # reads JSON data from source file
recipe = json.loads(inputJSON.read())  # decodes JSON to dictionary

# - - - - - - FUNCTIONS - - - - - -


def print_recipe(n):  # print a specified recipe
    n = str(n)
    print('\nHere\'s a recipe we found for', recipe[n]['name'])
    print('Tags:', recipe[n]['tags'])
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


def search_recipe():  # inputs parameter and search value from user to check and return valid recipes from dictionary
    search_parameters = ['name', 'time', 'ingredients', 'tags']
    print('Search for recipes based on the following parameters', search_parameters)
    k = input('Enter search parameter: ').lower()
    while k not in search_parameters:
        print('Incorrect search parameter')
        k = input('Enter search parameter: ')
    sv = input('Enter search value: ')
    
    c = 0
    for n in recipe.keys():
        if check_recipe(n, k, sv):
            print_recipe(n)
            c += 1
    if c == 0:
        print('\nSorry, we don\'t have any recipes that match your search criteria :(')
        print('Add some recipes of your own by typing /add\n')
        return
    else:
        print('\n\nLooks good!\nWe found', c, 'recipe(s) that match your search criteria\n')


def add_recipe():  # inputs all parameter values and adds recipe to dictionary
    av_name = input('Enter recipe name. If you don\'t want to add a recipe right now, type /back\n')
    if av_name == '/back' or av_name == '':
        return
    
    av_ingredients = input('Enter list of ingredients separated by commas and a space. Avoid mentioning quantities. (eg. milk, flour, eggs, sugar) \n')
    av_ingredients = list(av_ingredients.split(', '))
    
    av_time = input('Enter total cooking time in minutes. (eg. if a dish takes 20 minutes to prepare, only type the number 20) \n')
    
    av_tags = input('Enter a few tags separated by commas and a space. This will help identify your recipe when searching for it. (eg. noodles, Chinese, spicy) \n')
    av_tags = list(av_tags.split(', '))
    
    av_instructions = input('Lastly, enter the cooking instructions. Feel free to be as detailed as you want! \n')
    
    av_dict = {
        'name': str(av_name),
        'ingredients': list(av_ingredients),
        'time': int(av_time),
        'tags': list(av_tags),
        'instructions': str(av_instructions)
    }
    
    av = 1
    while str(av) in recipe:
        av += 1
    
    recipe.update({str(av): av_dict})
    print('\nYour recipe has been added to our collection. Try searching for it!')
    

def delete_recipe():  # deletes a specified recipe from the dictionary
    dv = input('Enter the name of the recipe you would like to remove: ')
    for n in recipe.keys():
        if check_recipe(n, 'name', dv):
            print('The recipe for', recipe.pop(n)['name'], 'was successfully deleted')
            return
    print('Could not find the recipe you were looking for')
    

# - - - - - - MAIN PROGRAM LOOP - - - - - -


def main():
    print('\nWelcome to RecipEasy - a program that lets you find the perfect recipe for you at any time\n')
    print('Enter a command to get started \nType /help to see the list of valid commands')
    while True:
        command = input('\n_')
        if command == '/exit':
            data = json.dumps(recipe)  # when exiting program, convert dictionary to JSON data
            with open("dictionary.json", 'w') as d:
                d.write(data)  # store data in a JSON file outside the program to ensure recipes are saved
            print('\nThank you for trying out RecipEasy :)')
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
