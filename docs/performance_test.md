## Performance Test Scenario

### Outline

**What is tested?**  
Execution time of `sympy.solve` function on a fixed, representative set of equations, executed on a clean, out-of-the-box installation (same inputs across runs)

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