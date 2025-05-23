from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import streamlit as st


class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(orientation='vertical', **kwargs)

        self.username_input = TextInput(hint_text='Username', multiline=False)
        self.password_input = TextInput(hint_text='Password', multiline=False, password=True)
        self.login_button = Button(text='Login')
        self.login_button.bind(on_press=self.validate_credentials)

        self.add_widget(Label(text='Login'))
        self.add_widget(self.username_input)
        self.add_widget(self.password_input)
        self.add_widget(self.login_button)

    def validate_credentials(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        # Simple hardcoded check (for demo)
        if username == 'admin' and password == '1234':
            self.show_popup('Success', 'Login successful!')
        else:
            self.show_popup('Error', 'Invalid username or password.')

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message),
                      size_hint=(None, None), size=(300, 200))
        popup.open()


class LoginApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    LoginApp().run()
