import fileinput
total = 0
try:
    for line in fileinput.input():
        try:
            total += float(line.strip())
        except ValueError:
            pass
except OSError as err:
    print(err)
print(total)