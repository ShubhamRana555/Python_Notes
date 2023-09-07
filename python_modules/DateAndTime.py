import datetime
def date_and_time(user_name):
    # Get the current date and time
    current_datetime = datetime.datetime.now()
    # Display the current date and time
    print("Current Date and Time:", current_datetime)
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print("Formatted Date and Time:", formatted_datetime)
    print(user_name)

def print_name(user_name):
    print(f"my name is {user_name}")