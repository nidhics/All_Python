# Python Program to convert temperature in celsius to fahrenheit

# change this value for a different result
#celsius = 37.5
#typecast
celsius = float(input("Please enter the temperature in celsius: "))


# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print(fahrenheit)

print(celsius,"clecius temprature in fehrenite",fahrenheit)
print(f"{celsius} degree Celsius is equal to {fahrenheit} degree Fahrenheit")

print('%i degree Celsius is equal to %i degree Fahrenheit' %(celsius,fahrenheit))
print('%0.1f \u00B0C is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))
# unicode character
print('%0.2f degree Celsius is equal to %0.2f degree Fahrenheit' %(celsius,fahrenheit))

# f is changing the formating of celsius and fahrenheit to string

temp = fahrenheit

if (temp >= 104):#100
  print("It's hot")
elif (temp <= 50):
  print("It's cold")
else:
  print("The temperature is nice")