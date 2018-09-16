class Sentinel:
    """A sentinel which is always bigger than anything"""

    def __lt__(self, other):
        return False

    def __le__(self, other):
        return False

    def __gt__(self, other):
        return True

    def __ge__(self, other):
        return True


if __name__ == '__main__':
    s = Sentinel()
    print(5 >= s)
    print(s >= 56)
