import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- Page Config ---
st.set_page_config(page_title="MathCraft: Riemann Sums", page_icon="📐", layout="wide")
st.title("📐 MathCraft: Riemann Sums – Code the Area Under the Curve")
st.markdown("*Developed by Xavier Honablue M.Ed for cognitivecloud.ai*")

# --- Explanation Section ---
st.header("🧮 What Do We Mean by “Code the Area”?")
st.markdown("""
In traditional calculus, we estimate the area under a curve using Riemann Sums — by drawing rectangles under the function and summing their areas.

In this app, you're not just watching it happen — **you’re coding it interactively**:

- You **choose** the function.
- You **set** the start and end points (`a`, `b`).
- You **adjust** the number of rectangles (`n`).
- You **decide** if the sum is Left, Right, or Midpoint.

Each decision generates new calculations and visuals — and shows you **Python code** behind the scenes.

### 🧠 Why it matters:
This helps you understand how math meets computer science: by using **code to simulate calculus**, you build intuition, precision, and real-world modeling skills.
""")

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

# --- Cultural & Historical Roots ---
st.header("🏺 Ancient Origins: Before Riemann")
st.markdown("""
Mathematics did not begin with textbooks — it began with the **stars, stones, and stories** of ancient people.

Long before Bernhard Riemann, many civilizations understood how to **partition space**, **estimate curved areas**, and use **discrete shapes to model the continuous**:

### 🌌 Constellation Mapping
- **Indigenous astronomers** in Africa, Mesoamerica, and Polynesia divided the sky into regions and used **celestial arc lengths** for navigation.

### 🕌 Arabic Architecture
- **Islamic architects** used intricate **tile tessellations** and **geometric repetition** to build domes — approximating curves with repeated flat forms.

### 📐 Egyptian & Babylonian Surveyors
- Used rectangular tools to measure land areas — much like early integration methods.
""")

# --- Standards Alignment ---
st.header("🎓 Common Core & Historical Relevance")
st.markdown("""
### 📏 Common Core State Standards Addressed

**High School – Functions**
- **F-IF.6**: Calculate and interpret the average rate of change of a function over a specified interval.

**High School – Number & Quantity**
- **N-Q.1**: Use units to solve problems.
- **N-Q.2**: Define quantities for modeling.
- **N-Q.3**: Choose levels of accuracy.

**High School – Modeling**
- **Modeling with mathematics**: Solve real-world problems through modeling.

---

### 🏺 Global & Historical STEM Connections

| Civilization         | Conceptual Link                         | Modern Equivalent          |
|----------------------|------------------------------------------|-----------------------------|
| Ancient Egyptians    | Rectangular partitions for land survey  | Left Riemann Sum            |
| Islamic Geometers    | Repetitive shapes in domes/tiles        | Discrete approximation      |
| African Astronomers  | Celestial partitions via arc lengths    | Interval subdivision        |
| Babylonian Farmers   | Area under irrigation paths             | Integral estimates          |
""")

# --- Quiz Section ---
st.header("🧪 Quiz Yourself!")
score = 0

with st.expander("🧠 Question 1: What does a Riemann Sum approximate?"):
    q1 = st.radio("Choose one:", [
        "The speed of an object at a single point",
        "The slope of a tangent line",
        "The average height of a function",
        "The area under a curve"
    ])
    if q1 == "The area under a curve":
        st.success("✅ Correct!")
        score += 1
    else:
        st.error("❌ Nope! Riemann Sums estimate area under a curve.")

with st.expander("🏺 Question 2: What ancient civilization used repeating geometric patterns to model domes?"):
    q2 = st.radio("Choose one:", [
        "Aztec",
        "Islamic (Arabic)",
        "Inca",
        "Greek"
    ])
    if q2 == "Islamic (Arabic)":
        st.success("✅ Correct!")
        score += 1
    else:
        st.error("❌ Try again. These appear in Arabic architecture and tile design.")

with st.expander("📏 Question 3: What Common Core standard is most directly aligned with using Riemann Sums?"):
    q3 = st.radio("Choose one:", [
        "N-Q.1: Use units in multi-step problems",
        "F-IF.6: Interpret average rate of change",
        "G-CO.1: Know precise definitions of geometric terms",
        "A-REI.3: Solve linear equations"
    ])
    if q3 == "F-IF.6: Interpret average rate of change":
        st.success("✅ Correct!")
        score += 1
    else:
        st.error("❌ Nope! F-IF.6 deals with function change — perfect fit.")

with st.expander("🌍 Question 4: Indigenous astronomers divided the sky into parts to track stars. What modern concept does this resemble?"):
    q4 = st.radio("Choose one:", [
        "Algebraic factoring",
        "Interval partitioning",
        "Volume calculation",
        "Slope finding"
    ])
    if q4 == "Interval partitioning":
        st.success("✅ Yes! Partitioning time/space is central to Riemann Sums.")
        score += 1
    else:
        st.error("❌ Think about splitting up data into pieces...")

with st.expander("🔢 Question 5: What happens when you increase the number of rectangles (n) in a Riemann Sum?"):
    q5 = st.radio("Choose one:", [
        "The estimate becomes worse",
        "The rectangles disappear",
        "The estimate gets more accurate",
        "The function becomes linear"
    ])
    if q5 == "The estimate gets more accurate":
        st.success("✅ Exactly! More rectangles = better precision.")
        score += 1
    else:
        st.error("❌ Nope! Riemann Sums get more accurate as n increases.")

# Final Score
st.markdown("---")
st.subheader(f"🎉 Your Score: {score}/5")
if score == 5:
    st.balloons()
    st.success("Incredible! You’re a Riemann Master!")
elif score >= 3:
    st.info("Nice work! Review a bit more and you'll master this.")
else:
    st.warning("Keep practicing — try re-reading the sections above!")
