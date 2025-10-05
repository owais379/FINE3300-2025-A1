# Part 2: Exchange Rate Converter
# Write a method/function (call it convert) that takes the amount and two currencies (USD or CAD) and converts from one currency to another using the exchange rate read from the file

import csv

class ExchangeRates:

    def __init__(self, filename):
        self.filename = filename
        self.usd_cad_rate = self._read_latest_rate()
    
    def _read_latest_rate(self):
        #read the latest usd/cad exhcant rate from the csv file
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                rows = list(reader)

                latest_rows = rows[-1]
                usd_cad_rate = float(latest_rows['USD/CAD'])

                return usd_cad_rate
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            return None
        except KeyError:
            print("Error: USD/CAD column not found in the file.")
            return None
        except ValueError:
            print("Error: Invalid data format in USD/CAD column.")
            return None
        
    def convert(self, amount, from_currency, to_currency):

        if self.usd_cad_rate is None:
            return None
        
        if from_currency == 'CAD' and to_currency == 'USD':
            return amount / self.usd_cad_rate
        
        elif from_currency == 'USD' and to_currency == 'CAD':
            return amount * self.usd_cad_rate
        else:
            print("Error! Only USD and CAD can be converted")
            return None

# Quick test to see the conversion rates
# exchange = ExchangeRates('exr.csv')
# print(f"Exchange rate: {exchange.usd_cad_rate}")

# Test USD to CAD
# usd_to_cad = exchange.convert(100000, 'USD', 'CAD')
# print(f"$100,000 USD = ${usd_to_cad:,.2f} CAD")

# Test CAD to USD  
# cad_to_usd = exchange.convert(100000, 'CAD', 'USD')
# print(f"$100,000 CAD = ${cad_to_usd:,.2f} USD")

#works!

# main program
print("FINE 3300: Assignment #1 Part 2: Currency Converter")
print("-" * 50)

# Initialize exchange rates with the CSV file
exchange = ExchangeRates('exr.csv')

if exchange.usd_cad_rate is not None:
    # user inputs here
    print("\nEnter conversion details:")
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the 'from' currency (USD or CAD): ")
    to_currency = input("Enter the 'to' currency (USD or CAD): ")
    
    # conversion is done here
    converted_amount = exchange.convert(amount, from_currency, to_currency)
    
    if converted_amount is not None:
        # Format and display output
        print(f"\nConversion Result:")
        print(f"{amount:,.2f} {from_currency.upper()} = {converted_amount:,.2f} {to_currency.upper()}")
else:
    print("Error exchange rates do not load")