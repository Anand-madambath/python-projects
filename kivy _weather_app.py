from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
import requests

API_KEY = "mykey"

class WeatherLayout(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=20, **kwargs)

        self.city_input = MDTextField(
            hint_text="Enter City Name",
            size_hint=(1, None),
            height="48dp",
            mode="rectangle"
        )
        self.add_widget(self.city_input)

        self.search_button = MDRaisedButton(
            text="Get Weather",
            pos_hint={"center_x": 0.5},
            size_hint=(None, None),
            size=("150dp", "40dp"),
            on_release=self.get_weather
        )
        self.add_widget(self.search_button)

        self.weather_label = MDLabel(
            text="",
            halign="center",
            theme_text_color="Primary",
            font_style="H6"
        )
        self.add_widget(self.weather_label)

    def get_weather(self, instance):
        city = self.city_input.text.strip()
        if not city:
            self.weather_label.text = "Please enter a city."
            return

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        try:
            response = requests.get(url)
            data = response.json()

            if data.get("cod") != 200:
                self.weather_label.text = f"Error: {data.get('message', 'Unknown error')}"
                return

            name = data["name"]
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]

            self.weather_label.text = (
                f"[b]{name}[/b]\n"
                f"Temperature: {temp}°C\n"
                f"Weather: {weather.title()}\n"
                f"Humidity: {humidity}%\n"
                f"Wind: {wind} m/s"
            )
        except Exception as e:
            self.weather_label.text = f"Error: {str(e)}"

class WeatherApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Light"
        return WeatherLayout()

if __name__ == '__main__':
    WeatherApp().run()
