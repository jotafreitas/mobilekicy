import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
import mysql.connector

class Select(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
        print("mostrar tudo")
        consulta = "SELECT * FROM duplas;"
        self.cursor.execute(consulta)
        linhas = self.cursor.fetchall()
        for linha in linhas:
            self.lbl_select=Label(text= f"ID: {linha[0]}\n Nome da Dupla: {linha[1]}\n Ano de Início: {linha[2]}\nCidade Natal: {linha[3]}\nEm Atividade: {linha[4]}")
            self.layout.add_widget(self.lbl_select)
            self.conexao.commit()
        self.add_widget(self.layout)
        print("deu certo")