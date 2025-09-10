"""with open("inputs_single.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

a = float(lines[0])
b = float(lines[1])
c = float(lines[2])
t = float(lines[3])

T = a * t**2 + b * t + c

print(f"Predicted temperature at t={t}: {T:.2f}°C")"""

def quadratic_weather_model(a, b, c, t):
    return a * (t**2) + b * t + c

def read_inputs(inputs_single):
    values = {}
    with open(inputs_single, "r") as f:
        for line in f:
            if "=" in line:
                key, val = line.split("=")
                values[key.strip()] = float(val.strip())
    return values

def main():
    # Read values from input.txt
    inputs = read_inputs("input_single.txt")

    a = inputs.get("a")
    b = inputs.get("b")
    c = inputs.get("c")
    t = inputs.get("t")

    # Calculate T
    T = quadratic_weather_model(a, b, c, t)

    print(f"Equation: T = {a}*t^2 + {b}*t + {c}")
    print(f"For t = {t}, Temperature T = {T:.2f} °C")

if __name__ == "__main__":
    main()
