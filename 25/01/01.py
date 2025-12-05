import sys

lines = list(map(lambda x: x.replace('\n',''), sys.stdin.readlines()))


class Part1:
    def __init__(self):
        self.dial = 50
        self.count_zero = 0

    def do(self, rot):
        dir, deg = rot[0], int(rot[1:])
        if self.dial == 0:
            self.count_zero += 1
        assert deg in range(0,1001)
        if dir == 'R':
            self.dial = (self.dial + deg) % 100
        elif dir == 'L':
            self.dial = (self.dial - deg) % 100
        else:
            assert False

    def ans(self):
        for l in lines:
            self.do(l)
        print(self.count_zero)

p1 = Part1()
p1.ans()

class Part2:
    def __init__(self):
        self.dial = 50
        self.count_zero = 0

    def do(self, rot):
        dir, deg = rot[0], int(rot[1:])
        assert deg in range(0,1001)
        if dir == 'R':
            while deg > 0:
                self.dial = (self.dial + 1) % 100
                if self.dial == 0:
                    self.count_zero += 1
                deg -= 1
        elif dir == 'L':
            while deg > 0:
                self.dial = (self.dial - 1) % 100
                if self.dial == 0:
                    self.count_zero += 1
                deg -= 1
        else:
            assert False

    def ans(self):
        for l in lines:
            self.do(l)
        print(self.count_zero)

p2 = Part2()
p2.ans()
