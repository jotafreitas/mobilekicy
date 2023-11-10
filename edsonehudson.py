import mysql.connector
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen

class DupraDeDois(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        host = "10.28.1.197"
        usuario = "suporte"
        senha = "suporte"
        banco_de_dados = "EdsonANDHudson"

        # Conectando ao banco de dados
        self.conexao = mysql.connector.connect(
            host=host,
            user=usuario,
            password=senha,
            database=banco_de_dados
        )

        self.cursor = self.conexao.cursor()
        print(self.conexao)
        layout = BoxLayout(orientation = 'vertical')
        grid = GridLayout(cols = 1, size_hint = (1,1))

        # Criando os INPUTS DO USUÁRIO
        self.nome_dupla = TextInput(hint_text="Digite o nome da dupla: ")
        grid.add_widget(self.nome_dupla)

        self.ano_inicio = TextInput(hint_text="Digite o ano de início: ")
        grid.add_widget(self.ano_inicio)

        self.cidade_natal= TextInput(hint_text="Cidade Natal: ")
        grid.add_widget(self.cidade_natal)

        self.em_atividade= TextInput(hint_text="Em Atividade (S/N): ")
        grid.add_widget(self.em_atividade)
       
       
        self.btn = Button(text='CADASTRAR!')
        grid.add_widget(self.btn)
        self.btn.bind(on_press=self.minha_funcao)

        self.btn2 = Button(text='MOSTRAR LISTA')
        grid.add_widget(self.btn2)
        self.btn2.bind(on_press=self.tela2)


        layout.add_widget(grid)
        self.add_widget(layout)

    def minha_funcao(self, aiaiai):
        print("carregando...")
        nome_dupla = self.nome_dupla
        ano_inicio = self.ano_inicio
        cidade_natal = self.cidade_natal
        em_atividade = self.em_atividade

        consulta = "INSERT INTO duplas (nome_dupla, ano_inicio,cidade_natal,em_atividade) VALUES (%s,%s,%s,%s)"
        valores = (nome_dupla.text, ano_inicio.text, cidade_natal.text, em_atividade.text)
        self.cursor.execute(consulta,valores)
        self.conexao.commit()
        #conexao.close()
        print("agora foi")
    
    def tela2(self, instance):
        self.manager.current = 'segunda'