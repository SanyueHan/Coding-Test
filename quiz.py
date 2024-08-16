from sudoku import Matrix


def reverse_list(input_list: list):
    """
    reverse a list without any built-in functions
    """
    res = []
    for i in input_list:
        res.insert(0, i)
    return res


def solve_sudoku(matrix: Matrix):
    print(f"solve_sudoku, completeness = {matrix.completeness}")

    matrix.fill_certain_grids()
    if matrix.is_complete:
        return matrix
    elif matrix.is_unsolvable:
        return None
    else:
        for branch in matrix.branches:
            result = solve_sudoku(branch)
            if result:
                return result
    return None



if __name__ == "__main__":
    # Test reverse_list
    l = [0, 1, 2]
    assert reverse_list(l) == l[::-1]

    # Test sudoku
    case_easy = Matrix([
        0, 6, 0, 8, 0, 0, 5, 0, 9,
        0, 2, 0, 6, 0, 0, 0, 0, 0,
        0, 0, 4, 5, 0, 0, 0, 0, 0,
        0, 5, 1, 3, 7, 0, 9, 0, 8,
        0, 4, 9, 0, 8, 0, 7, 6, 3,
        7, 0, 0, 0, 0, 2, 4, 1, 0,
        9, 0, 6, 0, 5, 3, 2, 8, 0,
        4, 0, 5, 0, 1, 0, 0, 9, 0,
        3, 0, 0, 4, 0, 6, 0, 0, 7,
    ])
    print("case 1: ")
    print(solve_sudoku(case_easy))

    case_medium = Matrix([
        0, 9, 0, 0, 3, 0, 1, 5, 0,
        2, 1, 8, 7, 0, 5, 0, 0, 6,
        0, 0, 0, 0, 0, 6, 0, 0, 4,
        9, 0, 0, 0, 7, 8, 4, 0, 0,
        1, 8, 5, 4, 2, 0, 7, 6, 0,
        3, 7, 0, 0, 6, 0, 0, 2, 8,
        0, 0, 1, 0, 0, 0, 0, 7, 0,
        0, 0, 9, 0, 5, 7, 0, 0, 1,
        8, 0, 7, 0, 0, 3, 0, 4, 0,
    ])
    print("case 2: ")
    print(solve_sudoku(case_medium))

    case_hard = Matrix([
        0, 0, 0, 5, 0, 0, 8, 0, 0,
        2, 5, 7, 0, 0, 0, 0, 4, 9,
        0, 8, 0, 0, 0, 0, 0, 0, 1,
        3, 0, 0, 0, 0, 0, 0, 6, 0,
        0, 2, 9, 7, 0, 3, 0, 0, 0,
        5, 0, 0, 0, 0, 8, 3, 0, 4,
        0, 0, 2, 1, 0, 0, 0, 9, 0,
        7, 4, 0, 0, 0, 0, 0, 0, 0,
        1, 0, 6, 0, 8, 4, 7, 0, 3,
    ])
    print("case 3: ")
    print(solve_sudoku(case_hard))

    case_expert = Matrix([
        0, 0, 0, 0, 0, 0, 0, 8, 0,
        0, 4, 6, 0, 0, 0, 0, 0, 2,
        7, 0, 8, 4, 5, 0, 0, 1, 0,
        0, 6, 9, 0, 0, 5, 0, 0, 0,
        0, 0, 1, 0, 7, 0, 0, 0, 4,
        4, 7, 0, 0, 0, 0, 0, 6, 0,
        8, 1, 0, 9, 0, 6, 5, 4, 0,
        0, 9, 0, 0, 0, 0, 0, 3, 0,
        0, 5, 0, 0, 0, 4, 6, 0, 1,
    ])
    print("case 4: ")
    print(solve_sudoku(case_expert))

    case_master = Matrix([
        0, 0, 8, 0, 0, 3, 0, 0, 0,
        0, 4, 0, 6, 8, 0, 0, 0, 0,
        1, 0, 7, 2, 5, 0, 8, 0, 0,
        9, 0, 6, 3, 0, 0, 0, 0, 0,
        8, 5, 0, 0, 2, 0, 0, 3, 0,
        0, 0, 0, 0, 0, 1, 5, 0, 0,
        7, 0, 0, 0, 6, 0, 9, 0, 0,
        0, 0, 0, 4, 0, 9, 0, 0, 2,
        2, 0, 9, 0, 0, 0, 0, 0, 4,
    ])  # in this case speculative filling and recursive method starts to be used
    print("case 5: ")
    print(solve_sudoku(case_master))

    case_ultimate = Matrix([
        0,0,9,0,0,5,2,0,0,
        3,5,0,0,6,0,1,0,0,
        0,0,7,0,0,0,0,3,0,
        0,9,0,0,0,0,0,0,0,
        5,1,0,0,0,2,0,8,0,
        0,0,0,0,7,0,0,0,2,
        0,0,3,0,0,0,0,0,0,
        0,0,0,4,0,0,6,0,0,
        8,2,0,0,0,7,0,1,0,
    ])
    print("case 6: ")
    print(solve_sudoku(case_ultimate))
