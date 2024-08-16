from typing import List, Set, Tuple


class Matrix:
    __map = {
        0: (0, 1, 2),
        1: (3, 4, 5),
        2: (6, 7, 8),
    }

    def __init__(self, data: List[int]):
        self.__data: List[int | None | set] = [i if i else None for i in data]
        self.__all_certain_grids_filled = False
        self.__solvable = None

    def __repr__(self):
        rows = []
        for i in range(9):
            row = ' '.join(str(i) if isinstance(i, int) else '?' for i in self.get_row(i))
            rows.append(row)
        return '\n'.join(rows)

    @property
    def completeness(self):
        return sum(isinstance(i, int) for i in self.__data)

    @property
    def is_complete(self):
        return self.completeness == 9 * 9

    @property
    def is_unsolvable(self):
        return self.__solvable is False

    @property
    def branches(self) -> List['Matrix']:
        if not self.__all_certain_grids_filled:
            self.fill_certain_grids()

        if self.is_complete:
            return []

        if self.is_unsolvable:
            return []

        i, j = self.__find_min_set_index()
        choices = self.get(i, j)
        branch = [v if isinstance(v, int) else None for v in self.__data]
        branches = []
        for choice in choices:
            branch[i * 9 + j] = choice
            branches.append(self.__class__(branch.copy()))
        return branches

    def get(self, i, j):
        return self.__data[i * 9 + j]

    def set(self, i, j, value):
        self.__data[i * 9 + j] = value

    def get_row(self, i):
        return [self.__data[i * 9 + j] for j in range(9)]

    def get_col(self, j):
        return [self.__data[i * 9 + j] for i in range(9)]

    def get_section(self, i, j):
        i_group = self.__map[i // 3]
        j_group = self.__map[j // 3]

        res = []
        for i_ in i_group:
            for j_ in j_group:
                res.append(self.get(i_, j_))
        return res

    def fill_certain_grids(self):
        while not self.__all_certain_grids_filled:
            self.__all_certain_grids_filled = self.__fill_certain_grids()

    def __fill_certain_grids(self):
        """
        :return: True if finished else False
        """
        for i in range(9):
            for j in range(9):
                value = self.get(i, j)
                if isinstance(value, int):
                    # this grid is solved / the value is provided
                    continue
                if value is None:
                    # this grid is unsolved
                    possibilities = self.__find_possibilities(i, j)
                    if len(possibilities) == 0:
                        self.__solvable = False
                        return True
                    elif len(possibilities) == 1:
                        # a certain answer is found
                        self.__fill_grid(i, j, possibilities.pop())
                        return False
                    else:
                        # store the analysis in the uncertain grid temporarily
                        self.__data[i * 9 + j] = possibilities
                        continue
                if isinstance(value, set):
                    if len(value) == 0:
                        self.__solvable = False
                        return True
                    elif len(value) == 1:
                        self.__fill_grid(i, j, value.pop())
                        return False
                    else:
                        continue
        return True

    def __fill_grid(self, i, j, v):
        self.__data[i * 9 + j] = v
        for obj in self.get_section(i, j):
            if isinstance(obj, set):
                obj.discard(v)
        for obj in self.get_row(i):
            if isinstance(obj, set):
                obj.discard(v)
        for obj in self.get_col(j):
            if isinstance(obj, set):
                obj.discard(v)

    def __find_possibilities(self, i, j) -> Set:
        possibilities = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        for v in self.get_section(i, j):
            possibilities.discard(v)
        for v in self.get_row(i):
            possibilities.discard(v)
        for v in self.get_col(j):
            possibilities.discard(v)
        return possibilities

    def __find_min_set_index(self) -> Tuple:
        min_set_length = 9
        min_set_index = None
        for i in range(9):
            for j in range(9):
                v = self.get(i, j)
                if isinstance(v, set) and len(v) < min_set_length:
                    min_set_index = (i, j)
                    min_set_length = len(v)
        if min_set_index is None:
            raise AssertionError("no set found")
        return min_set_index


if __name__ == "__main__":
    m = Matrix(
        [
            1, 2, 3, 9, 8, 4, 7, 1, 2,
            2, 3, 9, 8, 4, 7, 1, 2, 1,
            3, 9, 8, 4, 7, 1, 2, 1, 2,
            1, 2, 3, 9, 8, 4, 7, 1, 2,
            2, 3, 9, 8, 4, 7, 1, 2, 1,
            3, 9, 8, 4, 7, 1, 2, 1, 2,
            1, 2, 3, 9, 8, 4, 7, 1, 2,
            2, 3, 9, 8, 4, 7, 1, 2, 1,
            3, 9, 8, 4, 7, 1, 2, 1, 2,
        ]
    )

    print(m.get(8, 0))
    print(m.get_row(0))
    print(m.get_col(8))
    print(m.get_section(5, 5))
