# Build a Budget App

A Python certification project from the freeCodeCamp Python curriculum.

This project implements a simple budget management system that records transactions in different spending categories and generates a text-based chart showing the relative percentage spent by category.

## Project Objective

Build a `Category` class and a `create_spend_chart()` function that satisfy the certification project requirements and pass all automated tests.

## Features

* Create independent budget categories
* Record deposits
* Record withdrawals
* Calculate the current balance
* Check whether sufficient funds are available
* Transfer money between categories
* Print formatted transaction ledgers
* Calculate spending percentages
* Generate a vertical text-based spending chart

## Concepts Practiced

* Python classes and objects
* Instance attributes
* Instance methods
* Lists and dictionaries
* Loops and conditional logic
* String formatting
* Default parameters
* Boolean return values
* Data aggregation
* Percentage calculations
* Text-based chart generation

## Project Structure

```text
build-a-budget-app/
├── main.py
└── README.md
```

## Category Class

Each `Category` object contains:

* A category name
* A transaction ledger
* Deposit and withdrawal methods
* Balance calculation
* Fund validation
* Transfers between categories
* A custom string representation

Example:

```python
food = Category("Food")

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(
    15.89,
    "restaurant and more food for dessert",
)

clothing = Category("Clothing")
food.transfer(50, clothing)

print(food)
```

Expected output:

```text
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

## Spending Chart

The `create_spend_chart()` function:

1. Calculates withdrawals from each category.
2. Excludes deposits.
3. Calculates each category's percentage of total spending.
4. Rounds each percentage down to the nearest 10.
5. Produces a vertical text-based bar chart.

Example:

```python
print(
    create_spend_chart(
        [food, clothing, auto]
    )
)
```

Example output:

```text
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     
```

## Running the Project

Run the Python file with:

```bash
python main.py
```

No external libraries are required.

## Test Coverage

The freeCodeCamp project contains 24 automated tests covering:

* Deposits
* Withdrawals
* Balance calculations
* Transfers
* Fund validation
* Category formatting
* Spending percentage calculations
* Chart spacing and alignment

## Status

Completed — all 24 automated tests passed.

## Author

Duong Kim Cuong

## Learning Path

Completed as part of the freeCodeCamp Python learning curriculum.
