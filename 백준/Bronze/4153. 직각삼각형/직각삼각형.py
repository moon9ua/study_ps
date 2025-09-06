while True:
    nums = map(int, input().split())
    x, y, z = sorted(nums)

    if x == 0 and y == 0 and z == 0:
        break

    if x**2 + y**2 == z**2:
        print("right")
    else:
        print("wrong")
