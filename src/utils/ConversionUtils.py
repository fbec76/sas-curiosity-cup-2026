import pandas as pd
from logging import warning


def convert_length_unit(val, input_mode="inch", output_mode="cm"):
    if pd.isna(val) or str(val).strip() in ("-", "", "nan", "NA"):
        return pd.NA
    if input_mode == "inch" and output_mode == "cm":
        return float(val) * 2.54
    if input_mode == "cm" and output_mode == "inch":
        return float(val) / 2.54
    if input_mode == "ft" and output_mode == "cm":
        return float(val) * 30.48
    if input_mode == "cm" and output_mode == "ft":
        return float(val) / 30.48
    if input_mode == "ft_inch" and output_mode == "cm":
        s = str(val).replace("''", "")
        parts = s.split("'")
        feet = float(parts[0].strip()) if parts and parts[0].strip() != "" else 0.0
        inches = float(parts[1].strip()) if len(parts) > 1 and parts[1].strip() != "" else 0.0
        return convert_length_unit(feet * 12 + inches, input_mode="inch", output_mode="cm")
    if input_mode == "miles" and output_mode == "km":
        return float(val) * 1.60934
    if input_mode == "km" and output_mode == "miles":
        return float(val) / 1.60934
    warning("Unknown weight conversion mode: {} to {}. Using value as is.".format(input_mode, output_mode))
    return float(val)


def convert_weight_unit(val, input_mode="lbs", output_mode="kg"):
    if pd.isna(val) or str(val).strip() in ("-", "", "nan", "NA"):
        return pd.NA
    if input_mode == "lbs" and output_mode == "kg":
        return float(val) * 0.453592
    if input_mode == "kg" and output_mode == "lbs":
        return float(val) / 0.453592
    warning("Unknown weight conversion mode: {} to {}. Using value as is.".format(input_mode, output_mode))
    return float(val)


def convert_human_time(val, output_mode="min"):
    if pd.isna(val) or str(val).strip() in ("-", "", "NaN", "NA"):
        return 0
    val = str(val).replace("~", "")
    if output_mode == "min":
        if "hours" in val:
            value = float(val.strip().replace('hours', '').strip())
            minutes = value * 60
            return float(minutes)
        if "minutes" in val:
            return float(val.replace("minutes", "").strip())
    warning("Unknown time conversion mode: {}. Using value as is.".format(output_mode))
    return float(val)
