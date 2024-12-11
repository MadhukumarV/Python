class atm :
    customer_id = 0

    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.customer_id = atm.customer_id
        atm.customer_id += 1
        self.menu()
    
    def menu(self):
        user_input = int(input(
            """
            Hi , How can i help you
            \n 1. press 1 to create pin
            \n 2. press 2 to change pin
            \n 3. press 3 to check balance 
            \n 4. press 4 to withdraw 
            \n 5. press 5 to exit 
            """
        ))
    
        if user_input == 1 :
            #create pin 
            self.create_pin()
            
        elif user_input == 2 :
            # change pin
            self.change_pin()
            
        elif user_input == 3 :
            #check balance
            self.check_balance()
            
        elif user_input == 4 :
            # withdraw 
            self.withdraw()
            
        else:
            exit()
    
    
    def create_pin(self):
        user_pin = int(input("Enter the Pin :"))
        self.pin = user_pin
        
        user_balance = int(input("Enter the Balance :"))
        self.balance = user_balance 
        print("Pin created Successfuly  ")
        
    def change_pin(self):
        old_pin = int(input("Enter the Old Pin"))
        if old_pin ==self.pin:
            #changing the pin
            new_pin = int(input("Enter the New Pin :"))
            self.pin = new_pin
            print("Pin changed successfully ")
        else:
            print("Incorrect Pin,please try again")
    
    
    def check_balance(self):
        user_pin = int(input("Enter the Pin"))
        if user_pin == self.pin :
            print(f"Your Balance is {self.balance}")
        else :
            print("Incorrect Pin,please Try again") 
            
    def withdraw(self):
        user_pin = int(input("Enter the Pin"))
        if user_pin ==self.pin :
            amount = int(input("Enter the Amount"))
            if amount <= self.balance :
                self.balance = self.balance - amount
                print(f"Withdraw successful,current balance is {self.balance}")
            else:
                print("Insufficient Balance")
                
        else :
            print("Incorrect Pin")
        self.menu()
                     
