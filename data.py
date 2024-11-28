import sqlite3

def fetch_dersler():
    connection = sqlite3.connect("data.sqlite")  # Replace with your SQLite database file
    connection.row_factory = sqlite3.Row  # To fetch rows as dictionaries
    cursor = connection.cursor()
    query = "SELECT * FROM dersler;"  # Assuming 'dersler' is a table in your database
    cursor.execute(query)
    results = [dict(row) for row in cursor.fetchall()]  # Convert rows to dictionaries
    cursor.close()
    connection.close()
    return results


def fetch_ogrenciler():
    connection = sqlite3.connect("db.sqlite")  # Replace with your SQLite database file
    connection.row_factory = sqlite3.Row  # To fetch rows as dictionaries
    cursor = connection.cursor()
    query = "SELECT * FROM ogrenciler;"  # Assuming 'dersler' is a table in your database
    cursor.execute(query)
    results = [dict(row) for row in cursor.fetchall()]  # Convert rows to dictionaries
    cursor.close()
    connection.close()
    return results

