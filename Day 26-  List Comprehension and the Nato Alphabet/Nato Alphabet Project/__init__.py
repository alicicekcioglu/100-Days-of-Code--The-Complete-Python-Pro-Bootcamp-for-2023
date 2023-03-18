import pandas as pd
# How to iterate in data frame
# {new_key: new_value for (index, row) in df.iterrows()}

# 1- Create a dict in this format = {"A": "Alfa", "B": "Bravo"}
data = pd.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# Create a list of the phonetic code from a word that the user inputs.

word = input(" Enter a word: ").upper()
output_list = [data_dict[letter] for letter in word]
print(output_list)