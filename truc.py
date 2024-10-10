print('coucou')

# foreach & list
name = ['Pierre', 'Raph', "Kaya", "Mey"]
for x in name:
    print(x)

for y in range(10):
    print(y)

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")

import math

try:
    n = int(input('Entrez un nombre : '))
    print(math.sqrt(n))
except:
    print("Entrez un nombre valide !")
finally:
    print("A plus tard !")

