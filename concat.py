f_out = open('out.csv', 'w')

f_out.write('receipt,title,text\n')

files = ['raw_data_eac_part1.csv', 'raw_data.csv']

for filename in files:
  with open(filename, 'r') as f:
    next(f)
    for line in f:
      f_out.write(line)

f_out.close()
