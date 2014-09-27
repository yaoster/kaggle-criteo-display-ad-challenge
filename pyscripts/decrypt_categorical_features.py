#!/usr/bin/env python

import csv
import sys
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
        self.category_map = { }
        self.max_cat = 0

    def cat_to_int(self, cat):
        if cat not in self.category_map:
            self.max_cat += 1
            self.category_map[cat] = self.max_cat
        return self.category_map[cat]

    def to_string(self):
        return json.dumps(self.category_map)

    def from_string(self, s):
        self.category_map = json.loads(s)
        self.max_cat = max(self.category_map.values())


def read_cat_managers(json_file):
    cat_managers = { }
    with open(json_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            cat_managers[row[0]] = CategoryManager()
            cat_managers[row[0]].from_string(row[1])
    return cat_managers


def write_cat_managers(cat_managers, json_file):
    with open(json_file, 'w') as f:
        writer = csv.writer(f)
        for k, v in cat_managers.iteritems():
            writer.writerow([k, v.to_string()])


def main():
    if len(sys.argv) != 5:
        print 'Usage: python decrypt_categorial_features.py <mode> <input file> <output file> <json file>'
        exit()

    mode = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]
    json_file = sys.argv[4]
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f)
        if mode == 'training':
            cat_managers = dict(zip(CATEGORY_FIELDS, [CategoryManager() for i in xrange(len(CATEGORY_FIELDS))]))
        elif mode == 'testing':
            cat_managers = read_cat_managers(json_file)
        with open(output_file, 'w') as wf:
            writer = csv.DictWriter(wf, fieldnames=reader.fieldnames)
            writer.writerow(dict(zip(reader.fieldnames, reader.fieldnames)))
            for row in reader:
                for cat_field in CATEGORY_FIELDS:
                    cat = row[cat_field]
                    if cat != '':
                        row[cat_field] = cat_managers[cat_field].cat_to_int(cat)
                writer.writerow(row)

    if mode == 'training':
        write_cat_managers(cat_managers, json_file)

if __name__ == '__main__':
    main()
