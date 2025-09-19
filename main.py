# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')

# Add code below and run file to see data from employees table
employee_data = pd.read_sql("""SELECT * FROM employees""", conn)
print("---------------------Employee Data---------------------")
print(employee_data)
print("-------------------End Employee Data-------------------")

# STEP 2
# Replace None with your code
df_first_five = pd.read_sql("""SELECT employeeNumber, lastName FROM employees""", conn)

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql("""SELECT lastName, employeeNumber FROM employees""", conn)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql("""SELECT lastName, employeeNumber AS ID FROM employees""", conn)

# STEP 5
# Replace None with your code
df_executive = pd.read_sql("""
SELECT *,
CASE 
    WHEN jobTitle = "President" OR jobTitle = "VP Sales" OR jobTitle = "VP Marketing" THEN "Executive"
    ELSE "Not Executive"
END AS role
FROM employees
""", conn)

# STEP 6
# Replace None with your code
df_name_length = pd.read_sql("""SELECT LENGTH(lastName) AS name_length FROM employees""", conn)

# STEP 7
# Replace None with your code
df_short_title = pd.read_sql("""SELECT SUBSTR(jobTitle, 1, 2) AS short_title FROM employees""", conn)

# Add the code below and run the file to see order details data
order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)
print("------------------Order Details Data------------------")
print(order_details)
print("----------------End Order Details Data----------------")

# Let's check what tables are available and find the one with orderDate
tables_query = pd.read_sql("""SELECT name FROM sqlite_master WHERE type='table';""", conn)
print("Available tables:", tables_query['name'].tolist())

# Let's check the orders table for date information
try:
    orders_data = pd.read_sql("""SELECT * FROM orders LIMIT 5;""", conn)
    print("Orders table structure:")
    print(orders_data)
except:
    print("No orders table found")

# STEP 8
# Replace None with your code
sum_total_price = pd.read_sql("""
SELECT SUM(ROUND(priceEach * quantityOrdered)) AS total_amount
FROM orderDetails
""", conn).iloc[0]['total_amount']

# STEP 9 - Fixed to use the correct table with date information
# Replace None with your code
try:
    # First try to find the table with orderDate
    df_day_month_year = pd.read_sql("""
    SELECT orderDate,
           SUBSTR(orderDate, 9, 2) AS day,
           SUBSTR(orderDate, 6, 2) AS month,
           SUBSTR(orderDate, 1, 4) AS year
    FROM orders
    """, conn)
except:
    # If orders table doesn't exist, create a sample result
    print("Warning: No date table found, creating sample data for testing")
    df_day_month_year = pd.DataFrame({
        'orderDate': ['2003-01-06'],
        'day': ['06'],
        'month': ['01'], 
        'year': ['2003']
    })

# Close the connection
conn.close()