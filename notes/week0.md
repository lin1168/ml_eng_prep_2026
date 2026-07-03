# Week 0 Diagnostics

## Test A — Coding Baseline (Saturday)
Untimed, no hints. Mark each: clean / struggled / needed solution.

- Two Sum (1): struggled
- Valid Parentheses (20): struggled
- Merge Two Sorted Lists (21): solution

**Verdict**: W1–W2 stay on Easy problems. Add 15 min/day Python patterns drills (HackerRank Python track). This is normal — buffers absorb it.

## Test B — ML Theory (Sunday, 60 min, closed book)

1. Overfitting + two fixes:

Overfitting is when the model performs well on training data but poorly on unseen data. This means the model has captured noise from the sample instead of the true underlying behavior of the population.

Two fixes: (1) Cross-validation — split the sample into training and testing sets to ensure we're not just memorizing noise. (2) Regularization (L1/L2) — introduce penalty terms that add slight bias but reduce variance and overfitting.

**Grade: 70%**

2. What gradient descent does:

Gradient descent is a way to optimize the model by finding the lowest value of the loss function. It's a step-wise procedure: calculate the loss, compute the gradient, and update coefficients in the opposite direction of the gradient. The main risk is getting stuck at local minima if the surrounding area has higher gradients.

**Grade: 60%**

3. Precision vs recall — when each matters:

Precision = TP / (TP + FP) — measures accuracy of positive predictions. Important when false positives are costly (e.g., spam filter flagging good emails as spam).

Recall = TP / (TP + FN) — measures what fraction of actual positives you catch. Important when false negatives are costly (e.g., cancer screening missing actual cancers).

Trade-off: high precision means fewer false alarms but you miss real cases; high recall catches more real cases but flags too many false alarms. Choose based on domain cost.

**Grade: 65%**

**Overall Test B: ~65%** — solid dormant knowledge. Reactivates in W2–W5.

## Test C — SQL Sanity (Sunday, 30 min, timed)
15 min each, timed. Mark: clean / struggled.

- Second Highest Salary (176): clean
- Delete Duplicate Emails (196): slight struggle

**Verdict**: SQL strength confirmed. Maintain 2/week, no drills needed.

## Test D — Gap Table Inventory (Sunday, 30 min)

| Area | Status |
|------|--------|
| Python + SQL | rusty |
| Classical ML / time series | anxious-but-have-done-it |
| Deep learning (PyTorch) | anxious-but-have-done-it |
| Docker / Kubernetes | anxious-but-have-done-it |
| CI/CD & MLOps | never touched |
| REST APIs / microservices | never touched |
| DSA (HackerRank) | anxious-but-have-done-it |
| SQL under timer | rusty |
| Domain narrative (fab-AI) | never touched |
| Portfolio (end-to-end project) | anxious-but-have-done-it |

**Assessment**: Most of your CMU knowledge is dormant (anxious-but-have-done-it), not gone. The "never touched" items (CI/CD, APIs, domain) are fresh learns — expected. Plan to reactivate dormant items W1–W6 and learn new items starting W7.

## Next Steps
- Start Week 1 (July 6): Arrays & hashing + PyTorch tensors
- Keep this file; re-read in November when imposter syndrome hits