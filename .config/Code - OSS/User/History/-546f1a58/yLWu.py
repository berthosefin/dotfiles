from sys import argv


def time_converter(time_str: str) -> int:
    if time_str.count(':') == 1:
        time_str = '00:' + time_str
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s


if __name__ == "__main__":
    if len(argv[0]) != 2:
        exit(f"Usage: {argv[1]} time_str")
    
    assert time_converter("01:00:00") == 3600
    assert time_converter("04:45:23") == 17123
    assert time_converter("01:00") == 60
    assert time_converter("05:30") == 330