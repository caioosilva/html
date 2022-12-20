import shutil

def escerever_arquivo(texto):
    arquivo = open('nota.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)
    
def media_nota(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_nota =  x.split(',')
        aluno = lista_nota[0]
        lista_nota.pop(0)
        print(aluno)
        print(lista_nota) 
        media = lambda nota: sum([int(i) for i in nota]) / 4
        print(media(lista_nota))
        lista_media.append({aluno:media(lista_nota)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, "C:\Users\caioc\Desktop\projetos\novanota.txt")

def move_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, "C:\Users\caioc\Desktop\projetos\notaaluno.txt")


if __name__ == '__main__':
    #lista_media = media_nota('nota.txt')
    #print(lista_media)
    #media_nota('nota.txt')
    #aluno = '\n canguru, 7, 1, 9, 5 \n'
    #atualizar_arquivo('nota.txt', aluno)
    copia_arquivo('novanota.txt')
    move_arquivo('notaaluno.txt')