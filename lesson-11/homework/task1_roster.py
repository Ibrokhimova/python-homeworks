import sqlite3

# Step 1:
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")
conn.commit()
print("Step 1: 'Roster' table created.")

# Step 2: 
characters = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

cursor.executemany("INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)", characters)
conn.commit()
print("Step 2: Data inserted successfully.")

# Step 3: 
cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")
conn.commit()
print("Step 3: Name updated from 'Jadzia Dax' to 'Ezri Dax'.")

# Step 4:
cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
bajoran_characters = cursor.fetchall()
print("Step 4: Bajoran characters (Name, Age):")
for name, age in bajoran_characters:
    print(f"- {name}, {age} years old")

# Step 5: 
cursor.execute("DELETE FROM Roster WHERE Age > 100")
conn.commit()
print("Step 5: Characters older than 100 years deleted.")

# Bonus Task: 
cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")

rank_updates = [
    ("Captain", "Benjamin Sisko"),
    ("Lieutenant", "Ezri Dax"),
    ("Major", "Kira Nerys")
]

for rank, name in rank_updates:
    cursor.execute("UPDATE Roster SET Rank = ? WHERE Name = ?", (rank, name))
conn.commit()
print("Bonus: 'Rank' column added and updated.")

cursor.execute("SELECT Name, Species, Age, Rank FROM Roster ORDER BY Age DESC")
sorted_characters = cursor.fetchall()
print("Advanced Query: Characters sorted by age (descending):")
for row in sorted_characters:
    print(row)
conn.close()
