#!/usr/bin/env python

import csv
import sys
import random

ANALYSIS_PCT = .025
TRAINING_PCT = .85
VALIDATION_PCT = .125
SEED = 351


def main():
    if len(sys.argv) != 5:
        print 'Usage: python split_training_data.py <input file (with decrypted categories)> <analysis file> <training file> <validation file>'
        exit()

    input_file, analysis_file, training_file, validation_file = sys.argv[1:]
    num_samples = sum(1 for line in open(input_file, 'r')) - 1
    samples = range(num_samples)
    random.seed(SEED)
    random.shuffle(samples)
    output_map = [2]*num_samples
    for i in xrange(num_samples):
        if i < round(ANALYSIS_PCT*num_samples):
            output_map[i] = 0
        elif (i >= round(ANALYSIS_PCT*num_samples) and i < round((ANALYSIS_PCT + TRAINING_PCT)*num_samples)):
            output_map[i] = 1
    output_map = dict(zip(samples, output_map))

    with open(input_file, 'r') as f, open(analysis_file, 'w') as af, open(training_file, 'w') as tf, open(validation_file, 'w') as vf:
        # initialize readers and writers
        reader = csv.DictReader(f)
        af_writer = csv.DictWriter(af, reader.fieldnames)
        tf_writer = csv.DictWriter(tf, reader.fieldnames)
        vf_writer = csv.DictWriter(vf, reader.fieldnames)
        af_writer.writerow(dict(zip(reader.fieldnames, reader.fieldnames)))
        tf_writer.writerow(dict(zip(reader.fieldnames, reader.fieldnames)))
        vf_writer.writerow(dict(zip(reader.fieldnames, reader.fieldnames)))

        counter = 0
        for row in reader:
            if output_map[counter] == 0:
                af_writer.writerow(row)
            elif output_map[counter] == 1:
                tf_writer.writerow(row)
            else:
                vf_writer.writerow(row)
            counter += 1

if __name__ == '__main__':
    main()
