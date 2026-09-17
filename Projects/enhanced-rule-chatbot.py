import re, random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

weather_reports = {
    "london": "cloudy, 15°C",
    "new york": "sunny, 24°C",
    "tokyo": "rainy, 19°C",
    "sydney": "clear, 27°C"
}

city_times = {
    "london": "3:00 PM",
    "new york": "10:00 AM",
    "tokyo": "12:00 AM",
    "sydney": "1:00 AM"
}

news_headlines = [
    "Scientists discover a new exoplanet with signs of water.",
    "Local team wins championship after a dramatic overtime finish.",
    "New study finds that regular walking improves memory.",
    "Tech company unveils faster, more efficient batteries."
]

def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def matches(user_input, keywords):
    return any(re.search(rf"\b{re.escape(word)}\w*\b", user_input) for word in keywords)

def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains, or cities?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "yes":
            print(Fore.GREEN + f"TravelBot: Awesome! Enjoy {suggestion}!")
        elif answer == "no":
            print(Fore.RED + "TravelBot: Let's try another.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: I'll suggest again.")
            recommend()
    else:
        print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")
        recommend()

def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.YELLOW + "You: ")

    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers/adapters.")
    print(Fore.GREEN + "- Check the weather forecast.")

def tell_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(jokes)}")

def check_weather():
    print(Fore.CYAN + "TravelBot: Which city's weather?")
    city = normalize_input(input(Fore.YELLOW + "You: "))
    if city in weather_reports:
        print(Fore.GREEN + f"TravelBot: It's currently {weather_reports[city]} in {city.title()}.")
    else:
        print(Fore.RED + f"TravelBot: Sorry, I don't have weather data for {city.title()}.")

def check_time():
    print(Fore.CYAN + "TravelBot: Which city's local time?")
    city = normalize_input(input(Fore.YELLOW + "You: "))
    if city in city_times:
        print(Fore.GREEN + f"TravelBot: It's about {city_times[city]} in {city.title()}.")
    else:
        print(Fore.RED + f"TravelBot: Sorry, I don't have time data for {city.title()}.")

def check_news():
    print(Fore.YELLOW + f"TravelBot: {random.choice(news_headlines)}")

def show_history(history):
    if history:
        print(Fore.MAGENTA + "TravelBot: Here's what you've told me:")
        for line in history:
            print(Fore.MAGENTA + f"- {line}")
    else:
        print(Fore.MAGENTA + "TravelBot: I don't have anything remembered yet.")

def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.GREEN + "- Give simulated weather (say 'weather')")
    print(Fore.GREEN + "- Tell the local time in a city (say 'time')")
    print(Fore.GREEN + "- Share a news headline (say 'news')")
    print(Fore.GREEN + "- Recall what you've told me (say 'remember')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

def chat():
    print(Fore.CYAN + "Hello! I'm TravelBot.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    history = []
    show_help()

    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)
        history.append(user_input)

        if matches(user_input, ["recommend", "suggest"]):
            recommend()
        elif matches(user_input, ["pack", "packing"]):
            packing_tips()
        elif matches(user_input, ["joke", "funny"]):
            tell_joke()
        elif matches(user_input, ["weather", "forecast", "temperature"]):
            check_weather()
        elif matches(user_input, ["time", "clock"]):
            check_time()
        elif matches(user_input, ["news", "headline", "update"]):
            check_news()
        elif matches(user_input, ["remember", "recall", "history"]):
            show_history(history)
        elif matches(user_input, ["help", "menu"]):
            show_help()
        elif matches(user_input, ["exit", "bye", "quit"]):
            print(Fore.CYAN + "TravelBot: Safe travels! Goodbye!")
            break
        else:
            print(Fore.RED + "TravelBot: Could you rephrase?")

if __name__ == "__main__":
    chat()
