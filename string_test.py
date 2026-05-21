name = "Krishna yadav  "

print(f"Hello {name}")

print(name.upper())
print(name.lower())
print(len(name))

print(name.replace("Krishna","Mahesh"))

print("----")

replace = name.replace("Krishna","Chinu")
print(replace)

print(name.strip())

text = "\n\nPython\n"
print(text)
print(text.strip())

text1 = "###welcome###"
print(text1)
print(text1.strip("e"))

####Slice"

text = "apple banana mango"

print(text)
words = text.split()

print(words[0])


user_input = input("Enter names separated by commas: ")

names = [name.strip() for name in user_input.split(",")]

print(names)