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

## 238 - Product of Array Except Self
- Pattern: prefix/postfix products (two-pass O(n))
- Mistake: brute-forced O(n²) nested loop → TLE; first attempt compared by value not index; didn't know the prefix trick
- Status: ⚠️ needed solution → re-coded clean from blank → REDO LIST

## Week 1 - SQL

### 182 - Duplicate Emails
- Pattern: GROUP BY + HAVING count(*) > 1
- Mistake: None
- Status: ✅ passed clean (1:00)

### 183 - Customers Who Never Order
- Pattern: LEFT JOIN + WHERE IS NULL (anti-join)
- Mistake: None — anti-join pattern is solid
- Status: ✅ passed clean (2:00)


## Week 2 - DSA
### 125 - Valid Palindrome
  - Pattern: two pointers (solved via string reversal instead)
  - Mistake: first attempt used nested loops comparing each char against all others — misunderstood palindrome structure (each position pairs with ONE mirror position). Fixed with reversal trick; haven't written the true two-pointer version yet
  - Status: solved ✅ → REDO LIST (re-solve with left/right pointers, O(1) space)
  
## 167 - Two Sum II
  - Pattern: two pointers on sorted array (move based on sum vs target)
  - Mistake: first attempt was O(n²) brute force — ignored the sorted property entirely; then wrote `r-1` instead of `r-=1` (no-op expression) and typo'd variable name
  - Status: solved after hints → REDO LIST

## Redo List
- 217 Contains Duplicate - attempt 07/09 - ✅
- 49 Group Anagrams — attempt 07/12  ✅
- 347 Top K Frequent Elements — attempt 07/13 ✅