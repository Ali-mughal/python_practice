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

my_car =  Car('audi','a4','2016')
print my_car.get_descriptive_name()
print my_car.reading_odometer()
my_car.update_odometer(3)
my_car.increment_odometer(10)
print 'this Car has', my_car.reading_odometer(),'milage on it'
