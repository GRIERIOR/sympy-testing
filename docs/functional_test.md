## Functional Test Scenario

### Outline

**What is being tested?**  
Correctness of the `sympy.solve` function on a default, out-of-the-box installation of SymPy, using representative equation types:
- linear equations
- quadratic equations
- linear systems of equations
- edge cases: no solution / multiple solutions

**Why it is being tested?**  
This scenario verifies that `sympy.solve` returns mathematically correct and complete solutions for common equation types, and that these solutions can be substituted back into the original equations to satisfy them.

The goal is to catch regressions such as:
- returning incorrect or incomplete solution sets  
- introducing extraneous (invalid) solutions  
- changes in output structure that break typical usage (e.g. different formats or missing values)  

Since `solve` is one of the most commonly used entry points, failures here directly translate to the perception that the library is unreliable, even if other parts remain functional.