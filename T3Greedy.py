def Puntaje(array):
    if len(array) == 0 or len(array) == 1:
        print("error1")
        return(0)

    if len(array) == 2:
        print("error2")
        return(array[0]+array[1])

    else:
        i = j = pos = total = 0
        min = array[0] + array[1]
        for i in range(len(array)-2):
            if min > (array[i] + array[i+1]):
                min = (array[i] + array[i+1])
                if i != len(array)-1:
                    pos = i
                    print(pos)
        for j in range(len(array)):
            total += array[j]

        total -= min
        print("Puntaje maximo = ", total)
        print("Saltandose las preguntas ", pos+1 , "y", (pos+2))
    print(total)
    return(total)
