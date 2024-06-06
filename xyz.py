'''class Circuit:
    def get_resistance(self):
        raise NotImplementedError("Subclasses must implement get_resistance method")


class Resistor(Circuit):
    def __init__(self, resistance):
        self.resistance = resistance

    def get_resistance(self):
        return self.resistance


class Serial(Circuit):
    def __init__(self, circuits):
        self.circuits = circuits

    def get_resistance(self):
        total_resistance = 0
        for circuit in self.circuits:
            total_resistance += circuit.get_resistance()
        return total_resistance


class Parallel(Circuit):
    def __init__(self, circuits):
        self.circuits = circuits

    def get_resistance(self):
        total_resistance = 0
        for circuit in self.circuits:
            total_resistance += 1 / circuit.get_resistance()
        return 1 / total_resistance


# Test the implementation
resistor1 = Resistor(10)
resistor2 = Resistor(20)
serial_circuit = Serial([resistor1, resistor2])

resistor3 = Resistor(30)
parallel_circuit = Parallel([resistor3, serial_circuit])

print("Combined resistance of the parallel circuit:", parallel_circuit.get_resistance())
'''

'''def sumOfList(x):
    if x == []:
        return 0
    else:
        return x[0] + sumOfList(x[1:])
    
print(sumOfList([1,2,3]))    


def rev(x):
    if len(x) == 0:
        return x
    else:
        return rev(x[1:]) + x[0]'''
        
        
        
        