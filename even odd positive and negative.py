# even/odd and positive/negative combined

num = int (input("enter a number: "))

if num % 2 == 0 and num > 0:
  print("even and positive")
elif num % 2 == 0 and num < 0:
  print("even and negative")
elif num % 2 == 0 and num > 0:
  print("odd and positive")
else:
  print("odd and negative")

enter a number: 6
even and positive
