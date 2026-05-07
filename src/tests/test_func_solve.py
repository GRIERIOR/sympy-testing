import pytest
from sympy import Rational, symbols, Eq, sqrt, I, exp, simplify, LambertW
from sympy import solve

# Common symbols
x, y = symbols('x y')
a, b, c = symbols('a b c')
R1, R2, R3, R4, R5 = symbols('R1 R2 R3 R4 R5')
I1, I2, I3 = symbols('I1 I2 I3')
V1, V2 = symbols('V1 V2')


# -------------------------
# Helpers
# -------------------------

def assert_solutions_match(actual, expected):
    """
    Compare solution lists ignoring order.
    """
    assert set(actual) == set(expected), f"Expected {expected}, got {actual}"


def assert_solution_satisfies(expr, var, sol):
    """
    Check if solution satisfies equation.
    """
    result = simplify(expr.subs(var, sol))
    assert result == 0, f"Solution {sol} does not satisfy equation {expr}"


def assert_system_solution_satisfies(eqs, sol_dict):
    """
    Check if dict solution satisfies system.
    """
    for eq in eqs:
        result = simplify(eq.subs(sol_dict))
        assert result == 0, f"Solution {sol_dict} does not satisfy {eq}"


# -------------------------
# Numeric tests
# -------------------------

def test_linear_simple():
    sol = solve(x + 2, x)
    assert_solutions_match(sol, [-2])
    for s in sol:
        assert_solution_satisfies(x + 2, x, s)


def test_linear_scaled():
    sol = solve(3*x - 9, x)
    assert_solutions_match(sol, [3])
    for s in sol:
        assert_solution_satisfies(3*x - 9, x, s)


def test_quadratic_real():
    sol = solve(x**2 - 4, x)
    assert_solutions_match(sol, [-2, 2])
    for s in sol:
        assert_solution_satisfies(x**2 - 4, x, s)


def test_quadratic_complex():
    sol = solve(x**2 + 1, x)
    assert_solutions_match(sol, [-I, I])
    for s in sol:
        assert_solution_satisfies(x**2 + 1, x, s)


def test_linear_system_1():
    eqs = [x + y - 2, x - y]
    sol = solve(eqs, [x, y])

    assert isinstance(sol, dict), f"Expected dict, got {type(sol)}"
    assert sol == {x: 1, y: 1}

    assert_system_solution_satisfies(eqs, sol)


def test_linear_system_2():
    eqs = [2*x + y - 1, x - y]
    sol = solve(eqs, [x, y])

    assert isinstance(sol, dict), f"Expected dict, got {type(sol)}"
    assert sol == {x: Rational(1, 3), y: Rational(1, 3)}

    assert_system_solution_satisfies(eqs, sol)


def test_no_solution():
    sol = solve(x - x - 1)
    assert sol == [], f"Expected [], got {sol}"


def test_identity_equation():
    sol = solve(0)
    assert sol == [], f"Expected [], got {sol}"


def test_invalid_domain():
    sol = solve(sqrt(x) + 1, x)
    assert sol == [], f"Expected [], got {sol}"


# -------------------------
# Symbolic tests
# -------------------------

def test_symbolic_linear():
    sol = solve(a*x + b, x)

    assert len(sol) == 1
    assert_solution_satisfies(a*x + b, x, sol[0])


def test_symbolic_quadratic():
    sol = solve(a*x**2 + b*x + c, x)

    assert len(sol) == 2
    for s in sol:
        assert_solution_satisfies(a*x**2 + b*x + c, x, s)


def test_transcendental():
    sol = solve(x * exp(x) - a, x)

    # Expect LambertW form
    assert len(sol) >= 1
    for s in sol:
        assert s == LambertW(a)


def test_fraction_equation():
    expr = (3*a*x + b)/9 - x*a/3 - b/3
    sol = solve(expr, x)

    for s in sol:
        assert_solution_satisfies(expr, x, s)


# -------------------------
# Real-life system test
# -------------------------

def test_circuit_system():
    eqs = [
        (R1 + R2)*I1 - R2*I2 - V1,
        -R2*I1 + (R2 + R3 + R4)*I2 - R4*I3,
        -R4*I2 + (R4 + R5)*I3 + V2
    ]

    sol = solve(eqs, [I1, I2, I3])

    assert isinstance(sol, dict), f"Expected dict, got {type(sol)}"
    assert set(sol.keys()) == {I1, I2, I3}, "Missing variables in solution"

    assert_system_solution_satisfies(eqs, sol)