#!/usr/bin/env python

import csv
import sys

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
        self.category_map = { }
        self.max_cat = 0

    def cat_to_int(self, cat):
        if cat not in self.category_map:
            self.max_cat += 1
            self.category_map[cat] = self.max_cat
        return self.category_map[cat]


def main():
    if len(sys.argv) != 3:
        print 'Usage: python decrypt_categorial_features.py <input file> <output file>'
        exit()

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        cat_managers = dict(zip(CATEGORY_FIELDS, [CategoryManager() for i in xrange(len(CATEGORY_FIELDS))]))
        with open(output_file, 'w') as wf:
            writer = csv.DictWriter(wf, fieldnames=reader.fieldnames)
            writer.writerow(dict(zip(reader.fieldnames, reader.fieldnames)))
            for row in reader:
                for cat_field in CATEGORY_FIELDS:
                    cat = row[cat_field]
                    if cat != '':
                        row[cat_field] = cat_managers[cat_field].cat_to_int(cat)
                writer.writerow(row)

if __name__ == '__main__':
    main()
