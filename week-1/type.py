from typing import List, Dict, Set

Vector = List[float]

def summ(s: Vector) -> Vector:
    return ([s[0]+s[1], s[1]+s[2]])

def mul(t:Vector):
    return t

def addd(s: str, p: int) -> str:
    a = int(s)
    return str(a + p) 


if __name__ == "__main__":
    print(addd("1", 2))
    print(*summ([1.5, 3.0, 5.4]))
    print(*mul([1.5, 3.0, 5.4]))