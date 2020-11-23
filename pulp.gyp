from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable
# Create the model
model = LpProblem(name="small-problem", sense=LpMaximize)
# Initialize the decision variables
x = LpVariable(name="x", lowBound=0)
y = LpVariable(name="y", lowBound=0)

expression = 2 * x + 4 * y
type(expression)


constraint = 2 * x + 4 * y >= 8
type(constraint)

# Add the constraints to the model
model += (2 * x + y <= 20, "red_constraint")
model += (4 * x - 5 * y >= -10, "blue_constraint")
model += (-x + 2 * y >= -2, "yellow_constraint")
model += (-x + 5 * y == 15, "green_constraint")


# Add the objective function to the model
obj_func = x + 2 * y
model += obj_func

# Add the objective function to the model
#model += x + 2 * y

# Add the objective function to the model
model += lpSum([x, 2 * y])

print(model)

status =model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")


print(f"objective: {model.objective.value()}")


for var in model.variables():
    print(f"{var.name}: {var.value()}")




for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")



model.variables()

model.variables()[0] is x

model.variables()[1] is y

model.solver