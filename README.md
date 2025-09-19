# SQL Lab - Employee Database Queries

## Quick Start
1. Run `pipenv install` and `pipenv shell`
2. Complete the code in `main.py`
3. Test with `pytest` or `python3 main.py`

## Overview
You're working as an HR data analyst for Northwinds Company. Use SQL queries to retrieve employee information from the `data.sqlite` database.

## Tasks

### Step 1: Setup
Import `sqlite3` and `pandas`, connect to `data.sqlite`

### Step 2: Basic SELECT
Get employee number and last name from all employees

### Step 3: Column Order
Same as Step 2, but with last name first

### Step 4: Aliases
Repeat Step 3, rename employee number column to 'ID'

### Step 5: CASE Statement
Create a 'role' column:
- "Executive" for President, VP Sales, VP Marketing
- "Not Executive" for all others

### Step 6: String Functions
Get the length of each employee's last name

### Step 7: String Manipulation
Get the first 2 letters of each job title

### Step 8: Numeric Functions
Calculate total amount from orderDetails table:
- Multiply `priceEach` × `quantityOrdered` 
- Round the result
- Sum all orders

### Step 9: Date Functions
Extract day, month, year from date column (if available)

## Key SQL Functions Used
- `SELECT` - Choose columns
- `AS` - Create aliases
- `CASE WHEN` - Conditional logic
- `LENGTH()` - String length
- `SUBSTR()` - Extract substring
- `ROUND()` - Round numbers
- `SUM()` - Add values

## Testing
Each step has a corresponding test. Run `pytest` to check your work.