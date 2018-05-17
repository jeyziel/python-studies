'''
Escreva uma função que desenhe uma grade como a seguinte:
        + - - - - + - - - - +
        |         |         |
        |         |         |
        |         |         |
        |         |         |
        + - - - - + - - - - +
        |         |         |
        |         |         |
        |         |         |
        |         |         |
        + - - - - + - - - - +
'''

def print_rows():
    print('+ - - - - + - - - - +')

def print_columns():
    print('|         |         |')


def print_four_times(f):
    f()
    f()
    f()
    f()

def print_grade():
    print_rows()
    print_four_times(print_columns)
    print_rows()
    print_four_times(print_columns)
    print_rows()

print_grade()
