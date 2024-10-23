import time
# import numpy as np
# from functools import wraps

# from plot_julia_set import plot_the_iterations
from line_profiler import profile

x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193

def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        return result
    return measure_time

@profile
def calculate_z_serial_purepython(maxiter, zs, cs):
    """Calculate output list using Julia update rule"""
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while True:
            if abs(z) < 2:
                if n < maxiter:
                    z = z * z + c
                    n += 1
                else:
                    break
            else:
                break
        output[i] = n

    return output

# @timefn
def calc_pure_python(desired_width, max_iterations):
    """Create a list of complex coordinates (zs) and complex parameters (cs),
    build Julia set"""
    x_step = (x2 - x1) / desired_width
    y_step = (y1 - y2) / desired_width
    x = []
    y = []
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step
    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step
    # build a list of coordinates and the initial condition for each cell.
    # Note that our initial condition is a constant and could easily be removed,
    # we use it to simulate a real-world scenario with several inputs to our
    # function
    zs = []
    cs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))

    # print("Length of x:", len(x))
    # print("Total elements:", len(zs))
    # start_time = time.time()
    output = calculate_z_serial_purepython(max_iterations, zs, cs)
    # end_time = time.time()
    # secs = end_time - start_time
    # print(calculate_z_serial_purepython.__name__ + " took", secs, "seconds")

    # This sum is expected for a 1000^2 grid with 300 iterations
    # It ensures that our code evolves exactly as we'd intended
    assert sum(output) == 33219980
    return output

# calculate_z_serial_purepython took 4 seconds.

if __name__ == "__main__":
    # Calculate the Julia set using a pure Python solution with
    # reasonable defaults for a laptop
    desired_width = 1000
    output = calc_pure_python(desired_width, max_iterations=300)
    # output = np.split(np.array(output), desired_width)
    # plot_the_iterations(output, (x1, x2), (y1, y2), c_real + 1j * c_imag, "perf_issues1.png")


# Observations:
# 1. numpy variant is fast
# 2. As mentioned in the book, I didnt see any ever so slight improvement in performance when using the timefn decorator
#    Actually the timefn decorator added a slight overhead

# ❯ time python perf_issue_julia_set1.py
# @timefn: calc_pure_python took 4.142083168029785 seconds
# python perf_issue_julia_set1.py  4.40s user 0.15s system 97% cpu 4.684 total


# ❯ python -m cProfile -s cumulative  perf_issue_julia_set1.py
# 36221988 function calls in 11.997 seconds
#
# Ordered by: cumulative time
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.000    0.000   11.997   11.997 {built-in method builtins.exec}
# 1    0.020    0.020   11.997   11.997 perf_issue_julia_set1.py:1(<module>)
# 1    0.474    0.474   11.978   11.978 perf_issue_julia_set1.py:35(calc_pure_python)
# 1    9.098    9.098   11.414   11.414 perf_issue_julia_set1.py:21(calculate_z_serial_purepython)
# 34219980    2.316    0.000    2.316    0.000 {built-in method builtins.abs}
# 2002000    0.084    0.000    0.084    0.000 {method 'append' of 'list' objects}
# 1    0.005    0.005    0.005    0.005 {built-in method builtins.sum}
# 2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
