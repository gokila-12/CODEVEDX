import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
from colorama import Fore

from data_manager import read_data

FEATURES = ["Attendance", "Marks", "StudyHours"]
TARGET = "FinalPerformance"


def _train_model(df):
    """Internal helper: fit a Linear Regression model on the given data."""
    X = df[FEATURES]
    y = df[TARGET]

    model = LinearRegression()
    model.fit(X, y)
    return model


def evaluate_model():
    """Auto-train on a train/test split and report accuracy metrics (R2, MAE)."""
    df = read_data()

    if len(df) < 5:
        print(Fore.YELLOW + "⚠️ Not enough data to evaluate. Add at least 5 records.")
        return

    try:
        X = df[FEATURES]
        y = df[TARGET]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        eval_model = LinearRegression()
        eval_model.fit(X_train, y_train)
        predictions = eval_model.predict(X_test)

        r2 = r2_score(y_test, predictions)
        mae = mean_absolute_error(y_test, predictions)

        print(Fore.MAGENTA + "\n📈 Model Accuracy Evaluation")
        print(Fore.WHITE + f"R² Score: {r2:.3f}")
        print(Fore.WHITE + f"Mean Absolute Error: {mae:.2f}\n")

    except Exception as e:
        print(Fore.RED + f"Error during evaluation: {e}")


def predict_performance():
    """Auto-train on all available data, then predict a new student's performance."""
    df = read_data()

    if len(df) < 5:
        print(Fore.YELLOW + "⚠️ Not enough data to predict. Add at least 5 records.")
        return

    try:
        model = _train_model(df)

        attendance = float(input(Fore.CYAN + "Enter Attendance (%): ").strip())
        marks = float(input(Fore.CYAN + "Enter Marks: ").strip())
        study_hours = float(input(Fore.CYAN + "Enter Study Hours: ").strip())

        features = pd.DataFrame([[attendance, marks, study_hours]], columns=FEATURES)
        prediction = model.predict(features)[0]

        print(Fore.GREEN + f"\n🔮 Predicted Final Performance: {prediction:.2f}\n")

    except ValueError:
        print(Fore.RED + "❌ Invalid input. Please enter numeric values.")
    except Exception as e:
        print(Fore.RED + f"Error during prediction: {e}")