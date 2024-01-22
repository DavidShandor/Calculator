from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class CalculatorApp(App):
    def build(self):
        self.calculation = "0"
        layout = GridLayout(cols=4, spacing=10, padding=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]

        for button in buttons:
            layout.add_widget(Button(text=button, on_press=self.on_button_press))

        return layout

    def on_button_press(self, instance):
        button_value = instance.text

        if button_value == "=":
            try:
                self.calculation = str(eval(self.calculation))
            except Exception as e:
                self.calculation = "Error"
        elif button_value == "C":
            self.calculation = "0"
        else:
            if self.calculation == "0" or self.calculation == "Error":
                self.calculation = button_value
            else:
                self.calculation += button_value


if __name__ == '__main__':
    CalculatorApp().run()
