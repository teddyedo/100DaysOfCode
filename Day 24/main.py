with open("Day 24/Input/Names/invited_names.txt") as namesFile:
    names = namesFile.read().splitlines()

sample = ""
with open("Day 24/Input/Letters/starting_letter.txt") as sampleLetterFile:
    sample = sampleLetterFile.read()

for name in names:
    fileName = "letter_for_" + name + ".txt"
    with open(f"Day 24/Output/ReadyToSend/{fileName}", "w") as letter:
        letter.write(sample.replace("[name]", name))
