"""Statistics utilities."""
import numpy as np
# P-value threshold for statistical significance
# ABOVE THIS VALUE, WE FAIL TO REJECT THE NULL HYPOTHESIS
# BELOW THIS VALUE, WE REJECT THE NULL HYPOTHESIS
# COMMONLY USED THRESHOLD IS 0.05, MEANING THERE IS
# A 5% CHANCE OF OBSERVING THE DATA IF
# THE NULL HYPOTHESIS IS TRUE.
P_VALUE_THRESHOLD = 0.05


def linear_function(x: float, a: float, b: float) -> float:
    """Linear function."""
    return a * x + b


def exponential_function(x: float, a: float, b: float) -> float:
    """Exponential function."""
    return a * x ** 2 + b


def main() -> None:
    """Main function."""
    np.random.seed(0)


if __name__ == "__main__":
    main()
