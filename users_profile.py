
def build_profile(first_name,last_name,**user_info):
    profile = {}
    profile['first_name'] = first_name
    profile['last_name'] = last_name

    for key,value in user_info.items():
        profile[key] = value
    return profile

print build_profile('ali','raza',location = 'pakistan')






