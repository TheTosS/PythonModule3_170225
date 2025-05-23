-- Тут sql для второй части задания
--1.  **Студент 1**: Полностью заполненные данные.
INSERT OR IGNORE INTO students (first_name, last_name, email, course)
VALUES ('Eugen', 'Popov', 'popppgg@mail.com', 'math');

--2.  **Студент 2**: Студент, который пока не назначен на курс (используйте значение по умолчанию для `course`).
INSERT INTO students (first_name, last_name, email, course)
VALUES ('Anna', 'Yovova', 'QWERT@hot.ee', NULL );
--3.  **Студент 3**: Студент с необычным именем и фамилией.
INSERT INTO students (first_name, last_name, email, course)
VALUES ('Olja', 'Oja', 'zuzzza@webb.de', 'sport');
--4.  **Студент 4**: Студент, который записывается на курс "Математика"
INSERT INTO students (first_name, last_name, email, course)
VALUES ('Azur', 'Magamedov', 'asassw@aoll.com', 'sport');

--5.  **Студент 5**: Еще один студент, где вы полагаетесь на значение по умолчанию для `course`.
INSERT INTO students (first_name, last_name, email, course)
VALUES ('John', 'Wein', 'Johnn@yundex.ru', NULL );-- Тут sql для второй части задания
