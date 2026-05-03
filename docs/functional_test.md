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

**Function under test:**  
`sympy.solve`

---

### Numeric test cases

| Equation | Case | Expected result |
|----------|------|-----------------|
| $x = -2$ | `solve(x + 2, x)` | `[-2]` |
| $3x = 9$ | `solve(3*x - 9, x)` | `[3]` |
| $x^2 = 4$ | `solve(x**2 - 4, x)` | `[-2, 2]` |
| $x^2 = -1$ | `solve(x**2 + 1, x)` | `[-I, I]` |
| $x + y = 2,\; x = y$ | `solve([x + y - 2, x - y], [x, y])` | `{x: 1, y: 1}` |
| $2x + y = 1,\; x = y$ | `solve([2*x + y - 1, x - y], [x, y])` | `{x: 1/3, y: 1/3}` |
| $x - x = 1$ | `solve(x - x - 1)` | `[]` |
| $0 = 0$ | `solve(0)` | `[]` |
| $\sqrt{x} = -1$ | `solve(sqrt(x) + 1, x)` | `[]` |

### Symbolic test cases
| Equation | Case |
|----------|------|
| $$ax + b = 0$$ | `solve(a*x + b, x)` |
| $$ax^2 + bx + c = 0$$ | `solve(a*x**2 + b*x + c, x)` |
| $$x e^x = a$$ | `solve(x*e**x - a, x)` |
| $$\frac{3ax + b}{9} = \frac{x}{3} + \frac{b}{3}$$ | `solve((3*x*a + b)/9 - x*a/3 - b/3, x)` |

**Complex real-life case**

Input system of equations:
$$
\begin{cases}
(R_1 + R_2) I_1 - R_2 I_2 - V_1 = 0 \\
- R_2 I_1 + (R_2 + R_3 + R_4) I_2 - R_4 I_3 = 0 \\
- R_4 I_2 + (R_4 + R_5) I_3 + V_2 = 0
\end{cases}
$$
Case
```
solve([
    (R1 + R2)*I1 - R2*I2 - V1,
    -R2*I1 + (R2 + R3 + R4)*I2 - R4*I3,
    -R4*I2 + (R4 + R5)*I3 + V2
], [I1, I2, I3])
```

### Pass criterion:

- All solutions satisfy original equations when substituted (using `expr.subs()` from sympy)
- No extraneous solutions are present
- All expected solutions are returned
- Output structure remains consistent with documented behavior  