#Task E – Dashboard & Presentation
# 1. Dashboard must contain: summary KPIs, interactive filters, comparison panel.
# importing necessary libraries

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Colour pallete for the page contents
pastel_palette = ["#F7EDE2", "#F4D8CD", "#E8C6D8", "#DABFD3", "#F2D7D9"]
sns.set_palette(pastel_palette) 

# setup of page layout 

st.set_page_config(layout="wide")
st.title(" Fashion Clothing Product Rating Dashboard")
st.write("This dashboard provides insights into customer ratings, recommendations, and feedback for women’s e-commerce clothing.")
st.markdown("Dataset Source: [Kaggle - Women's E-Commerce Clothing Reviews](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews)")


# Reading the dataset from the file in local computer

df = pd.read_csv(r"C:\Users\reewa\Downloads\Womens Clothing E-Commerce Reviews.csv")
df.dropna(subset=["Rating"], inplace=True)  #This ensures all rows do have ratings


# Sidebar Filters where one can select department,ratings,age range

st.sidebar.header(" Filters")
selected_dept = st.sidebar.multiselect(
    "Select Department(s):",
    options=df["Department Name"].dropna().unique(),
    default=[d for d in ["Dresses", "Tops"] if d in df["Department Name"].dropna().unique()]
)

selected_rating = st.sidebar.slider("Select Rating Range:", 1, 5, (1, 5))
selected_age = st.sidebar.slider("Customer Age Range:", int(df["Age"].min()), int(df["Age"].max()), (20, 70))

# Applying filters to the dataset
filtered_df = df[
    (df["Department Name"].isin(selected_dept)) &
    (df["Rating"].between(*selected_rating)) &
    (df["Age"].between(*selected_age))
]


# KPI Summary Part Display quick view

total_reviews = len(filtered_df)
avg_rating = filtered_df["Rating"].mean()
rec_rate = filtered_df["Recommended IND"].mean() * 100

col_kpi1, col_kpi2, col_kpi3 = st.columns(3)
col_kpi1.metric("Total Reviews", f"{total_reviews:,}")
col_kpi2.metric("Average Rating", f"{avg_rating:.2f} ⭐")
col_kpi3.metric("Recommendation Rate", f"{rec_rate:.1f}% 👍")


# Main Charts Taking about 3 Columns that are side by side

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Rating Distribution")
    plt.figure(figsize=(7, 5))
    sns.countplot(x="Rating", data=filtered_df, hue="Rating", palette="pastel", legend=False)
    plt.xlabel("Rating")
    plt.ylabel("Count")
    st.pyplot(plt)
    plt.close()

with col2:
    st.subheader(" Avg Rating by Department")
    dept_avg = filtered_df.groupby("Department Name")["Rating"].mean().sort_values(ascending=False)
    plt.figure(figsize=(7, 5))
    dept_avg.plot(kind="bar", color="#D6C6E8")
    plt.xlabel("Department")
    plt.ylabel("Average Rating")
    st.pyplot(plt)
    plt.close()

with col3:
    st.subheader(" Recommendation %")
    rec_rate_plot = filtered_df["Recommended IND"].value_counts(normalize=True) * 100
    plt.figure(figsize=(6, 6))
    plt.pie(rec_rate_plot, labels=["Recommended", "Not Recommended"], autopct="%1.1f%%", colors=["#F4D8CD", "#DABFD3"])
    st.pyplot(plt)
    plt.close()

#The Age vs Positive Feedback Count Scatter plot
st.header("Age vs Positive Feedback Count")
plt.figure(figsize=(5, 3))  #giving size to able to make it in one screen
sns.scatterplot(x="Age", y="Positive Feedback Count", data=filtered_df,color="#CA9EFC", alpha=0.6)
st.pyplot(plt)
plt.close()


# Comparison Panel comparing product class to average rating
st.header(" Comparison Panel")
available_classes = df["Class Name"].dropna().unique().tolist()
default_classes = [c for c in ["Dresses", "Knits"] if c in available_classes]

selected_classes = st.multiselect(
    "Select Product Classes to Compare:",
    options=available_classes,
    default=default_classes
)

compare_df = df[df["Class Name"].isin(selected_classes)]
avg_compare = compare_df.groupby("Class Name")["Rating"].mean()

plt.figure(figsize=(4, 2))
avg_compare.plot(kind="bar", color="#FCB7CF")
plt.title("Average Rating by Product Class")
plt.xlabel("Product Class")
plt.ylabel("Average Rating")
st.pyplot(plt)
plt.close()

#providing some insights to make user have a simplified understanding of dashboard
st.header("Some Insights from the Rating Visualizations")
st.markdown("""
1. The younger reviwers 20–30 yrs give more extreme ratings as to (1★ or 5★) suggesting younger age groups have a strong brand opinions and expectations..
2. Dresses and Tops department shows higher average ratings that also consistently,showing the customer preferances.
3. The products having a higher recommendation rate by customer are highly likely to have higher feedback counts,meaning such engagements have higher 
            satisfaction to customers.
""")
#showing success comment in case of successful run
st.success(" For different visualizations adjust filters of age range to see review trends.")
    