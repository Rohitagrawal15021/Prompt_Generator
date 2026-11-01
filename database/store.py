import sqlite3
import os
import time

# Database folder (the directory containing this script)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Database file path: .../database/context.db
DB_PATH = os.path.join(BASE_DIR, "context.db")

# Connect to database
conn = sqlite3.connect(DB_PATH)

# Create cursor
cursor = conn.cursor()

print("Database connected successfully!")


# --- Database Schema Setup ---

# Table 1: Events
cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts REAL,
    app TEXT,
    title TEXT,
    text TEXT,
    img TEXT,
    session_id INTEGER,
    summarized INTEGER DEFAULT 0
)
""")

# Table 2: Sessions
cursor.execute("""
CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    start REAL,
    end REAL,
    summary TEXT,
    topics TEXT,
    activity TEXT
)
""")

# Table 3: Skills
cursor.execute("""
CREATE TABLE IF NOT EXISTS skills (
    topic TEXT PRIMARY KEY,
    score REAL,
    updated REAL
)
""")

# Table 4: Feedback
cursor.execute("""
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ts REAL,
    query TEXT,
    prompt TEXT,
    rating INTEGER,
    edited TEXT
)
""")

conn.commit()
print("All tables created successfully!")


# --- Helper Functions ---

def insert_event(app, title, text, img=None):
    """Inserts a new activity/window event into the events table."""
    cursor.execute("""
    INSERT INTO events (ts, app, title, text, img)
    VALUES (?, ?, ?, ?, ?)
    """, (time.time(), app, title, text, img))
    conn.commit()
    print("Event inserted successfully!")


def show_events():
    """Fetches and displays all logged events."""
    cursor.execute("SELECT * FROM events")
    records = cursor.fetchall()
    for row in records:
        print(row)
    return records


if __name__ == "__main__":
    print("My Prompt Agent Database is ready!")
    show_events()
    conn.close()
