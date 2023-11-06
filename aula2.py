'''import kivy
from kivymd.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class firstBotao(App):
    def build(self):
        layout = BoxLayout(orientation = 'vertical')
        button = Button(text = "Olá, eu sou o botão",size_hint = (0.5 , 0.5), pos_hint = {'center_x':0.5,'center_y':0.5})
        button.bind(on_press=self.sumir)
        layout.add_widget(button)
        return layout
    
    def sumir(self,button):
        button.opacity=0

if __name__ == '__main__':    
    firstBotao().run()'''


import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class firstBotao(App):
    def build(self):
        layout = BoxLayout(orientation = 'vertical')
        grid = GridLayout(cols = 1, size_hint = (1, 2.2))

        text_input = TextInput(text = 'Digite seu Nome')
        grid.add_widget(text_input)

        button1 = Button(text = 'Login')
        grid.add_widget(button1)

        button2 = Button(text = 'Cancelar')
        grid.add_widget(button2)

        layout.add_widget(grid)

        return layout
    

if __name__ == '__main__':    
    firstBotao().run()