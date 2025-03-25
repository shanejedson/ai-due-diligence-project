import streamlit as st
import yfinance as yf

# Page setup
st.set_page_config(page_title="AI Due Diligence Tool")

st.title("💼 AI-Powered Private Equity Due Diligence Tool")
st.markdown("Enter a company name to generate a due diligence-style report.")

company = st.text_input("Company Name", placeholder="e.g., Nike")

if st.button("Generate Report") and company:
    # Fetch company data using yfinance
    ticker = yf.Ticker(company)
    data = ticker.history(period="1y")
    info = ticker.info

    st.subheader(f"📄 Due Diligence Report: {company}")
    
    st.markdown(f"""
    **1. Executive Summary**  
    {company} is a company in its industry with strong growth potential. However, profitability and risk factors must be considered. Here's a snapshot of the latest financials and market data.

    **2. Financial Snapshot (Sample)**  
    - **Market Cap**: {info['marketCap']:,} USD  
    - **PE Ratio**: {info.get('trailingPE', 'N/A')}
    - **Revenue (TTM)**: {info.get('totalRevenue', 'N/A')}  
    - **Free Cash Flow**: {info.get('freeCashflow', 'N/A')}  
    - **Profit Margin**: {info.get('profitMargins', 'N/A')}  

    **3. Market Overview**  
    - **Industry**: {info.get('sector', 'N/A')}  
    - **Key Competitors**: {info.get('sector', 'N/A')}
    - **Positioning**: {info.get('longBusinessSummary', 'No detailed summary available.')}
    
    **4. Risk Factors**  
    - **Competitive threats**: {info.get('industry', 'N/A')}  
    - **Market volatility**: Current stock performance data available
    - **Regulatory pressure**: {info.get('country', 'N/A')} market risks

    **5. Investment Outlook**  
    - **Strengths**: Brand strength, reach, and innovation  
    - **Weaknesses**: Cost structures, margin pressures  
    - **Verdict**: {company}'s outlook suggests further review, with strong potential for growth.

    **6. Historical Stock Price Data**  
    {company}’s stock has shown the following performance over the past year:
    - **Max Price**: ${data['High'].max():,.2f}
    - **Min Price**: ${data['Low'].min():,.2f}
    - **Average Price**: ${data['Close'].mean():,.2f}
    """)

