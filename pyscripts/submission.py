#!/usr/bin/env python

import csv
import sys
import json
import numpy as np


def main():
    if len(sys.argv) != 4:
        print 'Usage: python submission.py <prediction file> <test file> <output file>'
        exit()

    pred_file, test_file, output_file = sys.argv[1:]
    predictions = []
    ids = []

    with open(pred_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            predictions.append(1.0 / (1.0 + np.exp(-float(row[0]))))

    with open(test_file, 'r') as f:
        reader = csv.reader(f)
        reader.next()
        for row in reader:
            ids.append(row[0])

    with open(output_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Id', 'Predicted'])
        for k, v in zip(ids, predictions):
            writer.writerow([k, v])

if __name__ == '__main__':
    main()
