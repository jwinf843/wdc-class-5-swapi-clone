import django
django.setup()
from api.models import People, Planet

people = People.objects.all()

'''
def exercise_0(person):
    character = {
    'name' : person.name,
    'homeworld' : person.homeworld.name,
    'height' : person.height,
    'mass' : person.mass,
    }
    
    return character


result_0 = exercise_0(people[0])
print(result_0)

result_expected_0 = {
    'name': 'Luke',
    'homeworld': 'Tatooine',
    'height': '....',
    'mass': '...'
}

'''
"""
def exercise_1(people):
    results = []
    
    for person in people:
        char_dict = {
        'name' : person.name,
        'homeworld' : person.homeworld.name,
        'height' : person.height,
        'mass' : person.mass,
        }
        
        results.append(char_dict)
    
    return results
"""    

"""

    
result_1 = exercise_1(people)
print(result_1)

def exercise_2():
    # pending
    results = []


# Exercise 1
result_example = [{
    'name': 'Luke',
    'homeworld': 'Tatooine',
    'height': '....',
    'mass': '...'
}]

# Exercise 2
result_example = [{
    'name': 'Luke',
    'homeworld': {
        'id': 1,
        'name': 'Tatooine'
    },
    'height': '....',
    'mass': '...'
}]

"""
data = {
 "name": "Santiago",
 "homeworld" : "Tatooine",
 "height" : 185,
 "mass" : 96,
}
'''
try:
    planet = Planet.objects.get(name=data["homeworld"])        
    result = People.objects.create(name = data["name"], homeworld = planet, height = data["height"], mass= data["mass"])
    print('It actually worked')
    
except Planet.DoesNotExist:
    print('you are a failure')
'''
    
if Planet.objects.filter(name=data['homeworld']).count() != 1:
    print('You are a failure')
else:
    result = People.objects.create(name = data["name"], homeworld = planet, height = data["height"], mass= data["mass"])
