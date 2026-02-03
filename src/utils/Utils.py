import pandas as pd
import chardet
import glob


def load_csv(csv_path, encoding=None, wildcard=False):
    if wildcard:
        df = pd.concat(pd.read_csv(f, encoding=encoding) for f in glob.glob(csv_path))
        return df
    if encoding is not None:
        df = pd.read_csv(csv_path, encoding=encoding)
        return df
    with open(csv_path, 'rb') as f:
        result = chardet.detect(f.read(10000))
        df = pd.read_csv(csv_path, encoding=result['encoding'])
        return df
