KV = """
<ContentNavigationDrawer>:
    orientation: 'vertical'
    padding: "8dp"
    spacing: "8dp"

    MDTextButton:
        id: main_button
        text: "Liste"
        on_press: root.screen_manager.current = "list"
    MDTextButton:
        id: list_button
        text: "Hauptseite"
        on_press: root.screen_manager.current = "main"

    MDLabel:
        text: "dada"
        size_hint_y: None
        font_style: "Caption"
        height: self.texture_size[1]

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
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            id: toolbar
            title:"birthdays"
            pos_hint:{"top":1}
            elevation:10

        MDNavigationLayout:
            MDScreenManager:
                id: screen_manager
                MainScreen:
                    name: "main"
                    BoxLayout:
                        id: box
                        orientation : 'vertical'  
                        
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

            MDNavigationDrawer:
                id: nav_drawer

                ContentNavigationDrawer:
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer
        MDBottomAppBar:
            MDTopAppBar:
                title: "Title"
                icon: "reload"
                type: "bottom"
                left_action_items:  [['menu', lambda x: nav_drawer.set_state("open")]]
                on_action_button: app.restart()
                mode: "end"                                    
                                    
                                
                            

"""
