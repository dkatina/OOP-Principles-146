#- Inheritance: Extending a parent class, and giving it additional 
#functionality and characteristic

#General -> Specific


#- Polymorphism: Objects from differnt classes responding similarly to the same method 
#in their unique way.


#Parent Class
class User():

    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username

    #All methods are inherited by the child
    def user_info(self):
        print(f"User: {self.username} can be contacted at {self.email}")

    def set_password(self, new_pass):
        self.password = new_pass


#Child Class that inherits from User
class AdminUser(User): #pass parent class in as a parameter
    isadmin = True
    def __init__(self, email, password, username, admin_id):
        super().__init__(email, password, username)
        self.admin_id = admin_id
        
    #polymorphism - Overwriting Parent method, but using it in a similar way.
    def user_info(self):
        print(f'Admin #{self.admin_id}: {self.username} can recieve support tickets at {self.email}.')


#instantiating Admin Class
billy_bob = User('bb@email.com', 'password', 'billy-b')
billy_bob.user_info()
#instantiating Admin Class
travis = AdminUser('travispeck@email.com', '12345', 'travisp', 1)
travis.user_info()
travis.set_password('1029383874')
print(travis.isadmin)
print(travis.password)

    



    
