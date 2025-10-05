# Part 1: Mortgage payment calculator

class MortgagePayments:
    #  A class to calculate various mortgage payment options for canadian fixed-rate mortgages
    
    # Fixed rate mortgages in Canada are quoted as semiannually compounded rates.
    def __init__(self, interest_rate, amortization_period):
        self.quoted_interest = interest_rate / 100 #convert to a decimal
        self.amortizations_years = amortization_period

    def pva(self, r, n):
        
        if r == 0:
            return n
        else:
            return (1 - (1 + r) ** -n) / r
        
    def calculate_periodic_rate(self, compounding_frequency, payment_frequency):
        effective_annual_rate = (1 + self.quoted_interest / compounding_frequency) ** compounding_frequency - 1

        periodic_rate = (1 + effective_annual_rate) ** (1 / payment_frequency) - 1

        total_periods = self.amortizations_years * payment_frequency
        
        return periodic_rate, total_periods
    
    def payments(self, principal):
        # Monthly payments (compounded semiannually, paid monthly)
        monthly_rate, monthly_periods = self.calculate_periodic_rate(2, 12)
        monthly_payment = principal / self.pva(monthly_rate, monthly_periods)
        
        # Semi-monthly payments 24 payments per year
        semi_monthly_rate, semi_monthly_periods = self.calculate_periodic_rate(2, 24)
        semi_monthly_payment = principal / self.pva(semi_monthly_rate, semi_monthly_periods)
        
        # Bi-weekly payments 26 payments per year
        bi_weekly_rate, bi_weekly_periods = self.calculate_periodic_rate(2, 26)
        bi_weekly_payment = principal / self.pva(bi_weekly_rate, bi_weekly_periods)
        
        # Weekly payments 52 payments per year
        weekly_rate, weekly_periods = self.calculate_periodic_rate(2, 52)
        weekly_payment = principal / self.pva(weekly_rate, weekly_periods)
        
        #  bi-weekly half of monthly payment
        rapid_bi_weekly_payment = monthly_payment / 2
        
        # weekly quarter of monthly payment
        rapid_weekly_payment = monthly_payment / 4
        
        # Round all payments to nearest penny
        payments_tuple = (
            round(monthly_payment, 2),
            round(semi_monthly_payment, 2),
            round(bi_weekly_payment, 2),
            round(weekly_payment, 2),
            round(rapid_bi_weekly_payment, 2),
            round(rapid_weekly_payment, 2)
        )
        
        return payments_tuple

# testing example from instructions
# mortgage = MortgagePayments(5.5, 25)
# payments = mortgage.payments(100000)

# print(payments)
# Works! - result: (610.39, 304.85, 281.38, 140.61, 305.2, 152.6)

#Formatted Payments (User Input)

# exeuction of program
print("FINE 3300: Assignment #1 Part 1: Mortgage Calculator")
print("-" * 50)

# prompt user for input
print("\nEnter mortgage details:")
principal = float(input("Enter the principal amount: 5000"))
interest_rate = float(input("Enter the quoted interest rate as a percent, e,g --> 4.85: "))
amortization_years = int(input("Enter the amortization period in years: "))

# calculate mortgage payments
mortgage = MortgagePayments(interest_rate, amortization_years)
payments = mortgage.payments(principal)

# format and display output
print(f"\nMortgage Payment Results:")
print(f"Monthly Payment: ${payments[0]:,.2f}")
print(f"Semi-monthly Payment: ${payments[1]:,.2f}")
print(f"Bi-weekly Payment: ${payments[2]:,.2f}")
print(f"Weekly Payment: ${payments[3]:,.2f}")
print(f"Rapid Bi-weekly Payment: ${payments[4]:,.2f}")
print(f"Rapid Weekly Payment: ${payments[5]:,.2f}")

# f string usage explained:

# , - Add thousand separators (commas)

# .2 - Show 2 decimal places

# f - Format as floating point number

