import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import datetime
from data_entry import get_amount,get_category,get_date,get_description

rupee_symbol = "\u20B9" 

class CSV:
    FORMAT = "%d-%m-%Y"
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date","amount","category","description"]

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=["date","amount","category","description"])
            df.to_csv(cls.CSV_FILE,index = False)

    @classmethod
    def add_entry(cls,date,amount,category,description):
        new_entry = {
            "date":date,
            "amount":amount,
            "category":category,
            "description":description
        }    
        with open(cls.CSV_FILE,"a",newline="") as csvfile:
            writer = csv.DictWriter(csvfile,cls.COLUMNS)
            writer.writerow(new_entry)
        print("Successfully Added!")    

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
        start_date = datetime.strptime(start_date, CSV.FORMAT)
        end_date = datetime.strptime(end_date, CSV.FORMAT)

        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No transactions found in the given date range")
        else:
            print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
            for _, row in filtered_df.iterrows():
                if row['category'] == "Income":
                    print(f"\033[92m{row['date'].strftime(CSV.FORMAT)} | {rupee_symbol}{row['amount']:.2f} | {row['category']} | {row['description']}\033[0m")
                else:
                    print(f"\033[91m{row['date'].strftime(CSV.FORMAT)} | {rupee_symbol}{row['amount']:.2f} | {row['category']} | {row['description']}\033[0m")

            total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
            print("\nSummary:")
            print(f"Total Income: {rupee_symbol}{total_income:.2f}")
            print(f"Total Expense: {rupee_symbol}{total_expense:.2f}")
            print(f"Net Savings: {rupee_symbol}{(total_income - total_expense):.2f}")

        return filtered_df

        

        



def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of transaction or enter for today's date(dd-mm-yyyy): ",allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date,amount,category,description)

def plot_transactions(df):
    df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
    df.set_index('date', inplace=True)
    full_range = pd.date_range(start=df.index.min(), end=df.index.max())
    income_df = df[df["category"] == "Income"].resample("D").sum().reindex(full_range, fill_value=0)
    expense_df = df[df["category"] == "Expense"].resample("D").sum().reindex(full_range, fill_value=0)
    income_cumsum = income_df["amount"].cumsum()
    expense_cumsum = expense_df["amount"].cumsum()
    net_money = income_cumsum - expense_cumsum
    plt.figure(figsize=(10, 5))
    plt.plot(net_money.index, net_money, label="Net Money", color="b")
    plt.title("Net Balance Over Time")
    plt.xlabel("Date")
    plt.ylabel("Net Amount ($)")
    plt.axhline(0, color='black', lw=0.8, ls='--')  
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()




 
def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary withnin a date range")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice =="1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")    
            end_date = get_date("Enter the end date (dd-mm-yyyy): ") 
            df = CSV.get_transactions(start_date,end_date)
            if input("Do you want to see the Net Balance Graph?(y/n) ").lower() =="y":
                plot_transactions(df)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1, 2 or 3.")

main()
