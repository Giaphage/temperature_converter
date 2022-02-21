### Simple temperature convertor to scale up and practice various skills

### NEED TO STOP IT AUTO RUNNING C_to_F when convertorRequired isn't set to Y or N !! ###

def initialiseConvertor():
    convertorRequired = "unset"
    convertor_required = convertorType(convertorRequired)
    if  convertor_required == "F" or 'f':
        C_to_F()
    elif convertor_required == "C" or 'c':no
        F_to_C()
    else:
        print("Input not recognised.")
        initialiseConvertor()
    postConversion()

def convertorType(convertorRequired):
    print("Would you like to convert to Farinheit or Celcius?")
    convertorRequired = input("Input ('F' or 'C'): ")
    if convertorRequired == 'F' or 'C' or 'f' or 'c':
        return convertorRequired
    else:
        print("Input not recognised, please try again.")
        convertorType(convertorRequired)

def C_to_F():

    C = float(input("Input Celcius Value to be Converted: "))

    F = (C*9/5)+32 #  °F = °C x 9 ÷ 5 + 32

    print(str(C) + " degrees Celcius in Farinheit is: " + str(F) + " degrees.")

def F_to_C():

    F = float(input("Input Farinheit Value to be Converted: "))

    C = (F-32)*5/9 # °C = [(°F-32)×5]/9

    print(str(F) + " degrees Farinheit in Celcius is: " + str(C) + " degrees.")

def postConversion():
    print("Do you require more conversions?")
    more_conv = input("Y/N: ")
    if more_conv == "Y" or 'y':
        initialiseConvertor()
    elif more_conv == "N" or 'n':
        print("Please close the program.")
    else:
        print("Input not recognised.")
        postConversion()

initialiseConvertor()