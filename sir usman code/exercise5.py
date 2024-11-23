month_days = {
1:31,
2:28,
3:31,
4:30,
5:31,
6:30, 
7:31,
8:31,
9:30,
10:31,
11:30,
12:31,
}

month_number = int(input("Enter the month number(1-12):"))
if 1 <= month_number <= 12:
    print(f"Month {month_number} has {month_days[month_number]} days.")
else:
    print("Invalid month number!")
    