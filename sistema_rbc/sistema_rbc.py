from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QMessageBox
from PySide6.QtCore import Slot, Qt
import time
import mysql.connector
import sys


class JanelaPrinciapl(QMainWindow):
    
    def __init__(self):
        super().__init__()

        # pesos fixos abaixo
        self.p_gen = 1
        self.p_prot_gen = 0.5
        self.p_tema = 0.7
        self.p_comp_ling = 0.8

        self.p_ano_lanc = 0 
        self.p_num_pag = 0 
        self.p_pop = 0 
        self.p_pub_alvo = 0 
        self.p_narracao = 0 
        self.p_idioma_original = 0

        self.pag_range_perc = 10
        self.ano_range = 5
        
        self.setWindowTitle("Sistema RBC de recomendação de livros") #nome do programa

        self.quadro_central= QWidget() # Tela no geral, composta pelas campos de input
        self.setCentralWidget(self.quadro_central)

        #começo form do peso do ano de lancamento
        self.inp_ano = QWidget()

        self.m_ano_lancamento = QLabel(text="Peso do ano de lançamento: ")

        self.p_ano_lancamento = QLineEdit()

        layout = QHBoxLayout()
        layout.addWidget(self.m_ano_lancamento)
        layout.addWidget(self.p_ano_lancamento)
        self.inp_ano.setLayout(layout)


        #começo form do peso do numero de paginas
        self.inp_pag_n = QWidget()

        self.m_pag_n = QLabel(text="Peso do ano do numero de paginas: ")

        self.p_pag_n = QLineEdit()

        layout = QHBoxLayout()
        layout.addWidget(self.m_pag_n)
        layout.addWidget(self.p_pag_n)
        self.inp_pag_n.setLayout(layout)

        #começo form do peso do numero de popularidade
        self.inp_pop = QWidget()

        self.m_pop = QLabel(text="Peso do ano de popularidade: ")

        self.p_pop = QLineEdit()

        layout = QHBoxLayout()
        layout.addWidget(self.m_pop )
        layout.addWidget(self.p_pop )
        self.inp_pop.setLayout(layout)

        #começo form do peso do publico alvo
        self.inp_pub_alvo = QWidget()

        self.m_pub_alvo = QLabel(text="Peso do ano de publico-alvo: ")

        self.p_pub_alvo = QLineEdit()

        layout = QHBoxLayout()
        layout.addWidget(self.m_pub_alvo )
        layout.addWidget(self.p_pub_alvo )
        self.inp_pub_alvo.setLayout(layout)

        #começo form do peso do tipo de narração
        self.inp_narracao = QWidget()

        self.m_narracao = QLabel(text="Peso do tipo de narração")

        self.p_narracao = QLineEdit()

        layout = QHBoxLayout()
        layout.addWidget(self.m_narracao )
        layout.addWidget(self.p_narracao )
        self.inp_narracao.setLayout(layout)
        
        #começo form do peso do idioma original
        self.inp_idio_orign= QWidget()

        self.m_idio_orign = QLabel(text="Peso do tipo do idioma original")

        self.p_idio_origin = QLineEdit()

        layout = QHBoxLayout()
        layout.addWidget(self.m_idio_orign)
        layout.addWidget(self.p_idio_origin)
        self.inp_idio_orign.setLayout(layout)

        # campo: Tema
        self.tema = QWidget()
        self.m_input_tema = QLabel(text="Tema do livro:")
        self.tema_valor = QLineEdit()
        layout_tema = QHBoxLayout()
        layout_tema.addWidget(self.m_input_tema)
        layout_tema.addWidget(self.tema_valor)
        self.tema.setLayout(layout_tema)

        # campo: Número de Páginas
        self.num_pag = QWidget()
        self.m_input_num_pag = QLabel(text="Número de páginas desejado:")
        self.num_pag_valor = QLineEdit()
        layout_num_pag = QHBoxLayout()
        layout_num_pag.addWidget(self.m_input_num_pag)
        layout_num_pag.addWidget(self.num_pag_valor)
        self.num_pag.setLayout(layout_num_pag)

        # campo: Ano de Lançamento
        self.ano_lanc = QWidget()
        self.m_input_ano = QLabel(text="Ano de lançamento desejado:")
        self.ano_valor = QLineEdit()
        layout_ano = QHBoxLayout()
        layout_ano.addWidget(self.m_input_ano)
        layout_ano.addWidget(self.ano_valor)
        self.ano_lanc.setLayout(layout_ano)

        # campo: Gênero do Protagonista
        self.genero_protagonista = QWidget()
        self.m_input_prot = QLabel(text="Gênero do protagonista:")
        self.prot_valor = QComboBox()
        self.prot_valor.addItems(["Masculino", "Feminino"])
        layout_prot = QHBoxLayout()
        layout_prot.addWidget(self.m_input_prot)
        layout_prot.addWidget(self.prot_valor)
        self.genero_protagonista.setLayout(layout_prot)

        # campo: Idioma Original
        self.idioma_original = QWidget()
        self.m_input_idioma = QLabel(text="Idioma original do livro:")
        self.idioma_valor = QLineEdit()
        layout_idioma = QHBoxLayout()
        layout_idioma.addWidget(self.m_input_idioma)
        layout_idioma.addWidget(self.idioma_valor)
        self.idioma_original.setLayout(layout_idioma)

        # campo: Complexidade da Linguagem
        self.complexidade = QWidget()
        self.m_input_complexidade = QLabel(text="Complexidade da linguagem:")
        self.complexidade_valor = QComboBox()
        self.complexidade_valor.addItems(["Simples", "Intermediária", "Complexa"])
        layout_comp = QHBoxLayout()
        layout_comp.addWidget(self.m_input_complexidade)
        layout_comp.addWidget(self.complexidade_valor)
        self.complexidade.setLayout(layout_comp)

        # campo: Popularidade (nota de 0 a 5)
        self.popularidade = QWidget()
        self.m_input_pop = QLabel(text="Popularidade mínima (0 a 5):")
        self.pop_valor = QLineEdit()
        layout_pop = QHBoxLayout()
        layout_pop.addWidget(self.m_input_pop)
        layout_pop.addWidget(self.pop_valor)
        self.popularidade.setLayout(layout_pop)

        # campo: Público-alvo
        self.pub_alvo = QWidget()
        self.m_input_pub = QLabel(text="Público-alvo:")
        self.pub_valor = QComboBox()
        self.pub_valor.addItems(["Infantil", "Jovem Adulto", "Adulto"])
        layout_pub = QHBoxLayout()
        layout_pub.addWidget(self.m_input_pub)
        layout_pub.addWidget(self.pub_valor)
        self.pub_alvo.setLayout(layout_pub)

        # campo: Narrador
        self.narrador = QWidget()
        self.m_input_narrador = QLabel(text="Tipo de narrador:")
        self.narrador_valor = QComboBox()
        self.narrador_valor.addItems(["1ª pessoa", "3ª pessoa", "Onisciente"])
        layout_narrador = QHBoxLayout()
        layout_narrador.addWidget(self.m_input_narrador)
        layout_narrador.addWidget(self.narrador_valor)
        self.narrador.setLayout(layout_narrador)

        #campo: genero
        self.genero = QWidget()

        self.m_input_genero = QLabel(text="Gênero: ")

        self.genero_valor = QLineEdit()

        layout = QHBoxLayout()
        layout.addWidget(self.m_input_genero)
        layout.addWidget(self.genero_valor)
        self.genero.setLayout(layout)


        # botão para recomendar o livro
        self.botao_recom= QPushButton(text="Recomende-me livros!")
        self.botao_recom.clicked.connect(self.recomendar_livros)

        # adicionando widgets para a tela principal
        layout = QVBoxLayout()
        layout.addWidget(self.inp_ano)
        layout.addWidget(self.inp_pag_n)
        layout.addWidget(self.inp_pop)
        layout.addWidget(self.inp_pub_alvo)
        layout.addWidget(self.inp_narracao)
        layout.addWidget(self.inp_idio_orign)

        # inserindo os campos para inputs dos usuario em relação ao livro 
        layout.addWidget(self.genero)
        layout.addWidget(self.tema)
        layout.addWidget(self.num_pag)
        layout.addWidget(self.ano_lanc)
        layout.addWidget(self.genero_protagonista)
        layout.addWidget(self.idioma_original)
        layout.addWidget(self.complexidade)
        layout.addWidget(self.popularidade)
        layout.addWidget(self.pub_alvo)
        layout.addWidget(self.narrador)


        layout.addWidget(self.botao_recom)
        # definindo o layout
        self.quadro_central.setLayout(layout)
    
    Slot()
    def inserir_caso(self, titulo, genero, tema, num_pag, ano, genero_prot, idioma, complexidade, popularidade, publico, narrador):
        try:
            connection = mysql.connector.connect(
                user='root', password='root', host='basededados', port="3306", database='db')
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO Livros(Titulo, Genero, Tema, NumeroDePaginas, AnoDeLancamento, GeneroProtagonista,
                                IdiomaOriginal, ComplexidadeDaLinguagem, Populariedade, PublicoAlvo, Narrador)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, (titulo, genero, tema, num_pag, ano, genero_prot, idioma, complexidade, popularidade, publico, narrador))
            connection.commit()
            connection.close()
            QMessageBox.information(self, "Sucesso", "Livro adicionado com sucesso!")
            self.voltar_para_tela_inicial()  # Função que você deve ter na interface
        except:
            QMessageBox.warning(self, "Erro", "Erro ao inserir no banco de dados.")

    Slot()
    def recomendar_livros(self):
        genero = self.genero_valor.text()
        tema = self.tema_valor.text()
        try:
            num_pag = int(self.num_pag_valor.text())
            ano = int(self.ano_valor.text())
        except ValueError:
            QMessageBox.warning(self, "Erro", "Ano e número de páginas devem ser números inteiros.")
            return
        genero_prot = self.gen_prot_valor.text()
        idioma = self.idioma_valor.text()
        complexidade = self.complexidade_valor.text()
        popularidade = self.pop_valor.text()
        publico = self.publico_valor.text()
        narrador = self.narrador_valor.text()

        try:
            p_ano_lanc = float(self.p_ano_lancamento.text())
            p_num_pag = float(self.p_pag_n.text())
            p_pop = float(self.p_pop.text())
            p_pub_alvo = float(self.p_pub_alvo.text())
            p_narracao = float(self.p_narracao.text())
        except ValueError:
            QMessageBox.warning(self, "Erro", "Todos os pesos devem ser números.")
            return
        print("Conectando à base de dados...")
        while(1):
            try:
                connection = mysql.connector.connect(
                    user='root', password='root', host='basededados', port="3306", database='db')
                break
            except:
                print("Erro ao tentar conectar com a base de dados, tentando novamente em 5 segundos!")
                time.sleep(5)
        try:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM Livros')
            livros = cursor.fetchall()
            connection.close()
        except:
            QMessageBox.warning(self, "Erro", "Erro ao conectar com o banco de dados.")
            return

        scores = []
        for livro in livros:
            score = 0
            score += self.p_gen if livro[2].lower() == genero.lower() else 0
            score += self.p_tema if livro[3].lower() == tema.lower() else 0
            score += p_num_pag if num_pag in range(int(livro[4] * 0.9), int(livro[4] * 1.1) + 1) else 0
            score += p_ano_lanc if ano in range(livro[5] - self.ano_range, livro[5] + self.ano_range + 1) else 0
            score += self.p_prot_gen if livro[6].lower() == genero_prot.lower() else 0
            score += self.p_idioma_original if livro[7].lower() == idioma.lower() else 0
            score += self.p_comp_ling if livro[8].lower() == complexidade.lower() else 0
            score += p_pop if livro[9].lower() == popularidade.lower() else 0
            score += p_pub_alvo if livro[10].lower() == publico.lower() else 0
            score += p_narracao if livro[11].lower() == narrador.lower() else 0
            scores.append((score, livro[1]))

        rank_recom = sorted(scores, key=lambda x: x[0], reverse=True)

        resultado_widget = QWidget()
        layout_result = QVBoxLayout()

        for score, titulo in rank_recom:
            info = QLabel(f"{titulo} — Score: {score:.2f}")
            botao = QPushButton("Adicionar este livro ao banco de dados")
            botao.clicked.connect(lambda _, t=titulo: self.inserir_caso(t, genero, tema, num_pag, ano, genero_prot, idioma, complexidade, popularidade, publico, narrador))
            layout_result.addWidget(info)
            layout_result.addWidget(botao)

        resultado_widget.setLayout(layout_result)
        self.setCentralWidget(resultado_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela_principal = JanelaPrinciapl()
    espaco_disp = janela_principal.screen().availableGeometry()
    janela_principal.resize(espaco_disp.width() * 2 / 3, espaco_disp.height() * 2 / 3)
    janela_principal.show()
    sys.exit(app.exec())