PLACEHOLDER = "[name]"

with open("./name/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Letter/letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        print(new_letter)
        with open(f"./Output/Ready To Send/letter_for_{stripped_name}.txt", "w")as completed_letter:
            completed_letter.write(new_letter)

