import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title("🎓 CGPA Calculator: Unlock Your Academic Potential 🚀📈")

# Custom CSS for a professional and clean interface
st.markdown("""
    <style>
        /* General Styles */
        body, html {
            background-color: #f0f8ff;
            color: #333333;
            font-family: 'Arial', sans-serif;
            height: 100%;
            margin: 0;
            padding: 0;
        }

        .main {
            background-color: #f0f8ff;
            color: #333333;
            font-family: 'Arial', sans-serif;
            min-height: 100vh;
        }

        /* Search bar boundary - Dark Red */
        .stTextInput>div>div>input {
            border: 2px solid #8B0000 !important;
            border-radius: 5px;
        }

        /* Styling for the Streamlit button */
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
            padding: 12px;
            margin-top: 10px;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }

        /* Sidebar styling */
        .sidebar {
            background-color: #222222;
            color: white;
            padding: 20px;
        }

        /* Sidebar links */
        .sidebar-links a {
            color: #4CAF50;  /* Green color like buttons */
            font-size: 18px;
            text-decoration: none;
            margin-bottom: 15px;
            display: block;
        }
        .sidebar-links a:hover {
            color: #45a049;  /* Slightly darker green on hover */
        }

        /* Header and text styling */
        .header {
            font-size: 24px;
            color: #4CAF50;
        }
        .subheader {
            font-size: 20px;
            color: #333333;
        }

        /* Footer section */
        .footer {
            font-size: 14px;
            color: #666666;
            text-align: center;
            padding: 20px 0;
        }

        /* Ensure the main content spans full page */
        .css-1l7u300 {
            background-color: #f0f8ff;
        }
    </style>
""", unsafe_allow_html=True)

# Introduction
st.write("""
This app helps you calculate your CGPA based on your semester GPAs. 
You can also visualize your GPA trends and reset inputs for a fresh calculation.
""")

# Sidebar content
st.sidebar.markdown("## 👨‍💻 Connect with Me")
st.sidebar.markdown("""
<div class="sidebar-links">
    <a href="https://github.com/marianadeem755" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="30px"> GitHub
    </a>
    <a href="https://www.kaggle.com/marianadeem755" target="_blank">
        <img src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/189_Kaggle_logo_logos-512.png" width="30px"> Kaggle
    </a>
    <a href="mailto:marianadeem755@gmail.com">
        <img src="https://cdn-icons-png.flaticon.com/512/561/561127.png" width="30px"> Email
    </a>
    <a href="https://huggingface.co/maria355" target="_blank">
        <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" width="30px"> Hugging Face
    </a>
</div>
""", unsafe_allow_html=True)

# Input Section
st.header("Enter Your Semester GPAs")
num_semesters = st.number_input("How many semesters have you completed?", min_value=1, max_value=20, step=1, value=1)

# GPA input fields
gpa_list = []
for i in range(1, num_semesters + 1):
    gpa = st.number_input(f"Enter GPA for Semester {i}:", min_value=0.0, max_value=4.0, step=0.01, value=0.0)
    gpa_list.append(gpa)

# Calculate CGPA
if st.button("Calculate CGPA"):
    if len(gpa_list) > 0:
        cgpa = sum(gpa_list) / len(gpa_list)
        st.success(f"Your CGPA is: {cgpa:.2f}")

        # GPA Summary
        highest_gpa = max(gpa_list)
        lowest_gpa = min(gpa_list)
        average_gpa = sum(gpa_list) / len(gpa_list)

        st.header("Advanced Features")

        st.subheader("GPA Summary")
        st.write(f"Highest GPA: {highest_gpa:.2f}")
        st.write(f"Lowest GPA: {lowest_gpa:.2f}")
        st.write(f"Average GPA: {average_gpa:.2f}")

        # GPA Trend Visualization
        st.subheader("GPA Trend")
        fig, ax = plt.subplots()
        ax.plot(range(1, len(gpa_list) + 1), gpa_list, marker='o', linestyle='-', color='b')
        ax.set_title("GPA Trend Over Semesters")
        ax.set_xlabel("Semester")
        ax.set_ylabel("GPA")
        ax.set_ylim(0, 4.0)
        st.pyplot(fig)

        # Create DataFrame for download
        data = {
            "Semester": [f"Semester {i+1}" for i in range(len(gpa_list))],
            "GPA": gpa_list
        }
        df = pd.DataFrame(data)
        summary_df = pd.DataFrame({
            "Metric": ["CGPA", "Highest GPA", "Lowest GPA", "Average GPA"],
            "Value": [cgpa, highest_gpa, lowest_gpa, average_gpa]
        })

        combined_df = pd.concat([df, pd.DataFrame([["", ""]], columns=["Semester", "GPA"]), summary_df.rename(columns={"Metric": "Semester", "Value": "GPA"})], ignore_index=True)

        csv = combined_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Results as CSV",
            data=csv,
            file_name="cgpa_results.csv",
            mime='text/csv'
        )
    else:
        st.error("Please enter at least one GPA.")

# Reset Button
if st.button("Reset"):
    st.experimental_rerun()

# Footer
st.markdown("""
    <div class="footer">
        <p>© 2025 CGPA Calculator | Made by Maria Nadeem</p>
    </div>
""", unsafe_allow_html=True)
