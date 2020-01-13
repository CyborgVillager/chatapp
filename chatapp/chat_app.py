## Imports ##
from kivy_source import *
from socket_client import *
from socket_server import *
## Imports ##



class ConnectPage(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols = 2
        # check if file exist
        if os.path.isfile('login_attempts.txt'):
            with open('login_attempts.txt', 'r') as f:
                d = f.read().split(',')
                prev_ip = d[0]
                prev_port = d[1]
                prev_username = d[2]
        else:
            prev_ip = ''
            prev_port = ''
            prev_username = ''
    ## Widgets & Buttons ##
        # widget 0
        self.add_widget(Label(text='IP: '))
        self.ip = TextInput(text=prev_ip,multiline=False)
        self.add_widget(self.ip)

        # widget 1
        self.add_widget(Label(text='Port: '))
        self.port = TextInput(text=prev_port,multiline=False)
        self.add_widget(self.port)

        # widget 2
        self.add_widget(Label(text='UserName: '))
        self.username = TextInput(text=prev_username,multiline=False)
        self.add_widget(self.username)

        # Button
        self.join = Button(text='Join')
        self.add_widget(Label())
        self.add_widget(self.join)
        # connecting w/ def join_button
        self.join.bind(on_press=self.join_button)
    ## Widgets & Buttons ##

    def join_button(self,instance):
        port = self.port.text
        ip = self.ip.text
        username = self.username.text

        # info the user will see once they have submmited the info

        with open('login_attempts.txt','w') as f:
            f.write(f'{ip},{port},{username}')
        information = f'You are attemping to join {ip}:{port} as {username}' + '\n' + 'Please Stand By!' + '\n' + '^_^'
        chat_app.info_page.update_info(information)

        #bring the screen to be seen
        chat_app.screen_manager.current = 'Information'
        # connect within 1 second
        Clock.schedule_once(self.connect, 1)

    # _ used to pass the # of seconds have passed, currently its 1 second
    # this will connect to the server
    def connect(self, _):
        # Establish Connections
        port = int(self.port.text)
        ip = self.ip.text
        username = self.username.text

        # this will return if the informaiton is not working at the moment
        if not socket_client.connect(ip, port, username, show_error):
            return

        # if the user is able to connect to the program chat feature
        # Page will be created for the chat/join
        chat_app.create_chat_page()
        chat_app.screen_manager.current = 'Chat'

# Information Screen
class InfoPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.message = Label(halign='center',valign='middle', font_size=30)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)
    def update_info(self,message):
        self.message.text = message

    # takes up the page to show the text
    def update_text_width(self,*_):
        self.message.text_size = (self.message.width*.9,None)

class ChatPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='Hello User'))


class ChatApp(App):
    # this is the init / chat info looking for
    # connections to the information
    def build(self):
        self.screen_manager = ScreenManager()
        self.connect_page = ConnectPage()
        screen = Screen(name='Connect')
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        self.info_page = InfoPage()
        screen = Screen(name='Information')
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager
    # once user has connect a chat page will be created
    def create_chat_page(self):
        self.chat_page = ChatPage()
        screen = Screen(name='Chat')
        screen.add_widget(self.chat_page)
        self.screen_manager.add_widget(screen)

    # Show the user an error
def show_error(message):
        chat_app.info_page.update_info(message)
        chat_app.screen_manager.current = 'Information'
        Clock.schedule_once(sys.exit, 10)

if __name__ =='__main__':
  chat_app = ChatApp()
  chat_app.run()