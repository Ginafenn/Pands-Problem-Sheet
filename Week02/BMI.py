#Calculating BMI
#author:Regina Fennessy
#Coverts the string that input returns to an int
height = int(input('Please enter your height in cm:'))
weight = int(input('Please enter your weight in kg:'))

BMI = weight / (height/100)**2

print (f"Your BMI is {BMI}")


