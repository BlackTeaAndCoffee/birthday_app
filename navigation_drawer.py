KV = """
<ContentNavigationDrawer>:
    orientation: 'vertical'
    padding: "8dp"
    spacing: "8dp"
    id: content

    MDTextButton:
        id: main_button
        text: "Liste"
        on_press: root.screen_manager.current = "list"
        on_release : app.screen_title("List View")

    MDTextButton:
        id: list_button
        text: "Main Page"
        on_press: root.screen_manager.current = "main"
        on_release : app.screen_title("Focus View")
    MDTextButton:
        text: "Add Entry"
        id: "entry_button"
        on_press: root.screen_manager.current = "entry"
        on_release : app.screen_title("Add Entry")


    ScrollView:
        MDList:
            OneLineIconListItem:
                text: "Profile"
            
                IconLeftWidget:
                    icon: "face-profile"
                    
            
                    
            OneLineIconListItem:
                text: "Upload"
            
                IconLeftWidget:
                    icon: "upload"
                    
            
            OneLineIconListItem:
                text: "Logout"
            
                IconLeftWidget:
                    icon: "logout"
 

<ClickableTextFieldRound>:
    size_hint_y: None
    height: text_field.height
    size_hint_x: .7
    pos_hint: {"center_x": .5, "center_y": .4}                            
    MDTextField:
        id: text_field
        hint_text: root.hint_text
        text: root.text
        mode:'rectangle' 

    MDIconButton:
        icon: "calendar"
        pos_hint: {"center_y": .5}
        pos: text_field.width - self.width + dp(8), 0
        theme_text_color: "Hint"
        on_release:
            #self.icon = "eye" if self.icon == "eye-off" else "eye-off"
            #text_field.password = False if text_field.password is True else True
            app.show_date_picker()


Screen:
    id: windscreen
    MDBoxLayout:
        id: bigbox
        orientation: 'vertical'
        MDTopAppBar:
            id: toolbar
            title: "Focus View"
            pos_hint:{"top":1}
            elevation:10

        MDNavigationLayout:
            id:nav_layout

            MDScreenManager:

                x: toolbar.height
                pos:0, 100

                id: screen_manager
                MainScreen:
                    pos:root.pos
                    name:"main"
                    CarouselWidget: 
                        id: caro
                      


                ListScreen:
                    name: "list"
                    BoxLayout:
                        id : listbox
                        orientation: 'vertical'
                        ScrollView:
                            MDList:
                                id:list_birthdays
                EntryScreen:
                    name: "entry"
                    FloatLayout:
                        id:entrybox
                        #padding :"20dp"
                        orientation: 'vertical'
                        MDTextField:
                            id: name
                            hint_text: "Name"
                            mode:'rectangle'
                            pos_hint: {'x':0.15, 'y':0.6}
                            size_hint_x : .7
                        ClickableTextFieldRound:
                            id:birthday
                            #size_hint_x: None
                            hint_text: "Birthday"
#                       MDRaisedButton:
#                           id:birthday
#                           text:'Birthday'
#                           pos_hint: {'x':0.15, 'y':0.4}
#                           on_release: app.show_date_picker()
                        MDRaisedButton:
                            id: AddButton
                            text:"Add Entry"
                            md_bg_color:0.5,0.8,0.7,1
                            pos_hint: {'x':0.15, 'y':0.2}
                            on_release:app.add_birthdays([root.ids.name.text, root.ids.birthday.text])
            MDNavigationDrawer:
                

                id: nav_drawer

                ContentNavigationDrawer:
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer
        MDBottomAppBar:
            id:bottom_bar

            MDTopAppBar:
                title: "Birthdays"
                icon: "reload"
                type: "bottom"
                left_action_items:  [['menu', lambda x: nav_drawer.set_state("open")]]
                on_action_button:app.reorder_carousel() # app.add_birthdays(["lala", "10-01-1999"])#print(app.birthdays_list)#app.restart()
                mode: "end"                                    
                                    
                                
                            

"""
