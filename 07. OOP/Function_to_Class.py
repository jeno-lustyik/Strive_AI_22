class StriveSchool:
    def __init__(self, n, k, list):
        self.n = n
        self.k = k
        self.list = list

    def strive(self):
        out = []
        for i in self.list:
            if i % self.n == 0 and i % self.k == 0:
                out.append('Strive School')
                continue
            if i % self.n == 0:
                out.append('Strive')
                continue
            if i % self.k == 0:
                out.append('School')
                continue
            else:
                out.append(i)
        print(out)
        return


x = StriveSchool(3, 5, [3, 5, 9, 10, 11, 15])
x.strive()
