# Amortized Analysis

## Introduction
Amortized analysis is a method of analyzing the runtime complexity of an algorithm over a sequence of operations, rather than focusing on a single operation's worst-case cost.

### Key Idea
- Instead of considering just the worst-case time complexity of a single operation, amortized analysis examines the average cost per operation in a sequence.
- Unlike average-case analysis, amortized analysis **does not involve probability or expectation**.

### Example Scenario
Consider a **stack** with the following operations:
- `PUSH(S, x)`: Push an item onto the stack.
- `k-POP(S, k)`: Pop *k* items from the stack (*k ≤ size(S)*).

If all operations were worst-case `O(N)`, then performing `N` operations might seem to take `O(N^2)`. However, using amortized analysis, we can show that the sequence actually runs in `O(N)`.

---

## Methods for Amortized Analysis

### **1. Aggregate Method**
- Sum up the costs of all operations and divide by the total number of operations to get the amortized cost per operation.

#### Example: Dynamic Array Expansion
A dynamic array starts with size 1 and doubles in size whenever it is full. The cost sequence looks like:
- `1, 2, 3, 1, 5, 1, 1, 1, 9, 1, ...`
- By summing the costs and dividing by the number of operations, we find the **amortized cost per operation is `O(1)`**.

---

### **2. Accounting Method (Banker's Method)**
- Assign a **credit (extra cost)** to each operation so that future expensive operations can be paid for.
- The goal is to never run out of credit.

#### Example: Dynamic Array Expansion
- Charge **$3 for each `APPEND` operation**:
  - `$1` for inserting the element.
  - `$1` for copying it later when resizing.
  - `$1` to recharge old elements that lost their copy dollar.
- With this approach, the total amortized cost per operation remains **`O(1)`**.

---

### **3. Potential Method**
- Define a **potential function** to measure the stored energy of the data structure.
- The **change in potential** determines the amortized cost.
- Example: If an operation increases efficiency later, it builds up potential.

*(This method is covered in CLRS Chapter 16.3 but was not discussed in lecture.)*

---

## Case Study: Amortized Analysis on Dynamic Arrays

### **Problem**
A **dynamic array** grows by doubling in size when full. Each `APPEND` operation takes `O(1)`, but resizing takes `O(N)`.

### **Analysis Using Aggregate Method**
- Total number of elements copied in `m` `APPEND` operations: `1 + 2 + 4 + ... + m`.
- This sums to `2m - 1 = O(m)`.
- Therefore, the amortized cost per operation is `O(1)`.

### **Alternative Strategies**
- **Double the size when full** → `O(1)` amortized cost per `APPEND`.
- **Increase size by 100 each time** → `O(N)` amortized cost.

---

## Shrinking Strategy
Just like expansion, a **dynamic array must also shrink** when it contains too much unused space.

### **Best Strategy:** Shrink when array is **1/4 full**
- Ensures `DELETE` operations maintain **O(1) amortized runtime**.
- This technique is also used in **hash tables**:
  - Java `HashMap`: Expand when **load factor > 3/4**.
  - Python `dict`: Expand when **load factor > 2/3**.

---

## Takeaways
- **Amortized analysis** helps evaluate sequences of operations rather than individual operations.
- The **aggregate method, accounting method, and potential method** are key techniques.
- **Dynamic array expansion** is a classic example where amortized analysis demonstrates that resizing still yields `O(1)` amortized cost.
- This technique is crucial for designing efficient **data structures** like hash tables, stacks, and dynamic arrays.

For more details, refer to CLRS Chapter 16.4 on amortized analysis.
