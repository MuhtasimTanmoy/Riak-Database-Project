with open("dataset.json") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
replace='['
for x in content:
    replace+=x+','
replace=replace.rstrip(',')


f = open('FixedDataset.json', 'w')
f.write(replace+']')  # python will cnvert \n to os.linesep
f.close()
