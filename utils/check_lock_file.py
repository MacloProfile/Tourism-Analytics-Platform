import time
import os


def wait_for_file_ready(path, timeout=30):
    start_time = time.time()
    last_size = -1

    while True:
        if time.time() - start_time > timeout:
            return False

        try:
            current_size = os.path.getsize(path)

            if current_size == last_size:
                return True

            last_size = current_size
            time.sleep(1)

        except PermissionError:
            time.sleep(1)
