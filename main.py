import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",  # change to your MySQL username
    password="password",  # change to your MySQL password
    database="Employee"
)

cursor = conn.cursor()


def add_employee(name, position, salary, hire_date):
    sql = "INSERT INTO employees (name, position, salary, hire_date) VALUES (%s, %s, %s, %s)"
    val = (name, position, salary, hire_date)
    cursor.execute(sql, val)
    conn.commit()
    print("Employee added successfully!")


def view_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def update_salary(emp_id, new_salary):
    sql = "UPDATE employees SET salary = %s WHERE emp_id = %s"
    val = (new_salary, emp_id)
    cursor.execute(sql, val)
    conn.commit()
    print("Salary updated successfully!")


def delete_employee(emp_id):
    sql = "DELETE FROM employees WHERE emp_id = %s"
    cursor.execute(sql, (emp_id,))
    conn.commit()
    print("Employee deleted successfully!")


# ---- Menu ----
while True:
    print("\n--- Employee Payroll System ---")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Salary")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        position = input("Enter position: ")
        salary = float(input("Enter salary: "))
        hire_date = input("Enter hire date (YYYY-MM-DD): ")
        add_employee(name, position, salary, hire_date)

    elif choice == "2":
        view_employees()

    elif choice == "3":
        emp_id = int(input("Enter employee ID: "))
        new_salary = float(input("Enter new salary: "))
        update_salary(emp_id, new_salary)

    elif choice == "4":
        emp_id = int(input("Enter employee ID to delete: "))
        delete_employee(emp_id)

    elif choice == "5":
        break

    else:
        print("Invalid choice. Try again.")

cursor.close()
conn.close()
