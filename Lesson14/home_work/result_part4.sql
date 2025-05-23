-- Тут sql для четвертой части задания
--1.  **Обновить курс студента**: Измените курс студента с **`student_id` равным 1** на "Веб-разработка".
UPDATE students
SET course = 'Веб-разработка'
WHERE student_ID = '1';
--2.  **Назначить курс неназначенным студентам**: Установите курс "Введение в ИТ" для всех студентов, у которых **`course` равен "Не назначен"**.
UPDATE  students
SET course = 'Введение в ИТ'
WHERE course  IS NULL;
--3.  **Исправить email**: Найдите студента с именем "Иван" и фамилией "Петров" и измените его email на "ivan.petrov@newdomain.com".
UPDATE students
SET email = 'JohnWein@newdomain.com'
WHERE first_name = 'John' AND last_name = 'Wein';


--4.  **Обновить фамилию и курс**: Для студента с **`email` "student3@example.com"** обновите фамилию на "Смирнов" и курс на "Алгоритмы и структуры данных" Тут sql для четвертой части задания
UPDATE students
SET last_name ='Смирнов' , course = 'Алгоритмы и структуры данных'
WHERE email = 'popppgg@mail.com'
