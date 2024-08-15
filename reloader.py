from kaki.app import App
from kivy.app import MDApp
from kivy.lang import Builder

class MDLive(App, MDApp):
    AUTORELOADER_PATHS = [
        (".", {"reload": True}),
    ]
    
    def build_app(self, *args):
        return Builder.load_file('restaurant_app_guiz.kv')
    
MDLive().run()
    