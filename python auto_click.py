import pyautogui
import time

# Define a posição onde o clique será realizado
x, y = 1050, 315

# Função para realizar o clique
def clicar_na_posicao():
    pyautogui.click(x, y)
    print(f"Clique realizado na posição ({x}, {y})")

try:
    while True:
        clicar_na_posicao()
        # Espera 15 minutos (900 segundos) antes de realizar o próximo clique
        time.sleep(10)
except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")
except Exception as e:
    print(f"\nOcorreu um erro: {e}")
