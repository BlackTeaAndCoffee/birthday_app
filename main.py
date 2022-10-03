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
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.carousel import Carousel 
from kivymd.uix.relativelayout import MDRelativeLayout
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


month_dict = ["January","February","March","April", "May", "June", "July", "August",
                      "September", "October","November","December"]

replace_year = 2000 #This is needed for sorting only in month and days, years are not to be included in the sorting.
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


class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
    # Here specify the required parameters for MDTextFieldRound:
    # [...]

class DemoApp(MDApp):

    birthdays_list = ListProperty([*birthdays])

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen
    def on_start(self):
        for i in range(len(birthdays)):
            self.root.ids.list_birthdays.add_widget(OneLineIconListItem(text =  birthdays[i]["name"] + ":" + birthdays[i]["birthday"]))
    
    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button of date picker is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''
        #self.add_birthdays([self.root.ids.name.text,value.strftime("%d-%m-%Y") ])
        self.root.ids.birthday.text = value.strftime("%d-%m-%Y")
        print(instance, value, date_range)
        print(type(instance), type(value), type(date_range))

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button of datepicker is clicked.''' 
    
    def screen_title(self, screen):
        self.root.ids.toolbar.title = screen

    def add_entry(self, name, birthday):
        last_id = birthdays.len()
        entry = {"id": str(last_id + 1),
                  "name": "" ,
                  "birthday":"" ,
                  "meal":"" }

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
    def restart(self):
        self.root.ids.caro.children[0].index = 0
    def reorder_carousel(self):
        #self.root.ids.caro.children[0].slides.sort(key= lambda slide: datetime.datetime.strptime(slide.children[0].text, '%d-%m-%Y').date().replace(year=replace_year))

        self.root.ids.caro.children[0].slides.sort(key= lambda slide: slide.id.replace(year=replace_year))
        today_date = datetime.datetime.today().date().replace(year=replace_year)
        
        #self.root.ids.caro.children[0].slides.insert(-1,self.root.ids.caro.children[0].slides.pop(0))
        #obj_to_end =  self.root.ids.caro.children[0].slides.pop(0)
        #self.root.ids.caro.children[0].slides.insert(len(self.root.ids.caro.children[0].slides), obj_to_end)
        help_list =[*self.root.ids.caro.children[0].slides] 
        
        for k,slide in enumerate(self.root.ids.caro.children[0].slides):
#            cand = datetime.datetime.strptime(slide.children[0].text, '%d-%m-%Y').date().replace(year=replace_year)

            cand = slide.id.replace(year=replace_year)

            if today_date > cand:
                help_list.insert(len(help_list),help_list.pop(0))
                print("yay")
                print(today_date, cand)
            else: 
                break
        self.root.ids.caro.children[0].slides = [*help_list]

        #print(self.root.ids.caro.children[0].slides[0].children[0].text)
    
    def add_birthdays(self, entry):
 
        if entry[0] == "":
            self.root.ids.name.helper_text = "Name Field cannot be empty."
        else:
            box_iter = BoxLayout(orientation = 'vertical')  
            
            date =  datetime.datetime.strptime(entry[1], '%d-%m-%Y').date()
            
            box_iter = BoxLayout(orientation = 'vertical')
            box_iter.id = date
            #box_iter.id = "box_" + "i"

 
            l_1 = MDLabel(text=entry[0] + ":", font_style = "H2",color = "black", size_hint =(1,.5))
            l_2 = MDLabel(text= str(date.day) + "." + month_dict[date.month -1], font_style = "H2",color = "black", size_hint =(1,.5))
            box_iter.add_widget(l_1)
            box_iter.add_widget(l_2)

            self.root.ids.caro.children[0].add_widget(box_iter)
            self.reorder_carousel()
class CarouselWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(CarouselWidget, self).__init__(**kwargs)
        carr = Carousel(direction='right',
            size_hint= (1,1),
            loop =True)
        carr.id = "carousel"

        print(birthdays) 
        for i, birthday in enumerate(birthdays):
           
            print("check",birthday["birthday"])
            date =  datetime.datetime.strptime(birthday["birthday"], '%d-%m-%Y').date()
            #ident = StringProperty()
            ident = birthday["birthday"]  
            box_iter = BoxLayout(orientation = 'vertical')
            box_iter.id = date
            #box_iter.id = "box_" + "i"
            l_1 = MDLabel(text=birthday["name"] + ":", font_style = "H2",color = "black", size_hint =(1,.5))
            l_2 = MDLabel(text= str(date.day) + "." + month_dict[date.month -1], font_style = "H2",color = "black", size_hint =(1,.5))
            box_iter.add_widget(l_1)
            box_iter.add_widget(l_2)
            carr.add_widget(box_iter)
        
        self.add_widget(carr)       
        
DemoApp().run()
