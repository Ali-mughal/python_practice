# def make_car(**car_info):
#     car_profile = {}
#     for key, value in car_info.items():
#         car_profile[key] = value
#     return car_profile

# print make_car(manufacturar='Honda',model='2012',color='blue',cc='1200 cc')

a = {'red': [2,3,4], 'blue': [6,7,8], 'green': [8,9,5]}
b = [5, 6, 8, 4, 3, 2, 1, 2, 4]

def get_dict(b,a):
    count = 0
    for i in b:
        if count==3:
            count=0
        if count==0:
            a['red'].append(i)
        if count==1:
            a['blue'].append(i)
        if count==2:
            a['green'].append(i)
        count +=1
    return a
res = get_dict(b,a)
    
print(res)        
        


c = {'red': [2,3,4,5,4], 'blue': [6,7,8,6,3], 'green': [8,9,5,8,2]}