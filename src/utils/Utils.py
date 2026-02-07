import json
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

def load_resultset_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)

    result_set = data["resultSets"][0]

    headers = result_set["headers"]
    rows = result_set["rowSet"]

    # Convert rows to DataFrame
    df = pd.DataFrame(rows, columns=headers)

    return df

def extract_source(value):
    if isinstance(value, dict):
        return value.get("source")
    return value