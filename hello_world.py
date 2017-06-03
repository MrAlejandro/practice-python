# age = input('How old are you? ')
# new_age = int(age) + 18
# print(new_age)

# print(type('string'))
# print(type(2))
# print(type(2.3))

# _int = int('123')
# _float = float('123.4')

# print(_int)
# print(_float)
# print(int(_float))
# print(_int + _float);


# string = 'string'
# print(dir(string)) # lists all string methods

# print(string.upper())

# print(help(''.count)) # shows an information about a method


# string characters access
# string = "Hello world!"

# print(string[0])
# print(string[11])

# print(string[-1])
# print(string[-2])

# print(string[0:2])
# print(string[:2]) # the same as the previous one
# print(string[6:])

# print(string[-3:-1])
# print(string[-3:])


# _list = [1, 1.2, 'Hello']
# print(type(_list))
# print(_list[2])
# print(_list[1:])
# print(type(_list[1:]))

# print(dir(list))


# tuples are immutable lists
# _tuple = (1, 1.2, 'Hello')
# print(_tuple[2])
# print(_tuple[:1])


# dictionary
# d = {
#     'name': 'Alex',
#     'surname': 'Test',
#     'languages': ['PHP', 'JavaScript', 'Python'],
# }

# print(d)
# print(d['languages'][2])


def sum_up_two_numbers(num1, num2):
    _sum = num1 + num2
    return _sum

print(sum_up_two_numbers(18, 7));
