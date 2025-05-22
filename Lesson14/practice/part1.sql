CREATE TABLE IF NOT EXISTS tasks
(
    task_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    title       TEXT NOT NULL,
    description TEXT,
    status      TEXT CHECK (status IN ('Pending', 'In Progress', 'Completed')) DEFAULT 'Pending',
    priority    INTEGER CHECK ( priority BETWEEN 1 AND 5) DEFAULT 3
);