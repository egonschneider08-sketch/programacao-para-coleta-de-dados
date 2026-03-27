import random

for i in range (0,20):
    ph = random.uniform(4,10)
    print("PH desse produto está em:",round(ph,2),)
    if ph > 8:
        print("ALERTA! PH DESSE PRODUTO ESTÁ ALTO EM:",round(ph,2),"O RECOMENDADO É DE 6 À 8")
    if ph < 6:
        print("ALERTA! PH DESSE PRODUTO ESTÁ BAIXO EM:",round(ph,2),"O RECOMENDADO É DE 6 À 8")
    print("")