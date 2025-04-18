import csv
from datetime import datetime

filename = 'trades.csv'
headers = ["Date", "Asset", "Direction", "Entry Price", "Exit Price", "Lot Size", "Pips/Points Gained", "Profit/Loss", "Notes"]

def record_trade():
    print("Enter trade details:")
    asset = input("Asset (e.g., EURUSD): ")
    direction = input("Direction (Buy/Sell): ")
    entry_price = float(input("Entry Price: "))
    exit_price = float(input("Exit Price: "))
    lot_size = float(input("Lot Size: "))
    result = float(input("Profit/Loss: "))
    pips = float(input("Pips/Points gained: "))
    notes = input("Any notes? ")
    trade_data = [datetime.now().strftime("%Y-%m-%d %H:%M:%S"), asset, direction, entry_price, exit_price, lot_size, pips, result, notes]
    try:
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(headers)
            writer.writerow(trade_data)
        print("Trade recorded successfully.")
    except Exception as e:
        print("Failed to record trade:", e)

def view_trades():
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except Exception as e:
        print("Failed to view trades:", e)

def calculate_total_profit():
    total_profit = 0
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                total_profit += float(row[7])  # Profit/Loss column
        print("Total profit:", total_profit)
    except Exception as e:
        print("Failed to calculate total profit:", e)

def calculate_average_lot_size():
    total_lot_size = 0
    count = 0
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                total_lot_size += float(row[5])  # Lot Size column
                count += 1
        average_lot_size = total_lot_size / count
        print("Average lot size:", average_lot_size)
    except Exception as e:
        print("Failed to calculate average lot size:", e)

def main():
    while True:
        print("\n1. Record trade")
        print("2. View trades")
        print("3. Calculate total profit")
        print("4. Calculate average lot size")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            record_trade()
        elif choice == '2':
            view_trades()
        elif choice == '3':
            calculate_total_profit()
        elif choice == '4':
            calculate_average_lot_size()
        elif choice == '5':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
