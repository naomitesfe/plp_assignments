# Streamlit App for CORD-19 Metadata

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Data
@st.cache_data  # cache to avoid reloading every time
def load_data():
    # Change path if your metadata file is in a subfolder
    df = pd.read_csv("unzipped_data/metadata.csv", low_memory=False, encoding="utf-8")
    # Extract year from publish_time (handle errors safely)
    df["year"] = pd.to_datetime(df["publish_time"], errors="coerce").dt.year
    return df

df = load_data()

# App Layout
st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers metadata.")

# Show sample of the data
st.subheader("Sample Data")
st.write(df.head())

# Interactive Widget: Year Range Selector
st.subheader("Filter by Year")
min_year, max_year = int(df["year"].min()), int(df["year"].max())
year_range = st.slider("Select year range", min_year, max_year, (2020, 2021))

# Filter data based on selection
filtered_df = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

st.write(f"Showing {len(filtered_df)} papers between {year_range[0]} and {year_range[1]}")

# Visualization: Publications by Year
st.subheader("Publications by Year")

year_counts = filtered_df["year"].value_counts().sort_index()

fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values, color="skyblue")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Publications")
ax.set_title("Publications by Year")

st.pyplot(fig)

# Dropdown Example: Journal Selection
st.subheader("Filter by Journal")
journal_list = df["journal"].dropna().unique().tolist()
journal_choice = st.selectbox("Select a journal", ["All"] + journal_list)

if journal_choice != "All":
    journal_df = filtered_df[filtered_df["journal"] == journal_choice]
    st.write(f"{len(journal_df)} papers in {journal_choice}")
    st.write(journal_df[["title", "authors", "publish_time"]].head())
else:
    st.write(filtered_df[["title", "authors", "publish_time"]].head())
