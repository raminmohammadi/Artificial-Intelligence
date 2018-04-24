rows = 'ABCDEFGHI'
cols = '123456789'


def cross(a, b):
    return [s + k for s in a for k in b]


boxes = cross(rows, cols)

# Defining Units
row_units = [cross(r, cols) for r in rows]
col_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI')
                for cs in ('123', '456', '789')]

unitlist = row_units + col_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in boxes)


def display(values):
    """
    Display the values in 2D grids
    Input: Sudoku dictionary form
    Output: None
    """
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width) +
                      ('|' if c in '36' else '')for c in cols))
        if r in 'CF':
            print(line)
    return


def grid_values(grid):
    values = []
    all_digits = '123456789'
    for c in grid:
        if c == '.':
            values.append(all_digits)
        elif c in all_digits:
            values.append(c)

    assert len(grid) == 81
    return dict(zip(boxes, values))


grid2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
values_puzzle = grid_values(grid2)


def eliminate(values):
    solved_values = [box for box in values.keys() if len(values[box])==1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit, '')
    return values


def only_choice(values):
    for unit in unitlist:
        for digit in '123456789':
            dplace = [box for box in unit if digit in values[box]]
            if len(dplace)==1:
                values[dplace[0]]=digit
    return values


def reduce_puzzle(values):
    stalled = False
    while not stalled:
        solved_units_before = [box for box in values.keys() if len(values[box]) ==1]
        values = eliminate(values)
        values = only_choice(values)
        solved_units_after = [box for box in values.keys() if len(values[box]) ==1]
        stalled = solved_units_after==solved_units_before
        # sanity check -- if there is a box with 0 value return False
        if len([box for box in values.keys() if len(values[box]) ==0 ]):
            return False
    return values

def search(values):
    values = reduce_puzzle(values)
    if values is False:
        return False
    if all(len(values[s])==1 for s in boxes):
        return values
    n,s = min((len(values[s]), s) for s in boxes if len(values[s])>1)
    for value in values[s]:
        new_suduko = values.copy()
        new_suduko[s] = value
        attemp = search(new_suduko)
        if attemp:
            return attemp

display(search(values=values_puzzle))
