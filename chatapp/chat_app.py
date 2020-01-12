from kivy_source import *


class ConnectPage(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        # widget 0
        self.add_widget(Label(text='IP: '))
        self.ip = TextInput(multiline=False)
        self.add_widget(self.ip)

        # widget 1
        self.add_widget(Label(text='Port: '))
        self.port = TextInput(multiline=False)
        self.add_widget(self.port)

        # widget 2
        self.add_widget(Label(text='UserName: '))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        # Button
        self.join = Button(text='Join')
        self.add_widget(Label())
        self.add_widget(self.join)







class ChatApp(App):
    # this is the init
    def build(self):
        return ConnectPage()

if __name__ =='__main__':
    ChatApp().run()