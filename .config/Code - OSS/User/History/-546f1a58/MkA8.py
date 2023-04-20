from utils import time_converter


if __name__ == "__main__":
    if len(argv) != 2:
        exit(f"Usage: {argv[1]} time_str")
    print(f"{argv[1]} -> {time_converter(argv[1])} seconds")