

magicians = ['samri jadu gar','jav','palow']
great_magician = []

def make_great(mag_list):
    while mag_list:
        current_magician =  "Great " + mag_list.pop()
        great_magician.append(current_magician)
        print great_magician
    
make_great(magicians[:])
print magicians

# def show_magicians(name_magicians):
#     for name_magician in name_magicians:
#         print name_magician

# show_magicians(name_magicians)