from utils import time_converter


if __name__ == "__main__":
    time_str = input('Entrez le temps à convertir en seconds (Ex: 12:04:52 ou 05:30): ')
    print(f"{time_str} -> {time_converter(time_str)} seconds")