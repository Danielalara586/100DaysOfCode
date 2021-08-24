# Day 3: Hours to seconds

def hours_to_seconds(hour: int, minute: int):
    hour_second = 3600
    minute_second = 60
    return (hour * hour_second) + (minute * minute_second)

def run():
    hour = int(input("Please enter the hours: "))
    minute = int(input("Please enter the minutes: "))
    time = hours_to_seconds(hour, minute)
    print(f"Time in seconds: {time}")


if __name__ == "__main__":
    run()
