import streamlit as st
import mysql.connector
import pandas as pd
import datetime

st.set_page_config(page_title="Employee Management System")

st.title("Employee Management System")
login = False
choice = st.sidebar.selectbox("My Menu", ("Home", "Admin", "Employee", "View Policies"))
st.write(choice)

if(choice == "Home"):
    st.image("https://png.pngtree.com/png-clipart/20230824/original/pngtree-quarantine-office-people-employee-manager-picture-image_8420225.png")
    st.markdown("<center> <h1>WELCOME</h1> </center>", unsafe_allow_html=True)
    st.write("This is a web application developed by Shubham as a part of Training project")

elif(choice == "Employee"):
    if 'login' not in st.session_state:
        st.session_state['login'] = False

    uid = st.text_input("Enter Employee ID")
    upwd = st.text_input("Enter Password", type="password", key="emp_pwd")
    btn = st.button("Login")

    if btn:
        mydb = mysql.connector.connect(host="localhost", user="root", password="S1@shubhamsoniji", database="employee_db")
        c = mydb.cursor()
        c.execute("select * from employees")
        for r in c:
            if(r[0] == uid and r[3] == upwd):
                st.session_state['login'] = True
                break

        if(not st.session_state['login']):
            st.error("Incorrect ID Or Password")

    if(st.session_state['login']):
        st.success("Login Successful")
        choice2 = st.selectbox("Features", ("None", "View Departments", "Apply Leave", "View Salary"))

        if(choice2 == "View Departments"):
            mydb = mysql.connector.connect(host="localhost", user="root", password="S1@shubhamsoniji", database="employee_db")
            df = pd.read_sql("select * from departments", mydb)
            st.dataframe(df)

        elif(choice2 == "Apply Leave"):
            from_date = st.date_input("From Date")
            to_date = st.date_input("To Date")
            reason = st.text_input("Reason")
            btn2 = st.button("Apply")
            if btn2:
                lid = str(datetime.datetime.now())
                mydb = mysql.connector.connect(host="localhost", user="root", password="S1@shubhamsoniji", database="employee_db")
                c = mydb.cursor()
                c.execute("Insert into leaves values(%s,%s,%s,%s,%s,%s)", (lid, uid, from_date, to_date, reason, "Pending"))
                mydb.commit()
                st.success("Leave Applied Successfully")

        elif(choice2 == "View Salary"):
            mydb = mysql.connector.connect(host="localhost", user="root", password="S1@shubhamsoniji", database="employee_db")
            df = pd.read_sql(f"select * from salaries where emp_id = '{uid}'", mydb)
            st.dataframe(df)

elif(choice == "Admin"):
    if 'alogin' not in st.session_state:
        st.session_state['alogin'] = False

    aid = st.text_input("Enter Admin ID")
    apwd = st.text_input("Enter Password", type="password", key="admin_pwd")
    btn = st.button("Login")

    if btn:
        mydb = mysql.connector.connect(host="localhost", user="root", password="S1@shubhamsoniji", database="employee_db")
        c = mydb.cursor()
        c.execute("select * from managers")
        for r in c:
            if(r[0] == aid and r[1] == apwd):
                st.session_state['alogin'] = True
                break

        if(not st.session_state['alogin']):
            st.error("Incorrect ID Or Password")

    if(st.session_state['alogin']):
        st.success("Login Successful")
        choice2 = st.selectbox("Features", ("None", "View Attendance", "Add Employee", "Delete Employee", "Add Manager Account"))

        if(choice2 == "View Attendance"):
            mydb = mysql.connector.connect(host="localhost", user="root", password="S1@shubhamsoniji", database="employee_db")
            df = pd.read_sql("select * from attendance", mydb)
            st.dataframe(df)

        elif(choice2 == "Add Employee"):
            eid = st.text_input("Enter Employee ID", key="add_emp_id")
            ename = st.text_input("Enter Employee Name", key="add_emp_name")
            erole = st.text_input("Enter Role", key="add_emp_role")
            epwd = st.text_input("Enter Password", type="password", key="add_emp_pwd")
            btn2 = st.button("Add Employee")
            if btn2:
                mydb = mysql.connector.connect(host="localhost", user="root", password="S1@shubhamsoniji", database="employee_db")
                c = mydb.cursor()
                c.execute("Insert into employees values(%s,%s,%s,%s)", (eid, ename, erole, epwd))
                mydb.commit()
                st.success("Employee Added Successfully")

        elif(choice2 == "Delete Employee"):
            emp_id = st.text_input("Enter Employee ID", key="del_emp_id")
            btn2 = st.button("Delete Employee")
            if btn2:
                mydb = mysql.connector.connect(host="localhost", user="root", password="S1@shubhamsoniji", database="employee_db")
                c = mydb.cursor()
                c.execute("delete from employees where emp_id = %s", (emp_id,))
                mydb.commit()
                st.success("Employee Deleted Successfully")

        elif(choice2 == "Add Manager Account"):
            mid = st.text_input("Enter Manager ID", key="add_mgr_id")
            mpwd = st.text_input("Enter Password", type="password", key="add_mgr_pwd")
            btn2 = st.button("Add Manager")
            if btn2:
                mydb = mysql.connector.connect(host="localhost", user="root", password="S1@shubhamsoniji", database="employee_db")
                c = mydb.cursor()
                c.execute("Insert into managers values(%s,%s)", (mid, mpwd))
                mydb.commit()
                st.success("Manager Account Added Successfully")

elif(choice == "View Policies"):
    choice3 = st.selectbox("Choose Policy Document", ("None", "Employee Code of Conduct", "Leave & Salary Policy"))
    if choice3 == "Employee Code of Conduct":
        st.markdown("<iframe src='https://connecteam.com/wp-content/uploads/2019/05/Code-of-Conduct-Example-Template.pdf' width='100%' height='500px'></iframe>", unsafe_allow_html=True)
    elif choice3 == "Leave & Salary Policy":
        st.markdown("<iframe src='https://files.serc.co/documents/bod/24/20240912_Disability%20Leave%20and%20Salary%20Continuation%20Policy_Aug24DRAFT.pdf' width='100%' height='500px'></iframe>", unsafe_allow_html=True)