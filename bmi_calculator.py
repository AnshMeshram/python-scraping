print('\t\t\t BMI Calculator')
print('\t\t\t By Abdinasir Hussein')
print('\n Hello, this is a BMI Calculator!')

input('Do you wish to enter metric units or imperial units: ')

while input == 'metric':
    height = float(input('Please enter your height input meters(decimals): '))
    weight = int(input('Please enter your weight input kg: '))
    bmi = weight/(height*height)

    if bmi <= 18.5:
        print('Your BMI is', bmi,'which means you are underweight.')

    elif bmi > 18.5 and bmi < 25:
        print('Your BMI is', bmi,'which means you are normal.')

    elif bmi > 25 and bmi < 30:
        print('your BMI is', bmi,'overweight.')

    elif bmi > 30:
        print('Your BMI is', bmi,'which means you are obese.')

    else:
        print('There is an error with your input')
        print('Please check you have entered whole numbers\n'
              'and decimals were asked.')

while input == 'imperial':
    height = int(input('Please enter your height input inputches(whole number): '))
    weight = int(input('Please enter your weight input pounds(whole number): '))
    bmi = (weight*703)/(height*height)

    if bmi <= 18.5:
        print('Your BMI is', bmi,'which means you are underweight.')

    elif bmi > 18.5 and bmi < 25:
        print('Your BMI is', bmi,'which means you are normal.')

    elif bmi > 25 and bmi < 30:
        print('Your BMI is', bmi,'which means you are overweight')

    elif bmi > 30:
        print('Your BMI is', bmi,'which means you are obese.')

    else:
        print('There is an error with your input')
        print('Please check you have entered whole numbers\n'
              'and decimals were asked.')

input('\n\nPlease press enter to exit.')
I've now changed it, but how do I go about editing this block:

input = input('Do you wish to enter metric units or imperial units: ')

if input == 'metric':
    height = float(input('Please enter your height input meters(decimals): '))
    weight = int(input('Please enter your weight input kg: '))
    bmi = weight/(height*height)

    if bmi <= 18.5:
        print('Your BMI is', bmi,'which means you are underweight.')

    elif bmi > 18.5 and bmi < 25:
        print('Your BMI is', bmi,'which means you are normal.')

    elif bmi > 25 and bmi < 30:
        print('your BMI is', bmi,'overweight.')

    elif bmi > 30:
        print('Your BMI is', bmi,'which means you are obese.')

    else:
        print('There is an error with you inputput')
        print('Please check you have entered whole numbers\n'
              'and decimals where asked.')
