class Restauarent():

    def __init__(self,name,type_name):
        self.restaurant_name = name
        self.cuisine_type = type_name
    
    def set_number_served(self,number_of_served):
        self.number_served = number_of_served
        total_served = self.number_served
        return total_served

    def describe_restaurant(self):
        restaurant_info = self.restaurant_name+ "Wonder full " + self.cuisine_type
        return restaurant_info.title()

    def restaurant_co(self):
        return 'restaurant is opened'
    
    def increment_number_served(self,increment_served):
        self.number_served += increment_served
        total_served = self.number_served
        return total_served 

    
class IceCreamStand(Restauarent,object):
    def __init__(self,name,type_name='ice_cream'):
        super(IceCreamStand,self).__init__(name,type_name)
        self.flavors = []

    def shows_flavors(self):
        print '\n We have following flavors available'
        for flavor in self.flavors:
            print "- " + flavor.title()
        

my_shop =  IceCreamStand('bhola cha wala')
my_shop.flavors = ['vanila', 'chocolate', 'black bary']
print my_shop.describe_restaurant()
print my_shop.shows_flavors()
