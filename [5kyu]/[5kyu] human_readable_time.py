def make_readable(seconds):
    import datetime
    row = str(datetime.timedelta(seconds=seconds))

    if len(row.split(', ')) == 1:
        if len(row.split(':')[0]) == 1:
            return '0' + row
        else:
            return row
    else:
        tmp = row.split(', ')[1]
        if len(tmp.split(':')[0]) == 1:
            return str(seconds // 3600) + tmp[1:]
        else:
            return str(seconds // 3600) + tmp[2:]