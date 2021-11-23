first_number = raw_input('please enter the First number')
second_number = raw_input('please enter the second number')
print first_number


try:
    res  = int(first_number) + int(second_number)
except ValueError:
    print 'Please enter the valid amount'
else:
    print res