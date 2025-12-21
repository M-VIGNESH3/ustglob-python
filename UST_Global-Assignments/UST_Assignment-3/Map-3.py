# Given a list of temperatures in Celsius, use map() to convert them to Fahrenheit.

c=[20,40,60,80]
print("Celsius list",c)
f=map(lambda i:round((i*1.8)+32,2) , c)
print("Fahrenheit list",list(f))