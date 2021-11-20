class Car():
    def __init__(self,name,model,year):
        self.name = name
        self.model = model
        self.year = year
        self.odometer = 0
    
    def get_descriptive_name(self):
        ## make one line output
        long_name = ' '+ self.name + ' '+ self.model+ ' '+ self.year
        return long_name.title()

    def reading_odometer(self):
        return self.odometer
        
    def update_odometer(self,milage):
        if milage >= self.odometer:
            self.odometer = milage
        else:
            print 'you cannot rollback odoo meter'

    def increment_odometer(self,mils):
        self.odometer += mils
        return self.odometer
    
    def fill_gas_tank(self):
        print 'this car have 23 liter gas capacity'


class Battery():
    def __init__(self,battery_size=12):
        self.battery_size = battery_size
    
    def battery_description(self):
        print 'this battery has a '+str(self.battery_size)+'-KWH battery'
    
    def get_range(self):
        if self.battery_size >= 70:
            range = 200
        else:
            range =100

        message = " your car range is "+ str(range)
        message += "milage"
        print message
        return message

class ElectericCar(Car,object):
    """ Represent the aspect of Car, spesific to electronic Car """
    def __init__(self, make, model, year):
        super(ElectericCar, self).__init__(make, model, year)
        # adding attribute and assigning class
        self.battery = Battery()
    
    def fill_gas_tank(self):
        print 'overide gas capacity'

my_tesla = ElectericCar('Tesla','models','2021')
print my_tesla.get_descriptive_name()
my_tesla.battery.battery_description()
my_tesla.battery.get_range()