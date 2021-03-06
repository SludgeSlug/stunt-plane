from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint


class Plane(Widget):
    pass

class StuntPlaneGame(Widget):
    def update(self, dt):
        pass

class StuntPlaneApp(App):
    def build(self):
        game = StuntPlaneGame()
        Clock.schedule_interval(game.update, 1.0/60.0)        
        return game

if __name__ == '__main__':
    StuntPlaneApp().run()

__version__ = '0.0.1'
