green = "\033[0;32m"
warning = '\033[93m'
reset = '\033[0m'

def FastPerson():
  velocity1 = float(input(f"{warning}Qual a velocidade do primeiro participante:{reset} "))
  velocity2 = float(input(f"{warning}Qual a velocidade do segundo participante:{reset} "))
  velocity3 = float(input(f"{warning}Qual a velocidade do terceiro participante:{reset} "))

  if velocity1 < velocity2 and velocity1 < velocity3:
    print(f"{green}JOGADOR 1 VENCEU!{reset}")
  elif velocity2 < velocity1 and velocity2 < velocity3:
    print(f"{green}JOGADOR 2 VENCEU!{reset}")
  elif velocity3 < velocity1 and velocity3 < velocity2:
    print(f"{green}JOGADOR 3 VENCEU!{reset}")
  elif velocity1 == velocity2 and velocity2 == velocity3:
    print(f"{warning}EMPATE GERAL{reset}")
  elif velocity1 == velocity2:
    print(f"{warning}EMPATE{reset} entre jogador 1 e o jogador 2")
  elif velocity2 == velocity3:
    print(f"{warning}EMPATE{reset} entre jogador 2 e o jogador 3")
  elif velocity1 == velocity3:
    print(f"{warning}EMPATE{reset} entre jogador 1 e o jogador 3")

FastPerson()
