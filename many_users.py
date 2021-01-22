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
    users1 = {
        'Zubair': {
            'first': 'Ali',
            'last': 'Raza',
            'location': 'Dubai'
        },
        'Hamza': {
            'first': 'Muhammad',
            'last': 'Mujtaba',
            'location': 'Pakistan'
        },
    }
    dic_list=[(k,v) for k,v in dict.items(users)]
    print("dic convert to dic",dic_list)
    for list in dic_list:
        print("outer list",list)
        for inlist in list:
            print("inner list",inlist)
    for user, names in users.items():
        full_name = names['first']+" "+names['last']
        location = names['location']
        print(full_name)
        print(location)
