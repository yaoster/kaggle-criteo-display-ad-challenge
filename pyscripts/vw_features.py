#!/usr/bin/env python

import sys
import csv
import numpy as np

def process_features(row):
    output = { }
    is_binary = { }

    # integer features
    is_binary['IntFeatures'] = False
    output['IntFeatures'] = { }
    output['IntFeatures']['I1'] = 0 if row['I1'] == '' else row['I1']
    output['IntFeatures']['I2'] = 0 if row['I2'] == '' else row['I2']
    output['IntFeatures']['I3'] = 0 if row['I3'] == '' else row['I3']
    output['IntFeatures']['I4'] = 0 if row['I4'] == '' else row['I4']
    output['IntFeatures']['I5'] = 0 if row['I5'] == '' else row['I5']
    output['IntFeatures']['I6'] = 0 if row['I6'] == '' else row['I6']
    output['IntFeatures']['I7'] = 0 if row['I7'] == '' else row['I7']
    output['IntFeatures']['I8'] = 0 if row['I8'] == '' else row['I8']
    output['IntFeatures']['I9'] = 0 if row['I9'] == '' else row['I9']
    output['IntFeatures']['I10'] = 0 if row['I10'] == '' else row['I10']
    output['IntFeatures']['I11'] = 0 if row['I11'] == '' else row['I11']
    output['IntFeatures']['I12'] = 0 if row['I12'] == '' else row['I12']
    output['IntFeatures']['I13'] = 0 if row['I13'] == '' else row['I13']

    # categorical features
    is_binary['CatFeatures'] = True
    output['CatFeatures'] = { }
    output['CatFeatures']['C1'] = 'C1_' + row['C1'] 
    output['CatFeatures']['C2'] = 'C2_' + row['C2']
    output['CatFeatures']['C3'] = 'C3_' + row['C3']
    output['CatFeatures']['C4'] = 'C4_' + row['C4']
    output['CatFeatures']['C5'] = 'C5_' + row['C5']
    output['CatFeatures']['C6'] = 'C6_' + row['C6']
    output['CatFeatures']['C7'] = 'C7_' + row['C7']
    output['CatFeatures']['C8'] = 'C8_' + row['C8']
    output['CatFeatures']['C9'] = 'C9_' + row['C9']
    output['CatFeatures']['C10'] = 'C10_' + row['C10']
    output['CatFeatures']['C11'] = 'C11_' + row['C11']
    output['CatFeatures']['C12'] = 'C12_' + row['C12']
    output['CatFeatures']['C13'] = 'C13_' + row['C13']
    output['CatFeatures']['C14'] = 'C14_' + row['C14']
    output['CatFeatures']['C15'] = 'C15_' + row['C15']
    output['CatFeatures']['C16'] = 'C16_' + row['C16']
    output['CatFeatures']['C17'] = 'C17_' + row['C17']
    output['CatFeatures']['C18'] = 'C18_' + row['C18']
    output['CatFeatures']['C19'] = 'C19_' + row['C19']
    output['CatFeatures']['C20'] = 'C20_' + row['C20']
    output['CatFeatures']['C21'] = 'C21_' + row['C21']
    output['CatFeatures']['C22'] = 'C22_' + row['C22']
    output['CatFeatures']['C23'] = 'C23_' + row['C23']
    output['CatFeatures']['C24'] = 'C24_' + row['C24']
    output['CatFeatures']['C25'] = 'C25_' + row['C25']
    output['CatFeatures']['C26'] = 'C26_' + row['C26']

    return (output, is_binary)

def main():
    if len(sys.argv) != 3:
        print 'Usage: python vw_features.py <input file> <output file>'

    input_file, output_file = sys.argv[1:]
    with open(input_file, 'r') as f, open(output_file, 'w') as wf:
        reader = csv.DictReader(f)
        for row in reader:
            features, is_binary = process_features(row)
            line = '-1 ' if row['Label'] == '0' else '1 '
            for namespace, namespace_features in features.iteritems():
                line += '| ' + namespace + ' '
                if is_binary[namespace] == False:
                    for k, v in namespace_features.iteritems():
                        line += k + ':' + str(v) + ' '
                else:
                    for k, v in namespace_features.iteritems():
                        line += str(v) + ' '
            wf.write(line + '\n')

if __name__ == '__main__':
    main()
