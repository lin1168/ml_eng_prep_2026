# SECOM - data card

Source: UCI ML Repository, dataset 179. Loaded 2026-09-02 via `src/load.py`.

## Shape
- rows: 1,567 (one per production entity / test run)
- features: 590 (anonymized sensor signals, float, NaN = missing)
- span: 2008-07-19 11:55 -> 2008-10-17 06:07 (~90 days)

## Target balance
- fail (1): 104 (6.64%)
- pass (0): 1,463 (93.36%)
- ratio: 1 fail : 14.1 pass

## Notes
- UCI page and secom.names both claim 591 features; the raw file has 590
  across all 1,567 rows. Documentation is wrong. Using 590.
- Labels ship as -1 = pass / +1 = fail; remapped to 0/1 in load.py so the
  rare class is positive.
- 104 positives against 590 features. Feature selection is the project.
- Accuracy is a dead metric here: predicting all-pass scores 93.36%.