import matplotlib.pyplot as plt
from colorama import Fore

from data_manager import read_data


def visualize_data():
    """Show scatter charts: Attendance/Marks/StudyHours vs Final Performance."""
    df = read_data()

    if df.empty:
        print(Fore.YELLOW + "No data available to visualize.")
        return

    try:
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))

        axes[0].scatter(df["Attendance"], df["FinalPerformance"], color="royalblue")
        axes[0].set_xlabel("Attendance (%)")
        axes[0].set_ylabel("Final Performance")
        axes[0].set_title("Attendance vs Performance")

        axes[1].scatter(df["Marks"], df["FinalPerformance"], color="seagreen")
        axes[1].set_xlabel("Marks")
        axes[1].set_ylabel("Final Performance")
        axes[1].set_title("Marks vs Performance")

        axes[2].scatter(df["StudyHours"], df["FinalPerformance"], color="darkorange")
        axes[2].set_xlabel("Study Hours")
        axes[2].set_ylabel("Final Performance")
        axes[2].set_title("Study Hours vs Performance")

        plt.tight_layout()
        plt.show()

        print(Fore.GREEN + "✅ Chart displayed.")

    except Exception as e:
        print(Fore.RED + f"Error generating chart: {e}")
