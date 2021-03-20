#!/usr/bin/env python3


import pandas as pd
import argparse

 
def merge(output_file, input_files, symbol_delimiter):
    
    dataset = pd.DataFrame()

    files = input_files

    print(f'Files to merge (in this order): {files}\n')
    
    for f in files:
        
        print(f'Reading {f}...')
        
        df_new = pd.read_csv(f, delimiter=symbol_delimiter)
        dataset = pd.concat([dataset,df_new], axis = 1)

    dataset.to_csv(output_file, index=False)
    
    
def main(output_file, input_files, symbol_delimiter):
    
    try:
        merge(output_file, input_files, symbol_delimiter)
    except Exception as e:
        print(f'ERROR: {e}')


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Merge data files.')
    parser.add_argument('-output', nargs=1, type=str, help="Output file name (remember to write extension!)")
    parser.add_argument('-input', nargs='+', type=str, help="Input file names")
    parser.add_argument('-symbol', type=str, help="Symbol used as delimiter. Default is tab '\t'. Can be used: " ", . ' ' etc.")
                                                   
    parser.set_defaults(empty=0)
    parser.set_defaults(symbol='\t')
    parser.set_defaults(output='merged.txt')
    
    args = parser.parse_args()
    
    main(args.output, args.input, args.symbol)