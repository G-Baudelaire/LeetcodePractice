import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    mask = patients["conditions"].str.match(r"DIAB1")
    return patients[mask]