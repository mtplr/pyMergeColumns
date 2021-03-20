#!/usr/bin/env python3

import pandas as pd
import argparse
import io
 
def merge(output_file, files, symbol_delimiter):
    
    dataset = pd.DataFrame()

    print(f'\nFiles to merge (in this order): {files}\n')
    
    for f in files:
                
        print(f'\nReading {f}...\n')
        
        df_new = pd.read_csv(f, delimiter=symbol_delimiter)
        dataset = pd.concat([dataset,df_new], axis = 1)

    dataset.to_csv(output_file, index=False)
    
    
def main(output_file, input_files, symbol_delimiter):
    
        merge(output_file, input_files, symbol_delimiter)


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description='Merge data files.')
    parser.add_argument('-o', '--output', nargs=1, type=str, help="Output file name (remember to write extension!)")
    parser.add_argument('-i', '--input', nargs='+', type=str, help="Input file names")
    parser.add_argument('-s', '--symbol', type=str, help="Symbol used as delimiter. Default is tab '\t'. Can be used: " ", . ' ' etc.")
                                                   
    parser.set_defaults(empty=0)
    parser.set_defaults(symbol='\t')
    parser.set_defaults(output='merged.txt')
    
    args = parser.parse_args()
    
    main(args.output[0], args.input, args.symbol)