## Week 1

### 217 - Contains Duplicate
- Pattern: hash set
- Mistake: used list (O(n)) instead of set (O(1))
- Status: ✅ passed (2:22) need redo 07/09

### 242 - Valid Anagram
- Pattern: Hash map counting (dictionary)
- Mistake: Forgot dict.get(i, 0) syntax — searched the detail, re-coded clean
- Status: ✅ passed (10:33)

### 1 - Two Sum
- Pattern: Hash map / one-pass
- Mistake: First attempt was O(n²) brute force — saw optimal O(n) solution
- Status: ✅ passed (2:53) → re-coded optimal version clean