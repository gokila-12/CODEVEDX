import csv
import os
import pandas as pd
from colorama import Fore

DATA_FILE = "news_data.csv"
HEADERS = ["Text", "Label"]  


def create_file():
    
    if not os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(HEADERS)
        except Exception as e:
            print(Fore.RED + f"Error creating file: {e}")


def read_data():
    
    try:
        create_file()
        return pd.read_csv(DATA_FILE)
    except Exception as e:
        print(Fore.RED + f"Error reading file: {e}")
        return pd.DataFrame(columns=HEADERS)


def save_data(df):
    
    try:
        df.to_csv(DATA_FILE, index=False)
    except Exception as e:
        print(Fore.RED + f"Error saving file: {e}")


def add_news_record():
    
    try:
        text = input(Fore.CYAN + "Enter news text: ").strip()
        if not text:
            print(Fore.RED + "❌ News text cannot be empty.")
            return

        label = input(Fore.CYAN + "Enter label (Real/Fake): ").strip().capitalize()
        if label not in ("Real", "Fake"):
            print(Fore.RED + "❌ Label must be 'Real' or 'Fake'.")
            return

        df = read_data()
        new_row = pd.DataFrame([[text, label]], columns=HEADERS)
        df = pd.concat([df, new_row], ignore_index=True)
        save_data(df)
        print(Fore.GREEN + "✅ News record added successfully.")

    except Exception as e:
        print(Fore.RED + f"Unexpected error: {e}")


def load_sample_dataset():
    
    samples = [
        ("Scientists confirm water discovered on Mars surface", "Real"),
        ("Local government announces new tax reforms for 2026", "Real"),
        ("Celebrity secretly an alien, government covers it up", "Fake"),
        ("Miracle pill cures all diseases overnight, doctors hate this", "Fake"),
        ("Central bank raises interest rates to control inflation", "Real"),
        ("Aliens land in city park, mayor shakes hands with them", "Fake"),
        ("New study links regular exercise to improved heart health", "Real"),
        ("Man claims he traveled through time using microwave oven", "Fake"),
        ("Stock markets close higher after strong earnings reports", "Real"),
        ("Drinking bleach cures common cold, viral post claims", "Fake"),
        ("University researchers develop more efficient solar panel", "Real"),
        ("Moon landing was staged in a movie studio, leaked memo says", "Fake"),
    ]

    try:
        df = read_data()
        new_rows = pd.DataFrame(samples, columns=HEADERS)
        df = pd.concat([df, new_rows], ignore_index=True)
        save_data(df)
        print(Fore.GREEN + f"✅ Loaded {len(samples)} sample records for training.")
    except Exception as e:
        print(Fore.RED + f"Error loading sample dataset: {e}")
