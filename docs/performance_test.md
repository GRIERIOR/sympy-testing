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

The benchmark uses predefined symbolic systems embedded directly in the benchmark implementation.

Input data:
TO-DO

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