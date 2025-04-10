from question_d import get_assessment_value, get_tax_assessed

def main():
    print("Property Tax Calculator")

    while True:
        try:
            actual_value = float(input("Enter the actual property value (e.g., 10000): "))
            if actual_value < 0:
                print("Value cannot be negative.")
                continue

            assessment = get_assessment_value(actual_value)
            tax = get_tax_assessed(assessment)

            print(f"Assessment value: ${assessment:,.2f}") 
            print(f"Property tax: ${tax:,.2f}")

        except ValueError:
            print("Please enter a valid number.")

        again = input("Would you like to calculate another? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
