import importlib

import aula090_m

print(aula090_m.variavel)

for i in range(10):
    importlib.reload(aula090_m)
    print(i)

print('Fim')