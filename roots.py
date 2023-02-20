import pulp as pp

Lp_prob_max=pp.LpProblem('Problem', pp.LpMaximize)

# Create problem Variables
a=pp.LpVariable("a",lowBound=0) # Create a variable a>=0
b=pp.LpVariable("b",lowBound=0) # Create a variable b>=0
c=pp.LpVariable("c",lowBound=0) # Create a variable c>=0

# Objective Function
Lp_prob_max+=(800*a+1300*b+1800*c)

# Constraints:
Lp_prob_max+=122*a+237*b+307*c<=3000 
Lp_prob_max+=95*a+130*b+180*c<=2000

# Display the problem
print(Lp_prob_max)
status=Lp_prob_max.solve()
print(pp.LpStatus[status])

#final solution 
print(pp.value(a),pp.value(b),pp.value(c),pp.value(Lp_prob_max.objective))
