if __name__=='__main__':
    users = {
        'mali':{
            'first':'Ali',
            'last': 'Raza',
            'location': 'Dubai'
        },
        'M Mujtaba':{
            'first':'Muhammad',
            'last':'Mujtaba',
            'location':'Pakistan'
        },
    }
    for user, names in users.items():
        print("user name \n"+user)
        full_name = names['first']+" "+names['last']
        location = names['location']
        print(full_name)
        print(location)