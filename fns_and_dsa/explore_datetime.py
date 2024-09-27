from datetime import timedelta, datetime

def display_current_datetime():
    current_time = datetime.now()
    print(f"Current date and time: {current_time.strftime("%Y-%m-%d %H:%M:%S")}")

def calculate_future_date(days_to_add):
    future_date = datetime.now() + timedelta(days=days_to_add)
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")


display_current_datetime()
days_to_add = int(input("Enter the number of days to add to the current date: "))
calculate_future_date(days_to_add)