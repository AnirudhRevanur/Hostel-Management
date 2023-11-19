-- Tables for Hostel Management System

CREATE TABLE student (
    hostelid INT PRIMARY KEY,
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
    FOREIGN KEY (SID) REFERENCES student(hostelid)
);

CREATE TABLE Room
(
  Room_Id INT NOT NULL,
  Type INT NOT NULL,
  Capacity INT NOT NULL,
  StudentID INT NOT NULL,
  BookingID INT NOT NULL,
  PRIMARY KEY (Room_Id),
  FOREIGN KEY (StudentID) REFERENCES Student(StudentID)
);

CREATE TABLE Mess
(
  Capacity INT NOT NULL,
  Location INT NOT NULL,
  Name INT NOT NULL,
  MessID INT NOT NULL,
  PRIMARY KEY (MessID),
);

CREATE TABLE hostellogin (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    password VARCHAR(255)
);

CREATE TABLE login (
    login_id INT PRIMARY KEY AUTO_INCREMENT,
    hostelids INT,
    sname VARCHAR(255),
    place VARCHAR(255),
    sem INT,
    date DATE,
    time TIME,
    FOREIGN KEY (hostelids) REFERENCES student(hostelid)
);

CREATE TABLE logout (
    logout_id INT PRIMARY KEY AUTO_INCREMENT,
    hostelids INT,
    sname VARCHAR(255),
    place VARCHAR(255),
    sem INT,
    date DATE,
    time TIME,
    FOREIGN KEY (hostelids) REFERENCES student(hostelid)
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
        UPDATE Room SET StudentID = NEW.hostelid WHERE Room_Id = roomID;
    END IF;
END;
//
DELIMITER ;

-- procedure to calculate the total fee paid by a specific student.

DELIMITER //
CREATE PROCEDURE CalculateTotalFee(IN student_id INT)
BEGIN
    SELECT SUM(CASE WHEN fee_status = 'Paid' THEN 1 ELSE 0 END) AS TotalPaidFees
    FROM fee
    WHERE SID = student_id;
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
JOIN Room r ON s.hostelid = r.StudentID;

-- Get the details of all unpaid fees.
SELECT * FROM fee WHERE fee_status = 'Unpaid';

-- List all messes and their capacities.
SELECT Name, Capacity FROM Mess;


-- Retrieve the names of students who have paid their fees.
SELECT sname
FROM student
WHERE hostelid IN (SELECT SID FROM fee WHERE fee_status = 'Paid');

-- Get the details of students staying in rooms with a capacity greater than 3.
SELECT *
FROM student
WHERE hostelid IN (SELECT StudentID FROM Room WHERE Capacity > 3);

-- Find students who have logged in and out on the same date.
SELECT sname
FROM login l1
WHERE EXISTS (
    SELECT 1
    FROM logout l2
    WHERE l1.date = l2.date AND l1.hostelids = l2.hostelids
);

-- Retrieve all rooms with students from the same semester.
SELECT *
FROM Room r
WHERE EXISTS (
    SELECT 1
    FROM student s
    WHERE r.StudentID = s.hostelid AND r.StudentID = s.hostelid AND r.StudentID = s.hostelid AND r.StudentID = s.hostelid s.sem = s.sem
);

-- Find rooms with more than 2 students.
SELECT Room_Id, COUNT(*) AS StudentCount
FROM Room
GROUP BY Room_Id
HAVING COUNT(*) > 2;

-- Calculate the total number of fees paid by each student.
SELECT SID, COUNT(*) AS TotalPaidFees
FROM fee
WHERE fee_status = 'Paid'
GROUP BY SID;



