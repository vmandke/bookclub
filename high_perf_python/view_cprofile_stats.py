import pstats

p = pstats.Stats("profile.stats")
p.sort_stats("cumulative")
p.print_stats()

"""
p.print_stats()
Tue Oct 22 22:58:58 2024    profile.stats
         36221988 function calls in 11.853 seconds
   Ordered by: cumulative time
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000   11.853   11.853 {built-in method builtins.exec}
        1    0.019    0.019   11.853   11.853 perf_issue_julia_set1.py:1(<module>)
        1    0.498    0.498   11.834   11.834 perf_issue_julia_set1.py:35(calc_pure_python)
        1    8.934    8.934   11.242   11.242 perf_issue_julia_set1.py:21(calculate_z_serial_purepython)
 34219980    2.308    0.000    2.308    0.000 {built-in method builtins.abs}
  2002000    0.090    0.000    0.090    0.000 {method 'append' of 'list' objects}
        1    0.004    0.004    0.004    0.004 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
"""
p.print_callers()

"""
   Ordered by: cumulative time
Function                                                    was called by...
                                                                ncalls  tottime  cumtime
{built-in method builtins.exec}                             <- 
perf_issue_julia_set1.py:1(<module>)                        <-       1    0.019   11.853  {built-in method builtins.exec}
perf_issue_julia_set1.py:35(calc_pure_python)               <-       1    0.498   11.834  perf_issue_julia_set1.py:1(<module>)
perf_issue_julia_set1.py:21(calculate_z_serial_purepython)  <-       1    8.934   11.242  perf_issue_julia_set1.py:35(calc_pure_python)
{built-in method builtins.abs}                              <- 34219980    2.308    2.308  perf_issue_julia_set1.py:21(calculate_z_serial_purepython)
{method 'append' of 'list' objects}                         <- 2002000    0.090    0.090  perf_issue_julia_set1.py:35(calc_pure_python)
{built-in method builtins.sum}                              <-       1    0.004    0.004  perf_issue_julia_set1.py:35(calc_pure_python)
{method 'disable' of '_lsprof.Profiler' objects}            <- 
{built-in method builtins.len}                              <-       2    0.000    0.000  perf_issue_julia_set1.py:21(calculate_z_serial_purepython)
<pstats.Stats object at 0x10b9a0c90>
"""

p.print_callees()

"""
   Ordered by: cumulative time
Function                                                    called...
                                                                ncalls  tottime  cumtime
{built-in method builtins.exec}                             ->       1    0.019   11.853  perf_issue_julia_set1.py:1(<module>)
perf_issue_julia_set1.py:1(<module>)                        ->       1    0.498   11.834  perf_issue_julia_set1.py:35(calc_pure_python)
perf_issue_julia_set1.py:35(calc_pure_python)               ->       1    8.934   11.242  perf_issue_julia_set1.py:21(calculate_z_serial_purepython)
                                                                     1    0.004    0.004  {built-in method builtins.sum}
                                                               2002000    0.090    0.090  {method 'append' of 'list' objects}
perf_issue_julia_set1.py:21(calculate_z_serial_purepython)  -> 34219980    2.308    2.308  {built-in method builtins.abs}
                                                                     2    0.000    0.000  {built-in method builtins.len}
{built-in method builtins.abs}                              -> 
{method 'append' of 'list' objects}                         -> 
{built-in method builtins.sum}                              -> 
{method 'disable' of '_lsprof.Profiler' objects}            -> 
{built-in method builtins.len}                              -> 
<pstats.Stats object at 0x10b9a0c90>

"""

