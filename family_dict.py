# assignment is to iterate over this dictionary template to get this output:
# "Krista is my sister and is 42 years old"
 
my_family = {
    'sister': {
        'name': 'Krista',
        'age': 42
    },
    'mother': {
        'name': 'Cathie',
        'age': 70
    }
}


print(my_family['sister']['name'], "is my", next(iter(my_family)), "and is", str(my_family['sister']['age']), "years old")