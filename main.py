from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

# Словарь замены японских символов на русские
replacement_map = {
    'カ': 'А',
    'キ': 'Б',
    'ク': 'В',
    'ケ': 'Г',
    'コ': 'Д',
    # Добавь больше замен по необходимости
}

class ConverterLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.input = TextInput(hint_text='Введите японский текст', multiline=True, size_hint_y=0.5)
        self.output = Label(text='', size_hint_y=0.5)
        self.input.bind(text=self.on_text_change)
        self.add_widget(self.input)
        self.add_widget(self.output)

    def on_text_change(self, instance, value):
        result = ''.join([replacement_map.get(ch, ch) for ch in value])
        self.output.text = result

class JpToRuApp(App):
    def build(self):
        return ConverterLayout()

if __name__ == '__main__':
    JpToRuApp().run()
