def wave(str):
    # Code here
    list = []
    for i, val in enumerate(str):
        if val == ' ':
            continue
        up = str[i].upper()
        c = str[:i] + up + str[i+1:]
        list.append(c)

    return list

print(wave('Two words'))