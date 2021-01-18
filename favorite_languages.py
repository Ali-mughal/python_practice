if __name__ == '__main__':
    favorite_languages = {
        'ali':['python', 'javascript'],
        'mujtaba':['python','c++'],
        'umer':['html']
    }
    for name,languages in favorite_languages.items():
        if len(languages)==1:
            print(name.title(),"'s favorite language is:")
            for language in languages:
                print("\t",language.title())
        elif len(languages)>=2:
            print(name.title()+"'s favorite languages are:")
            for language in languages:
                print("\t"+ language)

