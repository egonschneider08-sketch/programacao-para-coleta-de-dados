#importando bobliotecas 
import random

for i in range (0,20):
    temp = random.uniform(20,40)
    pres = random.uniform(1,8)
    print("Temperatura da maquina está em:",round(temp,2),"C°")
    if temp > 35:
        print("ALERTA! TEMPERATURA ESTÁ EM:",round(temp,2),"C° O RECOMENDADO É DE 20 C° à 35 C°")
    print("Pressão está em:",pres, round(pres,2),"Bar")
    print("")