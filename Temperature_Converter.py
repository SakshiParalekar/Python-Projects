#Goal of this tryout is to create a function from scratch and invoke it for the given problem
def convert_temp():
    celsius = int(input("Enter the Temperature in celsius:"))
    fahrenheit = (1.8 * celsius) + 32
    print("The celsius Temperature converted into Fahrenheit:",fahrenheit)
    
    fahrenheit = float(input("Enter the Temperature in fahrenheit:"))
    celsius = (fahrenheit-32)*(5/9)
    print("The Fahrenheit Temperature converted into celsius:",celsius)
    
convert_temp()
