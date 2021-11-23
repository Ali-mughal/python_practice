
flag = True
result = {}

while flag:
    name = input('\n What is your Name:')

    place = input('\n Which Place do you want to visit in the world:')    
    result[name] = place
    
    repeat = input('Do you want to continue yes/no')
    if repeat == 'no':
        flag = False
print (result)
for key,value in result.items():
    print(key,':Favroite',value)   

    

