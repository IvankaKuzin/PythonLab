def write_data(row):
    with open('data.txt', 'w') as fdata:
        fdata.writelines("%s\n" % line for line in row)
    fdata.close()