def ft_filter(function, iterable):
    return [it for it in iterable if function(it)]


if __name__ == "__main__":
    age = range(30)
    print(ft_filter(lambda x: x > 18, age))

