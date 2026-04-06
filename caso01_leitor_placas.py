# --- BLOCO DE IMPORTAÇÕES ---
# Importa a biblioteca OpenCV para capturar imagens da câmera
import cv2
# Importa a biblioteca Pytesseract para reconhecer texto em imagens (OCR)
import pytesseract

# --- BLOCO DE FUNÇÕES ---
# Função criada para centralizar a lógica de leitura da placa
def ler_placa():
    # Comando que liga a câmera (o número 0 indica a câmera padrão do notebook/PC)
    camera = cv2.VideoCapture(0)
    print("Capturando imagem da placa...")
    
    # Simulação da captura: o Tesseract analisa a imagem e extrai o texto
    # Na prática, 'frame' seria a foto tirada pela câmera acima
    texto = pytesseract.image_to_string(frame)
    
    # Retorna o texto encontrado para ser usado no aplicativo
    return texto

# --- CORPO DO BLOCO (EXECUÇÃO) ---
# Verifica se este arquivo é o principal sendo executado pelo Michael
if __name__ == "__main__":
    # Chama a função e guarda o que ela "leu" na variável resultado
    resultado = ler_placa()
    
    # Exibe o texto final para o usuário no terminal ou no App
    print("O APP ENCONTROU O TEXTO:", resultado)
