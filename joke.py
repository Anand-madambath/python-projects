import requests

def fetch_joke():
    url = "https://official-joke-api.appspot.com/random_joke"

    try:
        response = requests.get(url)
        response.raise_for_status() 
        joke_data = response.json()

        print("\nHere's a joke for you:")
        print(f"\n{joke_data['setup']}")
        input("🤔 (press Enter for the punchline...)")
        print(f"\n{joke_data['punchline']}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the joke: {e}")

fetch_joke()