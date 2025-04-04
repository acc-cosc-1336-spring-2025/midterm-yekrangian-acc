from question_c import reverse_string

def main():
    print("String Reverser 🔄")

    while True:
        string1 = input("Enter a string to reverse: ")
        reversed_result = reverse_string(string1)
        print("Reversed string:", reversed_result)

        again = input("Do you want to reverse another string? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("Goodbye! 👋")
            break

if __name__ == "__main__":
    main()
