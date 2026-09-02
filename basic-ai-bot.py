print("Hello! I am an AI bot. What is your name?: ")
name = input()
print(f"Hello {name}! Hope you're doing well!")
print("How are you doing? (good/bad): ")
mood = input().lower()
if mood == "good":
    print("That's great. I'm feeling well today too!")
elif mood == "bad":
    print("Hope you get better later")
else:
    print("Understood.")
print(f"Well it was great chatting with you. Until next time {name}!")