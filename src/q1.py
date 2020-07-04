import numpy as np
from itertools import product


def count_matching_determinant_filled(x, y, d):
    """xとyのうち重複を許して埋めた3×3正方行列の行列式と与えられた行列式とが一致する総数を返す
    x : 任意の値
    y : 任意の値
    d : 行列式
    """
    repeated_permutation_square = fill_squares([x, y], 3)
    return count_matching_determinant(repeated_permutation_square, d)


def fill_squares(data, n):
    """"与えられたリストの数値から重複を許して埋めた正方行列を返す
    data : 任意を値を持つリスト
    n : 正方行列の行数(列数)
    """
    repeated_permutation = np.array(list(product(data, repeat=n*n)))
    return repeated_permutation.reshape(-1, n, n)


def count_matching_determinant(array, d):
    """配列の行列式と一致する数を返す
    array : 正方行列からなる2次元以上の配列
    d : 配列の行列式との一致を確認したい値
    """
    determinant = np.round(np.linalg.det(array))  # 微小な誤差が発生するため丸めた
    return np.sum(determinant == d)


if __name__ == "__main__":
    import os
    abs_path = os.path.dirname(os.path.abspath(__file__))

    with open(abs_path + "/q1_in.txt") as f:
        rows = f.readlines()

    outputs = [None] * len(rows)

    for i, row in enumerate(rows):
        x, y, d = map(int, row.split(" "))
        outputs[i] = count_matching_determinant_filled(x, y, d)

    with open(abs_path + "/q1_out.txt", "w") as f:
        f.write("\n".join(map(str, outputs)))
