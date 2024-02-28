# lecture 4
s = "abc"
it = iter(s)
next(it)
next(it)
print(next(it))

# generator
def generate_ints(N):
    for i in range(N):
        yield i # yield сохраняет значение в памяти пк
gen = generate_ints(3)
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))

# registration form: password, email
import re
p = re.compile('')
m = p.match('tempo')
print(m)


