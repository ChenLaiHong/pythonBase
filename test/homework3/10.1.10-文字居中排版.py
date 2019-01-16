pos = int(input())
line_list = []
with open("listin.txt") as in_file:
    line_list= in_file.readlines()

with open("listout.txt", "w") as out_file:
    for line in line_list:
        left, right = line.split(':')
        left = ' '.join(left.split())
        left_out = ("{0:" + str(pos - 1) + "}").format(left.strip())
        right = right.strip()
        right = ' '.join(right.split())
        result = left_out + ": " + right + "\n"
        out_file.write(result)
