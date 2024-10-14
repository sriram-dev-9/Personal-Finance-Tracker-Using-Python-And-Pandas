```markdown
# Personal Finance Tracker

This is a simple personal finance tracking application written in Python. It allows you to track income and expenses, view transaction summaries over a selected date range, and visualize your net balance over time using graphs.

## Features

- Add transactions (date, amount, category, and description)
- View transaction history within a specified date range
- Get a summary of total income, expenses, and net savings
- Plot a graph of net balance over time

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/finance-tracker.git
   cd finance-tracker
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Make sure the `data_entry.py` file is present in the same directory. It contains the following functions:
   - **`get_date(prompt, allow_default=False)`**: Prompts the user for a valid date or defaults to today's date if allowed.
   - **`get_amount()`**: Asks the user for a valid transaction amount (must be a positive number).
   - **`get_category()`**: Lets the user choose between 'Income' or 'Expense'.
   - **`get_description()`**: Optionally captures a description for the transaction.

## Usage

1. Run the main program:
   ```bash
   python main.py
   ```

2. Follow the on-screen options:
   - **1**: Add a new transaction.
   - **2**: View transactions and summary within a date range.
   - **3**: Exit the application.

3. When viewing transactions, you can also choose to visualize the net balance graph by typing `y` when prompted.

## Example

### Adding a Transaction

```
1. Add a new transaction
Enter the date of transaction or enter for today's date (dd-mm-yyyy): 13-10-2024
Enter the amount: 1500
Enter the category ('I' for Income or 'E' for Expense): I
Enter the description (optional): Freelance Project
Successfully Added!
```

### Viewing Transactions and Summary

```
Enter the start date (dd-mm-yyyy): 01-10-2024
Enter the end date (dd-mm-yyyy): 13-10-2024
Transactions from 01-10-2024 to 13-10-2024:
13-10-2024 | ₹1500.00 | Income | Freelance Project

Summary:
Total Income: ₹1500.00
Total Expense: ₹0.00
Net Savings: ₹1500.00
```

### Net Balance Graph

When viewing the transaction summary, you can plot a graph that shows the net balance over time:

- **Blue Line**: Represents your net savings after considering income and expenses.
- **X-Axis**: The date range.
- **Y-Axis**: The net amount in rupees (₹).

## Requirements

- Python 3.x
- Libraries:
  - `pandas`
  - `matplotlib`

To install these, simply run:
```bash
pip install pandas matplotlib
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- [Your Name](https://www.linkedin.com/in/your-linkedin-profile)
```

This is the final version of your `README.md`. You can replace "yourusername" and "your-linkedin-profile" with your actual GitHub and LinkedIn information. Let me know if you need further changes!
