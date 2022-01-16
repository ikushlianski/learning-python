from datetime import datetime

user_input = input("Please enter your goal and deadline (DD.MM.YYYY) separated by a colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, '%d.%m.%Y')
today = datetime.today()
time_till = deadline_date - today

print(f'Time remaining for the goal "{goal}" is {time_till.days} days')
