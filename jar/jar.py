class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.amount = 0

    def __str__(self):
        return f"{self.amount * '🍪'}"

    def deposit(self, n):
        if self.amount + n > self.capacity:
            raise ValueError
        else:
            self.amount += n

    def withdraw(self, n):
        if self.amount - n < 0:
            raise ValueError
        else:
            self.amount -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, cookies):
        if isinstance(cookies, int) and cookies > 0:
            self._capacity = cookies
        else:
            raise ValueError

    @property
    def size(self):
        return self.amount


def main():
    ...


if __name__ == "__main__":
    main()
