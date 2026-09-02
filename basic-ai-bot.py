print("Hello! I am an AI bot. What is your name?: ")
name = input()
print(f"Hello {name}! Hope you're doing well!")
print("How are you doing? (good/bad): ")
mood = input().lower()
if mood == "good":
    print("That's great. I'm feeling well today too!")
elif mood == "bad":
    print("Hope you get better later.")
else:
    print("Understood.")
print("Do you like sports? (yes/no): ")
sports = input().lower()
if sports == "yes":
    print("It's good to get active!")
if sports == "no":
    print("Reasonable choice. Some sports can be quite extreme.")
else:
    print("Good choice.")
print("Do you enjoy academics? (yes/no): ")
academics = input().lower()
if academics == "yes":
    print("I'm glad you do!")
if academics == "no":
    print("Academic subjects such as mathematics can be extremely tricky.")
else:
    print("I understand your logic.")
if sports == "yes":
    if academics == "yes":
        print(f"Keep practicing your sports and academics {name}!")
    else:
        print(f"Keep practicing you sports {name}!")
else:
    if academics == "yes":
        print(f"Keep practicing your academics {name}!")
    else:
        print(f"Keep practicing your hobbies {name}!")