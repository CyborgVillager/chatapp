from kivy_source import *



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


    def join_button(self,instance):
        port = self.port.text
        ip = self.ip.text
        username = self.username.text

        # info the user will see once they have submmited the info
        print('\n')
        print(f'You are attemping to join {ip}:{port} as {username}')
        print(f'Please Stand By {username}...')

        with open('login_attempts.txt','w') as f:
            f.write(f'{ip},{port},{username}')
            f.close()



class ChatApp(App):
    # this is the init
    def build(self):
        return ConnectPage()

if __name__ =='__main__':
    ChatApp().run()