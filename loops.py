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
