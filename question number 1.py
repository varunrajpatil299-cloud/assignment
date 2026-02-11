# Smart Student Eligibility Checker (Improved Version)

# Taking inputs
student_name = input("Enter student name: ")
age = int(input("Enter age: "))
percentage = float(input("Enter percentage: "))
family_income = float(input("Enter family income: "))
is_rural = input("Is the student from a rural area? (True/False): ").strip().lower() == "true"

# Eligibility condition using short-circuit logic
eligible = (percentage > 85 and family_income < 300000) or (percentage > 90)

# Displaying student details using formatted string
print("\n--- Student Details ---")
print(f"Name: {student_name}")
print(f"Age: {age}")
print(f"Percentage: {percentage:.2f}%")
print(f"Family Income: ₹{family_income:.2f}")
print(f"Rural Area: {is_rural}")

# Final eligibility result
print("\nEligible for scholarship" if eligible else "\nNot eligible")
