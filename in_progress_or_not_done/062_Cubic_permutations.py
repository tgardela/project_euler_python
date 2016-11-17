import timeit

def get_answer():
    cubes = []
    permCubes = []
    for i in range(0, 9000):
        cubes.append(get_cube(i))
    for i in range(len(cubes)):
        tempPerm = [cubes[i]]
        for j in range(i + 1, len(cubes)):
            if is_permutation(str(cubes[i]), str(cubes[j])):
                tempPerm.append(cubes[j])
            if len(tempPerm) == 5:
                permCubes = tempPerm
                break
    return permCubes


def get_cube(number):
    return number ** 3


def is_permutation(number, perm):
    number = list(number)
    number.sort()
    perm = list(perm)
    perm.sort()
    if number == perm:
        return True
    return False


def get_number_and_look_for_cubes():
    permCubes = []
    allPermCubes = []
    for i in range(346, 600):
        cube = get_cube(i)
        perms = getPermutation(cube)
        for perm in perms:
            perm = int(perm)
            if isCube(perm):
                permCubes.append(perm)
        if len(permCubes) == 5:
            allPermCubes.append(permCubes)
        permCubes = []
    return allPermCubes


if __name__=="__main__":
    start = timeit.default_timer()

    print(get_answer())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
