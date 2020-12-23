def increment_string(strng):
    end = ''
    while True:
        try:
            last_char = str(int(strng[-1]) + 1)
            end = last_char[-1] + end
            strng = strng[:-1]
            if len(last_char) == 1:
                return strng + end
        except Exception:
            return strng + '1' + end