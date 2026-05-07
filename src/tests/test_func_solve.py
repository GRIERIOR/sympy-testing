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

@pytest.mark.parametrize(
    "expr, var, expected",
    [
        (x + 2, x, [-2]),
        (3*x - 9, x, [3]),
        (x**2 - 4, x, [-2, 2]),
        (x**2 + 1, x, [-I, I]),
    ]
)
def test_single_equations(expr, var, expected):
    sol = solve(expr, var)
    assert_solutions_match(sol, expected)
    for s in sol:
        assert_solution_satisfies(expr, var, s)


@pytest.mark.parametrize(
    "eqs, vars_, expected",
    [
        ([x + y - 2, x - y], [x, y], {x: 1, y: 1}),
        ([2*x + y - 1, x - y], [x, y], {x: Rational(1, 3), y: Rational(1, 3)}),
    ]
)
def test_linear_systems(eqs, vars_, expected):
    sol = solve(eqs, vars_)

    assert isinstance(sol, dict), f"Expected dict, got {type(sol)}"
    assert sol == expected

    assert_system_solution_satisfies(eqs, sol)


@pytest.mark.parametrize(
    "expr, var, expected",
    [
        (x - x - 1, x, []),
        (0, x, []),
        (sqrt(x) + 1, x, []),
    ]
)
def test_no_solution(expr, var, expected):
    sol = solve(expr, var)
    assert sol == expected, f"Expected {expected}, got {sol}"


# -------------------------
# Symbolic tests
# -------------------------

def test_symbolic_linear():
    sol = solve(a*x + b, x)

    # expected: [-b/a]
    assert len(sol) == 1
    assert simplify(sol[0] + b/a) == 0

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