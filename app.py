import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go



# Set the page configuration
st.set_page_config(page_title="Egypt’s Premier Fashion Sales Analysis Report", layout="wide", page_icon="📊")

# Custom CSS to center the content, reduce table width, and style answer text
st.markdown(
    """
    <style>
    .reportview-container .main .block-container{
        margin-left: auto;
        margin-right: auto;
        max-width: 900px;
        padding: 1rem 1rem;
    }
    table {
        max-width: 600px;

    }
    .answer {
        color: #0FA3B1;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
        tex
    }
    div[data-baseweb="select"] {
        width: 40% !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the report
st.title("Egypt’s Premier Fashion Sales Analysis 📊")


col1, col2 = st.columns(2)

with col1:
    # Select Language
    lang = st.selectbox("Choose Language For Report", ["English", "Arabic"])

    # Create a sub-row containing two columns for the buttons
    btn_col1, btn_col2 = st.columns(2)

    if lang == "English":
        with open("Report/Report Egypt’s Premier Fashion Sales Analysis -EN.pdf", "rb") as file:
            report_data = file.read()
        btn_col1.download_button(
            label="Download Report",
            data=report_data,
            file_name="Report Egypt’s Premier Fashion Sales Analysis -EN.pdf",
            mime="application/pdf"
        )
    else:
        with open("Report Egypt’s Premier Fashion Sales Analysis - AR.pdf", "rb") as file:
            report_data = file.read()
        btn_col1.download_button(
            label="Download Report",
            data=report_data,
            file_name="Report Egypt’s Premier Fashion Sales Analysis - AR.pdf",
            mime="application/pdf"
        )

    if btn_col2.button("Go to Dashboard"):
        st.markdown("<meta http-equiv='refresh' content='0; url=https://github.com/Mohamedmorad2/Egypt-Premier-Fashion-Sales-Analysis/tree/master/Dashborad'>", unsafe_allow_html=True)

with col2:
    pass


# Load data from Excel and display it
data = pd.read_excel('Data/Egypt Premier Fashion Sales Analysis.xlsx')
st.title('Egypt’s Premier Fashion Retail Analysis')
st.dataframe(data)

# Section: Analytical Questions for Egypt’s Premier Fashion Retail Analysis
st.header("Analytical Questions for Egypt’s Premier Fashion Retail Analysis")

# 1. Best-selling Category
st.subheader("1. Best-selling Category")
st.markdown(
    """
    **Which category is the best-selling in terms of quantity?**  
    <div class="answer">
    - <strong>Best-selling category by vale:</strong> Women’s Wear  <br>
    - <strong>Total Quantity:</strong> 678 
    </div>
    """, unsafe_allow_html=True)

category_quantity = data.groupby('Category')['Quantity'].sum().reset_index()
fig1 = px.bar(category_quantity,
            x='Category',
            y='Quantity',
            color='Quantity',
            title='Sales Quantity by Category',
            labels={'Quantity': 'Total Quantity Sold', 'Category': 'Product Category'},
            color_continuous_scale='Blues')
st.plotly_chart(fig1)

# 2. Highest Revenue Region
st.subheader("2. Highest Revenue Region")
st.markdown(
    """
    **Which region achieved the highest revenue?**  
    <div class="answer">
    - <strong>Region with highest total sales:</strong> Mansoura  <br>
    - <strong>Total Sales:</strong> 64,890.15 EGP
    </div>
    """, unsafe_allow_html=True)

region_revenue = data.groupby('Region')['Total_Sales'].sum().reset_index()
fig2 = px.pie(region_revenue,
            names='Region',
            values='Total_Sales',
            title='Revenue Distribution by Region',
            labels={'Total_Sales': 'Total Revenue (EGP)', 'Region': 'Sales Region'})
st.plotly_chart(fig2)

# 3. Month with Highest Sales
st.subheader("3. Month with Highest Sales")
st.markdown(
    """
    **Which month recorded the highest sales?**  
    <div class="answer">
    - <strong>Best sales month:</strong> November  <br>
    - <strong>Total Sales for this month:</strong> 24,937.34 EGP
    </div>
    """, unsafe_allow_html=True)

data['Month'] = pd.to_datetime(data['Date']).dt.month_name()
monthly_sales = data.groupby('Month')['Total_Sales'].sum().reset_index()
fig3 = px.line(monthly_sales,
            x='Month',
            y='Total_Sales',
            title='Monthly Sales Performance',
            labels={'Total_Sales': 'Total Revenue (EGP)', 'Month': 'Calendar Month'},
            markers=True)
st.plotly_chart(fig3)

# 4. Day with Highest Sales
st.subheader("4. Day with Highest Sales")
st.markdown(
    """
    **Which day recorded the highest sales?**  
    <div class="answer">
    - <strong>Day with highest total sales:</strong> 2024-08-31  <br>
    - <strong>Total Sales:</strong> 2,855.21 EGP
    </div>
    """, unsafe_allow_html=True)

daily_sales = data.groupby('Date')['Total_Sales'].sum().reset_index()
fig4 = px.scatter(daily_sales,
                x='Date',
                y='Total_Sales',
                title='Daily Sales Performance',
                labels={'Total_Sales': 'Daily Revenue (EGP)', 'Date': 'Transaction Date'},
                color='Total_Sales',
                size='Total_Sales')
st.plotly_chart(fig4)

# 5. Top Spending Customer
st.subheader("5. Top Spending Customer")
st.markdown(
    """
    **Which customer spent the most on purchases?**  
    <div class="answer">
    - <strong>Customer with highest total sales:</strong> C190  <br>
    - <strong>Total Amount:</strong> 5,610.98 EGP
    </div>
    """, unsafe_allow_html=True)

customer_spending = data.groupby('Customer_ID')['Total_Sales'].sum().reset_index()
top_customers = customer_spending.nlargest(10, 'Total_Sales')
fig5 = px.bar(top_customers,
            x='Customer_ID',
            y='Total_Sales',
            title='Top 10 Customers by Spending',
            labels={'Total_Sales': 'Total Spending (EGP)', 'Customer_ID': 'Customer ID'},
            color='Total_Sales')
st.plotly_chart(fig5)

# 6. Most Frequent Buyer
st.subheader("6. Most Frequent Buyer")
st.markdown(
    """
    **Which customer made the highest number of purchases?**  
    <div class="answer">
    - <strong>Customer with the highest number of purchases:</strong> C099  , C190<br>
    - <strong>Number of Purchases:</strong> 13
    </div>
    """, unsafe_allow_html=True)

purchase_counts = data['Customer_ID'].value_counts().reset_index()
purchase_counts.columns = ['Customer_ID', 'Purchase_Count']
top_buyers = purchase_counts.nlargest(10, 'Purchase_Count')
fig6 = px.bar(top_buyers,
            x='Customer_ID',
            y='Purchase_Count',
            title='Top 10 Frequent Buyers',
            labels={'Purchase_Count': 'Number of Purchases', 'Customer_ID': 'Customer ID'},
            color='Purchase_Count')
st.plotly_chart(fig6)

# 7. Most Profitable Product
st.subheader("7. Most Profitable Product")
st.markdown(
    """
    **Which product is the most profitable based on total sales?**  
    <div class="answer">
    - <strong>Most profitable product:</strong> Scarf  <br>
    - <strong>Total Sales:</strong> 5,610.98 EGP
    </div>
    """, unsafe_allow_html=True)

product_profit = data.groupby('Product_Name')['Total_Sales'].sum().reset_index()
top_products = product_profit.nlargest(10, 'Total_Sales')
fig7 = px.bar(top_products,
            x='Product_Name',
            y='Total_Sales',
            title='Top 10 Products by Revenue',
            labels={'Total_Sales': 'Total Revenue (EGP)', 'Product_Name': 'Product Name'},
            color='Total_Sales')
st.plotly_chart(fig7)

# 8. Least Profitable Product
st.subheader("8. Least Profitable Product")
st.markdown(
    """
    **Which product is the least profitable based on total sales?**  
    <div class="answer">
    - <strong>Least profitable product:</strong> T-Shirt  <br>
    - <strong>Total Sales:</strong> 73.47 EGP
    </div>
    """, unsafe_allow_html=True)

bottom_products = product_profit.nsmallest(10, 'Total_Sales')
fig8 = px.bar(bottom_products,
            x='Product_Name',
            y='Total_Sales',
            title='Bottom 10 Products by Revenue',
            labels={'Total_Sales': 'Total Revenue (EGP)', 'Product_Name': 'Product Name'},
            color='Total_Sales')
st.plotly_chart(fig8)

# For questions 9 to 19, each image is resized to (700, 400)
def load_and_resize(image_path):
    img = Image.open(image_path)
    return img.resize((700, 400))

# Question 9: Relationship Between Unit Price and Quantity Sold
st.subheader("9. Relationship Between Unit Price and Quantity Sold")
st.markdown(
    """
    <div class="answer">
    There is no relationship between the unit price and quantity sold.
    </div>
    """, unsafe_allow_html=True)

category_counts = data['Category'].value_counts().reset_index()
category_counts.columns = ['Category', 'Count']
fig9 = px.bar(
    category_counts,
    x='Category',
    y='Count',
    title="Number of Orders per Category"
)
st.plotly_chart(fig9)

# Question 10: Regional Sales (Bar Chart)
st.subheader("10. Sales Distribution by Region")
st.markdown("**What is the total sales for each region?**")
st.table({
    "Region": ["Mansoura", "Alex", "Tanta", "Madinaty", "New Cairo", "Nasr City"],
    "Total Sales (EGP)": [64890.15, 63305.60, 62583.19, 49515.69, 8845.99, 5549.57]
})
region_sales = data.groupby("Region")["Total_Sales"].sum().reset_index()
fig10 = px.bar(
    region_sales,
    x="Region",
    y="Total_Sales",
    title="Sales by Region",
    color="Region"
)
st.plotly_chart(fig10)

# Question 11:How were sales distributed among different categories throughout the year?
st.subheader("11. How were sales distributed among different categories throughout the year?")
data['Month'] = pd.to_datetime(data['Date']).dt.month
category_sales = data.groupby(['Month', 'Category'])['Total_Sales'].sum().reset_index()
fig11 = px.line(
    category_sales,
    x='Month',
    y='Total_Sales',
    color='Category',
    title='Monthly Sales Distribution by Category'
)
st.plotly_chart(fig11)


# Question 12: Category Contribution (Pie Chart)
st.subheader("12. Percentage Contribution by Category")
st.markdown("**What is the percentage contribution of sales by each category?**")
st.table({
    "Category": ["Women’s Wear", "Kids’ Wear", "Men’s Wear", "Accessories"],
    "Percentage": ["27.7%", "27.5%", "24.1%", "20.5%"]
})
category_sales = data.groupby("Category")["Total_Sales"].sum().reset_index()
fig12 = px.pie(
    category_sales,
    names="Category",
    values="Total_Sales",
    title="Sales by Category"
)
st.plotly_chart(fig12)

# Question 13: Order Values (Bar Chart)
st.subheader("13. Average Order Value")
st.markdown(
    """
    **What is the average order value (Total Sales)?**  
    <div class="answer">
    - <strong>Minimum Sales:</strong> 10.83  <br>
    - <strong>Average Sales:</strong> 254.69019  <br>
    - <strong>Maximum Sales:</strong> 798.34
    </div>
    """, unsafe_allow_html=True)
sales_stats = data['Total_Sales'].agg(['min', 'mean', 'max']).reset_index()
sales_stats.columns = ['Metric', 'Value']
fig13 = px.bar(
    sales_stats,
    x='Metric',
    y='Value',
    title='Sales Statistics (Min, Mean, Max)',
    color='Metric'
)
st.plotly_chart(fig13)

# 14. Total Quantity Sold per Product
st.subheader("14. Total Quantity Sold per Product")
st.markdown("**What is the total quantity sold for each product?**")
st.table({
    "Product Name": ["Polo Shirt", "Scarf", "Jeans", "Socks", "Belt", "Gloves", "Jacket", "Hat", "Dress", "Sweater", "Shorts", "Watch", "Shoes", "Boots", "Sandals", "Skirt", "Blazer", "T-Shirt"],
    "Quantity": [290, 290, 245, 206, 190, 173, 151, 120, 105, 103, 102, 98, 93, 77, 67, 61, 56, 42]
})
product_quantity = data.groupby("Product_Name")["Quantity"].sum().reset_index()
fig14 = px.bar(
product_quantity,
x="Product_Name",
y="Quantity",
title="Quantity Sold per Product",
labels={"Product_Name": "Product Name", "Quantity": "Quantity Sold"},
color="Quantity",
color_continuous_scale="Blues"
)
st.plotly_chart(fig14)

# 15. Highest Revenue Product
st.subheader("15. Highest Revenue Product")
st.markdown(
    """
    **Which product generated the highest revenue?**  
    <div class="answer">
    - <strong>Best-selling product by value:</strong> Scarf  <br>
    - <strong>Total Sales:</strong> 30,220.11 EGP
    </div>
    """, unsafe_allow_html=True)
product_revenue = data.groupby("Product_Name")["Total_Sales"].sum().reset_index()
top_product = product_revenue.nlargest(1, "Total_Sales")
fig15 = px.bar(
product_revenue,
x="Product_Name",
y="Total_Sales",
title="Revenue by Product",
color="Total_Sales",
color_continuous_scale="Blues"
)
st.plotly_chart(fig15)
st.markdown(f"**Top Revenue Product:** {top_product['Product_Name'].values[0]} ({top_product['Total_Sales'].values[0]:,.2f} EGP")

# Question 16: Quarterly Trends (Line Chart)
st.subheader("16. Quarterly Sales Change")
st.markdown(
    """
    <div class="answer">
    There is a significant increase in sales in the third and fourth quarters compared to the first and second quarters.
    </div>
    """, unsafe_allow_html=True)
data["Quarter"] = pd.to_datetime(data["Date"]).dt.quarter
quarterly_sales = data.groupby("Quarter")["Total_Sales"].sum().reset_index()
fig16 = px.line(
    quarterly_sales,
    x="Quarter",
    y="Total_Sales",
    title="Quarterly Sales Trend"
)
st.plotly_chart(fig16)

# Question 17: Regional Category Sales (Bar Chart)
st.subheader("17. Relationship Between Region and Best-Selling Category")
st.markdown(
    """
    <div class="answer">
    Yes, there is a relationship; consumer preferences vary from one region to another.
    </div>
    """, unsafe_allow_html=True)
region_category = data.groupby(["Region", "Category"])["Total_Sales"].sum().reset_index()
fig17 = px.bar(
    region_category,
    x="Region",
    y="Total_Sales",
    color="Category",
    title="Regional Category Performance"
)
st.plotly_chart(fig17)

# Question 18: New vs. Returning Customers
st.subheader("18. Repeat vs. New Customers")
st.markdown(
    """
    **What is the percentage of sales coming from repeat customers versus new customers?**  
    <div class="answer">
    - <strong>New Customers:</strong> 0.74%  <br>
    - <strong>Returning Customers:</strong> 99.2%
    </div>
    """, unsafe_allow_html=True)
customer_type = data["Customer_ID"].value_counts().reset_index()
customer_type.columns = ["Customer_ID", "Purchase Count"]
customer_type["Type"] = ["Returning" if count > 1 else "New" for count in customer_type["Purchase Count"]]
customer_dist = customer_type["Type"].value_counts().reset_index()
fig18 = px.pie(
customer_dist,
names="Type",
values="count",
title="Ratio of New and Returning Customers",
)
st.plotly_chart(fig18)

# Recommendations
st.subheader("19. Recommendations for Improvement")
st.markdown(
    """
    <div class="answer">
    Based on the trends and patterns extracted from the data, the following recommendations are suggested:<br>
    - <strong>Leverage Strengths:</strong> Focus on the high performance of Women’s Wear, especially in regions with high sales.<br>
    - <strong>Expand Customer Base:</strong> Develop strategies to attract more new customers to balance the overwhelming percentage of repeat buyers.<br>
    - <strong>Seasonal Strategies:</strong> Optimize inventory and promotional activities during peak sales months (May and November).<br>
    - <strong>Reevaluate Underperformers:</strong> Consider revising pricing or marketing strategies for products that are underperforming, such as T-Shirts.
    </div>
    """, unsafe_allow_html=True)

st.divider()
#Note
st.subheader("🔒 Note: Sensitive names and identifiers in the dataset have been anonymized to ensure data privacy.")