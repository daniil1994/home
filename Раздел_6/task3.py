number = int(input('Укажите число: '))
list_number = 0
while number > 0:
  number//=10
  list_number += 1
  print(list_number)