import os
from colorama import init, Fore, Style

import data_manager
import ml_model
import visualize

init(autoreset=True)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_banner():
    print(Fore.BLUE + Style.BRIGHT + "=" * 55)
    print(Fore.BLUE + Style.BRIGHT + "   🎓 STUDENT PERFORMANCE PREDICTION SYSTEM 🎓")
    print(Fore.BLUE + Style.BRIGHT + "=" * 55)


def show_menu():
    print(Fore.YELLOW + "\n1. ➕ Add student record")
    print(Fore.YELLOW + "2. 📋 View records")
    print(Fore.YELLOW + "3. ✏️  Update record")
    print(Fore.YELLOW + "4. 📊 Visualize data (charts)")
    print(Fore.YELLOW + "5. 📈 Evaluate model accuracy")
    print(Fore.YELLOW + "6. 🔮 Predict final performance")
    print(Fore.YELLOW + "7. 🚪 Exit")


def view_records():
    """Display all student records in a clean table."""
    from tabulate import tabulate
    df = data_manager.read_data()
    if df.empty:
        print(Fore.YELLOW + "No records found.")
        return
    print(Fore.MAGENTA + "\n📋 Student Records")
    print(Fore.WHITE + tabulate(df, headers="keys", tablefmt="fancy_grid", showindex=False))
    print()


def main():
    data_manager.create_file()
    clear_screen()
    show_banner()

    while True:
        show_menu()
        try:
            choice = input(Fore.CYAN + "\nEnter your choice (1-7): ").strip()

            if choice == "1":
                data_manager.add_student_record()
            elif choice == "2":
                view_records()
            elif choice == "3":
                data_manager.update_student_record()
            elif choice == "4":
                visualize.visualize_data()
            elif choice == "5":
                ml_model.evaluate_model()
            elif choice == "6":
                ml_model.predict_performance()
            elif choice == "7":
                print(Fore.GREEN + "\n👋 Exiting program. Goodbye!")
                break
            else:
                print(Fore.RED + "❌ Invalid choice. Please enter a number between 1 and 7.")

        except KeyboardInterrupt:
            print(Fore.GREEN + "\n👋 Program interrupted by user. Exiting.")
            break
        except Exception as e:
            print(Fore.RED + f"Unexpected error: {e}")


if __name__ == "__main__":
    main()