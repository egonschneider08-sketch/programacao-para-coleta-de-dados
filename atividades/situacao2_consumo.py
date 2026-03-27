#importando bobliotecas 
import random

for i in range (0,20):
    cons = random.uniform(100,700)
    print("Consumo das maquinas está em:",round(cons,2),"kWh")
    if cons > 500:
        print("ALERTA! CONSUMO DAS MAQUINAS ESTÁ EM:",round(cons,2),"C° O RECOMENDADO É DE 200 kWh à 500 kWh")
    print("")