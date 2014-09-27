#!/usr/bin/env python

import sys
import csv
import numpy as np
import json


csv.field_size_limit(sys.maxsize)

CATEGORY_FIELDS = [
        'C1',
        'C2',
        'C3',
        'C4',
        'C5',
        'C6',
        'C7',
        'C8',
        'C9',
        'C10',
        'C11',
        'C12',
        'C13',
        'C14',
        'C15',
        'C16',
        'C17',
        'C18',
        'C19',
        'C20',
        'C21',
        'C22',
        'C23',
        'C24',
        'C25',
        'C26']


class CategoryManager(object):
    def __init__(self):
        self.max_cat = 0
        self.starting_value = 0

    def from_string(self, s):
        category_map = json.loads(s)
        self.max_cat = max(category_map.values()) + 1 # 0 is saved for NA


def read_cat_managers(json_file):
    cat_managers = { }
    with open(json_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            cat_managers[row[0]] = CategoryManager()
            cat_managers[row[0]].from_string(row[1])
    return cat_managers


def process_features(row, cat_managers):
    output = { }

    output[0] = 1 if row['I1'] == '' else 0
    output[1] = 0 if row['I1'] == '' else int(row['I1'])
    output[2] = 1 if row['I2'] == '' else 0
    output[3] = 0 if row['I2'] == '' else int(row['I2'])
    output[4] = 1 if row['I3'] == '' else 0
    output[5] = 0 if row['I3'] == '' else int(row['I3'])
    output[6] = 1 if row['I4'] == '' else 0
    output[7] = 0 if row['I4'] == '' else int(row['I4'])
    output[8] = 1 if row['I5'] == '' else 0
    output[9] = 0 if row['I5'] == '' else int(row['I5'])
    output[10] = 1 if row['I6'] == '' else 0
    output[11] = 0 if row['I6'] == '' else int(row['I6'])
    output[12] = 1 if row['I7'] == '' else 0
    output[13] = 0 if row['I7'] == '' else int(row['I7'])
    output[14] = 1 if row['I8'] == '' else 0
    output[15] = 0 if row['I8'] == '' else int(row['I8'])
    output[16] = 1 if row['I9'] == '' else 0
    output[17] = 0 if row['I9'] == '' else int(row['I9'])
    output[18] = 1 if row['I10'] == '' else 0
    output[19] = 0 if row['I10'] == '' else int(row['I10'])
    output[20] = 1 if row['I11'] == '' else 0
    output[21] = 0 if row['I11'] == '' else int(row['I11'])
    output[22] = 1 if row['I12'] == '' else 0
    output[23] = 0 if row['I12'] == '' else int(row['I12'])
    output[24] = 1 if row['I13'] == '' else 0
    output[25] = 0 if row['I13'] == '' else int(row['I13'])
    for cat in CATEGORY_FIELDS:
        idx = cat_managers[cat].starting_value + (0 if row[cat] == '' else int(row[cat]) + 1)
        output[idx] = 1

    return output

def main():
    if len(sys.argv) != 5:
        print 'Usage: python fm_features.py <mode> <input file> <output file> <cat json file>'

    mode, input_file, output_file, json_file = sys.argv[1:]
    cat_managers = read_cat_managers(json_file)
    cat_managers['C1'].starting_value = 26
    for i in xrange(1, len(CATEGORY_FIELDS)):
        prev_cat = CATEGORY_FIELDS[i - 1]
        cat = CATEGORY_FIELDS[i]
        cat_managers[cat].starting_value = cat_managers[prev_cat].starting_value + cat_managers[prev_cat].max_cat

    with open(input_file, 'r') as f, open(output_file, 'w') as wf:
        reader = csv.DictReader(f)
        for row in reader:
            features = process_features(row, cat_managers) #{ID:value}
            line = '-1'
            if mode == 'training':
                line = '-1' if row['Label'] == '0' else '1'
            for k, v in features.iteritems():
                line += ' ' + str(k) + ':' + str(v)
            wf.write(line + '\n')

if __name__ == '__main__':
    main()
