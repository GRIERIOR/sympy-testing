## Performance Test Scenario

### Outline

**What is tested?**  
Execution time of `sympy.solve` function on a fixed, representative set of large systems of equations, including real-world models such as electrical circuit systems.

**Why it is tested?**  
The goal is to detect performance regressions between a stable release and the latest commit, under conditions identical to typical user environments.

In a library like SymPy:
- internal changes can degrade performance without breaking correctness  
- such regressions are not caught by functional tests  
- users experience slowdown immediately after upgrade  

This test provides a consistent baseline to compare:
- release vs latest commit  
- without interference from local optimizations or configuration differences  

**Metric**  
execution time (relative comparison between versions, not a fixed threshold)

---

### Benchmark Pipeline

The performance testing pipeline operates in two modes.

#### Reference Mode

The benchmark suite is executed using a stable reference version of SymPy.

Purpose:
- establish baseline performance results,
- generate reference benchmark data for future comparisons.

The output of this stage is a stored benchmark result file containing execution statistics.

---

#### Compare Mode

The benchmark suite is executed using the desired SymPy version to test.

Purpose:
- compare current benchmark results against the stored reference results,
- detect performance regressions.

The compare stage:
- loads previously stored reference benchmark data,
- computes relative execution time differences,
- evaluates regression thresholds,
- returns explicit PASS or FAIL results.

---

### Input Data

The benchmark uses a single fixed symbolic system designed to produce a computationally expensive workload for `sympy.solve`.

The system must remain unchanged between benchmark runs.

---

#### Dataset 1 — Large Nonlinear Symbolic Polynomial System

Variables:
```python
x1, x2, x3, x4, x5, x6, x7, x8
```

Equations:
```python
[
    x1**3 + x2**2 + x3*x4 - x5 + x6 - x7 + x8 - 15,
    x1*x2 + x2**3 - x3 + x4**2 + x5 - x6 + x7 - x8 - 10,
    x1**2 + x2*x3 + x3**3 - x4 + x5**2 - x6 + x7 - x8 - 20,
    x1*x4 + x2**2 - x3 + x4**3 + x5 - x6**2 + x7 - x8 - 5,
    x1 - x2 + x3*x5 + x4**2 + x5**3 - x6 + x7**2 - x8 - 12,
    x1**2 - x2 + x3 - x4*x6 + x5**2 + x6**3 - x7 + x8 - 18,
    x1*x7 - x2**2 + x3 + x4 - x5 + x6*x7 + x7**3 - x8 - 25,
    x1 - x2*x8 + x3**2 - x4 + x5 + x6 - x7 + x8**3 - 30,
]
```

---

The benchmark implementation must:
- execute this exact system in every benchmark run,
- use identical variable ordering,
- avoid any randomized modifications.

This system is intentionally computationally expensive in order to expose symbolic solving performance regressions between SymPy versions. Because if a benchmark finishes instantly, developers inevitably declare victory and go home before the real problems even wake up.

---

### Benchmark Environment

The benchmark must be executed:
- using the same Python version,
- on the same machine or equivalent CI environment,
- with identical benchmark configuration,
- without unrelated heavy background workload when possible.

The benchmark uses:
- locally installed SymPy versions installed with `pip`,
- `pytest`,
- `pytest-benchmark`.

---

### PASS / FAIL Criteria

The benchmark result must be unambiguous.

#### PASS

The test passes if execution time remains within the allowed regression threshold.