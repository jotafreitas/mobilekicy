import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

class firstBotao(App):
    def build(self):
        layout = BoxLayout(orientation = 'vertical')
        grid = GridLayout(cols = 2, size_hint = (1,1))

        self.image1 = Image(source = 'catcat.jpg', opacity = 0)
        self.image2 = Image(source = 'dogdog.jpg', opacity = 0)
        grid.add_widget(self.image1)
        grid.add_widget(self.image2)

        button1  = Button(text='Gato')
        grid.add_widget(button1)
        button2  = Button(text='Cachorro')
        grid.add_widget(button2)
        button1.bind(on_press=self.aparece_cachorro)
        button2.bind(on_press=self.aparece_gato)
        layout.add_widget(grid)
        return layout

    def aparece_gato(self,gato):
        self.image1.opacity=0
        self.image2.opacity=100

    def aparece_cachorro(self,cachorro):
        self.image1.opacity=100
        self.image2.opacity=0
        

if __name__ == '__main__':    
    firstBotao().run()