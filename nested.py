# 1 Update Values in Dictionaries and Lists

# 1.1 Change the value
x = [ [5,2,3], [10,8,9] ]
x[1][0] = 15
print(x)

# 1.2 Change the last_name
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)

# 1.3 Sports_directory
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# 1.4 Change the value
z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print(z)

# 2 Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary(students):
    for i in range(len(students)):
        print("first_name - "+students[i]['first_name']+",last_name -" +students[i]['last_name'])
iterateDictionary(students)

# 3 Get Values From a list of dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary2(key_name,some_lists):
    for i in range(len(some_lists)):
        print(some_lists[i][key_name])
iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

# 4 Iterate Through a Dictionary w/ List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def print_info(some_dict):
    print(some_dict)
    for key,val in some_dict.items():
        print("")
        print(f"{len(val)} {key.upper()}")
        for i in range(0, len(val)):
            print(val[i])

print_info(dojo)


# output:
# 7 LOCATIONS
# San
# Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
#
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

