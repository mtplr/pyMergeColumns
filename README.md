# pyMergeColumns
A Python script to merge plain text formatted data column by column sequentially into one file.

## Usage

```
pyMergeColumns.py [-h] [--empty EMPTY] [--symbol SYMBOL] outputfile inputfiles [inputfiles ...]
```

All lines beginning with `#` (comments) are skipped.

### Example

```
pyMergeColumns.py --empty 3 --symbol "," output.txt "file1" "file2" "file3"
```

* `--empty 3` add 3 empty columns between the ones merged
* `--symbol ","` use a comma delimiter instead of the default one (`\t`, tab)
* `"file1" "file2" "file3"` as input file: list of files to be merged (here three in the example)
* `output.txt` as output file: name of output. Extension is not mandatory

# License
(c) Ludovico Pavesi, Matteo Paolieri 2019

License: MIT

