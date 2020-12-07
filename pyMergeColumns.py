#!/usr/bin/env python3

"""

pyMergeColumns

A Python script to merge plain text formatted data column by column sequentially into one file.

usage: merge.py [-h] [--empty EMPTY] [--symbol SYMBOL] outputfile inputfiles [inputfiles ...]

Authors: Ludovico Pavesi, Matteo Paolieri, 2019

License: MIT

"""

import csv
import argparse
import os


def merge(output_file, input_files, empty_columns, symbol_delimiter):

    rows = []

    for data_file in input_files:

        with open(data_file) as file:
            print(f"Reading:\n{os.path.basename(data_file)}")
            rownum = 0
            data = csv.reader(file, delimiter=symbol_delimiter)
            for row in data:
                row: list
                while '' in row:
                    row.remove('')
                if len(row) < 2:
                    print(f"Skipped this line: {' '.join(row)}")
                    continue
                if len(rows) <= rownum:
                    rows.append([])
                rows[rownum].extend(row)
                rows[rownum].extend([''] * empty_columns)
                rownum += 1

    with open(output_file, "w") as file:
        writer = csv.writer(file, delimiter=symbol_delimiter, quoting=csv.QUOTE_NONE)
        for row in rows:
            writer.writerow(row)


def main(output_file, input_files, empty_columns, symbol_delimiter):
    try:
        merge(output_file, input_files, empty_columns, symbol_delimiter)
    except Exception as e:
        print(f'ERROR: {e}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Merge random data files.')
    parser.add_argument('outputfile', nargs=1, type=str, help="Output file name (remember to write extension!)")
    parser.add_argument('inputfiles', nargs='+', type=str, help="Input file names")
    parser.add_argument('--empty', type=int, help="Number of empty columns between files (default 0)")
    parser.add_argument('--symbol', type=str, help="Symbol used as delimiter. Default is tab '\t'. Can be used: "
                                                   ", . ' ' etc.")
                                                   
    parser.set_defaults(empty=0)
    parser.set_defaults(symbol='\t')
    
    args = parser.parse_args()
    main(args.outputfile[0], args.inputfiles, args.empty, args.symbol)

