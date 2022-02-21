### Simple temperature convertor to scale up and practice various skills

def F_to_C():

    F = input("Input Celcius Value to be Converted: ")

    C = ((int(F)-32)*5)/5 # °C = [(°F-32)×5]/9.

    print(str(F) + " degrees Celcius in Farinheit is: " + str(C) + " degrees.")

F_to_C()
