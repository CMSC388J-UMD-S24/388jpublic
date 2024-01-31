def hello_world():
    """ Returns 'Hello, World!'

    Arguments:
    None

    Usage:
    >>> hello_world()
    'Hello, World!'
    """
    return "Hello, World!"


def sum_unique(l):
    """ Sums values in l, not counting duplicates.

    Arguments:
    l -- a list of integers

    Usage:
    >>> sum_unique([])
    0
    >>> sum_unique([4, 4, 5])
    9
    >>> sum_unique([4, 2, 5])
    11
    >>> sum_unique([2, 2, 2, 2, 1])
    3
    """
    if len(l) == 0 or l is None:
        return 0
    
    sum_of_l = 0
    unique = []
    for num in l:
        if num not in unique:
            unique.append(num)
            sum_of_l += num

    return sum_of_l


def palindrome(x):
    """ Determines if x, an integer or string, is a palindrome, i.e.
    has the same value reversed.

    Arguments:
    x -- an integer or string

    Usage:
    >>> palindrome(1331)
    True
    >>> palindrome('racecar')
    True
    >>> palindrome(1234)
    False
    >>> palindrome('python')
    False
    """
    string = str(x)
    for i in range(int(len(string) / 2)):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True
        
        
        


def sum_multiples(num):
    """ Sums up all multiples of 3 and 5 upto and not including num.

    Arguments:
    num -- a positive integer

    Usage:
    >>> sum_multiples(10) # Multiples: [3, 5, 6, 9]
    23
    >>> sum_multiples(3) # Multiples: []
    0
    >>> sum_multiples(5) # Multiples: [3]
    3
    >>> sum_multiples(16) # Multiples: [3, 5, 6, 9, 10, 12, 15]
    60
    """
    sum_nums = 0
    print(num)
    for i in range(0, num):
        print(i)
        if i % 3 == 0 or i % 5 == 0:
            sum_nums = sum_nums + i
    return sum_nums



def num_func_mapper(nums, funs):
    """Applies each function in funs to the list of numbers, nums, and
    returns a list consisting of the results of those functions. 

    Arguments:
    nums -- a sequence of numbers
    funs -- a sequence of functions
          - each function in funs acts on a sequence of numbers and returns a number

    Usage:
    >>> f_list = [sum_unique, sum]
    >>> num_list = [2, 2, 2, 4, 5]
    >>> num_func_mapper(num_list, f_list)
    [11, 15]
    """
    new_list = [] 
    for function in funs:
        new_list.append(function(nums))
        # Function that maps each number to another value 
    return new_list



def height_sort(names, heights):
    """
    You are given an array of strings names, and an array heights that consists
    of distinct positive integers. Both arrays are of length n.
    For each index i, names[i] and heights[i] denote the name and height of the
    ith person. Return names sorted in descending order by the people's heights.

    Arguments:
    names -- a list of the names 
    height -- a list of the heights of the names
    
    Usage:
    >>> names = ["Mary","John","Emma"], heights = [180,165,170]
    Output: ["Mary","Emma","John"]
    Explanation: Mary is the tallest, followed by Emma and John.
    """
    map = {}
    new_heights = []
    for i in range(len(names)):
        map[heights[i]] = names[i]
    

    sorted_heights = sorted(heights)
    for height in sorted_heights:
        new_heights.append(map[height])

    new_heights.reverse()
    # Return the new height array
    return new_heights
        

    
    raise NotImplementedError('Please implement this function for full credit')
 
def custom_sort(lst):
    """ Use Python's built-in sort function to sort the list so that the odd numbers (in the same order as in the original list) come first, and then the even numbers (also in the same order).

    Examples:

    >>> custom_sort([1, 2, 3, 4, 5])
    [(1, 3, 5, 2, 4)]
    (Hint: use a lambda function) 
    """
    new_list = sorted(lst, key=lambda x: (x % 2 == 0, x))

    return new_list