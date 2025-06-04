import sqlite3
conn = sqlite3.connect("library.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
""")

books_data = [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
]
cursor.executemany("INSERT INTO Books VALUES (?, ?, ?, ?)", books_data)
conn.commit()
cursor.execute("""
UPDATE Books
SET Year_Published = 1950
WHERE Title = '1984'
""")
conn.commit()
print("Dystopian books:")
cursor.execute("""
SELECT Title, Author FROM Books
WHERE Genre = 'Dystopian'
""")
results = cursor.fetchall()
for title, author in results:
    print(f"{title} by {author}")

cursor.execute("""
DELETE FROM Books
WHERE Year_Published < 1950
""")
conn.commit()

try:
    cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
    conn.commit()
except sqlite3.OperationalError:
    print("Column 'Rating' already exists.")

ratings = {
    "To Kill a Mockingbird": 4.8,
    "1984": 4.7,
    "The Great Gatsby": 4.5
}
for title, rating in ratings.items():
    cursor.execute("""
    UPDATE Books
    SET Rating = ?
    WHERE Title = ?
    """, (rating, title))
conn.commit()

print("\nBooks sorted by Year Published:")
cursor.execute("""
SELECT * FROM Books
ORDER BY Year_Published ASC
""")
sorted_books = cursor.fetchall()
for book in sorted_books:
    print(book)

conn.close()
