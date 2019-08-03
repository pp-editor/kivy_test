import kivy
kivy.require("1.11.1")
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class CountupWidget(Widget):
	text = StringProperty()

	def __init__(self, **kwargs):
		super(CountupWidget, self).__init__(**kwargs)
		self.text = ""

	def buttonClicked(self):
		if not self.text.isdigit():
			self.text = str(0)
		else: 
			self.text = str(int(self.text)+1)

class CountupApp(App):
	def __init__(self, **kwargs):
		super(CountupApp, self).__init__(**kwargs)
		self.title = "countup"

	def build(self):
		return CountupWidget()

if __name__ == "__main__":
	CountupApp().run()