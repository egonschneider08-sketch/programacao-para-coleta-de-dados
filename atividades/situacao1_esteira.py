#importando bobliotecas 
import random

for i in range (0,20):
    vel = random.uniform(0,2)
    print("Velocidade da esteira está em:",round(vel,2),"m/s")
    if vel < 0.5:
        print("ALERTA! VELOCIDADE ESTÁ EM:",round(vel,2),"C° O RECOMENDADO É DE 0.5 m/s à 1.5 m/s")
    print("")