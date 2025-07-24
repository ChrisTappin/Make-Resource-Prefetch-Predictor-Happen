# Make-Resource-Prefetch-Predictor-Happen
Decode Resource Prefetch Predictor artefacts from protobuf blobs found inside Network Action Predictor SQLite databases.

For context please see the blog post [In the protobuf: Web browser artifacts using Google's data interchange format](https://www.ibm.com/think/x-force/web-browser-artifacts-using-googles-data-interchange-format).


```
usage: ParseRPP.py [-h] [-i INPUT] [-p PREFIX] [-s SUFFIX] [-c] [-o OUTPUT] [-d DELIMITER]

Parse Resource Prefetch Predictor data from Network Action Predictor databases.

options:
  -h, --help            show this help message and exit
  -i, --input INPUT     Database file to parse. Defaults to 'Network Action Predictor'.
  -p, --prefix PREFIX   Add text before each entry is printed. Defaults to none. Ignored in CSV mode.
  -s, --suffix SUFFIX   Add text after each entry is printed. Defaults to none. Ignored in CSV mode.
  -c, --csv             Enable CSV mode (disabled by default).
                          Enabled:  Prints the host and last accessed timestamp in each row, and doesn't convert timstamps to human readable values.
                                    Prefix and suffix are ignored.
                          Disabled: Prints the host and converted timestamp then lists each entry, once per table. Skips records only referring to themselves.
                                    Output and delimiter are ingnored.
  -o, --output OUTPUT   Initial portion of file names to write if CSV mode is enabled. Defaults to timestamp in format YYYY-MM-DD_HHMMSS.
  -d, --delimiter DELIMITER
                        The character to separate values when CSV mode is enabled. Defaults to comma. Use '\t' for tab.
```


Note: All files found in the ['supporting'](/supporting) subdirectory (except ```__init__.py```) are excerpts of source code from [the Chromium open-source browser project](https://source.chromium.org/chromium/chromium/src/+/main:) (.proto) or python files derived from those excerpts using [protoc](https://protobuf.dev/installation/) and therefore subject to the same licence of this source code. A copy of the Chromium licence file can be found in the same directory.
