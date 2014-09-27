#!/usr/bin/env python

import sys
import csv
import numpy as np


def get_category(name, value, nonrare_categories):
    if value in nonrare_categories[name]:
        return int(value)
    elif value == '':
        return -1
    else:
        return 0


def process_features(row, nonrare_categories, is_training):
    output = { }
    is_binary = { }

    # integer features
    is_binary['IntFeatures'] = False
    output['IntFeatures'] = { }
    # I1
    output['IntFeatures']['1'] = -4.725 if row['I1'] == '' else np.log(float(row['I1']) + .05)

    #I2
    x = 0 if row['I2'] == '' else int(row['I2'])
    x = -1 if x < 0 else x
    output['IntFeatures']['2'] = x
    output['IntFeatures']['3'] = x if x < 0 else 0
    output['IntFeatures']['4'] = x if x > 200 else 0
    output['IntFeatures']['5'] = x if x > 500 else 0

    #I3
    x = 0.0 if row['I3'] == '' else float(row['I3'])
    output['IntFeatures']['6'] = np.log(x + 1)
    output['IntFeatures']['7'] = 1 if row['I3'] == '' else 0
    output['IntFeatures']['8'] = 1 if row['I3'] == '0' else 0

    #I4
    x = 0.0 if row['I4'] == '' else float(row['I4'])
    output['IntFeatures']['9'] = np.log(x/5.0 + 1.0)
    output['IntFeatures']['10'] = 1 if row['I4'] == '' else 0
    output['IntFeatures']['11'] = 1 if row['I4'] == '0' else 0

    #I5
    x = 0.0 if row['I5'] == '' else float(row['I5'])
    output['IntFeatures']['12'] = np.log(x + 1)
    output['IntFeatures']['13'] = 1 if row['I5'] == '' else 0

    #I6
    x = 0.0 if row['I6'] == '' else float(row['I6'])
    output['IntFeatures']['14'] = np.log(x + 1)
    output['IntFeatures']['15'] = 1 if row['I6'] == '' else 0

    #I7
    x = 0.0 if row['I7'] == '' else float(row['I7'])
    output['IntFeatures']['16'] = np.log(x*20 + 1)
    output['IntFeatures']['17'] = 1 if row['I7'] == '' else 0

    #I8
    x = 0.0 if row['I8'] == '' else float(row['I8'])
    lx = np.log(x + 1)
    output['IntFeatures']['18'] = lx
    output['IntFeatures']['19'] = 1 if row['I8'] == '' else 0
    output['IntFeatures']['20'] = lx if lx > 2.0 else 0

    #I9
    x = 0.0 if row['I9'] == '' else float(row['I9'])
    lx = np.log(x + 1)
    output['IntFeatures']['21'] = lx
    output['IntFeatures']['22'] = lx if lx >= 4.0 else 0
    output['IntFeatures']['23'] = 1 if row['I9'] == '' else 0
    output['IntFeatures']['24'] = 1 if row['I9'] == '0' else 0

    #I10
    x = 0.0 if row['I10'] == '' else float(row['I10'])
    output['IntFeatures']['25'] = np.log(x + 1)
    output['IntFeatures']['26'] = 1 if row['I10'] == '' else 0

    #I11
    x = 0.0 if row['I11'] == '' else float(row['I11'])
    lx = np.log(x*5.0 + 1)
    output['IntFeatures']['27'] = lx
    output['IntFeatures']['28'] = 1 if row['I11'] == '' else 0
    output['IntFeatures']['29'] = lx if lx >= 4.0 else 0

    #I12
    x = 0.0 if row['I12'] == '' else float(row['I12'])
    output['IntFeatures']['30'] = np.log(x*20.0 + 1.0)
    output['IntFeatures']['31'] = 1 if row['I12'] == '' else 0
    output['IntFeatures']['32'] = 1 if row['I12'] == '0' else 0

    #I13
    x = 0.0 if row['I13'] == '' else float(row['I13'])
    output['IntFeatures']['33'] = np.log(x + 1.0)
    output['IntFeatures']['34'] = 1 if row['I13'] == '' else 0
    output['IntFeatures']['35'] = 1 if row['I13'] == '0' else 0

    # time features
    idx = (int(row['Id']) - 10000000) if is_training else (int(row['Id']) - 60000000)
    samples_per_day = 6548659.57 if is_training else 6042135.0
    day_frac = (idx / samples_per_day) % 1
    is_binary['TimeFeatures'] = True
    output['TimeFeatures'] = { }
    if day_frac < .33:
        output['TimeFeatures']['T1'] = 100
    elif day_frac >= .33 and day_frac < .66:
        output['TimeFeatures']['T1'] = 101
    else:
        output['TimeFeatures']['T1'] = 102

    # categorical features
    is_binary['CatFeatures'] = True
    output['CatFeatures'] = { }
    output['CatFeatures']['C1'] = 10000000 + get_category('C1', row['C1'], nonrare_categories)
    output['CatFeatures']['C2'] = 20000000 + get_category('C2', row['C2'], nonrare_categories)
    output['CatFeatures']['C3'] = 30000000 + get_category('C3', row['C3'], nonrare_categories)
    output['CatFeatures']['C4'] = 40000000 + get_category('C4', row['C4'], nonrare_categories)
    output['CatFeatures']['C5'] = 50000000 + get_category('C5', row['C5'], nonrare_categories)
    output['CatFeatures']['C6'] = 60000000 + get_category('C6', row['C6'], nonrare_categories)
    output['CatFeatures']['C7'] = 70000000 + get_category('C7', row['C7'], nonrare_categories)
    output['CatFeatures']['C8'] = 80000000 + get_category('C8', row['C8'], nonrare_categories)
    output['CatFeatures']['C9'] = 90000000 + get_category('C9', row['C9'], nonrare_categories)
    output['CatFeatures']['C10'] = 100000000 + get_category('C10', row['C10'], nonrare_categories)
    output['CatFeatures']['C11'] = 110000000 + get_category('C11', row['C11'], nonrare_categories)
    output['CatFeatures']['C12'] = 120000000 + get_category('C12', row['C12'], nonrare_categories)
    output['CatFeatures']['C13'] = 130000000 + get_category('C13', row['C13'], nonrare_categories)
    output['CatFeatures']['C14'] = 140000000 + get_category('C14', row['C14'], nonrare_categories)
    output['CatFeatures']['C15'] = 150000000 + get_category('C15', row['C15'], nonrare_categories)
    output['CatFeatures']['C16'] = 160000000 + get_category('C16', row['C16'], nonrare_categories)
    output['CatFeatures']['C17'] = 170000000 + get_category('C17', row['C17'], nonrare_categories)
    output['CatFeatures']['C18'] = 180000000 + get_category('C18', row['C18'], nonrare_categories)
    output['CatFeatures']['C19'] = 190000000 + get_category('C19', row['C19'], nonrare_categories)
    output['CatFeatures']['C20'] = 200000000 + get_category('C20', row['C20'], nonrare_categories)
    output['CatFeatures']['C21'] = 210000000 + get_category('C21', row['C21'], nonrare_categories)
    output['CatFeatures']['C22'] = 220000000 + get_category('C22', row['C22'], nonrare_categories)
    output['CatFeatures']['C23'] = 230000000 + get_category('C23', row['C23'], nonrare_categories)
    output['CatFeatures']['C24'] = 240000000 + get_category('C24', row['C24'], nonrare_categories)
    output['CatFeatures']['C25'] = 250000000 + get_category('C25', row['C25'], nonrare_categories)
    output['CatFeatures']['C26'] = 260000000 + get_category('C26', row['C26'], nonrare_categories)

    return (output, is_binary)


