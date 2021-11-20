# import print_model
# import print_model as pd
# from print_model import profile
# from print_model import profile as p
# from print_model import *
print('Please enter the two number: I will divide them')
print('please enter the q to quite')
while True:
    try:
        first_number = float(input('Please enter the first number'))
        if first_number == 'q':
            break
        second_number = float(input('Please enter the second number'))
        if first_number:
            try:
                result = float(first_number/second_number)
            except:
                print('enter the valid number')
            else:
                print(result)
    except:
        print('invalid input')
    



name = profile('11','Ali')

print name[1]