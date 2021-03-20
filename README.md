# pyMergeColumns
A Python script to merge plain text formatted data column by column sequentially into one file. It needs `pandas`.

## Usage

```
pyMergeColumns.py [-h] [-o OUTPUT] [-i INPUT [INPUT ...]] [-s SYMBOL]

Merge data files.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file name (remember to write extension!)
  -i INPUT [INPUT ...], --input INPUT [INPUT ...]
                        Input file names
  -s SYMBOL, --symbol SYMBOL
                        Symbol used as delimiter. Default is tab ' '. Can be used: , . '
                        ' etc.
```

### Example

```
pyMergeColumns.py -s "," -o output.txt -i "file1.txt" "~/docs/file2.txt" "file3"
```


# License
(c) Matteo Paolieri 2021

License: MIT

