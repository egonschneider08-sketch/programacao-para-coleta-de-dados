import random
import time

def gerar_dados():
    temperatura = random.uniform(30, 100)  # °C
    press = random.uniform(0.8, 1.2)     # bar
    return temperatura, press

def verifier_alarme(temp, press):
    if temp > 85 or press > 1.1:
        print(f"ALARME: Temp={temp:.1f}°C | Press={press:.2f}bar")
    else:
        print(f"Normal: Temp={temp:.1f}°C | Press={press:.2f}bar")

if __name__ == "__main__":
    for _ in range(20):
        t, p = gerar_dados()
        verifier_alarme(t, p)
        time.sleep(1)