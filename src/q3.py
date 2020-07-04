import heapq


def center_left_index(length):
    """配列の長さから中心のindexを返す。長さが偶数なら左寄りのindexを返す

    Note　: 取得するのは0-indexesであることに注意
    """
    return length - length // 2 - 1


def side_length(first_index, split_index, length):
    """`split_index`を除いた左右の長さのタプルを返す
    first_index : 基準となる初めのインデックス
    split_index : 分割する位置のインデックス
    length : first_indexからの長さ
    """
    left_length = split_index - first_index
    right_length = length - left_length - 1
    return left_length, right_length


def sum_even(x):
    "偶数項目のみを足し合わせた値を返す"
    return sum(x[1::2])


class SeatingArrangement:
    """最初の座席座席から座る席のリストを返す関数を持つクラス
    seats_left : 席の長さと席の最初のインデックスのタプルをからなるリスト
    first_index : first_indexは0-indexesか1-indexesの指定

    Note : 最小ヒープを使うため区間の長さは負の値で格納、一致する時はindexは低いほど優先順位が高い
    """
    def __init__(self, first_index=1):
        self.seats_left = []
        self.first_index = first_index

    def search(self, max_length, a):
        """座る席のリストを返す
        max_length : 席の長さ
        a : 最初に座る席のインデックス
        """
        arrangement = [None] * max_length
        last_index = max_length + self.first_index - 1

        left_length, right_length = side_length(self.first_index,
                                                a, max_length)
        self._add_seats_left(left_length, -2*left_length+1, self.first_index)
        self._add_seats_left(right_length, -2*right_length+1, last_index)
        arrangement[0] = a

        for i in range(1, max_length):
            a, index, length = self._select_seat(last_index)
            left_length, right_length = side_length(index, a, length)
            self._add_seats_left(left_length, -left_length, index)
            self._add_seats_left(right_length, -right_length, a+1)
            arrangement[i] = a

        return arrangement

    def _select_seat(self, last_index):
        length, index = heapq.heappop(self.seats_left)

        if index == self.first_index:
            a = self.first_index
            length = (length - 1) // 2
        elif index == last_index:
            a = last_index
            length = (length - 1) // 2
            index = last_index + length + 1
        else:
            a = center_left_index(-length) + index
        return a, index, -length

    def _add_seats_left(self, length, primary_key, priority):
        if length > 0:
            heapq.heappush(self.seats_left, (primary_key, priority))


if __name__ == "__main__":
    import os
    abs_path = os.path.dirname(os.path.abspath(__file__))

    with open(abs_path + "/q3_in.txt") as f:
        rows = f.readlines()

    outputs = [None] * len(rows)
    sa = SeatingArrangement(first_index=1)

    for i, row in enumerate(rows):
        n, a = map(int, row.split(" "))
        arrangement = sa.search(n, a)
        outputs[i] = sum_even(arrangement)

    with open(abs_path + "/q3_out.txt", "w") as f:
        f.write("\n".join(map(str, outputs)))
