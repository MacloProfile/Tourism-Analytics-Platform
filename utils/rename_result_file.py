from datetime import datetime
import os


def rename_file_to_processed(original_path):
    directory = os.path.dirname(original_path)
    filename = os.path.basename(original_path)

    name, ext = os.path.splitext(filename)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    new_filename = f"{timestamp}_{name}_processed{ext}"
    new_path = os.path.join(directory, new_filename)

    os.rename(original_path, new_path)
