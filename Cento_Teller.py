import datetime

# Small Python program that tells the year you'll be
# a hundred years old

__author__= "ADELEKE OMOTAYO <Dzhud on Github>"


class Cento:
    def __init__(self):
        
        self.dateToday = datetime.date.today()
        self.getThisYear = int(self.dateToday.year)

    def getDetails(self):        
        
        try:
            name = input("Please type in your Name ")
            age = int(input(f"{name.capitalize()} please type in your Age "))            
            calculate_cento = self.getThisYear - age + 100

            if age > self.getThisYear:                
                print("Okay Methuselah, press enter to type in your real age")                                           
            elif age > 100:            
                print(f"Hmmm. You were 100-Years-old in {calculate_cento}, {name.capitalize()}.")
            elif age == 100:
                print(f"Hi ***Centenary*** {name.capitalize()}, You Hit a 100 this Year!!!!")
            elif age < 100:
                print(f"{name.capitalize()}, You'll be 100-years-old in {calculate_cento}")
            elif age > self.getThisYear:
                agE = age - self.getThisYear
                print(f"Hmmm. You were 100-Years-old iin {agE}, {name.capitalize()}.")                                
            else:                
                pass
        except:
            print(f"\nError: \nEnsure your name is a string value and age is an integer\n")

if __name__ == '__main__':
    Cento = Cento()
    Cento.getDetails()
