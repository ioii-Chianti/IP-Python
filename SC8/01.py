def volumn(length = 10., width = 10., height = 10.):
    print(f'length = {length:.6f}')
    print(f'width = {width:.6f}')
    print(f'height = {height:.6f}')
    return int(length * width * height)

print(volumn())