def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
    """
    Approximate the square root of a non-negative number using the bisection method.

    Parameters:
        square_target:
            The number whose square root needs to be found.
        tolerance:
            The acceptable interval width between the lower and upper bounds.
            When the interval becomes smaller than or equal to this value,
            the current midpoint is accepted as the approximate square root.
        max_iterations:
            The maximum number of bisection steps allowed before stopping.

    Returns:
        The approximate square root if the method converges.
        The original number itself for 0 and 1.
        None if the method fails to converge within max_iterations.

    Raises:
        ValueError:
            If square_target is negative, because real square roots of negative
            numbers are not defined in this lab.
    """

    # Negative numbers do not have real square roots in this lab.
    if square_target < 0:
        raise ValueError(
            "Square root of negative number is not defined in real numbers"
        )

    # The square roots of 0 and 1 are exactly themselves.
    # These cases do not need the bisection loop.
    if square_target == 0 or square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return square_target

    # The lower bound always starts at 0 because square roots of positive
    # numbers are non-negative.
    lower_bound = 0

    # Choose an upper bound that guarantees the root is inside the interval.
    #
    # If square_target > 1:
    #     sqrt(square_target) is between 0 and square_target.
    #
    # If 0 < square_target < 1:
    #     sqrt(square_target) is greater than square_target but less than 1.
    if square_target > 1:
        upper_bound = square_target
    else:
        upper_bound = 1

    # Repeat the bisection process up to max_iterations times.
    # The underscore means the loop counter is intentionally not used.
    for _ in range(max_iterations):
        # The midpoint is the current best estimate of the square root.
        root = (lower_bound + upper_bound) / 2

        # Compare root squared with the original target number.
        root_squared = root * root

        # If root squared is too small, the true square root is larger.
        # Move the lower bound upward.
        if root_squared < square_target:
            lower_bound = root

        # If root squared is too large, the true square root is smaller.
        # Move the upper bound downward.
        else:
            upper_bound = root

        # Stop when the interval is small enough.
        # This means the current root is accurate within the required tolerance.
        if upper_bound - lower_bound <= tolerance:
            root = (lower_bound + upper_bound) / 2
            print(f"The square root of {square_target} is approximately {root}")
            return root

    # If the loop finishes without reaching the tolerance, the method failed
    # to converge within the allowed number of iterations.
    print(f"Failed to converge within {max_iterations} iterations")
    return None
