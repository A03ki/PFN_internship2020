from collections import deque


def recurrence_relation_elements(k):
    """k-1からk-3までのインデックスをタプルで返す
    k : 文字列Skに対応するインデックス

    Note : 本来はSk = Sk-3 + Sk-2 + Sk-1と結合するが、
        extendleftが逆順で結合するのでextendleftをした際に正しい順番になるように
        逆の順番にしている
    """
    return k-1, k-2, k-3


class CharactersABC:
    """abcの個数を保持、加算、参照するためのクラス
    a : 文字列に含まれるaの個数
    b : 文字列に含まれるbの個数
    c : 文字列に含まれるcの個数
    """
    def __init__(self):
        self.clear()

    def clear(self):
        "abcの個数は0にする"
        self.a = 0
        self.b = 0
        self.c = 0

    def add(self, a, b, c):
        "abcに加算する"
        self.a += a
        self.b += b
        self.c += c

    @property
    def abc(self):
        "abcの各値をタプルで返す"
        return self.a, self.b, self.c


class ABCCounter:
    """Skまでのabcの個数を保持し、pq間のabcの個数を数えるためのクラス
    counts : 各Skのabcの個数をタプルで持つリスト
    model : 文字列中のabcの個数を数えるためのモデル
    """
    def __init__(self):
        self.counts = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
        self.model = CharactersABC()

    def update(self, k):
        """"文字列Skまでのabcの個数をタプルとしてself.countsに加える
        k : 文字列Skに対応するインデックス(1-indexes)
        """
        if k > 2:
            indexes = deque(reversed(recurrence_relation_elements(k)))
        else:
            indexes = None

        self.model.clear()
        parent = None

        while indexes:
            index = indexes.popleft()

            if len(self.counts) <= index:  # countsに含まれていない時起こる
                parent = index
                indexes.extendleft(recurrence_relation_elements(index))
                self.model.clear()
            else:
                self.model.add(*self.counts[index])

            if parent == index + 1:
                self.counts.append(self.model.abc)

    def search(self, k, p, q):
        """pとqの間に含まれるa, b, cの個数をタプルで返す
        k : 文字列Skに対応するインデックス
        p : abcの数を数え始めるインデックス
        q : abcの数を数え終えるインデックス

        Note : k, p, qは1-indexesを使う
        """
        k = k - 1  # 1~50 -> 0~49
        if k > 2:
            indexes = deque(reversed(recurrence_relation_elements(k)))
        else:
            indexes = deque([k])

        self.model.clear()
        n_char = 0

        while indexes:
            index = indexes.popleft()

            length = sum(self.counts[index])

            if index > 2 and ((n_char < p and p <= n_char + length)
                              or q < n_char + length):
                indexes.extendleft(recurrence_relation_elements(index))
            else:
                n_char += length  # pやqを飛び出したのは足さないようにelseの時だけ足す

                if p <= n_char <= q:
                    self.model.add(*self.counts[index])

            if n_char == q:
                break

        return self.model.abc


if __name__ == "__main__":
    import os
    abs_path = os.path.dirname(os.path.abspath(__file__))

    with open(abs_path + "/q2_in.txt") as f:
        rows = f.readlines()

    outputs = [None] * len(rows)

    abc_counter = ABCCounter()
    abc_counter.update(50)
    for i, row in enumerate(rows):
        k, p, q = map(int, row.split(" "))
        outputs[i] = abc_counter.search(k, p, q)

    with open(abs_path + "/q2_out.txt", "w") as f:
        f.write("\n".join(map(lambda x: "a:{0},b:{1},c:{2}".format(*x),
                              outputs)))
