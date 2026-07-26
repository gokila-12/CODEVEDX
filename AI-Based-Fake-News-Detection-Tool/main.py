import os
from colorama import init, Fore, Style
from tabulate import tabulate

import data_manager
import ml_model

init(autoreset=True)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_banner():
    print(Fore.BLUE + Style.BRIGHT + "=" * 55)
    print(Fore.BLUE + Style.BRIGHT + "     📰 AI BASED FAKE NEWS DETECTION TOOL 📰")
    print(Fore.BLUE + Style.BRIGHT + "=" * 55)


def show_menu():
    print(Fore.YELLOW + "\n1. ➕ Add news record ")
    print(Fore.YELLOW + "2. 📋 View training data")
    print(Fore.YELLOW + "3. 📦 Load sample dataset")
    print(Fore.YELLOW + "4. 🔮 Check news")
    print(Fore.YELLOW + "5. 🚪 Exit")


def view_news_data():
   
    df = data_manager.read_data()
    if df.empty:
        print(Fore.YELLOW + "No records found.")
        return

    display_df = df.copy()
    display_df["Text"] = display_df["Text"].str.slice(0, 50) + "..."
    print(Fore.MAGENTA + "\n📋 News Training Data")
    print(Fore.WHITE + tabulate(display_df, headers="keys", tablefmt="fancy_grid", showindex=False))
    print()


def main():
    data_manager.create_file()
    clear_screen()
    show_banner()

    while True:
        show_menu()
        try:
            choice = input(Fore.CYAN + "\nEnter your choice (1-5): ").strip()

            if choice == "1":
                data_manager.add_news_record()
            elif choice == "2":
                view_news_data()
            elif choice == "3":
                data_manager.load_sample_dataset()
            elif choice == "4":
                ml_model.predict_news()
            elif choice == "5":
                print(Fore.GREEN + "\n👋 Exiting program. Goodbye!")
                break
            else:
                print(Fore.RED + "❌ Invalid choice. Please enter a number between 1 and 5.")

        except KeyboardInterrupt:
            print(Fore.GREEN + "\n👋 Exiting.")
            break
        except Exception as e:
            print(Fore.RED + f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
