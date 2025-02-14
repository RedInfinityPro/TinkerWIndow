CREATE TABLE Employees (
    employee_id INTEGER PRIMARY KEY,
    volunteer INTEGER NOT NULL,  -- Use INTEGER (0 = false, 1 = true)
    position VARCHAR(255) NOT NULL,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    pay DECIMAL(10, 2) CHECK (pay >= 0),
    password VARCHAR(255) NOT NULL
);

INSERT INTO Employees (employee_id, volunteer, position, firstname, lastname, email, pay, password)
VALUES
    (0, 1, 'Sound Design', 'Bob', 'Tommy', 'BobTommy@gmail.com', 200.00, '123!!'),
    (1, 0, 'Sound Design', 'Mack', 'Jack', 'MackJack@gmail.com', 1200.00, '112221!!');
GO

SELECT * FROM Employees;

SELECT @@SERVERNAME

DROP TABLE Employees;