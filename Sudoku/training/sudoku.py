rows = 'ABCDEFGHI'
digits = '123456789'
cols = digits
assignments = []
rows = 'ABCDEFGHI'


def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    while(True):
        copy_values = values.copy()
        for unit in unit_list:

            # Find all instances of naked twins in a unit
            naked_twin = [x for x in unit for y in unit if (len(values[x]) == 2) and (values[x] == values[y]) and x != y]
            if naked_twin != []:

                # Digits which need to be replaced in the unit because of naked twin
                digits = values[naked_twin[0]]

                # For every box in the unit, if any of the digits appear in the values[box], replace the value with ''
                for digit in digits:
                    for box in unit:
                        a = values[box]
                        if digit in a and box not in naked_twin:
                            #values[box] = values[box].replace(digit, '')
                            assign_value(values, box, values[box].replace(digit, ''))

        # Checking if board is changing while iterating through the naked twins procedure
        # If the board is not changing that we are breaking out of the while loop
        if all([values[x] == copy_values[x] for x in boxes]):
            break                         
    return values       


def cross(string1, string2):
    """
    :param string1: first input string
    :param string2: second input string
    :return: list of all possible concatenations of a letters in string 1 with letters in string 2
    """
    return [s+t for s in string1 for t in string2]


boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
col_units = [cross(rows, c) for c in cols]
square_units = [cross(rp, cp) for rp in ("ABC", "DEF", "GHI") for cp in ("123", "456", "789")]
diagonal_units = [[rows[i]+ cols[i] for i in range(9)], [rows[::-1][i]+ cols[i] for i in range(9)]]
unit_list = row_units + col_units + square_units + diagonal_units
units = dict((s, [u for u in unit_list if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in boxes)


def display(values):
    """
    display the values in 2D Format
    :param values: Sudoku in dictionary form
    :return: None
    """
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)

    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print


def grid_values(grids):
    """
    Convert grid string into {<boxes>: <values>} dict with '123456789' values for empties.
    :param grids: sudoku grid in string form, 81 characters long
    :return: sudoku grid in dictionary form, with elements in boxes as keys and values corresponding
    """
    values = []
    for c in grids:
        if c =='.':
            values.append(digits)
        elif c in digits:
            values.append(c)

    assert len(values) == 81
    return dict(zip(boxes, values))


def elimination(values):
    """
    Eliminate values from peers of each box which has single values
    :param values: sudoku in a dictionary form
    :return: sudoko in dictioonary form after elimination
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            assign_value(values, peer, values[peer].replace(digit, ''))
    return values


def only_choice(values):
    for unit in unit_list:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                #values[dplaces[0]] = digit
                assign_value(values, dplaces[0], digit)
    return values

def reduce_puzzle(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = elimination(values)
        values = only_choice(values)
        values = naked_twins(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    values = reduce_puzzle(values)

    if values == False:
        return False
    if all(len(values[s]) == 1 for s in boxes):
        return values    
        
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def cross(string1, string2):
    """
    :param string1: first input string
    :param string2: second input string
    :return: list of all possible concatenations of a letters in string 1 with letters in string 2
    """
    return [s+t for s in string1 for t in string2]


boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
col_units = [cross(rows, c) for c in cols]
square_units = [cross(rp, cp) for rp in ("ABC", "DEF", "GHI") for cp in ("123", "456", "789")]
diagonal_units = [[rows[i]+ cols[i] for i in range(9)], [rows[::-1][i]+ cols[i] for i in range(9)]]
unit_list = row_units + col_units + square_units + diagonal_units
units = dict((s, [u for u in unit_list if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in boxes)


def display(values):
    """
    display the values in 2D Format
    :param values: Sudoku in dictionary form
    :return: None
    """
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)

    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print


def grid_values(grids):
    """
    Convert grid string into {<boxes>: <values>} dict with '123456789' values for empties.
    :param grids: sudoku grid in string form, 81 characters long
    :return: sudoku grid in dictionary form, with elements in boxes as keys and values corresponding
    """
    values = []
    for c in grids:
        if c =='.':
            values.append(digits)
        elif c in digits:
            values.append(c)

    assert len(values) == 81
    return dict(zip(boxes, values))



def elimination(values):
    """
    Eliminate values from peers of each box which has single values
    :param values: sudoku in a dictionary form
    :return: sudoko in dictioonary form after elimination
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values = assign_value(values, peer, values[peer].replace(digit, ''))
    return values


def only_choice(values):
    """
    go through all the units, and whenever there is a unit with a value that only fits in the box, assign the value to
    this box
    :param values: sudoku in a dictionary form
    :return: resulting sudoku in dictionary form after filling in only choices.
    """
    for unit in unit_list:
        for digit in "123456789":
            dplace = [box for box in unit if digit in values[box]]
            if len(dplace) == 1:
                assign_value(values, dplace[0], digit)
    return values


def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        # Your code here: Use the Eliminate Strategy
        values = elimination(values)
        # Your code here: Use the Only Choice Strategy
        values = only_choice(values)
        values = naked_twins(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    display(values)
    return values



def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    values = search(values)
    return values

if __name__ == '__main__':
    diag_sudoku_grid = '9.1....8.8.5.7..4.2.4....6...7......5..............83.3..6......9................'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
