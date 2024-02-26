class Time:
    def __init__(self, hours, minutes, seconds, is_military_time=False):
        if is_military_time:
            # Military time representation
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
        else:
            # Standard time representation
            self.hours = hours % 12
            self.minutes = minutes
            self.seconds = seconds
            self.is_am = hours < 12

    def __str__(self):
        if hasattr(self, 'is_am'):
            # Display in standard time format
            period = 'AM' if self.is_am else 'PM'
            return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d} {period}"
        else:
            # Display in military time format
            return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d} (Military Time)"

# Example usage for standard time representation
standard_time = Time(3, 30, 0)
print("Standard Time:", standard_time)

# Example usage for military time representation
military_time = Time(15, 30, 0, is_military_time=True)
print("Military Time:", military_time)
