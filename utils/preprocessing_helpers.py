import pandas as pd

from config import CSV_SEPARATOR, DEFAULT_SUBJECT, TARGET_COLUMN


def load_student_csv(file_storage):
    df = pd.read_csv(file_storage, sep=CSV_SEPARATOR)

    if "subject" not in df.columns:
        df["subject"] = DEFAULT_SUBJECT

    return df


def extract_feature_row(df, row_index=0):
    if df.empty:
        return None

    row = df.drop(columns=[TARGET_COLUMN], errors="ignore").iloc[row_index]
    return row.to_dict()
