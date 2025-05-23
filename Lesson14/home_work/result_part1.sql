-- Тут sql для первой части задания-- Тут sql для первой части задания
CREATE TABLE IF NOT EXISTS students (
    student_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email    TEXT UNIQUE,
    course INTEGER DEFAULT 0
);
