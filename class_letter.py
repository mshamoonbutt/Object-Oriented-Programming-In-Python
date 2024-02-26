class Letter:
    def __init__(self, letterFrom, letterTo):
        self.letterFrom = letterFrom
        self.letterTo = letterTo
        self.body = []

    def addLine(self, line):
        """Add a line of text to the body of the letter."""
        self.body.append(line)

    def getText(self):
        """Return the entire text of the letter."""
        letter_text = f"Dear {self.letterTo}:\n\n"
        for line in self.body:
            letter_text += f"{line}\n"
        letter_text += "\nSincerely,\n\n"
        letter_text += f"{self.letterFrom}"
        return letter_text

# Driver program
letter_object = Letter("Mary", "John")

# Add lines to the letter
letter_object.addLine("I am sorry we must part.")
letter_object.addLine("I wish you all the best.")

# Get and print the entire text of the letter
print(letter_object.getText())
