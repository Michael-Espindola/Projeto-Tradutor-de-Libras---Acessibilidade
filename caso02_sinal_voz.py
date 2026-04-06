# --- BLOCO DE IMPORTAÇÕES ---
# Importa a biblioteca para capturar o vídeo da câmera frontal
import cv2
# Importa a inteligência artificial que rastreia os dedos (MediaPipe)
import mediapipe as mp
# Importa a biblioteca que transforma o texto em fala (voz do computador)
import pyttsx3

# --- BLOCO DE VARIÁVEIS E FUNÇÕES ---
# Inicia a ferramenta de voz para que ela fique pronta para falar
voz = pyttsx3.init()

# Função criada para cuidar da tradução dos movimentos das mãos
def traduzir_mao():
    # O MediaPipe mapeia os 21 pontos das mãos para entender o sinal feito
    # Aqui simulamos que o sistema identificou um sinal específico de socorro
    sinal = "PRECISO DE UM MÉDICO"
    
    # Comanda o computador para dizer a frase em voz alta para o ouvinte
    voz.say(sinal)
    # Faz o programa esperar a fala terminar antes de seguir adiante
    voz.runAndWait()

# --- CORPO DO BLOCO (EXECUÇÃO) ---
# Verifica se este é o arquivo principal que o Michael deu o "play"
if __name__ == "__main__":
    # Chama a função de tradução para executar todo o processo acima
    traduzir_mao()
