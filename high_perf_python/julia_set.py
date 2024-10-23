import numpy as np

from plot_julia_set import plot_the_iterations


# Function to compute the Julia set
def julia_set(c, xlim, ylim, desired_width=1000, max_iterations=300):
    # Create a complex grid of points
    x = np.linspace(xlim[0], xlim[1], desired_width)
    y = np.linspace(ylim[0], ylim[1], desired_width)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    # Initialize iteration counts
    iteration_counts = np.zeros(Z.shape, dtype=int)

    # Perform Julia set iterations
    for i in range(max_iterations):
        mask = np.abs(Z) < 2.0
        Z[mask] = Z[mask] ** 2 + c
        iteration_counts[mask] += 1

    return iteration_counts


if __name__ == "__main__":
    c=-0.62772-0.42193j
    xlim = [-1.8, 1.8]  # Range for the x-axis
    ylim = [-1.8, 1.8]  # Range for the y-axis
    output = julia_set(c, xlim, ylim)
    plot_the_iterations(output, xlim, ylim, c, "julia_set.png")

"""
Time without plotting
❯ time python julia_set.py --verbose
python julia_set.py --verbose  2.32s user 1.75s system 213% cpu 1.908 total
"""