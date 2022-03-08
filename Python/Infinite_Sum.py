numbers = []
green = "\033[0;32m"
warning = '\033[93m'
reset = '\033[0m'

def sumNumbers():
  totalSum = 0
  for cont in range(len(numbers)):
    totalSum += numbers[cont]
  return totalSum

while True:
  numbers.append(int(input(f"{green}Digite um valor para ser somado:{reset} ")))

  if (0 in numbers):
    print("\n")
    numbers.pop() # Remove the last element from the array, which will be 0
    break
  else:
    print(f"{warning}Caso queira parar de inserir números, digite 0{reset}")
    print("\n")

print(sumNumbers())
