# preco do livro
livro = "Pinóquio"
dic = {"Pinóquio": "azul", "Dom Quixote": "amarelo", "O Pequeno Príncipe": "vermelho"}
dic2 = {"vermelho": 10.0, "azul": 20.0, "amarelo": 40.0, "verde": 100.0 }
def verifica_preco(livro, dic, dic2):
    for livros in dic.keys():
        if livros == livro:
            cor = dic[livros]
    return dic2[cor]

print(verifica_preco(livro,dic,dic2))

