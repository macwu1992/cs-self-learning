def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    if pos == 0:
        return 0

    if pos % 10 == 8:
        return 1 + num_eights(pos // 10)
    else:
        return num_eights(pos // 10)

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(9)
    7
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(16)
    0
    >>> pingpong(17)
    1
    >>> pingpong(18)
    2
    >>> pingpong(19)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 8:
        return n

    def helper(n):
        if n < 8:
            return 0

        if n % 8 == 0 or num_eights(n) > 0:
            return 1 + helper(n - 1)
        else:
            return helper(n - 1)

    if helper(n - 1) % 2 == 0:
        return pingpong(n - 1) + 1
    else:
        return pingpong(n - 1) - 1

pingpong(16)

def get_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> get_larger_coin(1)
    5
    >>> get_larger_coin(5)
    10
    >>> get_larger_coin(10)
    25
    >>> get_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def dfs(change, cur_coin):
    if change == 0:
        return 1
    
    if change < 0:
        return 0

    if cur_coin == None:
        return 0

    with_cur_coin = dfs(change - cur_coin, cur_coin)
    without_cur_coin = dfs(change, get_larger_coin(cur_coin))

    return with_cur_coin + without_cur_coin

dfs(6, 1)