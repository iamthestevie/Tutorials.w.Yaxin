
import sys
#import scipy
from scipy.optimize import linprog

lp_content = []

for line in sys.stdin:
    # check line for spaces
    if line.rstrip() == '':
        continue

    # type 'q' to exit program
    elif 'q' == line.rstrip():
        print("You've exited from the input procedure.")
        break
    else:
        # process line input
        cur_line = [float(e) for e in line.split()]
        lp_content.append(cur_line)

# print(lp)

c = [-e for e in lp_content[0]]
A = [arr[:-1] for arr in lp_content[1:]]
b = [arr[-1] for arr in lp_content[1:]]

res = linprog(c, A_ub = A, b_ub = b)


"""
################################################
### Section three: output                    ###
################################################
"""
status = res.status

# unbounded
if status == 2:
    print("Unbounded")
# infeasible
elif status == 3:
    print("Infeasible")
else:
    print('Optimal')
    print(res.x)