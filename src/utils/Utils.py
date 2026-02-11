import json
import pandas as pd
import chardet
import glob

# NBA_TEAMS maps all historical and current team names to their present franchise abbreviation.
NBA_TEAMS = {
    # Charlotte franchise (current: Charlotte Hornets, "CHA")
    "Charlotte Hornets": "CHA",
    "Charlotte Bobcats": "CHA",

    # New Orleans franchise (current: New Orleans Pelicans, "NOP")
    "New Orleans Pelicans": "NOP",
    "New Orleans Hornets": "NOP",
    "New Orleans/Oklahoma City Hornets": "NOP",

    # Nets franchise (current: Brooklyn Nets, "BKN")
    "Brooklyn Nets": "BKN",
    "New Jersey Nets": "BKN",

    # OKC/Seattle franchise (current: Oklahoma City Thunder, "OKC")
    "Oklahoma City Thunder": "OKC",
    "Seattle SuperSonics": "OKC",

    # Memphis/Vancouver franchise (current: Memphis Grizzlies, "MEM")
    "Memphis Grizzlies": "MEM",
    "Vancouver Grizzlies": "MEM",

    # Other teams (no name/abbreviation changes)
    "Los Angeles Lakers": "LAL",
    "Phoenix Suns": "PHX",
    "Indiana Pacers": "IND",
    "Utah Jazz": "UTA",
    "Portland Trail Blazers": "POR",
    "Detroit Pistons": "DET",
    "New York Knicks": "NYK",
    "LA Clippers": "LAC",
    "Los Angeles Clippers": "LAC",
    "Denver Nuggets": "DEN",
    "Cleveland Cavaliers": "CLE",
    "Chicago Bulls": "CHI",
    "Boston Celtics": "BOS",
    "Dallas Mavericks": "DAL",
    "Milwaukee Bucks": "MIL",
    "Miami Heat": "MIA",
    "San Antonio Spurs": "SAS",
    "Toronto Raptors": "TOR",
    "Atlanta Hawks": "ATL",
    "Golden State Warriors": "GSW",
    "Minnesota Timberwolves": "MIN",
    "Sacramento Kings": "SAC",
    "Orlando Magic": "ORL",
    "Houston Rockets": "HOU",
    "Philadelphia 76ers": "PHI",
    "Washington Wizards": "WAS"
}


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


def team_name_to_abbr(name):
    return NBA_TEAMS.get(name, name)
