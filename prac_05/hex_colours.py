COLOUR_TO_CODE = {"BLACK": "#000000", "BRONZE": "#cd7f32", "ALICEBLUE": "#f0f8ff",
                  "BLOND": "#faf0be", "AMARANTH": "#e52b50", "AMBER": "#ffbf00",
                  "AMETHYST": "#9966cc", "BISTRE": "#3d2b1f", "BROWN": "#a52a2a",
                  "BRASS": "#b5a642"}

user_choice = input("Enter colour:").upper()
while user_choice != "":
    try:
        print(f"{user_choice} is {COLOUR_TO_CODE[user_choice]}")

    except KeyError:
        print("Invalid colour")
    user_choice = input("Enter colour:").upper()