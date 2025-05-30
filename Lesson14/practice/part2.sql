-- Задача 1: Обычная задача со всеми заполненными полями.
INSERT INTO tasks(title, description, status, priority)
VALUES ('Создать задачи', 'Описание задач', 'Pending', 2);
-- Задача 2: Задача без описания, но с высоким приоритетом (5), статусом "В ожидании" и названием "Позвонить другу".
INSERT INTO tasks(title, status, priority)
VALUES ('Позвонить другу',  'Pending', 5);
INSERT INTO tasks(title, status, priority)
VALUES ('Позвонить на работу',  'Pending', 3);
-- Задача 3: Задача со статусом "В процессе" и названием "Завершить отчёт".
INSERT INTO tasks(title, status)
VALUES ('Завершить отчёт',  'In Progress');
-- Задача 4: Задача с минимальным приоритетом (1).
-- Задача 5: Задача, в которой вы полагаетесь на значения по умолчанию для status и priority.