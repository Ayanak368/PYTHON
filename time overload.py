class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour  # Private attribute
        self.__minute = minute  # Private attribute
        self.__second = second  # Private attribute

    def __add__(self, other):
        # Adding seconds, minutes, and hours
        total_seconds = self.__second + other.__second
        total_minutes = self.__minute + other.__minute + (total_seconds // 60)
        total_hours = self.__hour + other.__hour + (total_minutes // 60)

        # Normalize the time
        total_seconds %= 60
        total_minutes %= 60
        total_hours %= 24  # Assuming time wraps around 24 hours

        # Return a new Time object with the resulting time
        return Time(total_hours, total_minutes, total_seconds)

    def display_time(self):
        return f"{self.__hour:02}:{self.__minute:02}:{self.__second:02}"


# Input first time
hour1 = int(input("Enter hours for the first time: "))
minute1 = int(input("Enter minutes for the first time: "))
second1 = int(input("Enter seconds for the first time: "))
time1 = Time(hour1, minute1, second1)

# Input second time
hour2 = int(input("Enter hours for the second time: "))
minute2 = int(input("Enter minutes for the second time: "))
second2 = int(input("Enter seconds for the second time: "))
time2 = Time(hour2, minute2, second2)

# Adding two time objects
t3 = time1 + time2

# Displaying the result
print("Sum of the two times:", t3.display_time())
