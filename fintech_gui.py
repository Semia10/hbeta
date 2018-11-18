"""
Python GUI for Budgeting App using FinTech Solution

Author: Wonseok Han
Institution: University of Alberta
"""
import kivy
kivy.require('1.10.1')

from enum import Enum
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.button import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.uix.textinput import TextInput
from kivy.lang import Builder

Builder.load_string("""
#:import RiseInTransition kivy.uix.screenmanager.RiseInTransition
<Classify>:
    canvas:
        Rectangle:
            size: self.size
    Label:
        font_size: 42
        text: root.name
    BoxLayout:
        size_hint: .75, 0.75
        height: 250
        pos_hint: {'center_x': .5, 'center_y': .5}
        orientation: 'vertical'
        Button:
            text: 'Youth (18-35)'
            on_press:
                group = 'youth'
                root.manager.transition = RiseInTransition()
                root.manager.transition.duration = 0.75
                root.manager.current = "budget_amount"
        Button:
            text: 'Adult (36-55)'
            on_press:
                group = 'adult'
                root.manager.transition = RiseInTransition()
                root.manager.transition.duration = 0.75
                root.manager.current = "budget_amount"
        Button:
            text: 'Senior (56>)'
            on_press:
                group = 'senior'
                root.manager.transition = RiseInTransition()
                root.manager.transition.duration = 0.75
                root.manager.current = "budget_amount"
<BudgetAmount>:
    FloatLayout:
        Label:
            font_size: 40
            text: 'Enter Weekly Budget Amount Here'
            pos_hint: {'center_x': .5, 'top': 1.46}
    GridLayout:
        id: BudgetAmount
        display: weekly
        rows: 5
        padding: 10
        spacing: 10
        BoxLayout:
            TextInput:
                id: weekly
                size_hint: 0.65, 0.65
                font_size: 32
                multiline: False
        BoxLayout:
            spacing: 10
            Button:
                text: '7'
                on_press: weekly.text += weekly.text
            Button:
                text: '8'
                on_press: weekly.text += self.text
            Button:
                text: '9'
                on_press: weekly.text += self.text
        BoxLayout:
            spacing: 10
            Button:
                text: '4'
                on_press: weekly.text += self.text
            Button:
                text: '5'
                on_press: weekly.text += self.text
            Button:
                text: '6'
                on_press: weekly.text += self.text
        BoxLayout:
            spacing: 10
            Button:
                text: '1'
                on_press: weekly.text += self.text
            Button:
                text: '2'
                on_press: weekly.text += self.text
            Button:
                text: '3'
                on_press: weekly.text += self.text
        BoxLayout:
            spacing: 10
            Button:
                text: 'Clear'
                on_press: weekly.text = ''
            Button:
                text: '0'
                on_press: weekly.text += self.text
            Button:
                text: 'Enter'
                on_press:
                    user_budget = weekly.text
                    root.manager.transition = RiseInTransition()
                    root.manager.current = "daily_spend"
<DailySpendings>
    FloatLayout:
        Label:
            font_size: 40
            text: 'Enter Your Daily Spendings'
            pos_hint: {'center_x': .5, 'top': 1.46}
    GridLayout:
        id: DailySpendings
        display: daily
        rows: 5
        padding: 10
        spacing: 10
        BoxLayout:
            TextInput:
                id: daily
                size_hint: 0.65, 0.65
                font_size: 32
                multiline: False
        BoxLayout:
            spacing: 10
            Button:
                text: '7'
                on_press: daily.text += self.text
            Button:
                text: '8'
                on_press: daily.text += self.text
            Button:
                text: '9'
                on_press: daily.text += self.text
        BoxLayout:
            spacing: 10
            Button:
                text: '4'
                on_press: daily.text += self.text
            Button:
                text: '5'
                on_press: daily.text += self.text
            Button:
                text: '6'
                on_press: daily.text += self.text
        BoxLayout:
            spacing: 10
            Button:
                text: '1'
                on_press: daily.text += self.text
            Button:
                text: '2'
                on_press: daily.text += self.text
            Button:
                text: '3'
                on_press: daily.text += self.text
        BoxLayout:
            spacing: 10
            Button:
                text: 'Clear'
                on_press: daily.text = ''
            Button:
                text: '0'
                on_press: daily.text += self.text
            Button:
                text: 'Enter'
                on_press:
                    user_daily = daily.text
                    root.manager.transition = RiseInTransition()
                    root.manager.current = "info_graph"
<InfoGraph>
    BoxLayout:
        Label:
            text: "Hello! We'll try our hardest to keep you within your stated budget."
""")

class Classify(Screen):
    pass

class BudgetAmount(Screen):
    pass

class InfoGraph(Screen):
    pass

class DailySpendings(Screen):
    pass

class BudgetWidget(App):

    def build(self):
        root = ScreenManager()
        root.add_widget(Classify(name = 'classify'))
        root.add_widget(BudgetAmount(name = 'budget_amount'))
        root.add_widget(InfoGraph(name = 'info_graph'))
        root.add_widget(DailySpendings(name = 'daily_spend'))
        return root

if __name__ == '__main__':
    BudgetWidget().run()
