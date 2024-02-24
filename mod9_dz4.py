def all_variants(s):
    n = len(s)
    for i in range(1, 2**n):
        subset = ''.join(s[j] for j in range(n) if (i >> j) & 1)
        yield subset

# Пример использования:
a = all_variants("abc")
for i in a:
    print(i)