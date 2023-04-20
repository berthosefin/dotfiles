import random


def call(number):
    print("Im'm calling" + str(number))
    print("bip ...")
    print("bip ...")
    print("bip ...")
    print("bip ...")
    if random.randint(0, 1) == 0:
        raise RuntimeError("Nobody answered")


def talk():
    print("Bla bla bla")


def hang_up_the_phone():
    print("*Click*")