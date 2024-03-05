'''class ComboLock :
    def ComboLock(self, secret1, secret2, secret3) :
        self.secret1=secret1
        self.secret2=secret2
        self.secret3=secret3
    def reset(self) :
        pass
    def turnLeft(self, ticks) :
        pass
    def turnRight(self, ticks) :
        pass
    def open(self) :
        pass'''
        
'''class ComboLock:
    def __init__(self, secret1, secret2, secret3):
        self.secret1 = secret1
        self.secret2 = secret2
        self.secret3 = secret3
        self.reset()

    def reset(self):
        self.dial_position = 0
        self.first_turn = True

    def turnLeft(self, ticks):
        if self.first_turn:
            self.dial_position = (self.dial_position + ticks) % 40
            self.first_turn = False
        else:
            self.reset()

    def turnRight(self, ticks):
        if not self.first_turn:
            self.dial_position = (self.dial_position - ticks) % 40

    def open(self):
        if not self.first_turn and self.dial_position == self.secret1:
            self.reset()
            return "Lock opened"
        else:
            self.reset()
            return "Incorrect combination"

# Example usage:
combo_lock = ComboLock(10, 20, 30)

# Incorrect combination
print(combo_lock.turnLeft(8))
print(combo_lock.open())

# Correct combination
print(combo_lock.turnRight(30))
print(combo_lock.open())'''

class ComboLock:
    def __init__(self, secret1, secret2, secret3):
        self.secret1 = secret1
        self.secret2 = secret2
        self.secret3 = secret3
        self.reset()

    def reset(self):
        self.dial_position = 0
        self.first_turn = True
        self.second_turn = False

    def turnLeft(self, ticks):
        if not self.first_turn and not self.second_turn:
            self.dial_position = (self.dial_position + ticks) % 40
            self.second_turn = True
        else:
            self.reset()

    def turnRight(self, ticks):
        if self.first_turn:
            self.dial_position = (self.dial_position + ticks) % 40
            self.first_turn = False
        elif self.second_turn:
            self.dial_position = (self.dial_position - ticks) % 40
            self.second_turn = False
        else:
            self.reset()

    def open(self):
        if not self.first_turn and not self.second_turn and self.dial_position == self.secret3:
            self.reset()
            return "Lock opened"
        else:
            self.reset()
            return "Incorrect combination"

# Example usage:
combo_lock = ComboLock(10, 20, 30)

# Incorrect combination
combo_lock.turnRight(10)
combo_lock.turnLeft(20)
print(combo_lock.open())

# Correct combination
combo_lock.turnRight(10)
combo_lock.turnLeft(30)
combo_lock.turnRight(10)
print(combo_lock.open())

       