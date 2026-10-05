import joblib
import pandas as pd
from pathlib import Path
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from src.load import load_secom
from src.features import build_feature_spec, apply_feature_spec

ROOT = Path(__file__).resolve().parents[1]
INTERIM = ROOT / "data" / "interim"
MODELS = ROOT / "models"

THRESHOLD = 0.30
VERSION = "logreg-2026-09-19"

X_all, y, ts = load_secom()

splits = pd.read_csv(INTERIM / "split_idx.csv")
train_idx = splits.loc[splits["split"] == "train", "idx"].values

spec = build_feature_spec(X_all.loc[train_idx])
X = apply_feature_spec(X_all, spec).loc[train_idx]
y_tr = y[train_idx]

pipe = Pipeline([
    ("impute", SimpleImputer(strategy="median")),
    ("scale", StandardScaler()),
    ("clf", LogisticRegression(class_weight="balanced", max_iter=2000)),
])
pipe.fit(X, y_tr)

MODELS.mkdir(parents=True, exist_ok=True)

artifact = {
    "pipeline": pipe,
    "spec": spec,
    "threshold": THRESHOLD,
    "version": VERSION,
}
joblib.dump(artifact, MODELS / "model.joblib")
print("saved", MODELS / "model.joblib")

if __name__ == "__main__":
    loaded = joblib.load(MODELS / "model.joblib")
    p = loaded["pipeline"].predict_proba(X)[:, 1]
    print("version:", loaded["version"])
    print("threshold:", loaded["threshold"])
    print("flagged:", (p >= loaded["threshold"]).sum(), "of", len(p))