
import math

def investment_calculator(amount, interest_rate, years, interest_type):
  """Calculates the total amount of money an investment will be worth after a given period of time, at a given interest rate.

  Args:
    amount: The amount of money being invested.
    interest_rate: The interest rate, as a percentage.
    years: The number of years the money is being invested for.
    interest_type: The type of interest, either "simple" or "compound".

  Returns:
    The total amount of money the investment will be worth.
  """

  interest_rate = interest_rate / 100

  if interest_type == "simple":
    total_amount = amount * (1 + interest_rate * years)
  else:
    total_amount = amount * math.pow((1 + interest_rate), years)

  return total_amount


def bond_calculator(present_value, interest_rate, months):
  """Calculates the monthly repayment amount for a home loan.

  Args:
    present_value: The present value of the house.
    interest_rate: The interest rate, as a percentage.
    months: The number of months over which the bond will be repaid.

  Returns:
    The monthly repayment amount.
  """

  interest_rate = interest_rate / 12

  monthly_interest = interest_rate / (1 + interest_rate)**(-months)
  monthly_repayment = present_value * monthly_interest

  return monthly_repayment


def main():
  """The main function of the program.

  Prompts the user to select a calculation, and then calls the appropriate function to calculate the desired result.
  """

  print("Welcome to the financial calculators!")
  print("Please select a calculation to perform:")
  print("1. Investment calculator")
  print("2. Home loan repayment calculator")

  selection = input("Your selection: ")

  if selection == "1":
    amount = float(input("Amount of money to invest: "))
    interest_rate = float(input("Interest rate (as a percentage): "))
    years = int(input("Number of years to invest: "))
    interest_type = input("Type of interest (simple/compound): ").lower()

    total_amount = investment_calculator(amount, interest_rate, years, interest_type)
    print(f"The total amount after {years} years will be {total_amount}")

  elif selection == "2":
    present_value = float(input("Present value of the house: "))
    interest_rate = float(input("Interest rate (as a percentage): "))
    months = int(input("Number of months to repay the bond: "))

    monthly_interest_rate = interest_rate / 12 / 100
    monthly_repayment = (monthly_interest_rate * present_value) / (1 - math.pow((1 + monthly_interest_rate), -months))
    print(f"You will need to repay {monthly_repayment:.2f} per month for {months} months.")

  else:
    print("Invalid selection.")


if __name__ == "__main__":
  main()