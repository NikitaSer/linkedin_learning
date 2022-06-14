import stack

str = "gninraeL nIdekniL htiw tol a nraeL"
reversed_str = ""
s = stack.Stack()

s.items = list(str)

while not s.is_empty():
    reversed_str += s.pop()

print(reversed_str)
