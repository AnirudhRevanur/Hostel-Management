from tkinter import *
import tkinter.messagebox as MessageBox
from mysql.connector import connection
from PIL import ImageTk, Image
from tkinter import ttk
from dotenv import load_dotenv
import os

load_dotenv()


class HostelManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x466")
        self.root.title("HOSTEL DATABASE")

        self.canvas = Canvas(self.root, width=700, height=466)
        self.canvas.pack()

        ide = Label(
            self.root, text="LOGIN PAGE", bg="#041d78", fg="#83e6e6", font=("bold", 30)
        )
        ide.place(x=180, y=30)

        self.but1 = Button(
            self.root,
            text="HOSTEL LOGIN",
            font=("italic", 20),
            bg="#83e6e6",
            command=lambda: [self.hostel_login()],
        )
        self.but1.place(x=190, y=170)

        self.but2 = Button(
            self.root,
            text="STUDENT LOGIN",
            font=("italic", 20),
            bg="#83e6e6",
            command=lambda: [self.student_login(), self.root.quit()],
        )
        self.but2.place(x=190, y=250)

    def hostel_login(self):
        hostel = Toplevel(self.root)
        hostel.geometry("525x328")
        hostel.title("HOSTEL Login page")

        ide = Label(
            hostel,
            text="HOSTEL LOGIN PAGE",
            bg="#041d78",
            fg="#83e6e6",
            font=("bold", 20),
        )
        ide.place(x=200, y=20)

        name = Label(hostel, text="USER NAME", font=("bold", 15))
        name.place(x=70, y=80)

        password = Label(hostel, text="PASSWORD", font=("bold", 15))
        password.place(x=70, y=130)

        self.e1 = Entry(hostel, show=None, font=("Arial", 17))
        self.e2 = Entry(hostel, show="*", font=("Arial", 17))
        self.e1.place(x=230, y=80)
        self.e2.place(x=230, y=130)

        submit_button = Button(
            hostel,
            text="SUBMIT",
            font=("italic", 20),
            bg="#05f6fa",
            fg="blue",
            command=self.hostel_submit,
        )
        submit_button.place(x=200, y=200)

    def hostel_submit(self):
        name = self.e1.get()
        password = self.e2.get()

        if name == "" or password == "":
            MessageBox.showerror("Insert Status", "All Fields are required")
        else:
            mydb = connection.MySQLConnection(
                host=os.environ["HOST"],
                port=3306,
                user=os.environ["USER"],
                password=os.environ["PASSWORD"],
                database=os.environ["DATABASE"],
            )
            mycursor = mydb.cursor()
            sql = "SELECT * FROM hostellogin WHERE  name = %s AND  password = %s"
            mycursor.execute(sql, (name, password))

            if mycursor.fetchone():
                MessageBox.showinfo("LOGIN Status", "Successful")
                self.but1[
                    "state"
                ] = "disabled"  # Disable HOSTEL LOGIN button after successful login
                self.option()
            else:
                MessageBox.showerror("LOGIN Status", "Invalid password or username")

    def student_login(self):
        login = Toplevel(self.root)
        login.geometry("600x300")
        login.title("Student Login Page")

        hostelid = Label(login, text="ENTER YOUR ROOMID", font=("bold", 10))
        hostelid.place(x=20, y=30)

        sname = Label(login, text="ENTER YOUR NAME", font=("bold", 10))
        sname.place(x=20, y=70)

        place = Label(login, text="ENTER PLACE", font=("bold", 10))
        place.place(x=20, y=100)

        sem = Label(login, text="ENTER SEM", font=("bold", 10))
        sem.place(x=20, y=130)

        date = Label(login, text="ENTER DATE IN THE FORM YYYY-MM-DD", font=("bold", 10))
        date.place(x=20, y=160)

        time = Label(login, text="ENTER TIME", font=("bold", 10))
        time.place(x=20, y=190)

        self.e1_hostelid = Entry(login, show=None, font=("Arial", 14))
        self.e1_sname = Entry(login, show=None, font=("Arial", 14))
        self.e1_place = Entry(login, show=None, font=("Arial", 14))
        self.e1_sem = Entry(login, show=None, font=("Arial", 14))
        self.e1_date = Entry(login, show=None, font=("Arial", 14))
        self.e1_time = Entry(login, show=None, font=("Arial", 14))

        self.e1_hostelid.place(x=300, y=30)
        self.e1_sname.place(x=300, y=70)
        self.e1_place.place(x=300, y=100)
        self.e1_sem.place(x=300, y=130)
        self.e1_date.place(x=300, y=160)
        self.e1_time.place(x=300, y=190)

        subtn = Button(
            login,
            text="submit",
            font=("italic", 15),
            bg="#83e6e6",
            command=self.submit,
        )
        subtn.place(x=300, y=220)

    def submit(self):
        hostelid = self.e1_hostelid.get()
        sname = self.e1_sname.get()
        place = self.e1_place.get()
        sem = self.e1_sem.get()
        date = self.e1_date.get()
        time = self.e1_time.get()

        if (
            hostelid == ""
            or sname == ""
            or place == ""
            or sem == ""
            or date == ""
            or time == ""
        ):
            MessageBox.showerror("Insert Status", "All Fields are required")
        else:
            mydb = connection.MySQLConnection(
                host=os.environ["HOST"],
                port=3306,
                user=os.environ["USER"],
                password=os.environ["PASSWORD"],
                database=os.environ["DATABASE"],
            )
            mycursor = mydb.cursor()
            sql = "INSERT INTO student VALUES(%s,%s,%s,%s,%s,%s)"
            val = (hostelid, sname, place, sem, date, time)
            mycursor.execute(sql, val)

            mydb.commit()
            MessageBox.showinfo("Insert Status", "Inserted Successfully")
            mydb.close()

    def option(self):
        hostelopt = Toplevel(self.root)
        hostelopt.geometry("760x700")
        hostelopt.title("Choose an option")

        ide = Label(
            hostelopt,
            text="CHOOSE AN OPTION",
            bg="#041d78",
            fg="#83e6e6",
            font=("bold", 15),
        )
        ide.place(relx=0.5, rely=0.05, anchor="center")

        button_positions = [
            (0.5, 0.2),
            (0.5, 0.3),
            (0.5, 0.4),
            (0.5, 0.5),
            (0.5, 0.6),
            (0.5, 0.7),
            (0.5, 0.8),
        ]

        button_texts = [
            "INSERT A STUDENT RECORD",
            "UPDATE A STUDENT RECORD",
            "DELETE A STUDENT RECORD",
            "STUDENT DETAILS",
            "INSERT A ROOM",
            "ROOM DETAILS",
            "LOGOUT",
        ]

        for position, text in zip(button_positions, button_texts):
            Button(
                hostelopt,
                text=text,
                font=("italic", 20),
                bg="#83e6e6",
                command=lambda: self.button_commands[text](),
            ).place(relx=position[0], rely=position[1], anchor="center")

        self.button_commands = {
            "INSERT A STUDENT RECORD": self.insert_option,
            "UPDATE A STUDENT RECORD": self.update_option,
            "DELETE A STUDENT RECORD": self.delete_option,
            "STUDENT DETAILS": self.student_details,
            "INSERT A ROOM": self.insert_room,
            "ROOM DETAILS": self.room_details,
            "LOGOUT": self.logout,
        }

    def insert_option(self):
        ins = Toplevel(self.root)
        ins.geometry("750x550")
        ins.title("Insert Page")

        ide = Label(
            ins,
            text="INSERT A STUDENT RECORD",
            bg="#041d78",
            fg="#83e6e6",
            font=("bold", 25),
        )
        ide.place(x=150, y=20)

        sid = Label(ins, text="ROOM ID", font=("bold", 15))
        sid.place(x=50, y=80)

        sname = Label(ins, text="NAME", font=("bold", 15))
        sname.place(x=50, y=130)

        splace = Label(ins, text="PLACE", font=("bold", 15))
        splace.place(x=50, y=180)

        ssem = Label(ins, text="SEM", font=("bold", 15))
        ssem.place(x=50, y=230)

        sdate = Label(ins, text="DATE", font=("bold", 15))
        sdate.place(x=50, y=280)

        stime = Label(ins, text="TIME", font=("bold", 15))
        stime.place(x=50, y=330)

        student_id = Label(ins, text="STUDENT ID", font=("bold", 15))
        student_id.place(x=50, y=380)

        self.e1_sid = Entry(ins, show=None, font=("Arial", 14))
        self.e1_sname = Entry(ins, show=None, font=("Arial", 14))
        self.e1_splace = Entry(ins, show=None, font=("Arial", 14))
        self.e1_ssem = Entry(ins, show=None, font=("Arial", 14))
        self.e1_sdate = Entry(ins, show=None, font=("Arial", 14))
        self.e1_stime = Entry(ins, show=None, font=("Arial", 14))
        self.e1_student_id = Entry(ins, show=None, font=("Arial", 14))

        self.e1_sid.place(x=200, y=80)
        self.e1_sname.place(x=200, y=130)
        self.e1_splace.place(x=200, y=180)
        self.e1_ssem.place(x=200, y=230)
        self.e1_sdate.place(x=200, y=280)
        self.e1_stime.place(x=200, y=330)
        self.e1_student_id.place(x=200, y=380)

        ins_submit_button = Button(
            ins,
            text="SUBMIT",
            font=("italic", 20),
            bg="#05f6fa",
            fg="blue",
            command=self.insert_submit,
        )
        ins_submit_button.place(x=200, y=450)

    def insert_submit(self):
        sid = self.e1_sid.get()
        sname = self.e1_sname.get()
        splace = self.e1_splace.get()
        ssem = self.e1_ssem.get()
        sdate = self.e1_sdate.get()
        stime = self.e1_stime.get()

        if (
            sid == ""
            or sname == ""
            or splace == ""
            or ssem == ""
            or sdate == ""
            or stime == ""
        ):
            MessageBox.showerror("Insert Status", "All Fields are required")
        else:
            mydb = connection.MySQLConnection(
                host=os.environ["HOST"],
                port=3306,
                user=os.environ["USER"],
                password=os.environ["PASSWORD"],
                database=os.environ["DATABASE"],
            )
            mycursor = mydb.cursor()
            sql = "INSERT INTO student (roomno, sname, address, sem, date, time) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (sid, sname, splace, ssem, sdate, stime)
            mycursor.execute(sql, val)

            mydb.commit()
            MessageBox.showinfo("Insert Status", "Inserted Successfully")
            mydb.close()

    def update_option(self):
        update_window = Toplevel(self.root)
        update_window.geometry("400x300")
        update_window.title("Update Student Record")

        ide = Label(
            update_window,
            text="UPDATE A STUDENT RECORD",
            bg="#041d78",
            fg="#83e6e6",
            font=("bold", 20),
        )
        ide.place(x=50, y=20)

        sid_label = Label(update_window, text="Enter Room ID:", font=("bold", 12))
        sid_label.place(x=50, y=80)

        self.sid_entry = Entry(update_window, show=None, font=("Arial", 14))
        self.sid_entry.place(x=220, y=80)

        update_button = Button(
            update_window,
            text="UPDATE",
            font=("italic", 15),
            bg="#05f6fa",
            fg="blue",
            command=self.update_submit,
        )
        update_button.place(x=150, y=150)

    def update_submit(self):
        sid = self.sid_entry.get()

        if sid == "":
            MessageBox.showerror("Update Status", "Please enter Room ID")
        else:
            mydb = connection.MySQLConnection(
                host=os.environ["HOST"],
                port=3306,
                user=os.environ["USER"],
                password=os.environ["PASSWORD"],
                database=os.environ["DATABASE"],
            )
            mycursor = mydb.cursor()

            # Check if the entered Room ID exists
            check_sql = "SELECT * FROM student WHERE roomno = %s"
            mycursor.execute(check_sql, (sid,))
            result = mycursor.fetchone()

            if result:
                update_window = Toplevel(self.root)
                update_window.geometry("600x400")
                update_window.title("Update Student Record")

                ide = Label(
                    update_window,
                    text="UPDATE A STUDENT RECORD",
                    bg="#041d78",
                    fg="#83e6e6",
                    font=("bold", 20),
                )
                ide.place(x=150, y=20)

                sname_label = Label(update_window, text="Name:", font=("bold", 12))
                sname_label.place(x=50, y=80)

                sname_entry = Entry(update_window, show=None, font=("Arial", 14))
                sname_entry.place(x=200, y=80)

                splace_label = Label(update_window, text="Place:", font=("bold", 12))
                splace_label.place(x=50, y=120)

                splace_entry = Entry(update_window, show=None, font=("Arial", 14))
                splace_entry.place(x=200, y=120)

                sem_label = Label(update_window, text="Semester:", font=("bold", 12))
                sem_label.place(x=50, y=160)

                sem_entry = Entry(update_window, show=None, font=("Arial", 14))
                sem_entry.place(x=200, y=160)

                date_label = Label(update_window, text="Date:", font=("bold", 12))
                date_label.place(x=50, y=200)

                date_entry = Entry(update_window, show=None, font=("Arial", 14))
                date_entry.place(x=200, y=200)

                time_label = Label(update_window, text="Time:", font=("bold", 12))
                time_label.place(x=50, y=240)

                time_entry = Entry(update_window, show=None, font=("Arial", 14))
                time_entry.place(x=200, y=240)

                update_submit_button = Button(
                    update_window,
                    text="UPDATE",
                    font=("italic", 15),
                    bg="#05f6fa",
                    fg="blue",
                    command=lambda: self.perform_update(
                        sid,
                        sname_entry.get(),
                        splace_entry.get(),
                        sem_entry.get(),
                        date_entry.get(),
                        time_entry.get(),
                        update_window,
                    ),
                )
                update_submit_button.place(x=200, y=300)

            else:
                MessageBox.showerror("Update Status", "Room ID does not exist")

            mydb.close()

    def perform_update(self, sid, sname, splace, sem, date, time, update_window):
        mydb = connection.MySQLConnection(
            host=os.environ["HOST"],
            port=3306,
            user=os.environ["USER"],
            password=os.environ["PASSWORD"],
            database=os.environ["DATABASE"],
        )
        mycursor = mydb.cursor()

        # Update student record
        update_sql = "UPDATE student SET sname = %s, address = %s, sem = %s, date = %s, time = %s WHERE roomno = %s"
        val = (sname, splace, sem, date, time, sid)
        mycursor.execute(update_sql, val)

        mydb.commit()
        MessageBox.showinfo("Update Status", "Record Updated Successfully")
        mydb.close()

        # Close the update window
        update_window.destroy()

    def delete_option(self):
        delete_window = Toplevel(self.root)
        delete_window.geometry("400x300")
        delete_window.title("Delete Student Record")

        ide = Label(
            delete_window,
            text="DELETE A STUDENT RECORD",
            bg="#041d78",
            fg="#83e6e6",
            font=("bold", 20),
        )
        ide.place(x=50, y=20)

        sid_label = Label(delete_window, text="Enter Room ID:", font=("bold", 12))
        sid_label.place(x=50, y=80)

        self.sid_delete_entry = Entry(delete_window, show=None, font=("Arial", 14))
        self.sid_delete_entry.place(x=220, y=80)

        delete_button = Button(
            delete_window,
            text="DELETE",
            font=("italic", 15),
            bg="#f65454",
            fg="white",
            command=self.delete_submit,
        )
        delete_button.place(x=150, y=150)

    def delete_submit(self):
        sid = self.sid_delete_entry.get()

        if sid == "":
            MessageBox.showerror("Delete Status", "Please enter Room ID")
        else:
            mydb = connection.MySQLConnection(
                host=os.environ["HOST"],
                port=3306,
                user=os.environ["USER"],
                password=os.environ["PASSWORD"],
                database=os.environ["DATABASE"],
            )
            mycursor = mydb.cursor()

            # Check if the entered Room ID exists
            check_sql = "SELECT * FROM student WHERE roomno = %s"
            mycursor.execute(check_sql, (sid,))
            result = mycursor.fetchone()

            if result:
                delete_confirmation = MessageBox.askyesno(
                    "Delete Confirmation",
                    "Are you sure you want to delete this record?",
                )

                if delete_confirmation:
                    # Delete student record
                    delete_sql = "DELETE FROM student WHERE roomno = %s"
                    mycursor.execute(delete_sql, (sid,))

                    mydb.commit()
                    MessageBox.showinfo("Delete Status", "Record Deleted Successfully")
                else:
                    MessageBox.showinfo("Delete Status", "Record Deletion Cancelled")

            else:
                MessageBox.showerror("Delete Status", "Room ID does not exist")

            mydb.close()

    def student_details(self):
        details_window = Toplevel(self.root)
        details_window.geometry("600x400")
        details_window.title("Student Details")

        ide = Label(
            details_window,
            text="STUDENT DETAILS",
            bg="#041d78",
            fg="#83e6e6",
            font=("bold", 20),
        )
        ide.place(x=180, y=20)

        mydb = connection.MySQLConnection(
            host=os.environ["HOST"],
            port=3306,
            user=os.environ["USER"],
            password=os.environ["PASSWORD"],
            database=os.environ["DATABASE"],
        )
        mycursor = mydb.cursor()

        # Retrieve all student records
        select_sql = "SELECT * FROM student"
        mycursor.execute(select_sql)
        records = mycursor.fetchall()

        tree = ttk.Treeview(details_window)
        tree["columns"] = ("Room ID", "Name", "Place", "Semester", "Date", "Time")
        tree.column("#0", width=0, stretch=NO)
        tree.column("Room ID", anchor=W, width=80)
        tree.column("Name", anchor=W, width=120)
        tree.column("Place", anchor=W, width=80)
        tree.column("Semester", anchor=W, width=80)
        tree.column("Date", anchor=W, width=100)
        tree.column("Time", anchor=W, width=80)

        tree.heading("#0", text="", anchor=W)
        tree.heading("Room ID", text="Room ID", anchor=W)
        tree.heading("Name", text="Name", anchor=W)
        tree.heading("Place", text="Place", anchor=W)
        tree.heading("Semester", text="Semester", anchor=W)
        tree.heading("Date", text="Date", anchor=W)
        tree.heading("Time", text="Time", anchor=W)

        for record in records:
            tree.insert("", "end", values=record)

        tree.pack()

        mydb.close()

    def insert_room(self):
        room_window = Toplevel(self.root)
        room_window.geometry("400x300")
        room_window.title("Insert Room")

        ide = Label(
            room_window,
            text="INSERT A ROOM",
            bg="#041d78",
            fg="#83e6e6",
            font=("bold", 20),
        )
        ide.place(x=100, y=20)

        room_id_label = Label(room_window, text="Enter Room ID:", font=("bold", 12))
        room_id_label.place(x=50, y=80)

        self.room_id_entry = Entry(room_window, show=None, font=("Arial", 14))
        self.room_id_entry.place(x=200, y=80)

        room_type_label = Label(room_window, text="Enter Room Type:", font=("bold", 12))
        room_type_label.place(x=50, y=120)

        self.room_type_entry = Entry(room_window, show=None, font=("Arial", 14))
        self.room_type_entry.place(x=200, y=120)

        capacity_label = Label(room_window, text="Enter Capacity:", font=("bold", 12))
        capacity_label.place(x=50, y=160)

        self.capacity_entry = Entry(room_window, show=None, font=("Arial", 14))
        self.capacity_entry.place(x=200, y=160)

        insert_room_button = Button(
            room_window,
            text="INSERT",
            font=("italic", 15),
            bg="#05f6fa",
            fg="blue",
            command=self.insert_room_submit,
        )
        insert_room_button.place(x=150, y=220)

    def insert_room_submit(self):
        room_id = self.room_id_entry.get()
        room_type = self.room_type_entry.get()
        capacity = self.capacity_entry.get()

        if room_id == "" or room_type == "" or capacity == "":
            MessageBox.showerror("Insert Status", "All Fields are required")
        else:
            mydb = connection.MySQLConnection(
                host=os.environ["HOST"],
                port=3306,
                user=os.environ["USER"],
                password=os.environ["PASSWORD"],
                database=os.environ["DATABASE"],
            )
            mycursor = mydb.cursor()

            # Check if the Room ID already exists
            check_sql = "SELECT * FROM Room WHERE Room_Id = %s"
            mycursor.execute(check_sql, (room_id,))
            result = mycursor.fetchone()

            if result:
                MessageBox.showerror("Insert Status", "Room ID already exists")
            else:
                # Insert room record
                insert_sql = (
                    "INSERT INTO Room (Room_Id, Type, Capacity) VALUES (%s, %s, %s)"
                )
                val = (room_id, room_type, capacity)
                mycursor.execute(insert_sql, val)

                mydb.commit()
                MessageBox.showinfo("Insert Status", "Inserted Successfully")

            mydb.close()

    def room_details(self):
        room_details_window = Toplevel(self.root)
        room_details_window.geometry("600x400")
        room_details_window.title("Room Details")

        ide = Label(
            room_details_window,
            text="ROOM DETAILS",
            bg="#041d78",
            fg="#83e6e6",
            font=("bold", 20),
        )
        ide.place(x=180, y=20)

        mydb = connection.MySQLConnection(
            host=os.environ["HOST"],
            port=3306,
            user=os.environ["USER"],
            password=os.environ["PASSWORD"],
            database=os.environ["DATABASE"],
        )
        mycursor = mydb.cursor()

        # Retrieve all room records
        select_sql = "SELECT * FROM Room"
        mycursor.execute(select_sql)
        records = mycursor.fetchall()

        tree = ttk.Treeview(room_details_window)
        tree["columns"] = ("Room ID", "Type", "Capacity", "Student ID", "Booking ID")
        tree.column("#0", width=0, stretch=NO)
        tree.column("Room ID", anchor=W, width=80)
        tree.column("Type", anchor=W, width=120)
        tree.column("Capacity", anchor=W, width=80)
        tree.column("Student ID", anchor=W, width=80)
        tree.column("Booking ID", anchor=W, width=80)

        tree.heading("#0", text="", anchor=W)
        tree.heading("Room ID", text="Room ID", anchor=W)
        tree.heading("Type", text="Type", anchor=W)
        tree.heading("Capacity", text="Capacity", anchor=W)
        tree.heading("Student ID", text="Student ID", anchor=W)
        tree.heading("Booking ID", text="Booking ID", anchor=W)

        for record in records:
            tree.insert("", "end", values=record)

        tree.pack()

        mydb.close()

    def logout(self):
        MessageBox.showinfo("Logout", "You have been logged out.")
        self.but1["state"] = "normal"  # Enable HOSTEL LOGIN button after logout
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    app = HostelManagementApp(root)
    root.mainloop()
