if __name__ == '__main__':
    pizza={
        'crust': 'thick',
        'toppings':['mashrooms','extra cheese']
    }
    print('you ordered a '+pizza['crust']+'-crust pizza with following toppings:')
    for topping in pizza['toppings']:
        print('\t',topping)


#     You ordered a thick-crust pizza with the following toppings:
# mushrooms
    # extra cheese