using DifferentialEquations

f(phi, k, t) = 1.01 - sin(phi)
phi0 = 0
tspan = (0.0, 10.0)
kvals = [1.01, 1.0, 0.99]
prob = ODEProblem(f, phi0, tspan, kvals)
sol = solve(prob)

using Plots
println("For multiple k values")
plot(sol)
