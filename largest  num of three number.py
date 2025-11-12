#largest of three number

a=float(input("enter the first number: "))
b=float(input("enter the second number: "))
c=float(input("enter the third number: "))

if a >= b and a>=c:
  print("largest number is:",a)
elif b >= a and b >=c:
  print("largest number is:",b)
else:
  print("largest number is:",c)

enter the first number: 3
enter the second number: 4
enter the third number: 5
largest number is: 5.0
