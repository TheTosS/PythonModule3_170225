-- Тут sql для третьей части задания
--1.  **Выбрать всех студентов**: Получить все столбцы для всех студентов.
SELECT *
FROM students;


--2.  **Выбрать имена и email**: Получить только **`first_name`**, **`last_name`** и **`email`** всех студентов.
SELECT first_name, last_name, email
FROM students;

--3. **Студенты на конкретном курсе**: Выбрать всех студентов, которые изучают курс "sport", отсортированных по фамилии в алфавитном порядке.
SELECT *
FROM students
WHERE course = 'sport'
ORDER BY last_name ASC ;


--4. **Количество студентов по курсу**: Посчитать, сколько студентов на каждом курсе.
SELECT course , COUNT(*) AS student_count
FROM students
GROUP BY course;

--5. **Найти студента по части email**: Найти студента, чей email содержит "@aoll.com".
SELECT *
FROM students
WHERE email LIKE '%@aoll.com';-- Тут sql для третьей части задания
