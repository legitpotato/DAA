def Puntaje(array):
    if len(array) == 0 or 1:
        return(0)

    if len(array) == 2:
        return(array[0]+array[1])

    else:
        min = 0
        pos = 0
        for i in range(len(array)):
            if min < array[i] + array[i+1]:
                if array[i] =! array[(len(array)-1)]:
                    pos = i
        for j in range(len(array)):
            if j =! pos:
                total += array[i]
            else:
                j +=2

    print(total)
    return(total)

array = [10, 30, 50, 60, 5, 60]
print(Puntaje(array))
