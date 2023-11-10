import mysql.connector
import kivy
from kivy.app import App
from edson import MostrarTudo
from edsonehudson import DupraDeDois
from kivy.uix.screenmanager import ScreenManager
from mostrartudo import Select
class Principal(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(DupraDeDois(name = 'inicio'))
        sm.add_widget(MostrarTudo(name = 'segunda'))
        #sm.add_widget(Select(name = 'terceira'))
        return sm
    
if __name__ == '__main__':
    Principal().run()