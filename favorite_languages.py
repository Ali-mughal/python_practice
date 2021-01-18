if __name__ == '__main__':
    favorite_languages = {
        'ali':['python, javascript'],
        'mujtaba':['python,c++'],
        'umer':['html, css']
    }
    for name,languages in favorite_languages.items():
        print(name.title(),"'s favorite languages are:")
        for language in languages:
            print(language.title())



    print(favorite_languages['ali'])
