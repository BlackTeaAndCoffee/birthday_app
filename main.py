from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivymd.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import BoxLayout
from kivy.lang import Builder 
from kivy.properties import Property, NumericProperty, AliasProperty, StringProperty, ObjectProperty
from kivymd.uix.list import MDList
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout


from kivymd.uix.carousel import Carousel 

from kivymd.uix.label import MDLabel, MDIcon

import navigation_drawer as navdraw

import configparser 

import datetime 
import requests
import json
import time

cfg = configparser.ConfigParser()
cfg.read("Settings.cfg")

ip_adress_api = cfg.get("adress", "ip_adress_api")
graphql_port = cfg.get("ports", "graphql")
screen_helper = navdraw.KV
qu1 = """
  query
AllBirthdays{
listBirthdays {
    success
    errors
    birthdays {
      id
      name
      meal
      birthday
    }
  }

}
"""




query = json.dumps({'query': qu1})

try:
    r = requests.post(url = 'http://{}:{}/graphql'.format(ip_adress_api,graphql_port ), json={"operationName":"AllBirthdays","query":qu1, "variables":{}})
    birthdays = r.json()['data']['listBirthdays']['birthdays']
except Exception as e:
    print(e)
    with open("birthdays.json") as infile:
        r = json.load(infile)
    birthdays = r['listBirthdays']['birthdays']

class ScreenWidget(Screen):
    pass


class CarouselWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(CarouselWidget, self).__init__(**kwargs)
        carr = Carousel(direction='right',
            size_hint= (1,1),
            loop =True)
        carr.id = "carousel"
        
        for i in range(len(birthdays)):
            box_iter = BoxLayout(orientation = 'vertical')  
            box_iter.id = "box_" + "i" 
            l_1 = MDLabel(text=birthdays[i]["name"] + ":", font_style = "H2",color = "black", size_hint =(1,.5))
            l_2 = MDLabel(text= str(birthdays[i]["birthday"]), font_style = "H2",color = "black", size_hint =(1,.5))
            box_iter.add_widget(l_1)
            box_iter.add_widget(l_2)
            carr.add_widget(box_iter)
        
        self.add_widget(carr)

class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class MainScreen(Screen):
    pass

class ListScreen(Screen):
    pass

class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen
    def on_start(self):
        for i in range(len(birthdays)):
            self.root.ids.list_birthdays.add_widget(OneLineIconListItem(text =  birthdays[i]["name"] + ":" + birthdays[i]["birthday"]))


    def restart(self):
        print(self.root.ids.caro.children[0]._get_index())
        self.root.ids.caro.children[0].index = 0
    def add_birthdays(self, entry):
        
        
        
DemoApp().run()
