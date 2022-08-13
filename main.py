from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder 
from kivy.properties import Property, NumericProperty, AliasProperty, StringProperty

from kivy.uix.carousel import Carousel 

from kivymd.uix.label import MDLabel, MDIcon

import configparser 

import datetime 
import requests
import json
import time

cfg = configparser.ConfigParser()
cfg.read("Settings.cfg")

ip_adress_api = cfg.get("adress", "ip_adress_api")
graphql_port = cfg.get("ports", "graphql")
screen_helper = """
Screen:
    BoxLayout:
        id: box
        orientation : 'vertical'  
        MDToolbar: 
            title:"birthdays"
            elevation:10
        
        CarouselWidget:
            id: caro
        MDBottomAppBar:
            MDTopAppBar:
                title: "Title"
                icon: "git"
                type: "bottom"
                on_action_button: app.restart()
                mode: "end"


"""

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
r = requests.post(url = 'http://{}:{}/graphql'.format(ip_adress_api,graphql_port ), json={"operationName":"AllBirthdays","query":qu1, "variables":{}})

birthdays = r.json()['data']['listBirthdays']['birthdays']


class ScreenWidget(Screen):
    pass


class CarouselWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(CarouselWidget, self).__init__(**kwargs)
        carr = Carousel(direction='right',
            size_hint= (1,1),
            loop =False)
        
        for i in range(len(birthdays)):
            box_iter = BoxLayout(orientation = 'vertical')  
            box_iter.id = "box_" + "i" 
            l_1 = MDLabel(text=birthdays[i]["name"] + ":", font_style = "H2",color = "black", size_hint =(1,.5))
            l_2 = MDLabel(text= str(birthdays[i]["birthday"]), font_style = "H2",color = "black", size_hint =(1,.5))
            box_iter.add_widget(l_1)
            box_iter.add_widget(l_2)
            carr.add_widget(box_iter)
        
        self.add_widget(carr)

class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

    def restart(self):
        print(self.root.ids.caro.children[0]._get_index())
        self.root.ids.caro.children[0].index = 0
        #self.root.ids.caro.bind(index = 0)


        #print(self.root.ids.caro.index)

        #self.root.ids.caro.load_slide()
DemoApp().run()
