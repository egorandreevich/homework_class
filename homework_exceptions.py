calculation_input = input()
calculation_list = calculation_input.split()

try:
  assert int(calculation_list[1]) >= 0 or int(calculation_list[2]) >= 0, 'введенное число отрицательное'
except AssertionError:
  print('одно из чисел - отрицательное')

try:
  int(calculation_list[1])
except ValueError:
  print('введенное значение "{}" не является числом'.format(calculation_list[1]))

try:
  int(calculation_list[2])
except ValueError:
  print('введенное значение "{}" не является числом'.format(calculation_list[2]))

i = 0
try:
  if calculation_list[0] == '+':
    i = (int(calculation_list[1])) + (int(calculation_list[2]))
    print(i)
  elif calculation_list[0] == '-':
    i = (int(calculation_list[1])) - (int(calculation_list[2]))
    print(i)
  elif calculation_list[0] == '*':
    i = (int(calculation_list[1])) * (int(calculation_list[2]))
    print(i)
  elif calculation_list[0] == '/':
    i = (int(calculation_list[1])) / (int(calculation_list[2]))
    print(i)
  else:
    print('операция невозможна, оператор указан неверно')
except Exception:
  print('операция не была выполнена')
