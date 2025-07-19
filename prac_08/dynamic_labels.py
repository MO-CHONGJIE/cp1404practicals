"""
dynamic_labels
Estimate: 60 minutes
Actual:  minutes
"""

from kivy.app import App

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        """Define the data"""
        super().__init__(**kwargs)
        self.names = ["John", "Lily", "Clara", "Rose"]



DynamicLabelsApp().run()