import csv
import pprint

villains = [['Doctor', 'No']
            ,['Rosa','Klebb']
            ,['Mister', 'Big']
            ,['Auric', 'GoldFinger']
            ,['Ernst','Blofeld']]

print (villains)

filepath = r'c:\users\bluefish\desktop\villans.csv'

csvout = csv.writer(fout)
csv.writer()

with open(filepath, 'wb') as fout:
    csvout = csv.writer(fout,dialect='excel')
    csvout.writerows(villains)

print("write complete")

with open(filepath, 'rt') as fin:
    cin = csv.reader(fin)
    villains1 = [row for row in cin]

print(villains1)


with open(filepath,'rt') as fin:
    cin = csv.DictReader(fin,fieldnames=['firstname','lastname'])
    dd = [row for row in cin]
pprint.pprint(dd)

outfilepath = r'c:\users\bluefish\desktop\villansdict.csv'

with open(outfilepath , 'wb') as fout:
    fout = csv.DictWriter(fout, ['firstname','lastname'])
    # fout.writeheader()
    fout.writerows(dd)

with open(outfilepath , 'rb') as fin:
    cin = csv.DictReader(fin)
    print([row for row in cin])
