import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

kivy.require('2.1.0') # Укажите вашу версию Kivy, если она отличается

class TicTacToeGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3 # Устанавливаем количество колонок
        self.rows = 3 # Устанавливаем количество строк

        # Создаем и добавляем 9 кнопок
        for _ in range(9):
            button = Button(
                text='', # Изначально текст пустой
                font_size=50 # Устанавливаем размер шрифта для символов X/O
                # Здесь можно добавить привязку к функции обработки нажатия, например:
                # on_press=self.on_button_press
            )
            self.add_widget(button)


class TicTacToeApp(App):
    def build(self):
        return TicTacToeGrid()

if __name__ == '__main__':
    TicTacToeApp().run()