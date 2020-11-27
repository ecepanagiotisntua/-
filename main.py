from typing import List
Matrix = List[List[int]]

def MOD(k) :
  dig = 10 ** k 
  return dig



def identity_2x2() -> Matrix:
    return [1, 0, 0, 1]


def multiply_2x2(mat1: Matrix, mat2: Matrix, copy: Matrix,k) -> None:
    a00, a01, a10, a11 = mat1
    b00, b01, b10, b11 = mat2
    t = MOD(k)
    copy[0] = (a00 * b00 + a01 * b10) % t
    copy[1] = (a00 * b01 + a01 * b11) % t
    copy[2] = (a10 * b00 + a11 * b10) % t
    copy[3] = (a10 * b01 + a11 * b11) % t


def power_2x2(mat: Matrix, n: int,k) -> Matrix:
    res = identity_2x2()

    while n:
        if n & 1:
            multiply_2x2(res, mat, res,k)

        multiply_2x2(mat, mat, mat,k)

        n >>= 1

    return res


def fib(n: int,k) -> int:
    if n == 0:
        return 0
    
    magic = [1, 1, 1, 0]
    mat = power_2x2(magic, n - 1,k)
    return mat[0]