def main():
    if len(sys.argv) != 5:
        print 'Usage: python vw_features.py <mode> <input file> <output file> <category file>'
    mode, input_file, output_file, category_file = sys.argv[1:]
    is_training = True if (mode == 'training') else False

    nonrare_categories = { }
    with open(category_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            nonrare_categories[row['name']] = set(row['variables'].split(':'))

    with open(input_file, 'r') as f, open(output_file, 'w') as wf:
        reader = csv.DictReader(f)
        for row in reader:
            features, is_binary = process_features(row, nonrare_categories, is_training)
            line = '-1 '
            if is_training:
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


# NOTES:
# with I1 transformation
# 1 pass: .4721
# 5 pass: .470614
# with I1+I2 transformations
# 1 pass: .471916
# 5 pass: .470536
# with I1-I3 transformations
# 1 pass: .471246
# 5 pass: .469988
# with I1-I8 transformations
# 1 pass: .464209
# 5 pass: .463242
# with I1-I13 transformations
# 1 pass: .462932
# 5 pass: .461797; submission: .46901
# 5 pass (2.0 learning rate): ?; submission: .46893
# 5 pass reversed: ?; submission: .47030

# with I1-I13 transformations using NN
# 1 pass (1.0 learning rate, .75 pt, 2 nodes): .464514
# 1 pass (1.0 learning rate, .75 pt, 4 nodes): .462089
# 1 pass (1.0 learning rate, .75 pt, 8 nodes): .461483
# 1 pass (1.0 learning rate, .75 pt, 16 nodes): .462704
# 1 pass (1.0 learning rate, .75 pt, 12 nodes): .462137
# 1 pass (1.0 learning rate, .75 pt, 6 nodes): .461826
# 1 pass (1.0 learning rate, .75 pt, 10 nodes): .461413

# 1 pass (1.5 learning rate, .75 pt, 10 nodes): .460977
# 2 pass (1.5 learning rate, .75 pt, 10 nodes): .458293
# 2 pass (1.5 learning rate, .90 pt, 10 nodes): .465723
# 2 pass (1.5 learning rate, .5 pt, 10 nodes): 0.457017
# 2 pass (1.0 learning rate, .5 pt, 10 nodes): 0.455483; submission: .46253
# 2 pass (0.5 learning rate, .5 pt, 10 nodes): 0.455816
# 3 pass (0.5 learning rate, .5 pt, 10 nodes): 0.455061
# 4 pass (0.5 learning rate, .5 pt, 10 nodes): 0.45475
# 5 pass (0.5 learning rate, .5 pt, 10 nodes): 0.454651
# 3 pass (0.5 learning rate, .5 pt, 12 nodes): 0.453785
# 3 pass (0.25 learning rate, .5 pt, 12 nodes): 0.454482
# 3 pass (0.5 learning rate, .25 pt, 12 nodes): 0.454575
# 4 pass (0.5 learning rate, .25 pt, 12 nodes): 0.453642
# 3 pass (0.5 learning rate, .5 pt, 14 nodes): 0.454481
# 3 pass (0.25 learning rate, .5 pt, 14 nodes): 0.453808
# 3 pass (1.5 learning rate, .75 pt, 10 nodes): .458355
# 3 pass (1.5 learning rate, .75 pt, 10 nodes, .00000000001 l1): .458418
# 5 pass (1.5 learning rate, .75 pt, 10 nodes): .4616
# 5 pass (.2517 learning rate, .4537 pt, 16 nodes): .454564
# 6 pass (1.8287 learning rate, .8727 pt, 14 nodes): .460486
# --nn 19 -l 0.60249 --power_t 0.40422 --passes 4: .453205
# --nn 18 -l 0.935687 --power_t 0.612685 --passes 7: .452558
# --nn 21 -l 0.721956 --power_t 0.613682 --passes 7: .452974
# --nn 20 -l 0.71626 --power_t 0.39208 --passes 10: 0.451057; submission: .45893
# --nn 17 -l 1.575 --power_t 0.454288 --passes 2 --l1 0.00000001 --l2 0.0000000001: .48259
# --nn 22 -l 1.1376 --power_t 0.52974 --passes 4 --l1 0.000000000001 --l2 0.000000000001: .454138
# --nn 20 -l 0.73387 --power_t 0.737734 --passes 2 --l1 0.000000000001 --l2 0.000000000008356: .462019
# --nn 22 -l 0.623 --power_t 0.78995 --passes 5 --l1 0.000000000050378 --l2 0.0000000000000036667:
# --nn 21 -l 0.76916 --power_t 0.20782 --passes 4  --l1 0.00000000001 --l2 0.000000000000001: .452447
# --nn 20 -l 0.2 --power_t 0.45 --passes 10 -b 29 -k -c --l1 0.0000000000001 --l2 0.00000000000001: .450786, submission:

# 5 pass (1.5 learning rate, .75 pt, 10 nodes, .0000000001 l1): .461584
# passes, learning rate, power_t, nodes, l1
