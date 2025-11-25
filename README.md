# Fashion Product Rating Analysis & Dashboard

# Submitted by:
**Reewani Guruwacharya**  
Data Science Final Project — Nov 2025  
Subject: Data Science With Python


# 1. Project Description
This project analyzes women’s fashion e-commerce reviews from Kaggle to identify trends in customer satisfaction, ratings, and recommendations.  
It includes:
- Data analysis and preprocessing (Jupyter Notebook)
- Machine learning models (OLS Regression, Random Forest Regression)
- Interactive dashboard (Streamlit)



# 2. Dataset
**Source:** [Kaggle – Women’s E-Commerce Clothing Reviews](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews)  
- ~23,000 rows, 10 columns  
- Main six features: `Rating`, `Age`, `Recommended IND`, `Department Name`, `Class Name`, `Positive Feedback Count`



# 3. Dashboard Features
**Summary KPIs** - Displays 
- total reviews, 
- average rating, and 
- recommendation percentage

**Interactive Filters in Sidebar** -Has filters of
- Department selection (like Dresses, Tops)  
- Rating range (1–5 stars)  
- Customer age range filter (18-99 customer age range)

**Charts & Panels:** 
- Rating Distribution (bar chart)  
- Average Rating by Department (bar chart)
- Recommendation Percentage (pie chart)  
- Age vs Positive Feedback (scatter plot)  
- Product Class Comparison (bar chart)

**Insights Section:**
The points summarizes key patterns observed from the various visualizations

# 4. Use guide to run locally
## Install required dependencies
- Make sure python is installed
- Open the terminal directory as the same one where the app file is
- Then install all packages using in terminal :
pip install -r requirements.txt

# 5. Run dashboard
- In same directory terminal run:
streamlit run dashboard.py

# 6. Streamlit launches app and opens in browser automatically
If for some reason does not open the open manually: 
http://localhost:8501