class factorial:
    def solve(self, n):
        return n if n <= 1 else n * self.solve(n-1)


a = factorial()
b = a.solve(3)
print(b)