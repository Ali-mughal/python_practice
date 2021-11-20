class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name.title() + "is now sitting")
    
    def roll_over(self):
        print (self.name.title() + " is roll_over")

my_dog = Dog('tomi',12)

print 'my dog name',my_dog.name,'and age is',my_dog.age
print my_dog.sit()