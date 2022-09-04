from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivymd.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import BoxLayout
from kivy.lang import Builder 
from kivy.properties import Property, NumericProperty, AliasProperty, StringProperty, ObjectProperty, ListProperty
from kivymd.uix.list import MDList
from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField

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
        r= json.load(infile)
    birthdays = r["birthdays"]
class ScreenWidget(Screen):
    pass


class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()
class MainScreen(Screen):
    pass

class ListScreen(Screen):
    pass
class EntryScreen(Screen):
    pass

class DemoApp(MDApp):

    birthdays_list = ListProperty([*birthdays])

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen
    def on_start(self):
        for i in range(len(birthdays)):
            self.root.ids.list_birthdays.add_widget(OneLineIconListItem(text =  birthdays[i]["name"] + ":" + birthdays[i]["birthday"]))
    
    def screen_title(self, screen):
        self.root.ids.toolbar.title = screen

    def add_entry(self, name, birthday):
        last_id = birthdays.len()
        entry = {"id": str(last_id + 1),
                  "name": "" ,
                  "birthday":"" ,
                  "meal":"" }


    def restart(self):
        self.root.ids.caro.children[0].index = 0
    def reorder_carousel(self):
        replace_year = 2000 #This is needed for sorting only in month and days, years are not to be included in the sorting.
        self.root.ids.caro.children[0].slides.sort(key= lambda slide: datetime.datetime.strptime(slide.children[0].text, '%d-%m-%Y').date().replace(year=replace_year))
        today_date = datetime.datetime.today().date().replace(year=replace_year)
        
        #self.root.ids.caro.children[0].slides.insert(-1,self.root.ids.caro.children[0].slides.pop(0))
        #obj_to_end =  self.root.ids.caro.children[0].slides.pop(0)
        #self.root.ids.caro.children[0].slides.insert(len(self.root.ids.caro.children[0].slides), obj_to_end)
        help_list =[*self.root.ids.caro.children[0].slides] 
        
        for k,slide in enumerate(self.root.ids.caro.children[0].slides):
            cand = datetime.datetime.strptime(slide.children[0].text, '%d-%m-%Y').date().replace(year=replace_year)
            if today_date > cand:
                help_list.insert(len(help_list),help_list.pop(0))
                print("yay")
                print(today_date, cand)
            else: 
                break
        self.root.ids.caro.children[0].slides = [*help_list] 
        #print(self.root.ids.caro.children[0].slides[0].children[0].text)
    
    def add_birthdays(self, entry):
        box_iter = BoxLayout(orientation = 'vertical')  
        l_1 = MDLabel(text=entry[0] + ":", font_style = "H2",color = "black", size_hint =(1,.5))
        l_2 = MDLabel(text= entry[1],  font_style = "H2",color = "black", size_hint =(1,.5))
        box_iter.add_widget(l_1)
        box_iter.add_widget(l_2)

        self.root.ids.caro.children[0].add_widget(box_iter)
        
class CarouselWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(CarouselWidget, self).__init__(**kwargs)
        carr = Carousel(direction='right',
            size_hint= (1,1),
            loop =True)
        carr.id = "carousel"
        for i in range(len(birthdays)):
            box_iter = BoxLayout(orientation = 'vertical')  
            #box_iter.id = "box_" + "i" 
            l_1 = MDLabel(text=birthdays[i]["name"] + ":", font_style = "H2",color = "black", size_hint =(1,.5))
            l_2 = MDLabel(text= str(birthdays[i]["birthday"]), font_style = "H2",color = "black", size_hint =(1,.5))
            box_iter.add_widget(l_1)
            box_iter.add_widget(l_2)
            carr.add_widget(box_iter)
        
        self.add_widget(carr)       
        
DemoApp().run()
