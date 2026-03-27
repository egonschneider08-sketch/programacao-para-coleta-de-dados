import random

for i in range (0,20):
    prcntg = random.uniform(10,100)
    print("O nível desse tanque está em:",round(prcntg,2),"%")
    if prcntg > 90:
        print("ALERTA! O TANQUE ESTÁ CHEGANDO AO LIMITE TETO, TANQUE EM:",round(prcntg,2),"% O RECOMENDADO É DE 10% À 90%")
    if prcntg < 20:
        print("ALERTA! O TANQUE ESTÁ CHEGANDO AO FIM, TANQUE EM:",round(prcntg,2),"% O RECOMENDADO É DE 10% À 90%")
    print("")