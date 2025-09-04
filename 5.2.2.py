# write a python prompt for loan approval for john. 
# The prompt should ask for his age, income, credit score, and loan amount requested.
# Based on the input, the system should determine if he is eligible for the loan or not.
def loan_approval():
    age = int(input("Enter your age: "))
    income = float(input("Enter your annual income: "))
    credit_score = int(input("Enter your credit score: "))
    loan_amount = float(input("Enter the loan amount requested: "))

    # Define eligibility criteria
    if age < 18:
        print("You must be at least 18 years old to apply for a loan.")
        return
    if income < 30000:
        print("Your income is too low to qualify for a loan.")
        return
    if credit_score < 600:
        print("Your credit score is too low to qualify for a loan.")
        return
    if loan_amount > income * 0.5:
        print("The requested loan amount exceeds the maximum allowable limit based on your income.")
        return

    print("Congratulations! You are eligible for the loan.")
if __name__ == "__main__":
    loan_approval()
