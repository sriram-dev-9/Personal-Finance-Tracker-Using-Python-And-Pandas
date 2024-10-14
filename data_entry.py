from datetime import datetime
format = "%d-%m-%Y"
CATEGORIES = {"I":"Income","E":"Expense"}

def get_date(prompt,allow_default = False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(format)
    else:
        try:
            valid_datetime = datetime.strptime(date_str,format)
            return valid_datetime.strftime(format)
        except ValueError:
            print("Invalid data format, Please enter properly.")
            return get_date(prompt,allow_default)

def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("Amount be a non-negative non-zero integer")
        return amount
    except Exception as e:
        print(e)
        return get_amount()
    
def get_category():
    category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    print("You have entered an invalid input.") 
    return get_category

def get_description():
    return input("Enter the description (optional): ")
