def celcius_to_fahrenheit(celcius = 0):
    celcius = float(celcius)

    if celcius < -273.15:
        result = 'The temeperature you have specified is too low to be true'
    else:
        with open('temps.txt', 'a+') as handler:
            handler.write(str(round(celcius*1.8 + 32, 2)) + '\n')
            handler.close()

    # return result

temperatures = [10,-20,-289,100]

# empty temps file
with open('temps.txt', 'w') as handler:
    handler.close()

for item in temperatures:
    celcius_to_fahrenheit(item)
    # print(celcius_to_fahrenheit(item))

# money={"saving_account":200, "checking_account":100, "under_bed":[500,10,100]}
# print(money['under_bed'][1]);
