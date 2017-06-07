import random, string

def get_random_character(seq):
    return random.choice(str(seq))

lowercase_letters = string.ascii_lowercase
vowels_list = ['e', 'y', 'u', 'i', 'o', 'a']
vowels = ''.join(vowels_list)
consonants = ''.join([l for l in lowercase_letters if l not in vowels_list])

user_input = []
allowed_input = ('c', 'v', 'a')

for i in range(3):
    _input = None

    while (not _input):
        _input = input("Enter 'v' for vowel, 'c' for consonant, and 'a' for any letter: ")

        if (_input in allowed_input):
            user_input.append(_input)
        else:
            _input = None
            print('Invalid entry, please repeat again!')

result = ''

for char_type in user_input:
    if (char_type == 'c'):
        result += get_random_character(consonants)
    elif (char_type == 'v'):
        result += get_random_character(vowels)
    else:
        result += get_random_character(lowercase_letters)

print(result)

# print(get_random_character('asfhfalkhdsafhqprnvljxch'))
