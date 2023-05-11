import json

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
    k = input('Enter search parameter: ')
    sv = input('Enter search value: ')
    for n in recipe.keys():
        if check_recipe(n, k, sv):
            print_recipe(n)


def add_recipe():
    pass


def del_recipe():
    pass

# - - - - - - MAIN EVENT LOOP - - - - - -


def main():
    print(type(recipe['3']['time']))
    print_recipe(3)
    print(list(recipe['3'].values()))
    print(check_recipe(3, 'ingredient', 'Broccoli'))
    search_recipe()


main()
