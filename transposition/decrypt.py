
with open('message.txt') as f:
    line = f.read()
    print(line)
    finished = ''
    i = 0
    while i < len(line):
        finished += line[i+2]
        finished += line[i]
        finished += line[i+1]
        i += 3

    print(finished)
