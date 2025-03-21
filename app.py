import streamlit as st
import pandas as pd
from PIL import Image




# Set the page configuration
st.set_page_config(page_title="Town Team Sales Report", layout="wide")


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
st.title("Town Team Sales Report")

# Display header image (replace with your actual image file)
header_image = Image.open("Image/44027548_2201662006513500_1850313580889505792_n_98818c77-464e-4c63-84a3-95a7b4730846.webp")
header_image = header_image.resize((600, 400))
st.image(header_image, use_container_width=False)



col1, col2 = st.columns(2)

with col1:
    # Select Language
    lang = st.selectbox("Choose Language For Report", ["English", "Arabic"])

    # Create a sub-row containing two columns for the buttons
    btn_col1, btn_col2 = st.columns(2)

    if lang == "English":
        with open("Report/Report Town Team Sales - EN.pdf", "rb") as file:
            report_data = file.read()
        btn_col1.download_button(
            label="Download Report",
            data=report_data,
            file_name="Report_Town_Team_Sales_EN.pdf",
            mime="application/pdf"
        )
    else:
        with open("Report/Report Town Team Sales - AR.pdf", "rb") as file:
            report_data = file.read()
        btn_col1.download_button(
            label="Download Report",
            data=report_data,
            file_name="Report_Town_Team_Sales_AR.pdf",
            mime="application/pdf"
        )

    if btn_col2.button("Go to Dashboard"):
        st.markdown("<meta http-equiv='refresh' content='0; url=https://github.com/Mohamedmorad2/Town-Team-Sales-Analysis/tree/master/Dashborad'>", unsafe_allow_html=True)

with col2:
    pass


# Load data from Excel and display it
data = pd.read_excel('Data/New_data.xlsx')
st.title('Town Team Sales Data')
st.dataframe(data)

# Section: Analytical Questions for Town Team Sales Data
st.header("Analytical Questions for Town Team Sales Data")

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

# 6. Most Frequent Buyer
st.subheader("6. Most Frequent Buyer")
st.markdown(
    """
    **Which customer made the highest number of purchases?**  
    <div class="answer">
    - <strong>Customer with the highest number of purchases:</strong> C099  <br>
    - <strong>Number of Purchases:</strong> 13
    </div>
    """, unsafe_allow_html=True)

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

# For questions 9 to 19, each image is resized to (700, 400)
def load_and_resize(image_path):
    img = Image.open(image_path)
    return img.resize((700, 400))

# 9. Relationship Between Unit Price and Quantity Sold
st.subheader("9. Relationship Between Unit Price and Quantity Sold")
st.markdown(
    """
    <div class="answer">
    There is no relationship between the unit price and quantity sold.
    </div>
    """, unsafe_allow_html=True)
st.image(load_and_resize("Image/9.png"), caption="9. Analysis", use_container_width=False)

# 10. Sales Distribution by Region
st.subheader("10. Sales Distribution by Region")
st.markdown("**What is the total sales for each region?**")
st.table({
    "Region": ["Mansoura", "Alex", "Tanta", "Madinaty", "New Cairo", "Nasr City"],
    "Total Sales (EGP)": [64890.15, 63305.60, 62583.19, 49515.69, 8845.99, 5549.57]
})
st.image(load_and_resize("Image/10.png"), caption="10. Analysis", use_container_width=False)

# 11. Seasonal Trends
st.subheader("11. Seasonal Trends")
st.markdown(
    """
    **Are there any seasonal trends in the sales?**  
    <div class="answer">
    Yes, there is an increase in sales in May and November.  
    This is because May marks the beginning of summer—resulting in higher demand for clothing—and November signals the beginning of winter.
    </div>
    """, unsafe_allow_html=True)
st.image(load_and_resize("Image/11.png"), caption="11. Analysis", use_container_width=False)

# 12. Percentage Contribution by Category
st.subheader("12. Percentage Contribution by Category")
st.markdown("**What is the percentage contribution of sales by each category?**")
st.table({
    "Category": ["Women’s Wear", "Kids’ Wear", "Men’s Wear", "Accessories"],
    "Percentage": ["27.7%", "27.5%", "24.1%", "20.5%"]
})
st.image(load_and_resize("Image/12.png"), caption="12. Analysis", use_container_width=False)

# 13. Average Order Value
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
st.image(load_and_resize("Image/13.png"), caption="13. Analysis", use_container_width=False)

# 14. Total Quantity Sold per Product
st.subheader("14. Total Quantity Sold per Product")
st.markdown("**What is the total quantity sold for each product?**")
st.table({
    "Product Name": ["Polo Shirt", "Scarf", "Jeans", "Socks", "Belt", "Gloves", "Jacket", "Hat", "Dress", "Sweater", "Shorts", "Watch", "Shoes", "Boots", "Sandals", "Skirt", "Blazer", "T-Shirt"],
    "Quantity": [290, 290, 245, 206, 190, 173, 151, 120, 105, 103, 102, 98, 93, 77, 67, 61, 56, 42]
})
st.image(load_and_resize("Image/14.png"), caption="14. Analysis", use_container_width=False)

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
st.image(load_and_resize("Image/15.png"), caption="15. Analysis", use_container_width=False)

# 16. Quarterly Sales Change
st.subheader("16. Quarterly Sales Change")
st.markdown(
    """
    <div class="answer">
    There is a significant increase in sales in the third and fourth quarters compared to the first and second quarters.
    </div>
    """, unsafe_allow_html=True)
st.image(load_and_resize("Image/16.png"), caption="16. Analysis", use_container_width=False)

# 17. Relationship Between Region and Best-Selling Category
st.subheader("17. Relationship Between Region and Best-Selling Category")
st.markdown(
    """
    <div class="answer">
    Yes, there is a relationship; consumer preferences vary from one region to another.
    </div>
    """, unsafe_allow_html=True)
st.image(load_and_resize("Image/17.png"), caption="17. Analysis", use_container_width=False)

# 18. Repeat vs. New Customers
st.subheader("18. Repeat vs. New Customers")
st.markdown(
    """
    **What is the percentage of sales coming from repeat customers versus new customers?**  
    <div class="answer">
    - <strong>New Customers:</strong> 0.74%  <br>
    - <strong>Returning Customers:</strong> 99.2%
    </div>
    """, unsafe_allow_html=True)
st.image(load_and_resize("Image/18.png"), caption="18. Analysis", use_container_width=False)

# 19. Recommendations for Improvement
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

