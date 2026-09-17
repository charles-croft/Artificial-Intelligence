import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

conversation_history = []
sentiment_counts = {"Positive": 0, "Neutral": 0, "Negative": 0}


def show_processing_animation():
    print(f"{Fore.CYAN}Decrypting message", end="", flush=True)
    for _ in range(3):
        print(".", end="", flush=True)
    print(f"{Style.RESET_ALL}")


def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😞"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😭"
    return polarity, sentiment_type, color, emoji


def get_valid_name():
    while True:
        name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()
        if name.isalpha():
            return name
        print(f"{Fore.RED}Names must contain letters only. Please try again.{Style.RESET_ALL}")


def print_summary():
    print(f"{Fore.CYAN} Sentiment Analysis Summary:{Style.RESET_ALL}")
    print(f"{Fore.GREEN}Positive: {sentiment_counts['Positive']}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Neutral: {sentiment_counts['Neutral']}{Style.RESET_ALL}")
    print(f"{Fore.RED}Negative: {sentiment_counts['Negative']}{Style.RESET_ALL}")


def print_help():
    print(f"{Fore.CYAN}Available commands:{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}summary{Style.RESET_ALL} - Show the sentiment analysis summary")
    print(f"{Fore.YELLOW}reset{Style.RESET_ALL} - Clear all stored data")
    print(f"{Fore.YELLOW}history{Style.RESET_ALL} - Show all previous messages and sentiments")
    print(f"{Fore.YELLOW}help{Style.RESET_ALL} - List available commands")
    print(f"{Fore.YELLOW}exit{Style.RESET_ALL} - Quit and save a summary report")


def execute_command(command):
    if command == "summary":
        print_summary()
    elif command == "reset":
        conversation_history.clear()
        sentiment_counts["Positive"] = 0
        sentiment_counts["Neutral"] = 0
        sentiment_counts["Negative"] = 0
        print(f"{Fore.CYAN} All conversation history cleared!{Style.RESET_ALL}")
    elif command == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN} Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😞"
                else:
                    color = Fore.YELLOW
                    emoji = "😭"

                print(f"{idx}. {color}{emoji} {text} "
                    f"Polarity: {polarity:.2f}, {sentiment_type}{Style.RESET_ALL}")
    elif command == "help":
        print_help()


print(f"{Fore.CYAN} 🐍 Welcome to Sentiment Spy! 🐍{Style.RESET_ALL}")

user_name = get_valid_name()

print(f"\n{Fore.CYAN}Hello, Agent {user_name}!")
print(f"Type a Sentence and I will analyze your sentences with TextBlob and show you the sentiment. ")
print(f"Type {Fore.YELLOW}summary{Fore.CYAN}, {Fore.YELLOW}reset{Fore.CYAN}, {Fore.YELLOW}history{Fore.CYAN}, "
    f"{Fore.YELLOW}help{Fore.CYAN}, or {Fore.YELLOW}exit{Fore.CYAN} to quit.{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

    if user_input.lower() == "exit":
        break

    if user_input.lower() in ("summary", "reset", "history", "help"):
        execute_command(user_input.lower())
        continue

    show_processing_animation()

    polarity, sentiment_type, color, emoji = analyze_sentiment(user_input)
    conversation_history.append((user_input, polarity, sentiment_type))
    sentiment_counts[sentiment_type] += 1

    print(f"{color}{emoji} {sentiment_type} sentiment detected! "
        f"Polarity: {polarity:.2f}")

print(f"\n{Fore.BLUE} Exiting Sentiment Spy. Farewell, Agent {user_name}! 😊{Style.RESET_ALL}")
print_summary()

report_filename = f"{user_name}_sentiment_analysis.txt"
with open(report_filename, "w") as report_file:
    report_file.write(f"Sentiment Analysis Summary for Agent {user_name}\n")
    report_file.write(f"Positive: {sentiment_counts['Positive']}\n")
    report_file.write(f"Neutral: {sentiment_counts['Neutral']}\n")
    report_file.write(f"Negative: {sentiment_counts['Negative']}\n")

print(f"{Fore.CYAN}Summary saved to {report_filename}{Style.RESET_ALL}")