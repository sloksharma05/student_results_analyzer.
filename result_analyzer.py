import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_NAME = "student_results.csv"

if not os.path.exists(FILE_NAME):
    pd.DataFrame(columns=["Roll No", "Name", "Math", "Science", "English"]).to_csv(FILE_NAME, index=False)

def add_student():
    roll = input("Enter Roll No: ")
    df = pd.read_csv(FILE_NAME, dtype={"Roll No": str})
    if roll in df["Roll No"].values:
        print("Roll No already exists.\n")
        return

    name = input("Enter Name: ")
    try:
        math = int(input("Math Marks: "))
        sci = int(input("Science Marks: "))
        eng = int(input("English Marks: "))
    except:
        print("Marks must be numbers.\n")
        return

    pd.DataFrame([[roll, name, math, sci, eng]], columns=df.columns).to_csv(FILE_NAME, mode="a", index=False, header=False)
    print("Student added.\n")

def view_all():
    print(pd.read_csv(FILE_NAME, dtype={"Roll No": str}), "\n")

def analyze_results():
    df = pd.read_csv(FILE_NAME, dtype={"Roll No": str})
    df["Total"] = df[["Math", "Science", "English"]].sum(axis=1)
    print("Topper:", df.loc[df["Total"].idxmax(), "Name"])
    print("Lowest:", df.loc[df["Total"].idxmin(), "Name"])
    print("\nAverage per subject:\n", df[["Math", "Science", "English"]].mean())

    df.plot(kind="bar", x="Name", y=["Math", "Science", "English"])
    plt.show()

def search_student():
    roll = input("Enter Roll No: ")
    df = pd.read_csv(FILE_NAME, dtype={"Roll No": str})
    s = df[df["Roll No"] == roll]
    print(s if not s.empty else "No record found.\n")

def main():
    while True:
        print("1. Add Student\n2. View All\n3. Analyze Results\n4. Search\n5. Exit")
        c = input("Choice: ")
        if c == "1": add_student()
        elif c == "2": view_all()
        elif c == "3": analyze_results()
        elif c == "4": search_student()
        elif c == "5": break
        else: print("Invalid choice.\n")

if __name__ == "__main__":
    main()
