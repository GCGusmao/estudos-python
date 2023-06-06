# Generator expression, Interables e Interators em Python.
interable = ['Eu', 'Tenho', '__iter__']
iterator = iter(interable)  # tem __iter__ e __next__

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))