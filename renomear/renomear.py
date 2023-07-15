import os

caminho_pasta = input("Digite o caminho da pasta: ")

for nome_arquivo in os.listdir(caminho_pasta):
    caminho_completo = os.path.join(caminho_pasta, nome_arquivo)
    
    # Exclui os primeiros 10 caracteres do nome do arquivo
    novo_nome = nome_arquivo[10:]
    
    # Renomeia os últimos 10 caracteres do nome do arquivo
    novo_nome = novo_nome[:-14]
    
    # Adiciona a extensão ".mp3" caso não exista
    if not novo_nome.endswith(".mp3"):
        novo_nome += ".mp3"
    
    novo_caminho = os.path.join(caminho_pasta, novo_nome)
    os.rename(caminho_completo, novo_caminho)

print("Arquivos renomeados com sucesso!")
