def process(str):
    print('Processing: ', str)

f = open('somefile.txt')
for line in f.readlines():
    if line != '\n':
        process(line)
