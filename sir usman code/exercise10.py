def check_even_odd(number):
    
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

def main():
    user_input = int(input("Please enter a number: "))
    result = check_even_odd(user_input)
    print(result)
main()

    