import kivy
from kivy.app import App

# text for screen
from kivy.uix.label import Label

# organize the widgets
from kivy.uix.gridlayout import GridLayout

# text for user
from kivy.uix.textinput import TextInput

# button
from kivy.uix.button import Button

# screen manager
from kivy.uix.screenmanager import Screen, ScreenManager

# time
from kivy.clock import Clock

# for socket client info
import socket_client

# Import Os
import os

# Import Sys
import sys


# Required/current version of the program
kivy.require('1.11.1')