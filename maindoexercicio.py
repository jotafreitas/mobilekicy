import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import random

kivy.require('1.11.1')  # Substitua a versão pelo seu próprio Kivy

class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.secret_number = random.randint(1, 50)
        self.attempts = 0

        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Tente adivinhar o número (1-50):")
        self.input = TextInput(multiline=False)
        self.check_button = Button(text="Verificar")
        self.check_button.bind(on_press=self.check_guess)

        self.layout.add_widget(self.label)
        self.layout.add_widget(self.input)
        self.layout.add_widget(self.check_button)

        self.add_widget(self.layout)

    def check_guess(self, instance):
        guess = int(self.input.text)
        self.attempts += 1

        if guess < self.secret_number:
            self.label.text = f"Tente um número maior! Tentativas: {self.attempts}"
        elif guess > 50:
            self.label.text = f'Apenas números menores que 50'
        elif guess > self.secret_number:
            self.label.text = f"Tente um número menor! Tentativas: {self.attempts}"
        else:
            self.label.text = f"Parabéns! Você adivinhou o número em {self.attempts} tentativas."
            self.input.text = ""
            self.secret_number = random.randint(1, 100)
            self.attempts = 0

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        exit_button = Button(text = 'Fechar')
        layout.add_widget(exit_button)
        start_button = Button(text="Iniciar Jogo")
        start_button.bind(on_press=self.start_game)
        exit_button.bind(on_press = self.exit_game)
        layout.add_widget(Label(text="Bem-vindo ao Jogo de Adivinhação!"))
        layout.add_widget(start_button)
        self.add_widget(layout)

    def exit_game(self, instance):
        App.get_running_app().stop()


        App.get_running_app()

        App.get_running_app

        App.get
        
    def start_game(self, instance):
        self.manager.current = 'game'

class GuessingGameApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(GameScreen(name='game'))
        
        return sm

if __name__ == '__main__':
    GuessingGameApp().run()

        
       
# Declare both screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm

if __name__ == '__main__':
    TestApp().run()
