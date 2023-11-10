import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
import mysql.connector

class MostrarTudo(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
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
        self.layout = BoxLayout(orientation = 'vertical')
        self.grid = GridLayout(cols = 3, size_hint = (1,1))

        self.btn = Button(text='MOSTRAR TUDO')
        self.grid.add_widget(self.btn)
        self.btn.bind(on_press=self.showall)

        print("mostrar tudo")
        consulta = "SELECT * FROM duplas;"
        self.cursor.execute(consulta)
        linhas = self.cursor.fetchall()
        for linha in linhas:
            self.lbl_select=Label(text= f"ID: {linha[0]}\n Nome da Dupla: {linha[1]}\n Ano de Início: {linha[2]}\nCidade Natal: {linha[3]}\nEm Atividade: {linha[4]}")
            #self.layout.add_widget(self.lbl_select)
            self.grid.add_widget(self.lbl_select)
            self.conexao.commit()
        

        self.layout.add_widget(self.grid)
        
        self.add_widget(self.layout)
    
    def showall(self, instance):
        self.manager.current = 'terceira'