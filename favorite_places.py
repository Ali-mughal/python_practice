if __name__ == '__main__':
    cities = { 'Dubai':{'UAE','200','tourit city'},
               'lahore': {'Pakista','500','historical City'},
               'Dilhi': {'India','1000','Capital of India'}
    }
    for city,city_infos in cities.items():
        print(city,' Info:')
        for city_info in city_infos:
            print("\t",city_info)

















    # favorite_places = {
    # 'Ali':{'Dubai','Sharjah','Abu Dhabi'},
    # 'Raza':{'Pakistan','Islamabad','Lahore'}
    # }
    # print(favorite_places)
    # for name,places in favorite_places.items():
    #     print(name,"Have following favorite places")
    #     for place in places:
    #         print('\t',place)
