##Super Class Employee
class Employee:
    ##Employee Contructor
    def __init__(self, lastname, firstname, address, socialnum, monthsal, annualsal):
        self.lastname = input("Last Name: ")
        self.firstname = input("First Name: ")
        self.address = input("Address:  ")
        self.socialnum = input("Social Number: ")
        self.monthsal = input("Monthly Salary: ")
        self.annualsal = annualsal
    
    def calculate_annualsal(self):
      self.annualsal = int(self.monthsal) * 12

    def display(self):
      print("\nLast Name: " + self.lastname)
      print("First Name: "+ self.firstname)
      print("Address: "+ self.address)
      print("Social Number: "+ self.socialnum)
      print("Annual Payment: "+ str(self.annualsal))


class Technician(Employee):
     ##Technician Contructor
     def __init__(self,lastname, firstname, address, socialnum, monthsal, annualsal, overtime):
       super().__init__(lastname, firstname, address, socialnum, monthsal, annualsal)
       self.overtime = input("Overtime: ")
       if(int(self.overtime) > 0):
         # 40 is the amount of pay per hour for this position due to the overtime hours
         # The other positions don't need their pay per hour
         self.annualsal = 40 * int(self.overtime) * 1.5

     ##Override Function
     def calculate_annualsal(self):
        self.annualsal = self.annualsal + int(self.monthsal) * 12
        
     ##Override Function
     def display(self):
        print("\nLast Name: " + self.lastname)
        print("First Name: "+ self.firstname)
        print("Address: "+ self.address)
        print("Social Number: "+ self.socialnum)
        if (int(self.overtime) > 0):
         print("Total Overtime: "+ str(40 * int(self.overtime) * 1.5))
        if (int(self.overtime) <= 0):
          print("Total Overtime: "+ str(0))
        print("Annual Payment: "+ str(self.annualsal))


class Engineer(Employee):
    ##Engineer Contructor
    def __init__(self,lastname, firstname, address, socialnum, monthsal, annualsal, bonus):
       super().__init__(lastname, firstname, address, socialnum, monthsal, annualsal)
       # checks for a bonus
       self.bonus = input("\nDid you produce a successful profit? Yes or No: ")
       if (self.bonus == "Yes"):
         self.annualsal = self.annualsal + 5000
         
       elif (self.bonus == "No"):
         self.annualsal = 0

    def calculate_annualsal(self):
        self.annualsal = self.annualsal + (int(self.monthsal) * 12)
        
    def display(self):
        print("\nLast Name: " + self.lastname)
        print("First Name: "+ self.firstname)
        print("Address: "+ self.address)
        print("Social Number: "+ self.socialnum)
        if (self.bonus == "Yes"):
         print("Total Bonus: "+ str(5000))
        if (self.bonus == "No"):
          print("Total Bonus: "+ str(0))
        print("Annual Payment: "+ str(self.annualsal))

class MarketManager(Employee):
    ##MarketManager Constructor
    def __init__(self,lastname, firstname, address, socialnum, monthsal, annualsal, one_percent_payment):
       super().__init__(lastname, firstname, address, socialnum, monthsal, annualsal)
       # checks for the one_percent_payment
       self.one_percent_payment = input("\nDid you sell more than one thousand new products? Yes or No: ")
       if (self.one_percent_payment == "Yes"):
        self.annualsal = 5000

       elif (self.one_percent_payment == "No"):
         self.annual = 0
    def calculate_annualsal(self):
        if (self.one_percent_payment == "Yes"):
          self.annualsal = self.annualsal + ((int(self.monthsal) * 12 ) + (int(self.monthsal) * 12) * 0.01)
        elif(self.one_percent_payment == "No"):
          self.annualsal = self.annualsal + (int(self.monthsal) * 12)
    
    def display(self):
        print("\nLast Name: " + self.lastname)
        print("First Name: "+ self.firstname)
        print("Address: "+ self.address)
        print("Social Number: "+ self.socialnum)
        if (self.one_percent_payment == "Yes"):
         print("Total Bonus: "+ str((int(self.monthsal) * 12) * 0.01+5000))
        if (self.one_percent_payment == "No"):
          print("Total Bonus: "+ str(0))
        print("Annual Payment: "+ str(self.annualsal))

## Driver code
print("\nWhat is your job position?\n")
# calls for job position
position = input("Enter T for Technician, E for Engineer, M for Market Manager, G for Employee: ")

## if statements that would call for each position
if(position == "T"):
  tech = Technician(0, 1, 2, 3, 4, 5, 6)
  tech.calculate_annualsal()
  # calls to see if user wants annual salary
  ans = input("\nWould you like to see your Annual Salary? Yes or No: ")
  if (ans == "Yes"):
    tech.display()
 

elif(position == "E"):
  eng = Engineer(0, 1, 2, 3, 4, 0, 6)
  eng.calculate_annualsal()
  ans = input("\nWould you like to see your Annual Salary? Yes or No: ")
  if (ans == "Yes"):
    eng.display()

elif(position == "M"):
  mark = MarketManager(0, 1, 2, 3, 4, 0, 6)
  mark.calculate_annualsal()
  ans = input("\nWould you like to see your Annual Salary? Yes or No: ")
  if (ans == "Yes"):
    mark.display()


elif(position == "G"):
  emply = Employee(0, 1, 2, 3, 4, 5)
  emply.calculate_annualsal()
  ans = input("\nWould you like to see your Annual Salary? Yes or No: ")
  if (ans == "Yes"):
    emply.display()
## Driver code

