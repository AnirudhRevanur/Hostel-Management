import streamlit as st
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


def main():
    st.title("Hostel Database")

    option = st.sidebar.selectbox("Select Option", ["Hostel Login", "Student Login"])

    if option == "Hostel Login":
        hostel_login()
    elif option == "Student Login":
        student_login()


def hostel_login():
    st.subheader("Hostel Login Page")

    name = st.text_input("User Name")
    password = st.text_input("Password", type="password", key="password")

    if st.button("Submit"):
        authenticate_hostel(name, password)


def authenticate_hostel(name, password):
    try:
        mydb = mysql.connector.connect(
            host=os.environ["HOST"],
            user=os.environ["USER"],
            password=os.environ["PASSWORD"],
            database=os.environ["DATABASE"],
        )
        cursor = mydb.cursor()

        sql = "SELECT * FROM hostellogin WHERE name = %s AND password = %s"
        val = (name, password)
        cursor.execute(sql, val)
        result = cursor.fetchone()

        if result:
            st.success("Login successful")
            option()
        else:
            st.error("Invalid username or password")

    except Exception as e:
        st.error(f"Error: {e}")
    finally:
        cursor.close()
        mydb.close()


def student_login():
    st.subheader("Student Login Page")

    student_id = st.text_input("Enter Your Student ID")
    student_name = st.text_input("Enter Your Name")
    place = st.text_input("Enter Place")
    sem = st.text_input("Enter Sem")

    if st.button("Submit"):
        authenticate_student(
            student_id,
            student_name,
            place,
            sem,
        )


def authenticate_student(student_id, student_name, place, sem):
    try:
        mydb = mysql.connector.connect(
            host=os.environ["HOST"],
            user=os.environ["USER"],
            password=os.environ["PASSWORD"],
            database=os.environ["DATABASE"],
        )
        cursor = mydb.cursor()

        sql = "INSERT INTO student_login (student_id, sname, place, sem,) VALUES (%s, %s, %s, %s,)"
        val = (student_id, student_name, place, sem)
        cursor.execute(sql, val)
        mydb.commit()

        st.success("Login successful")

    except Exception as e:
        st.error(f"Error: {e}")
    finally:
        cursor.close()
        mydb.close()


def option():
    st.subheader("Hostel Options")

    selected_option = st.selectbox(
        "Select Option",
        [
            "Select an option",
            "Insert New Student",
            "Delete Student",
            "Update Student",
            "Fee Details",
            "Student Details",
            "Add Room",
        ],
    )


    if selected_option == "Select an option":
        default_text()
    elif selected_option == "Insert New Student":
        insert_student()
    elif selected_option == "Delete Student":
        delete_student()
    elif selected_option == "Update Student":
        update_student()
    elif selected_option == "Fee Details":
        fee_details()
    elif selected_option == "Student Details":
        student_details()
    elif selected_option == "Add Room":
        add_room()


def default_text():
    st.subheader("Select an option")



def insert_student():
    st.subheader("Insert New Student")
    
    # Add Streamlit components for input (st.text_input, st.button, etc.)

    # Call the corresponding function to handle the insertion


def delete_student():
    st.subheader("Delete Student")

    # Add Streamlit components for input (st.text_input, st.button, etc.)

    # Call the corresponding function to handle the deletion


def update_student():
    st.subheader("Update Student")

    # Add Streamlit components for input (st.text_input, st.button, etc.)

    # Call the corresponding function to handle the update


def fee_details():
    st.subheader("Fee Details")

    # Add Streamlit components for input (st.text_input, st.button, etc.)

    # Call the corresponding function to handle fee details


def student_details():
    st.subheader("Student Details")

    # Add Streamlit components for input (st.text_input, st.button, etc.)

    # Call the corresponding function to display student details


def add_room():
    st.subheader("Add Room")

    # Add Streamlit components for input (st.text_input, st.button, etc.)

    # Call the corresponding function to handle adding a room


if __name__ == "__main__":
    main()
