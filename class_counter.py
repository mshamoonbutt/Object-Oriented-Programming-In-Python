class Counter :
    def getValue(self) :
        return self._value
    def click(self) :
        self._value = self._value + 1
    def reset(self) :
        self._value = 0
    def undo(self)  :
        if (self._value > 0) :
            self._value = self._value - 1     
    def setLimit(self, maximum) :
        self.maximum = maximum
        if (result > self.maximum) :
            print("Limit Exceeded")
# from counter import Counter
tally = Counter()
tally.reset()
tally.click()
tally.click()
tally.click()   
tally.click()
tally.click()
tally.click()
tally.undo()
maximum=10
result = tally.getValue()
print("Value:", result)
tally.click()
result = tally.getValue()
print("Value:", result)

'''class Counter :
    def __init__(self) :
        self._strokes = ""
    def click(self) :
        self._strokes = self._strokes + "|"'''