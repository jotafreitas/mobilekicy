from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager

from random import randint

class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.play_button = Button(text='Jogar', font_size=20)
        self.play_button.bind(on_press=self.switch_to_game)
        self.exit_button = Button(text='Sair', font_size=20)
        self.exit_button.bind(on_press=App.get_running_app().stop)
        layout.add_widget(self.play_button)
        layout.add_widget(self.exit_button)
        self.add_widget(layout)

    def switch_to_game(self, *args):
        self.manager.current = 'game'