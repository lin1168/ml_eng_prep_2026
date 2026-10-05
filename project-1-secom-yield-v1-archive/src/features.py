BLK_SOURCES = [
    "sensor_157", "sensor_492", "sensor_518",
    "sensor_579", "sensor_346", "sensor_112",
]

def build_feature_spec(X_train):

    top_share = X_train.apply(lambda s: s.value_counts(normalize=True).iloc[0])

    miss = X_train.isna().mean()

    drop = (top_share > 0.99) | (miss > 0.45)

    kept = list(X_train.columns[~drop])

    flags = {f"blk_{src}": src for src in BLK_SOURCES}


    return {"kept": kept, "flags": flags, "columns": kept + list(flags)}


def apply_feature_spec(X, spec):
    out = X.copy()
    for name, src in spec["flags"].items():
        out[name] = out[src].isna().astype(int)
    return out[spec["columns"]]