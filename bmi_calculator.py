def get_positive_number(prompt):
    """Read a positive number from the user, retrying on invalid input."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= 0:
                print("Please enter a number greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number, such as 65 or 1.70.")


def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    return "Obese"


def main():
    print("=== BMI Calculator ===")
    weight = get_positive_number("Enter your weight in kilograms (kg): ")
    height = get_positive_number("Enter your height in metres (m): ")

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Category: {category}")
    print("\nNote: BMI is a screening measure, not a medical diagnosis.")


if __name__ == "__main__":
    main()
