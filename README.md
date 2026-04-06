# 🤟 Projeto Acessibilidade: Tradutor Bilateral Libras-Voz

Este projeto foi desenvolvido durante o curso **Jovem Programador (Senac/SC)**. O objetivo é criar um "Norte Tecnológico" para um aplicativo que quebra barreiras de comunicação entre surdos e ouvintes em espaços públicos através de Python e Inteligência Artificial.

---

## 🛠️ Tecnologias e Tags
* **Linguagem:** `python`
* **Visão Computacional:** `opencv`, `mediapipe`
* **Acessibilidade:** `libras`, `acessibilidade`
* **Domínio:** `computer-vision`
* **Curso:** `jovem-programador`

---

## 📋 Detalhamento dos Casos de Uso

### 📸 Caso 01: Visão Computacional (Ler Placas)
**O que faz:** O aplicativo "lê" placas e ofertas de supermercado e traduz para sinais de Libras para o usuário surdo.

**Fluxo de Planejamento:**
![Desenho Caso 01](desenho_caso01.jpg)

```python
# --- BLOCO DE IMPORTAÇÕES ---
# Importa a biblioteca para capturar imagens da câmera
import cv2
# Importa a biblioteca que reconhece texto em imagens (OCR)
import pytesseract

# --- BLOCO DE FUNÇÕES ---
# Função criada para centralizar a lógica de leitura da placa
def ler_placa():
    # Comando que liga a câmera (o número 0 indica a câmera padrão)
    camera = cv2.VideoCapture(0)
    
    # Captura um quadro (foto) da câmera
    sucesso, frame = camera.read()
    
    # O Tesseract analisa a imagem capturada e extrai o texto escrito
    texto = pytesseract.image_to_string(frame)
    
    # Desliga a câmera
    camera.release()
    
    # Retorna o texto encontrado para quem chamou a função
    return texto

# --- CORPO DO BLOCO (EXECUÇÃO) ---
if __name__ == "__main__":
    resultado = ler_placa()
    print("O APP ENCONTROU O TEXTO:", resultado)

**Fluxo de Planejamento:**
![Desenho Caso 02](desenho_caso02.jpg)
# --- BLOCO DE IMPORTAÇÕES ---
# Importa a biblioteca para capturar o vídeo da câmera
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
    # Aqui simulamos que o sistema identificou o sinal de socorro
    sinal = "PRECISO DE UM MÉDICO"
    
    # Comanda o computador para dizer a frase em voz alta para o ouvinte
    voz.say(sinal)
    # Faz o programa esperar a fala terminar antes de seguir
    voz.runAndWait()

# --- CORPO DO BLOCO (EXECUÇÃO) ---
# Verifica se este é o arquivo principal que o Michael deu o play
if __name__ == "__main__":
    # Chama a função de tradução para executar todo o processo acima
    traduzir_mao()


**Fluxo de Planejamento:**
![Desenho Caso 03](desenho_caso03.jpg)

# --- BLOCO DE IMPORTAÇÕES ---
# Importa a biblioteca de reconhecimento de fala
import speech_recognition as sr

# --- BLOCO DE FUNÇÕES ---
# Função para ativar o microfone e escutar o que está sendo dito
def ouvir_voz():
    # Cria o objeto de reconhecimento
    rec = sr.Recognizer()
    
    # Abre o microfone padrão do dispositivo (celular ou notebook)
    with sr.Microphone() as fonte:
        # Sistema fica ouvindo o som do ambiente
        audio = rec.listen(fonte)
        
    # Transforma o som ouvido em texto escrito (Português Brasil) usando o Google
    texto = rec.recognize_google(audio, language='pt-BR')
    
    # Retorna o texto para ser exibido como sinal na tela
    return texto

# --- CORPO DO BLOCO (EXECUÇÃO) ---
if __name__ == "__main__":
    # Captura a fala da atendente ou ouvinte
    frase = ouvir_voz()
    
    # Mostra o resultado da tradução no console do app
    print("A PESSOA FALOU:", frase)


