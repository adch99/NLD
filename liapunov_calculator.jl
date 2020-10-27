nt = 300 # Iterations for transient
n = 1000 # Iterations for calculations
x0 = rand(Float64)

f(x, r) = r * x * (1 - x)
df(x, r) = r * (1 - 2*x)

function liapunov(r, x0)
    x = x0
    logsum = 0
    for i = 1 : nt
        x = f(x, r)
    end

    for i = 1:n
        logsum += log(abs(df(x, r)))
        x = f(x, r)
    end

    logsum /= n
    return logsum
end

using PlotlyJS
r = LinRange(3, 4, 100)
λ = liapunov.(r, x0)
for i = 1:length(r)
    println("r:", r[i], " λ:", λ[i])
end
p = plot(r, λ, xlabel = "r", ylabel = "λ",
    title = "Logistic Map Liapunov Exponent",
    legend = false)
scatter!(r, λ)
savefig("plots/logisitic_map_liapunov_exponent.png")
gui(p)
println("Press enter to finish:")
readline()
