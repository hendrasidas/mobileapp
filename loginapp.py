from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.clock import Clock

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'login'
        
        # Main layout
        layout = BoxLayout(orientation='vertical', padding=dp(40), spacing=dp(20))
        
        # Add background color
        with layout.canvas.before:
            Color(0.31, 0.78, 0.74, 1)  # Teal color
            self.rect = RoundedRectangle(size=layout.size, pos=layout.pos)
            layout.bind(size=self._update_rect, pos=self._update_rect)
        
        # Logo/Icon area (simplified)
        logo_layout = BoxLayout(size_hint_y=0.4)
        logo_label = Label(
            text='♥\n\nAPP NAME',
            font_size=dp(32),
            color=(1, 1, 1, 1),
            halign='center',
            text_size=(None, None)
        )
        logo_layout.add_widget(logo_label)
        
        # Input fields
        self.username_input = TextInput(
            hint_text='Username',
            size_hint_y=None,
            height=dp(50),
            background_color=(1, 1, 1, 0.9),
            foreground_color=(0, 0, 0, 1),
            multiline=False
        )
        
        self.password_input = TextInput(
            hint_text='Password',
            password=True,
            size_hint_y=None,
            height=dp(50),
            background_color=(1, 1, 1, 0.9),
            foreground_color=(0, 0, 0, 1),
            multiline=False
        )
        
        # Login button
        login_btn = Button(
            text='Login',
            size_hint_y=None,
            height=dp(50),
            background_color=(0.2, 0.6, 0.6, 1)
        )
        login_btn.bind(on_press=self.login)
        
        # Forgot password
        forgot_label = Label(
            text='Forgot password?',
            size_hint_y=None,
            height=dp(30),
            color=(1, 1, 1, 0.8)
        )
        
        # Add widgets
        layout.add_widget(logo_layout)
        layout.add_widget(self.username_input)
        layout.add_widget(self.password_input)
        layout.add_widget(login_btn)
        layout.add_widget(forgot_label)
        
        self.add_widget(layout)
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
    def login(self, instance):
        # Simple validation
        if self.username_input.text and self.password_input.text:
            self.manager.current = 'search'
        else:
            popup = Popup(title='Error', content=Label(text='Please fill all fields'), size_hint=(0.8, 0.4))
            popup.open()

class SearchScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'search'
        
        # Main layout
        layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        
        # Header
        header = BoxLayout(size_hint_y=None, height=dp(60), spacing=dp(10))
        header.add_widget(Button(text='<', size_hint_x=None, width=dp(50)))
        header.add_widget(Label(text='SEARCH FILTER', color=(0.31, 0.78, 0.74, 1), bold=True))
        header.add_widget(Button(text='⋮', size_hint_x=None, width=dp(50)))
        
        # Filter options
        filter_layout = BoxLayout(size_hint_y=None, height=dp(50), spacing=dp(5))
        filter_layout.add_widget(Button(text='Option 1', background_color=(0.8, 0.8, 0.8, 1)))
        filter_layout.add_widget(Button(text='Option 2', background_color=(0.31, 0.78, 0.74, 1)))
        filter_layout.add_widget(Button(text='Option 3', background_color=(0.8, 0.8, 0.8, 1)))
        
        # Scroll view for charity items
        scroll = ScrollView()
        scroll_layout = GridLayout(cols=1, spacing=dp(10), size_hint_y=None)
        scroll_layout.bind(minimum_height=scroll_layout.setter('height'))
        
        # Add charity items
        charities = [
            ('Help Lorem Ipsum 01', 'Lorem ipsum dolor sit amet, adipiscing elit, sed diam nonummy nibh euismod'),
            ('Help Lorem Ipsum 02', 'Lorem ipsum dolor sit amet, adipiscing elit, sed diam nonummy nibh euismod'),
            ('Help Lorem Ipsum 03', 'Lorem ipsum dolor sit amet, adipiscing elit, sed diam nonummy nibh euismod'),
            ('Help Lorem Ipsum 04', 'Lorem ipsum dolor sit amet, adipiscing elit, sed diam nonummy nibh euismod')
        ]
        
        for title, desc in charities:
            item = self.create_charity_item(title, desc)
            scroll_layout.add_widget(item)
        
        scroll.add_widget(scroll_layout)
        
        # Add all widgets
        layout.add_widget(header)
        layout.add_widget(filter_layout)
        layout.add_widget(scroll)
        
        self.add_widget(layout)
    
    def create_charity_item(self, title, description):
        item_layout = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=dp(100),
            padding=dp(10),
            spacing=dp(10)
        )
        
        # Add background
        with item_layout.canvas.before:
            Color(1, 1, 1, 1)
            self.item_rect = RoundedRectangle(size=item_layout.size, pos=item_layout.pos, radius=[10])
            item_layout.bind(size=self._update_item_rect, pos=self._update_item_rect)
        
        # Icon placeholder
        icon_btn = Button(
            text='📷',
            size_hint_x=None,
            width=dp(60),
            background_color=(0.31, 0.78, 0.74, 1)
        )
        icon_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'donate'))
        
        # Text content
        text_layout = BoxLayout(orientation='vertical', spacing=dp(5))
        title_label = Label(
            text=title,
            color=(0.31, 0.78, 0.74, 1),
            bold=True,
            text_size=(dp(200), None),
            halign='left'
        )
        desc_label = Label(
            text=description,
            color=(0.5, 0.5, 0.5, 1),
            text_size=(dp(200), None),
            halign='left'
        )
        
        text_layout.add_widget(title_label)
        text_layout.add_widget(desc_label)
        
        item_layout.add_widget(icon_btn)
        item_layout.add_widget(text_layout)
        
        return item_layout
    
    def _update_item_rect(self, instance, value):
        self.item_rect.pos = instance.pos
        self.item_rect.size = instance.size

class DonateScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'donate'
        
        # Main layout
        layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(20))
        
        # Header
        header = BoxLayout(size_hint_y=None, height=dp(60), spacing=dp(10))
        back_btn = Button(text='<', size_hint_x=None, width=dp(50))
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'search'))
        header.add_widget(back_btn)
        header.add_widget(Label(text='DONATE', color=(0.31, 0.78, 0.74, 1), bold=True))
        header.add_widget(Button(text='⋮', size_hint_x=None, width=dp(50)))
        
        # Donation info
        donate_title = Label(
            text='Make a donation to',
            size_hint_y=None,
            height=dp(40),
            color=(0.31, 0.78, 0.74, 1),
            font_size=dp(20)
        )
        
        # Charity info card
        charity_layout = BoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height=dp(80),
            padding=dp(15),
            spacing=dp(15)
        )
        
        with charity_layout.canvas.before:
            Color(1, 1, 1, 1)
            self.charity_rect = RoundedRectangle(size=charity_layout.size, pos=charity_layout.pos, radius=[10])
            charity_layout.bind(size=self._update_charity_rect, pos=self._update_charity_rect)
        
        charity_icon = Button(
            text='📷',
            size_hint_x=None,
            width=dp(60),
            background_color=(0.31, 0.78, 0.74, 1)
        )
        
        charity_text = Label(
            text='Help Lorem Ipsum 01\nLorem ipsum dolor sit amet, adipiscing elit, sed diam nonummy nibh euismod',
            color=(0.31, 0.78, 0.74, 1),
            text_size=(dp(200), None),
            halign='left'
        )
        
        charity_layout.add_widget(charity_icon)
        charity_layout.add_widget(charity_text)
        
        # Payment section
        payment_label = Label(
            text='Select Card',
            size_hint_y=None,
            height=dp(30),
            color=(0.31, 0.78, 0.74, 1)
        )
        
        # Card display
        card_btn = Button(
            text='💳 VISA',
            size_hint_y=None,
            height=dp(60),
            background_color=(0.31, 0.78, 0.74, 1)
        )
        
        # Amount input
        self.amount_input = TextInput(
            hint_text='Select Amount',
            size_hint_y=None,
            height=dp(50),
            background_color=(0.9, 0.9, 0.9, 1),
            multiline=False
        )
        
        # Donate button
        donate_btn = Button(
            text='Send Donation',
            size_hint_y=None,
            height=dp(60),
            background_color=(0.31, 0.78, 0.74, 1),
            color=(1, 1, 1, 1)
        )
        donate_btn.bind(on_press=self.send_donation)
        
        # Add all widgets
        layout.add_widget(header)
        layout.add_widget(donate_title)
        layout.add_widget(charity_layout)
        layout.add_widget(payment_label)
        layout.add_widget(card_btn)
        layout.add_widget(self.amount_input)
        layout.add_widget(donate_btn)
        
        self.add_widget(layout)
    
    def _update_charity_rect(self, instance, value):
        self.charity_rect.pos = instance.pos
        self.charity_rect.size = instance.size
    
    def send_donation(self, instance):
        if self.amount_input.text:
            popup = Popup(
                title='Success!',
                content=Label(text=f'Donation of ${self.amount_input.text} sent successfully!'),
                size_hint=(0.8, 0.4)
            )
            popup.open()
        else:
            popup = Popup(
                title='Error',
                content=Label(text='Please enter donation amount'),
                size_hint=(0.8, 0.4)
            )
            popup.open()

class DonationApp(App):
    def build(self):
        # Create screen manager
        sm = ScreenManager()
        
        # Add screens
        sm.add_widget(LoginScreen())
        sm.add_widget(SearchScreen())
        sm.add_widget(DonateScreen())
        
        return sm

if __name__ == '__main__':
    DonationApp().run()
Made with
