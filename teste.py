def symmetric_difference(m:list, n:list) -> list:
    '''
    Funcional apenas para sorted list
    Complexidade atual:
    O(n+m)
    Complexidade Espacial:
    O(n+m)
    '''
    m.sort()
    n.sort()
    i, j = (0,0)
    result = []
    while i < len(m) and j < len(n):
        # Faz peneira dos elementos aqui
        if m[i] == n[j]:
            i += 1
            j += 1
            continue
        elif m[i] < n[j]:
            result.append(m[i])
            i += 1
        else: # m[i] > n[j]
            result.append(n[j])
            j += 1

    # Soma o resto das duas listas, levando em conta que uma das listas foi totalmente percorrida
    result += n[j:] + m[i:]
    return result

def definitive_symmetric_difference(m:list, n:list) -> list:
    '''
    Funcional apenas para sorted list
    Complexidade atual:
    O(n+m)
    Complexidade Espacial:
    O(n+m)
    '''
    m.sort()
    n.sort()
    result = []
    intersection = set(m).intersection(n)

    for element in set(m + n):
        if element not in intersection:
            result.append(element)
    return result


import unittest
import random

# Testes
class TestSymmetricDifference(unittest.TestCase):
    def test_symmetric_difference(self):
        for _ in range(10000):
            m_size = random.randint(1, 100)
            n_size = random.randint(1, 100)

            m = random.sample(range(1, 1000), m_size)
            n = random.sample(range(1, 1000), n_size)

            result = symmetric_difference(m, n).sort()
            expected = definitive_symmetric_difference(m, n).sort()

            self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()