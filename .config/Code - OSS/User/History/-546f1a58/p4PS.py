

def time_converter(time_str: str) -> int:
    h, m, s = map(int, time_str.split(":"))
    return h * 3600 + m * 60 + s


if __name__ == "__main__":
    assert time_converter("01:00:00") == 3600
    assert time_converter("04:45:23") == 17123