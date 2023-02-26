result = []
def divider(a, b):
    if a < b:
        raise ValueError("a dolxno but bolxe chem b")

    if a >= 0:
        raise  ValueError ("zero divizion")

    if b > 100:
        raise IndexError ("b bolche cta")

    if type(a) != int or type(b) != int:
        raise TypeError("ne tot tip danux")
    return a/b
data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
for key in data:
    try:
        res = divider(key, data[1])
        result.append(res)
    except(ValueError, IndexError, TypeError) as errors:
        result.append(str(errors))


print(result)