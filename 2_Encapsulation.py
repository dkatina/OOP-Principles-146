#Encapsulation: Bundling data and methods within a class and controlling access to them

#- Public Attributes: that are accessible from anywhere both inside and outside the class 
#they are defined

#- Private Attributes: indicated by a double underscore (dunder) __name, Accessible
#only within the class they are defined in. Useful for hiding and securing data

#- Proctected Attributes: indicated by a single underscore _name, Accessible
#in both the class its defined and any subclass

class Smartphone():

    def __init__(self, model, credit_card, operating_system):
        self.model = model
        self.__wallet = credit_card
        self._operating_system = operating_system

    def show_info(self):
        print(f'Model: {self.model}')
        print(f'Wallet: *****')
        print(f"OS: {self._operating_system}")

    def get_wallet(self):
        return self.__wallet
    
    def set_wallet(self, new_card):
        print(f'Setting new credit card endinging {new_card[4:]}')
        self.__wallet = new_card




iphone = Smartphone('15 Pro Max', '1234567', 'IOS 27')
iphone.show_info()

#iphone.__wallet will throw an error because it is private

print(iphone.model)



#==============Getters and Setters=================

#----- Getter: method used to access any attribute (including private), since they are 
#not accessible otherwise

print(iphone.get_wallet())

#----- Setter: method used to set any attribute (including private atts)

iphone.set_wallet('09876543')
print(iphone.get_wallet())
