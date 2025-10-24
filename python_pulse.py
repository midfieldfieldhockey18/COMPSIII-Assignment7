import sqlite3

# Connect to the database
connection = sqlite3.connect('python_pulse.db')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# ---------------------------------------------------
# Drop tables if they already exist to avoid duplicates
# ---------------------------------------------------
cursor.execute("DROP TABLE IF EXISTS user_workouts")
cursor.execute("DROP TABLE IF EXISTS workouts")
cursor.execute("DROP TABLE IF EXISTS goals")
cursor.execute("DROP TABLE IF EXISTS profiles")
cursor.execute("DROP TABLE IF EXISTS users")

# ---------------------------------------------------
# Create Users table
# ---------------------------------------------------
cursor.execute("""
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

# ---------------------------------------------------
# Create Profiles table (one-to-one with Users)
# ---------------------------------------------------
cursor.execute("""
CREATE TABLE profiles (
    profile_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL UNIQUE,
    height INTEGER,
    weight INTEGER,
    age INTEGER,
    bio TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)
""")

# ---------------------------------------------------
# Create Goals table (one-to-many with Users)
# ---------------------------------------------------
cursor.execute("""
CREATE TABLE goals (
    goal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    goal_name TEXT,
    target INTEGER,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)
""")

# ---------------------------------------------------
# Create Workouts table
# ---------------------------------------------------
cursor.execute("""
CREATE TABLE workouts (
    workout_id INTEGER PRIMARY KEY AUTOINCREMENT,
    workout_name TEXT,
    description TEXT,
    duration INTEGER
)
""")

# ---------------------------------------------------
# Create user_workouts table (many-to-many)
# ---------------------------------------------------
cursor.execute("""
CREATE TABLE user_workouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    workout_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (workout_id) REFERENCES workouts(workout_id)
)
""")

# ---------------------------------------------------
# Insert sample Users data
# ---------------------------------------------------
users_data = [
    ('john_doe', 'password123', 'john_doe@gmail.com'),
    ('jane_smith', 'mypassword', 'jane@gmail.com'),
    ('alice_jones', 'alicepassword', 'ajones@yahoo.com'),
    ('bob_brown', 'bobpassword', 'bobby@yahoo.com'),
    ('rebecca_charles', 'rebeccapassword', 'becky123@gmail.com')
]

cursor.executemany("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", users_data)

# ---------------------------------------------------
# Insert sample Profiles data
# ---------------------------------------------------
profiles_data = [
    (1, 180, 75, 28, 'Loves hiking and outdoor activities.'),
    (2, 165, 60, 25, 'Enjoys painting and art.'),
    (3, 170, 65, 30, 'Passionate about technology and coding.'),
    (4, 175, 80, 22, 'Avid reader and writer.'),
    (5, 160, 50, 27, 'Fitness enthusiast and gym lover.')
]

cursor.executemany("INSERT INTO profiles (user_id, height, weight, age, bio) VALUES (?, ?, ?, ?, ?)", profiles_data)

# ---------------------------------------------------
# Insert sample Goals data
# ---------------------------------------------------
goals_data = [
    ('Run 5km', 5, 1),
    ('Lose 10kg', 10, 2),
    ('Lift 100kg 3x', 100, 3),
    ('Meditate daily', 1, 5),
    ('Cycle 100km', 100, 4),
    ('Complete a marathon', 42, 5),
    ('Run 5 km', 5, 5)
]

cursor.executemany("INSERT INTO goals (goal_name, target, user_id) VALUES (?, ?, ?)", goals_data)

# ---------------------------------------------------
# Insert sample Workouts data
# ---------------------------------------------------
workouts_data = [
    ('Morning Yoga', 'A refreshing morning yoga session.', 30),
    ('HIIT Workout', 'High-Intensity Interval Training.', 45),
    ('Weightlifting', 'Full body weightlifting session.', 60),
    ('Cycling', 'Outdoor cycling for endurance.', 120),
    ('Meditation', 'Guided meditation for relaxation.', 15)
]

cursor.executemany("INSERT INTO workouts (workout_name, description, duration) VALUES (?, ?, ?)", workouts_data)

# ---------------------------------------------------
# Insert sample User_Workouts data
# ---------------------------------------------------
user_workouts_data = [
    (1, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 1),
    (5, 2)
]

cursor.executemany("INSERT INTO user_workouts (user_id, workout_id) VALUES (?, ?)", user_workouts_data)

# ---------------------------------------------------
# Commit all changes to the database
# ---------------------------------------------------
connection.commit()



# DON'T DELETE THIS LINE - Commit the changes and close the connection. This should be the LAST line of your program.
connection.commit()
connection.close()
