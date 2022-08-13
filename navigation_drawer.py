navigation_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
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
                            icon: "reload"
                            type: "bottom"
                            left_action_items:  [['menu', lambda x: nav_drawer.set_state("open")]]
                            on_action_button: app.restart()
                            mode: "end"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"

                MDIconButton:
                    id: cake
                    size_hint:1,1
                    icon: "cake"
                MDLabel:
                    text: "See"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: "dada"
                    size_hint_y: None
                    font_style: "Caption"
                    height: self.texture_size[1]

                ScrollView:

                    DrawerList:
                        id: md_list
                        
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
                                    
                           
                                
                            
                            

"""
