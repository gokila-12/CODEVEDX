import csv
import os
import pandas as pd
from colorama import Fore

FILE_NAME = "student_data.csv"
HEADERS = ["StudentID", "Attendance", "Marks", "StudyHours", "FinalPerformance"]


def create_file():
    """Create the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, mode="w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(HEADERS)
        except Exception as e:
            print(Fore.RED + f"Error creating file: {e}")


def read_data():
    """Read all student records into a pandas DataFrame."""
    try:
        create_file()
        return pd.read_csv(FILE_NAME)
    except Exception as e:
        print(Fore.RED + f"Error reading file: {e}")
        return pd.DataFrame(columns=HEADERS)


def save_data(df):
    """Save the DataFrame back to the CSV file."""
    try:
        df.to_csv(FILE_NAME, index=False)
    except Exception as e:
        print(Fore.RED + f"Error saving file: {e}")


def add_student_record():
    """Prompt user for a new student record and save it."""
    try:
        student_id = int(input(Fore.CYAN + "Enter Student ID: ").strip())
        attendance = float(input(Fore.CYAN + "Enter Attendance (%): ").strip())
        marks = float(input(Fore.CYAN + "Enter Marks (out of 100): ").strip())
        study_hours = float(input(Fore.CYAN + "Enter Study Hours (per day): ").strip())
        final_performance = float(input(Fore.CYAN + "Enter Final Performance (score/%): ").strip())

        if not (0 <= attendance <= 100) or not (0 <= marks <= 100) or study_hours < 0:
            print(Fore.RED + "❌ Please enter realistic values (0-100 range where applicable).")
            return

        df = read_data()
        new_row = pd.DataFrame([[student_id, attendance, marks, study_hours, final_performance]],
                                columns=HEADERS)
        df = pd.concat([df, new_row], ignore_index=True)
        save_data(df)
        print(Fore.GREEN + "✅ Student record added successfully.")

    except ValueError:
        print(Fore.RED + "❌ Invalid input. Please enter numeric values.")
    except Exception as e:
        print(Fore.RED + f"Unexpected error: {e}")


def update_student_record():
    """Update an existing student record by Student ID."""
    df = read_data()
    if df.empty:
        print(Fore.YELLOW + "No records available to update.")
        return

    try:
        student_id = int(input(Fore.CYAN + "Enter Student ID to update: ").strip())
        mask = df["StudentID"] == student_id

        if not mask.any():
            print(Fore.YELLOW + "⚠️ Student ID not found.")
            return

        attendance = float(input(Fore.CYAN + "Enter new Attendance (%): ").strip())
        marks = float(input(Fore.CYAN + "Enter new Marks: ").strip())
        study_hours = float(input(Fore.CYAN + "Enter new Study Hours: ").strip())
        final_performance = float(input(Fore.CYAN + "Enter new Final Performance: ").strip())

        df.loc[mask, "Attendance"] = attendance
        df.loc[mask, "Marks"] = marks
        df.loc[mask, "StudyHours"] = study_hours
        df.loc[mask, "FinalPerformance"] = final_performance

        save_data(df)
        print(Fore.GREEN + "✅ Record updated successfully.")

    except ValueError:
        print(Fore.RED + "❌ Invalid input. Please enter numeric values.")
    except Exception as e:
        print(Fore.RED + f"Unexpected error: {e}")
