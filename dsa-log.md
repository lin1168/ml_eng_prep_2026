## Week 1 - DSA

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

### 49 - Group Anagrams
- Pattern: Hash map with character frequency counter (tuple as key)
- Mistake: Tried sorted() on string (can't use list as dict key) — saw solution, learned tuple + frequency counter
- Status: ⚠️ needed solution (16+ min) → re-coded clean after

### 347 - Top K Frequent Elements
- Pattern: Hash map + sorting (lambda key, dict.items() unpacking)
- Mistake: Didn't know dict.items() unpacking or lambda sort-key syntax — researched and re-coded from scratch
- Status: ⚠️ needed solution (25+ min research) → re-coded clean, redo 07/13

## Week 1 - SQL

### 182 - Duplicate Emails
- Pattern: GROUP BY + HAVING count(*) > 1
- Mistake: None
- Status: ✅ passed clean (1:00)

### 183 - Customers Who Never Order
- Pattern: LEFT JOIN + WHERE IS NULL (anti-join)
- Mistake: None — anti-join pattern is solid
- Status: ✅ passed clean (2:00)


## Redo List
- 217 Contains Duplicate - attempt 07/09 - ✅
- 49 Group Anagrams — attempt 07/12
- 347 Top K Frequent Elements — attempt 07/13