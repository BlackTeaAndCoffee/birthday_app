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
                        MDTextField:
                            id:birthday
                            hint_text: "Birthday"
                            pos_hint: {'x':0.15, 'y':0.4}
                            mode:'rectangle'
                            size_hint_x : .7
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
