def cond_test(num):
    if num > 5:
        print(str(num) + ' is greater than 5')
    elif num == 5:
        print('%i is equals to 5' % num)
    else:
        print(str(num) + ' is less than 5')

cond_test(3)
cond_test(5)
cond_test(7)
