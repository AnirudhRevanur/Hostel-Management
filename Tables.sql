-- Tables for Hostel Management System

-- Tables for Hostel Management System

CREATE TABLE student (
    StudentID INT PRIMARY KEY AUTO_INCREMENT,
    sname VARCHAR(255),
    address VARCHAR(255),
    phone VARCHAR(15),
    fathername VARCHAR(255),
    mothername VARCHAR(255),
    sem INT,
    roomno INT
);

CREATE TABLE fee (
    fee_id INT PRIMARY KEY AUTO_INCREMENT,
    fee_month VARCHAR(20),
    fee_status VARCHAR(20),
    SID INT,
    FOREIGN KEY (SID) REFERENCES student(StudentID)
);

CREATE TABLE Room (
  Room_Id INT NOT NULL,
  Type INT NOT NULL,
  Capacity INT NOT NULL,
  StudentID INT,
  BookingID INT,
  PRIMARY KEY (Room_Id),
  FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
);

CREATE TABLE Mess (
  Capacity INT NOT NULL,
  Location INT NOT NULL,
  Name INT NOT NULL,
  MessID INT NOT NULL,
  PRIMARY KEY (MessID)
);

CREATE TABLE hostellogin (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    password VARCHAR(255)
);

INSERT INTO hostellogin(name, password)
VALUES ('admin', 'admin');

CREATE TABLE student_login (
    login_id INT PRIMARY KEY AUTO_INCREMENT,
    studentid INT,
    roomid INT,
    sname VARCHAR(255),
    place VARCHAR(255),
    sem INT,
    date DATE,
    time TIME,
    FOREIGN KEY (roomid) REFERENCES Room(Room_Id),
    FOREIGN KEY (studentid) REFERENCES student(StudentID)
);

CREATE TABLE student_logout (
    logout_id INT PRIMARY KEY AUTO_INCREMENT,
    studentid INT,
    roomid INT,
    sname VARCHAR(255),
    place VARCHAR(255),
    sem INT,
    date DATE,
    time TIME,
    FOREIGN KEY (roomid) REFERENCES Room(Room_Id),
    FOREIGN KEY (studentid) REFERENCES student(StudentID)
);


--Trigger to automatically update the Room table whenever a student is assigned to a 

DELIMITER //
CREATE TRIGGER AssignRoom
AFTER INSERT ON student
FOR EACH ROW
BEGIN
    DECLARE roomID INT;
    SELECT Room_Id INTO roomID FROM Room WHERE StudentID IS NULL LIMIT 1;
    IF roomID IS NOT NULL THEN
        INSERT INTO student_login (studentid, roomid, sname, place, sem, date, time)
        VALUES (NEW.StudentID, roomID, NEW.sname, NEW.address, NEW.sem, CURRENT_DATE(), CURRENT_TIME());
        UPDATE Room SET StudentID = NEW.StudentID, BookingID = roomID WHERE Room_Id = roomID;
    END IF;
END;
//
DELIMITER ;


-- procedure to calculate the total fee paid by a specific student.

DELIMITER //
CREATE PROCEDURE CalculateTotalFee(IN student_id INT)
BEGIN
    SELECT COUNT(*) AS TotalPaidFees
    FROM fee
    WHERE SID = student_id AND fee_status = 'Paid';
END;
//
DELIMITER ;


-- function to retrieve the number of students in each room.

DELIMITER //
CREATE FUNCTION CountStudentsInRoom(room_id INT)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE student_count INT;
    SELECT COUNT(*) INTO student_count FROM Room WHERE Room_Id = room_id AND StudentID IS NOT NULL;
    RETURN student_count;
END;
//
DELIMITER ;


-- Retrieve all students' names and their corresponding room numbers.
SELECT s.sname, r.roomno
FROM student s
JOIN Room r ON s.StudentID = r.StudentID;

-- Get the details of all unpaid fees.
SELECT * FROM fee WHERE fee_status = 'Unpaid';

-- List all messes and their capacities.
SELECT Name, Capacity FROM Mess;

-- Retrieve the names of students who have paid their fees.
SELECT s.sname
FROM student s
JOIN fee f ON s.StudentID = f.SID
WHERE f.fee_status = 'Paid';

-- Get the details of students staying in rooms with a capacity greater than 3.
SELECT *
FROM student
WHERE StudentID IN (SELECT StudentID FROM Room WHERE Capacity > 3);

-- Find students who have logged in and out on the same date.
SELECT l1.sname
FROM student_login l1
WHERE EXISTS (
    SELECT 1
    FROM student_logout l2
    WHERE l1.date = l2.date AND l1.studentid = l2.studentid
);

-- Retrieve all rooms with students from the same semester.
SELECT *
FROM Room r
WHERE EXISTS (
    SELECT 1
    FROM student s
    WHERE r.StudentID = s.StudentID AND r.sem = s.sem
);

-- Find rooms with more than 2 students.
SELECT Room_Id, COUNT(*) AS StudentCount
FROM Room
WHERE StudentID IS NOT NULL
GROUP BY Room_Id
HAVING COUNT(*) > 2;

-- Calculate the total number of fees paid by each student.
SELECT SID, COUNT(*) AS TotalPaidFees
FROM fee
WHERE fee_status = 'Paid'
GROUP BY SID;




