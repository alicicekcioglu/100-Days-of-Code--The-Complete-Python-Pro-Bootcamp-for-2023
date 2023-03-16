file = open("my_file.txt")
content = file.read()
print(content)
file.close()

with open("my_file.txt") as my_file:
    contents = my_file.read()
    print(contents)

# Delete all text and write New text
with open("my_file.txt", mode="w") as my_file:
    my_file.write("New text")

# Append
with open("my_file.txt", mode="a") as my_file:
    my_file.write("\nNew text")