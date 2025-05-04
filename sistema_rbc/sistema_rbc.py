import time
import mysql.connector

p_gen = 1
p_prot_gen = 0.5
p_tema = 0.7
p_idioma_original = 0.6
p_comp_ling = 0.8

pag_range_perc = 10
ano_range = 5

def pesos ():
    p_ano_lanc = float(input("Defina o peso do ano de lançamento: "))
    p_num_pag = float(input("Defina o peso do numero de páginas: "))
    p_pop = float(input("Defina o peso da populariedade"))
    p_pub_alvo = float(input("Defina o peso do publico-alvo"))
    p_narracao = float(input("Defina o peso do tipo de narração"))
    return p_ano_lanc, p_num_pag, p_pop, p_pub_alvo, p_narracao
def get_caso_similar():
    pass

print("Conectando à base de dados...")
while(1):
    try:
        connection = mysql.connector.connect(
            user='root', password='root', host='basededados', port="3306", database='db')
        break
    except:
        print("Erro ao tentar conectar com a base de dados, tentando novamente em 5 segundos!")
        time.sleep(5)

cursor = connection.cursor()
cursor.execute('Select * FROM Livros')
students = cursor.fetchall()
connection.close()

if __name__ == "__main__":
    print("Seja bem-vindo ao sistema RBC para recomendações de livros! Insira os pesos de algumas variáveis antes de começar a usa-lo.")
    p_ano_lanc, p_num_pag, p_pop, p_pub_alvo, p_narracao = pesos()

    while 1:
        escolha = int(input("1 - Consultar caso similar\n2 - Adicionar um caso\n3 - mudar os pesos\n4 - Sair do programa"))
        if escolha == 1:
            get_caso_similar()
        elif escolha == 2:
            pass
        elif escolha == 3:
            pass
        elif escolha == 4:
            break
        else:
            print("Opção invalida")



print(students)