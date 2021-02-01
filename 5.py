class A:
    def __init__(self, val):
        self.a = val
    def a(self):
        return self.a
    def __call__(self):
        return 'called'*3

my_a = A(12)
print(my_a.a)
val = my_a()
print(val)
