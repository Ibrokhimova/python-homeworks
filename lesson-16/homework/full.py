import pandas as pd
import sqlite3
try:
    conn = sqlite3.connect('chinook.db')
    customers_df = pd.read_sql_query("SELECT * FROM customers", conn)
    print("=== Customers (chinook.db) – First 10 Rows ===")
    print(customers_df.head(10))
except Exception as e:
    print("Error reading chinook.db:", e)
finally:
    conn.close()
try:
    iris_df = pd.read_json('iris.json')
    print("\n=== Iris (iris.json) – Shape and Column Names ===")
    print("Shape:", iris_df.shape)
    print("Columns:", iris_df.columns.tolist())
except Exception as e:
    print("Error reading iris.json:", e)

try:
    titanic_df = pd.read_excel('titanic.xlsx')
    print("\n=== Titanic (titanic.xlsx) – First 5 Rows ===")
    print(titanic_df.head())
except Exception as e:
    print("Error reading titanic.xlsx:", e)

try:
    flights_df = pd.read_parquet('flights.parquet')
    print("\n=== Flights (flights.parquet) – Data Summary ===")
    print(flights_df.info())
except Exception as e:
    print("Error reading flights.parquet:", e)
try:
    movies_df = pd.read_csv('movie.csv')
    print("\n=== Movies (movie.csv) – Random Sample of 10 Rows ===")
    print(movies_df.sample(10))
except Exception as e:
    print("Error reading movie.csv:", e)
