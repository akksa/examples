import csv
import os
if __name__ == '__main__':
    fpath = '/home/saravanan/workspace/Dummy'
    fnames = [x for x in os.listdir(fpath) if x.startswith('data1')]
    print len(fnames)
    a = []
    for x in fnames:
        a.append([open(fpath+'/' + x).read()])
    f = open('insurance_fraud.csv','w')
    w = csv.writer(f, csv.QUOTE_ALL)
    w.writerows(a)
    f.close()
    print 'Hello, world'
    
