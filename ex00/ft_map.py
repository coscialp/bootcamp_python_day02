def ft_map(function, iterables):
    return (function(it) for it in iterables)


if __name__ == "__main__":
    age = range(10)
    print(list(ft_map(lambda x: x * 2, age)))
