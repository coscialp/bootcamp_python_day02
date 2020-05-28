def ft_reduce(function, iterable):
    ret = function(iterable[0], iterable[1])
    for i in range(2, len(iterable)):
        ret = function(ret, iterable[i])
    return ret


if __name__ == "__main__":
    def display(a, b):
        print("Input :", a, b)
        print("Output :", a + b)
        return a + b

    res = ft_reduce(display, range(10))
    print("Final", res)
