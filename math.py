

def to_base_x(n, x):
    if n == 0:
        return '0'
    ret_val = ''
    while n:
        ret_val = str(n % x) + ret_val
        n = n / x
    return ret_val

def to_base_x_padded(n, x, pad):
    return to_base_x(n, x).zfill(pad)

def to_tic_tac_toe(n):
    num_val = to_base_x_padded(n, 3, 9)
    num_val = num_val.replace('0', ' ')
    num_val = num_val.replace('1', 'X')
    return num_val.replace('2', 'O')
