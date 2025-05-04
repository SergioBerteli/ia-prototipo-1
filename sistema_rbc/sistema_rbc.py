import time
import mysql.connector

p_gen = 1
p_prot_gen = 0.5
p_tema = 0.7
p_idioma_original = 0.6
p_comp_ling = 0.8

p_ano_lanc = 0 
p_num_pag = 0 
p_pop = 0 
p_pub_alvo = 0 
p_narracao = 0 

pag_range_perc = 10
ano_range = 5

def pesos ():
    p_ano_lanc = float(input("Defina o peso do ano de lançamento: "))
    p_num_pag = float(input("Defina o peso do numero de páginas: "))
    p_pop = float(input("Defina o peso da populariedade"))
    p_pub_alvo = float(input("Defina o peso do publico-alvo"))
    p_narracao = float(input("Defina o peso do tipo de narração"))
    return p_ano_lanc, p_num_pag, p_pop, p_pub_alvo, p_narracao

def get_caso_similar(Genero, Tema, NumeroDePaginas, AnoDeLancamento, GeneroProtagonista, IdiomaOriginal, ComplexidadeDaLinguagem, Populariedade, PublicoAlvo, Narrador):
    cursor = connection.cursor()
    cursor.execute('Select * FROM Livros')
    livros = cursor.fetchall()
    connection.close()
    print(livros)
    scores = list()
    for livro in livros:
        score = 0
        score += p_gen if livro[2].lower() == Genero.lower() else 0
        score += p_tema if livro[3].lower() == Tema.lower() else 0
        score += p_num_pag if  NumeroDePaginas in range (round(livro[4]*(1-pag_range_perc/100)), round(livro[4]*(1+pag_range_perc/100))) else 0
        score += p_ano_lanc if AnoDeLancamento in range(livro[5]-ano_range, livro[5]+ano_range) else 0
        score += p_prot_gen if livro[6].lower() == GeneroProtagonista.lower() else 0
        score += p_idioma_original if livro[7].lower() == IdiomaOriginal.lower() else 0
        score += p_comp_ling if livro[8].lower() == ComplexidadeDaLinguagem.lower() else 0
        score += p_pop if livro[9].lower() == Populariedade.lower() else 0
        score += p_pub_alvo if livro[10].lower() == PublicoAlvo.lower() else 0
        score += p_narracao if livro[11].lower() == Narrador.lower() else 0
        scores.append(score)
    valor_maximo = max(scores)
    livro_index = scores.index(valor_maximo)
    livro_escolhido = livros[livro_index][1]
    print(livro_escolhido)
    print(valor_maximo)
        



print("Conectando à base de dados...")
while(1):
    try:
        connection = mysql.connector.connect(
            user='root', password='root', host='basededados', port="3306", database='db')
        break
    except:
        print("Erro ao tentar conectar com a base de dados, tentando novamente em 5 segundos!")
        time.sleep(5)


if __name__ == "__main__":
    print("Seja bem-vindo ao sistema RBC para recomendações de livros! Insira os pesos de algumas variáveis antes de começar a usa-lo.")
    #p_ano_lanc, p_num_pag, p_pop, p_pub_alvo, p_narracao = pesos()
    p_ano_lanc, p_num_pag, p_pop, p_pub_alvo, p_narracao = 1, 1, 1, 1, 1

    Genero, Tema, NumeroDePaginas, AnoDeLancamento, GeneroProtagonista, IdiomaOriginal, ComplexidadeDaLinguagem, Populariedade, PublicoAlvo, Narrador = ("Romance",
    "Redenção", 400, 2015, "M", "Português", "Simples",  "Muito Popular", "Infantil", "Narrador Onisciente")

    while 1:
        #escolha = int(input("1 - Consultar caso similar\n2 - Adicionar um caso\n3 - mudar os pesos\n4 - Sair do programa"))
        escolha = 4
        if escolha == 1:
            get_caso_similar(Genero, Tema, NumeroDePaginas, AnoDeLancamento, GeneroProtagonista, IdiomaOriginal, ComplexidadeDaLinguagem, Populariedade, PublicoAlvo, Narrador )
        elif escolha == 2:
            pass
        elif escolha == 3:
            pass
        elif escolha == 4:
            break
        else:
            print("Opção invalida")



get_caso_similar(Genero, Tema, NumeroDePaginas, AnoDeLancamento, GeneroProtagonista, IdiomaOriginal, ComplexidadeDaLinguagem, Populariedade, PublicoAlvo, Narrador )