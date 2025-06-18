
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Cyber Recovery Time Simulator", layout="wide")

st.title("🔁 Cyber Recovery Time Comparison Tool")

st.markdown("Use this tool to simulate the time savings between manual and automated cyber recovery tasks.")

# Input section
task_count = st.number_input("Number of recovery tasks", min_value=1, max_value=10, value=5)

tasks = []
for i in range(task_count):
    st.markdown(f"### Task {i+1}")
    name = st.text_input(f"Task Name {i+1}", key=f"name_{i}")
    manual = st.number_input(f"Manual Time (minutes) {i+1}", min_value=1, value=60, key=f"manual_{i}")
    automated = st.number_input(f"Automated Time (minutes) {i+1}", min_value=1, value=20, key=f"auto_{i}")
    tasks.append({"name": name, "manual_time": manual, "automated_time": automated})

# Show results
if st.button("Simulate"):
    task_names = [t["name"] for t in tasks]
    manual_times = [t["manual_time"] for t in tasks]
    automated_times = [t["automated_time"] for t in tasks]

    x = range(len(task_names))
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x, manual_times, width=0.4, label='Manual', align='center')
    ax.bar([i + 0.4 for i in x], automated_times, width=0.4, label='Automated', align='center')

    ax.set_xlabel("Recovery Tasks")
    ax.set_ylabel("Time (minutes)")
    ax.set_title("Manual vs Automated Recovery Time")
    ax.set_xticks([i + 0.2 for i in x])
    ax.set_xticklabels(task_names, rotation=45, ha='right')
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    st.pyplot(fig)

    # Optional summary
    total_manual = sum(manual_times)
    total_auto = sum(automated_times)
    saved = total_manual - total_auto
    cost_saved = saved / 60 * 50  # €50/hour

    st.markdown(f"**Total Manual Time:** {total_manual} minutes")
    st.markdown(f"**Total Automated Time:** {total_auto} minutes")
    st.markdown(f"**Time Saved:** {saved} minutes")
    st.markdown(f"**Estimated Cost Savings:** €{cost_saved:.2f}")
