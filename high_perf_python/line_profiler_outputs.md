"""
❯ kernprof -l -v  perf_issue_julia_set1.py
Wrote profile results to perf_issue_julia_set1.py.lprof
Timer unit: 1e-06 s

Total time: 26.3836 s
File: perf_issue_julia_set1.py
Function: calculate_z_serial_purepython at line 21

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    21                                           @profile
    22                                           def calculate_z_serial_purepython(maxiter, zs, cs):
    23                                               """Calculate output list using Julia update rule"""
    24         1       2025.0   2025.0      0.0      output = [0] * len(zs)
    25   1000001     225411.0      0.2      0.9      for i in range(len(zs)):
    26   1000000     161860.0      0.2      0.6          n = 0
    27   1000000     220096.0      0.2      0.8          z = zs[i]
    28   1000000     183463.0      0.2      0.7          c = cs[i]
    29  34219980   11674872.0      0.3     44.3          while abs(z) < 2 and n < maxiter:
    30  33219980    7316334.0      0.2     27.7              z = z * z + c
    31  33219980    6388084.0      0.2     24.2              n += 1
    32   1000000     211426.0      0.2      0.8          output[i] = n
    33         1          0.0      0.0      0.0      return output
"""

"""
❯ kernprof -l -v  perf_issue_julia_set1.py
Wrote profile results to perf_issue_julia_set1.py.lprof
Timer unit: 1e-06 s

Total time: 36.8507 s
File: perf_issue_julia_set1.py
Function: calculate_z_serial_purepython at line 21

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    21                                           @profile
    22                                           def calculate_z_serial_purepython(maxiter, zs, cs):
    23                                               """Calculate output list using Julia update rule"""
    24         1       2007.0   2007.0      0.0      output = [0] * len(zs)
    25   1000001     216898.0      0.2      0.6      for i in range(len(zs)):
    26   1000000     152737.0      0.2      0.4          n = 0
    27   1000000     238488.0      0.2      0.6          z = zs[i]
    28   1000000     184784.0      0.2      0.5          c = cs[i]
    29  34219980    6187320.0      0.2     16.8          while True:
    30  34219980    9408894.0      0.3     25.5              if abs(z) < 2:
    31  33320301    6308556.0      0.2     17.1                  if n < maxiter:
    32  33219980    7244191.0      0.2     19.7                      z = z * z + c
    33  33219980    6495360.0      0.2     17.6                      n += 1
    34                                                           else:
    35    100321      15145.0      0.2      0.0                      break
    36                                                       else:
    37    899679     134773.0      0.1      0.4                  break
    38   1000000     261569.0      0.3      0.7          output[i] = n
    39         1          0.0      0.0      0.0      return output

"""
