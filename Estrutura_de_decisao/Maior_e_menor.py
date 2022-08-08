print('#'*20)
n1 = int(input('Numero 1 : '))
print('#'*20)
n2 = int(input('Numero 2: '))
print('#'*20)
n3 = int(input('Numero 3: '))
print('#'*20)

def maior():
    if n1 > n2 and n1 > n3:
        print('Maior numero: {}'.format(n1))
    elif n2 > n1 and n2 > n3:
        print('Maior numero: {}'.format(n2))
    elif n3 > n1 and n3 > n2:
        print('Maior numero: {}'.format(n3))
maior()
print('#'*20)
def menor():
    if n1 < n2 and n1 < n3:
        print('Menor numero: {}'.format(n1))
    elif n2 < n1 and n2 < n3:
        print('Menor numero: {}'.format(n2))
    elif n3 < n1 and n3 < n2:
        print('Menor numero: {}'.format(n3))
menor()
print('#'*20)