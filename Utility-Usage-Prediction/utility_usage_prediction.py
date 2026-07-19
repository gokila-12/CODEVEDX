import csv
import os
import time
import numpy as np
from colorama import init, Fore, Style
from tabulate import tabulate

init(autoreset=True)  
FILENAME = "usage_data.csv"
HEADERS = ["Utility_Type", "Month", "Usage"]
VALID_TYPES = ["Electricity", "Water", "Gas"]

def initialize_file():
    """Create the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILENAME):
        try:
            with open(FILENAME, mode="w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(HEADERS)
        except Exception as e:
            print(Fore.RED + f"Error creating file: {e}")


def read_data():
    """Read all records from the CSV file. Returns a list of [utility_type, month, usage]."""
    data = []
    try:
        with open(FILENAME, mode="r", newline="") as f:
            reader = csv.reader(f)
            next(reader, None)  # skip header
            for row in reader:
                if row:
                    data.append(row)
    except FileNotFoundError:
        print(Fore.YELLOW + "No data file found. It will be created when you add data.")
    except Exception as e:
        print(Fore.RED + f"Error reading file: {e}")
    return data


def write_all_data(data):
    """Overwrite the CSV file with the given data (used for updates)."""
    try:
        with open(FILENAME, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)
            writer.writerows(data)
    except Exception as e:
        print(Fore.RED + f"Error writing file: {e}")


def append_data(utility_type, month, usage):
    """Append a single new record to the CSV file."""
    try:
        with open(FILENAME, mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([utility_type, month, usage])
        print(Fore.GREEN + "✅ Record added successfully.")
    except Exception as e:
        print(Fore.RED + f"Error adding record: {e}")


def choose_utility_type():
    """Prompt user to select a utility type from a fixed list."""
    print(Fore.MAGENTA + "\nSelect Utility Type:")
    icons = {"Electricity": "⚡", "Water": "💧", "Gas": "🔥"}
    for i, u in enumerate(VALID_TYPES, start=1):
        print(Fore.CYAN + f"{i}. {icons.get(u, '')} {u}")

    try:
        choice = int(input(Fore.CYAN + "Enter choice (1-3): ").strip())
        if 1 <= choice <= len(VALID_TYPES):
            return VALID_TYPES[choice - 1]
        else:
            print(Fore.RED + "❌ Invalid choice.")
            return None
    except ValueError:
        print(Fore.RED + "❌ Invalid input. Please enter a number.")
        return None


def unit_for(utility_type):
    """Return the display unit for a given utility type."""
    units = {"Electricity": "kWh", "Water": "Liters", "Gas": "m3"}
    return units.get(utility_type, "units")


def add_usage_data():
    """Prompt user for a new usage record and save it."""
    try:
        utility_type = choose_utility_type()
        if utility_type is None:
            return

        month = input(Fore.CYAN + "Enter month (e.g., Jan-2025): ").strip()
        usage = float(input(Fore.CYAN + f"Enter usage in {unit_for(utility_type)}: ").strip())

        if usage < 0:
            print(Fore.RED + "Usage cannot be negative.")
            return

        append_data(utility_type, month, usage)

    except ValueError:
        print(Fore.RED + "❌ Invalid input. Usage must be a number.")
    except Exception as e:
        print(Fore.RED + f"Unexpected error: {e}")


def view_usage_data():
    """Display all stored records, filtered by utility type, in a clean table."""
    data = read_data()
    if not data:
        print(Fore.YELLOW + "No records found.")
        return

    utility_type = choose_utility_type()
    if utility_type is None:
        return

    filtered = [[row[1], row[2]] for row in data if row[0] == utility_type]

    if not filtered:
        print(Fore.YELLOW + f"No records found for {utility_type}.")
        return

    print(Fore.MAGENTA + f"\n📊 {utility_type} Usage ({unit_for(utility_type)})")
    print(Fore.WHITE + tabulate(filtered, headers=["Month", "Usage"], tablefmt="fancy_grid"))
    print()


def update_usage_data():
    """Update an existing record by utility type and month."""
    data = read_data()
    if not data:
        print(Fore.YELLOW + "No records available to update.")
        return

    try:
        utility_type = choose_utility_type()
        if utility_type is None:
            return

        month = input(Fore.CYAN + "Enter the month to update: ").strip()
        found = False

        for row in data:
            if row[0] == utility_type and row[1].lower() == month.lower():
                new_usage = float(input(Fore.CYAN + f"Enter new usage ({unit_for(utility_type)}): ").strip())
                if new_usage < 0:
                    print(Fore.RED + "Usage cannot be negative.")
                    return
                row[2] = new_usage
                found = True
                break

        if found:
            write_all_data(data)
            print(Fore.GREEN + "✅ Record updated successfully.")
        else:
            print(Fore.YELLOW + "⚠️ No matching record found for that utility type and month.")

    except ValueError:
        print(Fore.RED + "❌ Invalid input. Usage must be a number.")
    except Exception as e:
        print(Fore.RED + f"Unexpected error: {e}")


def predict_usage():
    """Simple ML model: Linear Regression to predict next month's usage for a chosen utility."""
    data = read_data()

    utility_type = choose_utility_type()
    if utility_type is None:
        return

    filtered = [row for row in data if row[0] == utility_type]

    if len(filtered) < 2:
        print(Fore.YELLOW + f"⚠️ Not enough {utility_type} data to predict. Add at least 2 records.")
        return

    try:
        x = np.array(range(len(filtered)))
        y = np.array([float(row[2]) for row in filtered])

        print(Fore.CYAN + "🤖 Training model...", end="\r")
        time.sleep(0.6)  

        m, c = np.polyfit(x, y, 1)

        next_index = len(filtered)
        predicted_usage = m * next_index + c

        print(Fore.GREEN + f"🔮 Predicted {utility_type} usage for next month: "
              f"{predicted_usage:.2f} {unit_for(utility_type)}          ")
        print(Fore.WHITE + f"(Model: usage = {m:.3f} * month_index + {c:.3f})\n")

    except ValueError:
        print(Fore.RED + "Data contains invalid numbers. Please check your records.")
    except Exception as e:
        print(Fore.RED + f"Error during prediction: {e}")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_banner():
    print(Fore.BLUE + Style.BRIGHT + "=" * 50)
    print(Fore.BLUE + Style.BRIGHT + "     ⚡ UTILITY USAGE PREDICTION TOOL 💧🔥")
    print(Fore.BLUE + Style.BRIGHT + "=" * 50)


def show_menu():
    print(Fore.YELLOW + "\n1. ➕ Add usage data")
    print(Fore.YELLOW + "2. 📋 View usage data")
    print(Fore.YELLOW + "3. ✏️  Update usage data")
    print(Fore.YELLOW + "4. 🔮 Predict next month's usage (ML)")
    print(Fore.YELLOW + "5. 🚪 Exit")


def main():
    initialize_file()
    clear_screen()
    show_banner()

    while True:
        show_menu()
        try:
            choice = input(Fore.CYAN + "\nEnter your choice (1-5): ").strip()

            if choice == "1":
                add_usage_data()
            elif choice == "2":
                view_usage_data()
            elif choice == "3":
                update_usage_data()
            elif choice == "4":
                predict_usage()
            elif choice == "5":
                print(Fore.GREEN + "\n👋 Exiting. Goodbye!")
                break
            else:
                print(Fore.RED + "❌ Invalid choice. Please enter a number between 1 and 5.")

        except KeyboardInterrupt:
            print(Fore.GREEN + "\n👋 Program interrupted by user. Exiting.")
            break
        except Exception as e:
            print(Fore.RED + f"Unexpected error: {e}")


if __name__ == "__main__":
    main()