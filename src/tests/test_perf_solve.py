import pytest

from sympy import symbols, exp, solve


# Shared symbols
x1, x2, x3, x4, x5, a = symbols("x1 x2 x3 x4 x5 a")

# Test cases in format: (name, [equations], [variables])
TEST_CASES = [
    (
        "complex_polynomial_system",
        [
            x1**3 - x5 - a,
            x2**3 - x1**6 - a,
            x3**3 - x2**9 - a,
            x4**3 - x1**6 - a,
        ],
        [x1, x2, x3, x4, x5],
    ),
    (
        "exponential_nonlinear_system",
        [
            exp(x1) + x4 + x3,
            exp(x2**2) - exp(x3),
            exp(-x3) + 2 * x1**2,
        ],
        [x1, x2, x3, x4],
    ),
]


@pytest.mark.benchmark(group="sympy_solve")
@pytest.mark.parametrize(
    "case_name,equations,variables",
    TEST_CASES,
)
def test_sympy_solve_performance(
    benchmark,
    case_name,
    equations,
    variables,
):

    def run():
        return solve(equations, variables)

    result = benchmark(run)

    assert result is not None