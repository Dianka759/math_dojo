class MathDojo:
    def __init__(self):
        self.result = 0

#  * = splat operator, enables to provide multiple arguments
    def add(self, num, *nums):
        self.result += num
        for i in nums:
            self.result += i
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i
        return self

md = MathDojo()
x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)  # should print 5

new_instance = MathDojo().add(30).subtract(20).result
print(new_instance)

new_instance2 = MathDojo().add(1, 2, 3, 4).result
print(new_instance2)