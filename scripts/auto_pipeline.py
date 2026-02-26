import time
import os

from etl.extract import extract
from etl.transform import transform
from etl.load import load

from utils.check_lock_file import wait_for_file_ready
from utils.rename_result_file import rename_file_to_processed

RAW_DATA_DIR = "/app/data/raw"


def is_processed_file(filename: str) -> bool:
    return filename.endswith("_processed.csv")


def scan_and_process_folder(app):
    try:
        files = os.scandir(RAW_DATA_DIR)

        for entry in files:

            if not entry.is_file():
                continue

            filename = entry.name

            if not filename.endswith(".csv"):
                continue

            if is_processed_file(filename):
                continue

            file_path = entry.path

            print(f"Found file: {file_path}")

            if not wait_for_file_ready(file_path):
                continue

            try:
                with app.app_context():
                    for chunk in extract(file_path):
                        chunk = transform(chunk)
                        load(chunk)

                rename_file_to_processed(original_path=file_path)

                print(f"Pipeline executed successfully: {file_path}")

            except Exception as e:
                print(f"Pipeline error {file_path}: {e}")

    except Exception as e:
        print("Watcher scan error:", e)


def start_watcher(app):
    os.makedirs(RAW_DATA_DIR, exist_ok=True)

    print("Auto pipeline watcher started")

    while True:
        scan_and_process_folder(app)
        time.sleep(15)
