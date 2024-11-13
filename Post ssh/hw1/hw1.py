"""
Name: Fin Goscha
Section: 275-02
Desc: Lab3

"""


def days_of_the_week():


    # 0 1 2 3 4 5 6
    # array for indexing over
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    users_date = int(input("Please enter a day in december 1 throuygh 31: "))

    # check if the date is to low or to high than 1 or 31
    if users_date <= 1 or users_date >= 31:
        return 'to low or high'

    # days of the week calculation
    day_index = (users_date - 1) % 7
    return f"December {users_date} 2024 is a {days[day_index]}."

answer = days_of_the_week()
print(answer)
~                                                                                                                                                                                           ~                                                                                                                                                                                           ~                                                                                                                                                                                           ~                                                                                                                                                                                           ~                                                                                                                                                                                           ~                                                                                                                                                                                           ~                           