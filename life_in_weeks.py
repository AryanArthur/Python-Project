# small exercise - Life in Weeks

weeks_in_year = 52
total_age = 90
total_weeks = total_age *weeks_in_year
def life_in_weeks():
    current_age = int(input("whats your age: "))
    remaining_weeks = total_weeks - current_age*weeks_in_year
    print(f"You have {remaining_weeks} weeks left.")

life_in_weeks()
