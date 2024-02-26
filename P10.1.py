from datetime import date

class Appointment:
    def __init__(self, description, date):
        self.description = description
        self.date = date

    def occursOn(self, year, month, day):
        return self.date.year == year and self.date.month == month and self.date.day == day

class Onetime(Appointment):
    def occursOn(self, year, month, day):
        return super().occursOn(year, month, day)

class Daily(Appointment):
    def occursOn(self, year, month, day):
        return True

class Monthly(Appointment):
    def occursOn(self, year, month, day):
        return self.date.day == day

# Example usage
appointments = [
    Onetime("See the dentist", date(2022, 9, 15)),
    Daily("Go for a run", date(2022, 9, 15)),
    Monthly("Pay rent", date(2022, 9, 1)),
]

user_date = date(2022, 9, 15)

matching_appointments = [appointment for appointment in appointments if appointment.occursOn(user_date.year, user_date.month, user_date.day)]

for appointment in matching_appointments:
    print(appointment.description)