def isRotated(str1, str2):
    if (len(str1) != len(str2)):
        return False

    clock_rot = ""
    anticlock_rot = ""
    l = len(str2)
    # Initialize string as anti-clockwise rotation
    anticlock_rot = (str2[l - 2:] +
                     str2[0: l - 2])

    # Initialize string as clock wise rotation
    clock_rot = str2[2:] + str2[0:2]

    import pdb; pdb.set_trace()
    # check if any of them is equal to string1
    return (str1 == clock_rot or str1 == anticlock_rot)


print(isRotated("geeks", "eksge"))