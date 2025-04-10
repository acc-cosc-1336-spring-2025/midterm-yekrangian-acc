# src/question_b/main.py

from question_b import get_day_of_week

def main():
    print("Day of the Week Finder") 

    while True:
        try:
            day_input = int(input("Enter a number (1–7) to get the day of the week: "))
            result = get_day_of_week(day_input)
            print("Result:", result)
        except ValueError:
            print("Please enter a valid number.")

        again = input("Would you like to try again? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
