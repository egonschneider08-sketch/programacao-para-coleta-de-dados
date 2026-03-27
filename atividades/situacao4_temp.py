#importando bobliotecas 
import random

for i in range (0,20):
    temp = random.uniform(0,15)
    print("Temperatura da maquina está em:",round(temp,2),"C°")
    if temp > 10:
        print("ALERTA! TEMPERATURA ESTÁ EM:",round(temp,2),"C° O RECOMENDADO É ABAIXO DE 10 C°")
    print("")