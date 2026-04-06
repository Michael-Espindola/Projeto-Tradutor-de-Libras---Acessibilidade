# --- BLOCO DE IMPORTAÇÕES ---
# Importa a biblioteca que reconhece a fala humana e transforma em texto
import speech_recognition as sr

# --- BLOCO DE FUNÇÕES ---
# Função criada para ativar o microfone e escutar a voz da atendente
def ouvir_voz():
    # Cria um objeto que vai gerenciar o reconhecimento da voz (o "ouvido" do PC)
    rec = sr.Recognizer()
    
    # Abre o microfone padrão do computador ou celular para ser a fonte do som
    with sr.Microphone() as fonte:
        print("Ouvindo a fala da atendente...")
        # Avisa ao sistema para capturar o que está vindo do microfone
        audio = rec.listen(fonte)
        
    # Usa a inteligência do Google para transformar o som em texto (Português Brasil)
    texto = rec.recognize_google(audio, language='pt-BR')
    # Devolve o texto pronto para que o avatar possa fazer os sinais na tela
    return texto

# --- CORPO DO BLOCO (EXECUÇÃO) ---
# Verifica se este arquivo é o principal que o Michael deu o "play"
if __name__ == "__main__":
    # Chama a função e guarda a frase falada na variável 'frase'
    frase = ouvir_voz()
    
    # Exibe na tela exatamente o que a atendente falou para o surdo ler
    print("A ATENDENTE FALOU:", frase)
