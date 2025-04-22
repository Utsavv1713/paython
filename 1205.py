class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def add(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours + total_minutes // 60
        return Time(total_hours, total_minutes % 60)

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

# Test
t1 = Time(2, 45)
t2 = Time(1, 30)
t3 = t1.add(t2)
print("Added Time:", t3)
