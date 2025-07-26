import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- Page Config ---
st.set_page_config(page_title="MathCraft: Riemann Sums", page_icon="📐", layout="wide")
st.title("📐 MathCraft: Riemann Sums – Code the Area Under the Curve")
st.markdown("*Developed by Xavier Honablue M.Ed for cognitivecloud.ai*")

# --- Sidebar ---
st.sidebar.header("🔧 Customize Your Approximation")
func_choice = st.sidebar.selectbox("Choose a function to model:", [
    "f(x) = x²", 
    "f(x) = sin(x)", 
    "f(x) = e^x", 
    "f(x) = ln(x+1)", 
    "f(x) = 1/x"
])
a = st.sidebar.number_input("Start of interval (a)", value=0.0)
b = st.sidebar.number_input("End of interval (b)", value=2.0)
n = st.sidebar.slider("Number of rectangles (n)", 1, 100, 10)
method = st.sidebar.radio("Choose Riemann Sum Method:", ["Left", "Right", "Midpoint"])

# --- Define Function ---
def f(x):
    if func_choice == "f(x) = x²":
        return x**2
    elif func_choice == "f(x) = sin(x)":
        return np.sin(x)
    elif func_choice == "f(x) = e^x":
        return np.exp(x)
    elif func_choice == "f(x) = ln(x+1)":
        return np.log(x + 1)
    elif func_choice == "f(x) = 1/x":
        return 1 / (x + 0.001)

# --- Riemann Sum Calculation ---
dx = (b - a) / n
if method == "Left":
    x = np.linspace(a, b - dx, n)
elif method == "Right":
    x = np.linspace(a + dx, b, n)
else:  # Midpoint
    x = np.linspace(a + dx / 2, b - dx / 2, n)

y = f(x)
area = np.sum(y * dx)

# --- Plotting ---
fig, ax = plt.subplots()
x_vals = np.linspace(a, b, 1000)
ax.plot(x_vals, f(x_vals), label='f(x)', color='blue')
ax.bar(x, y, width=dx, alpha=0.3, align='center', edgecolor='black')
ax.set_title(f"{method} Riemann Sum Approximation: {area:.4f}")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.legend()

st.pyplot(fig)

# --- Real-World Scenario ---
st.header("🌍 Real-World Challenge")
st.markdown("""
You're designing a car dashboard. The car reports **velocity every second**, but you want to estimate the **total distance** driven during the trip.

Using Riemann Sums, how can you estimate the total distance without integrating?

Try entering values like `a = 0`, `b = 10`, and increasing `n` to simulate higher-frequency data collection.
""")

# --- Reveal Python Code (Optional) ---
with st.expander("👨‍💻 Show me the Python code!"):
    st.code(f"""
# Function: {func_choice}
a = {a}
b = {b}
n = {n}
method = "{method}"

dx = (b - a) / n
# Choose x values
if method == "Left":
    x = np.linspace(a, b - dx, n)
elif method == "Right":
    x = np.linspace(a + dx, b, n)
else:  # Midpoint
    x = np.linspace(a + dx/2, b - dx/2, n)

y = f(x)
area = np.sum(y * dx)
    """, language="python")

# --- Common Core & CS Alignment ---
with st.expander("🎯 Standards Alignment"):
    st.markdown("""
**Common Core Math:**
- *F-IF.6*: Calculate and interpret the average rate of change of a function.
- *N-Q.1-3*: Use units to solve problems.
- *Modeling ★*: Apply mathematics to real-world problems.

**Computer Science Connections:**
- Algorithmic thinking: Approximate continuous quantities using loops.
- Data Science: Simulating sensor data and estimation.
- Numerical methods: Foundation for integral approximation.
    """)

# --- Reflection ---
st.header("🧠 Reflect & Extend")
st.markdown("""
- What happens to the approximation as you increase `n`?
- Which method tends to **overestimate**? Which **underestimate**?
- Why is this useful when programming robots or simulations?

Try writing your own Python code to estimate other areas using `f(x) = sin(x²)` or real data!
""")
