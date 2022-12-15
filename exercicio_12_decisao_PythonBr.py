"""Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos
são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para 
o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
(é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.


    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
    dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a 
    quantidade de hora é 220.

Salário Bruto: (5 * 220)        : R$ 1100,00
(-) IR (5%)                     : R$   55,00  
(-) INSS ( 10%)                 : R$  110,00
FGTS (11%)                      : R$  121,00
Total de descontos              : R$  165,00
Salário Liquido                 : R$  935,00"""




hora = float(input("Informe o valor da sua hora trabalhada R$: "))
horast = float(input("Informe a quantidade de  horas trabalhadas: "))
sal_bruto = (hora * horast)
inss = (sal_bruto*10)/100
fgts = (sal_bruto*11)/100
sindicato = (sal_bruto *3)/100

print(f"\nSalario  Bruto:{hora} * {horast} : R$ {hora * horast:.2f}")

if sal_bruto > 900 and sal_bruto <= 1500:
    ir5 =(sal_bruto * 5)/100
    print(f"(-) IR (5%): R$ {ir5:.2f}")
    print(f"(-) INSS(10%): R$ {inss:.2f}")
    print(f"FGTS (11%): R$ {fgts:.2f}")
    print(f"Total de descontos : R$ {inss + ir5:.2f}")
    print(f"Sindicato (3%) :R$ {sindicato:.2f}")
    print(f"Salario Liquido                         : R$ {sal_bruto - ir5 - inss - sindicato:.2f}")
    
elif sal_bruto > 1500 and sal_bruto  <= 2500:
    ir10 = (sal_bruto *10)/100
    print(f"(-) IR (10%)                            : R$ {ir10:.2f}")
    print(f"(-) INSS(10%)                           : R$ {inss:.2f}")
    print(f"FGTS (11%)                              : R$ {fgts:.2f}")
    print(f"Total de descontos                      : R$ {inss + ir10:.2f}")
    print(f'Sindicato (3%)                          : R$ {sindicato:.2f}')
    print(f"Salario Liquido                         : R$ {sal_bruto - ir10 - inss - sindicato:.2f}")

elif sal_bruto > 2500:
    ir20 = (sal_bruto *20)/100
    print(f"(-) IR (10%)                            : R$ {ir20:.2f}")
    print(f"(-) INSS(10%)                           : R$ {inss:.2f}")
    print(f"FGTS (11%)                              : R$ {fgts:.2f}")
    print(f"Total de descontos                      : R$ {inss + ir20:.2f}")
    print(f'Sindicato (3%)                          : R$ {sindicato:.2f}')
    print(f"Salario Liquido                         : R$ {sal_bruto - ir20 - inss - sindicato:.2f}")

elif sal_bruto <= 900:
    print(f"(-) IR (isento)                         : R$ 0.00")
    print(f"(-) INSS(10%)                           : R$ {inss:.2f}")
    print(f"FGTS (11%)                              : R$ {fgts:.2f}")
    print(f"Total de descontos                      : R$ {inss:.2f}")
    print(f'Sindicato (3%)                          : R$ {sindicato:.2f}')
    print(f"Salario Liquido                         : R$ {sal_bruto - inss - sindicato:.2f}")
