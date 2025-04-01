import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="subscriber_db"
)

cursor = conn.cursor()

# Check if the subscriber table exists
cursor.execute("SHOW TABLES LIKE 'subscriber'")
table_exists = cursor.fetchone()
assert table_exists, "Table 'subscriber' does not exist!"

# Validate columns
cursor.execute("DESCRIBE subscriber")
columns = {col[0] for col in cursor.fetchall()}
required_columns = {"id", "email", "subscription_date"}
assert required_columns.issubset(columns), f"Missing columns: {required_columns - columns}"

# verify inserted data
cursor.execute("SELECT subscription_date FROM subscriber LIMIT 1")
assert cursor.fetchone(), "Subscription date column is missing data!"


print(" Schema validation passed!")
conn.close()
