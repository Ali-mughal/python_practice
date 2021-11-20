class User():
    def __init__(self,first_name,last_name,location):
        self.f_name = first_name
        self.l_name = last_name
        self.location = location
        self.login_attempts = 0
    
    def describe_user(self):
        user_info = self.f_name + ' '+ self.l_name + ' ' + self.location
        return user_info.title()
    
    def greate_user(self):
        great_user = ' Welcome '+ self.f_name + ' ' + self.l_name 
        return great_user

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts

my_user = User('ali','raza','Abu Dhabi')

user_profile = my_user.describe_user()
print user_profile
print my_user.greate_user() 