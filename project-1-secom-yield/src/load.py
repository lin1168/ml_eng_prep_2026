"""Canonical loader for SECOM. Everything else imports from here."""
from pathlib import Path
import pandas as pd

RAW = Path(__file__).resolve().parents[1] / "data" / "raw"


def load_secom(raw_dir=RAW):
    """
    Returns
    -------
    X  : DataFrame (1567, 590), float, NaN for missing
    y  : Series of int8 -- 1 = fail, 0 = pass
    ts : Series of datetime64
    """
    raw_dir = Path(raw_dir)

    # 1. sensor matrix: space-separated, no header, 'NaN' = missing
    X = pd.read_csv(raw_dir / "secom.data", sep=r"\s+", header=None)

    # 2. columns are anonymous -> zero-padded names so they sort correctly
    X.columns = [f"sensor_{i:03d}" for i in range(X.shape[1])]

    # 3. labels file: <label> "<dd/mm/yyyy hh:mm:ss>" -- quotes keep the
    #    timestamp as one field even though sep=" "
    labels = pd.read_csv(
        raw_dir / "secom_labels.data",
        sep=" ",
        header=None,
        names=["label", "timestamp"],
    )

    # 4. -1/+1 -> 0/1 so that the rare class (fail) is the positive class
    y = labels["label"].map({-1: 0, 1: 1}).astype("int8").rename("fail")

    # 5. day-first, explicit format so 07/06/2008 can't be read as 6 July
    ts = pd.to_datetime(
        labels["timestamp"], format="%d/%m/%Y %H:%M:%S"
    ).rename("timestamp")

    # 6. rows are matched by position only -- fail loudly if they drift
    assert len(X) == len(y) == len(ts), f"{len(X)}, {len(y)}, {len(ts)}"
    assert y.isna().sum() == 0, "unmapped label value in secom_labels.data"

    return X, y, ts


if __name__ == "__main__":
    X, y, ts = load_secom()
    print("shape :", X.shape)
    print(y.value_counts().rename({0: "pass", 1: "fail"}))
    print("span  :", ts.min(), "->", ts.max())