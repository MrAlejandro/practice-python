emails = ['1@gmail.com', '2@yahoo.com', '3@gmail.com'];

for email in emails:
    if 'gmail' in email:
        print(email)


# entry = ''

# while entry != 'test':
#     entry = input('Enter the "test" word: ')

#     if entry == 'test':
#         print('Success')


names = ['alex', 'nat', 'lisa', 'igor']
domains = ['gmail', 'hotmail', 'yahoo', 'mail']

for i,j in zip(names, domains):
    print('%s@%s.com' % (i, j))

first = ['facebook.com', 'gmail.com', 'yelp.com']
second = ['yelp.com', 'yahoo.com', 'newyork.com']

for item in second:
    if not any(website in item for website in first):
        print(item)

