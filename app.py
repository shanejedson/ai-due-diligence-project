import streamlit as st

st.set_page_config(page_title="AI Due Diligence Tool")

st.title("💼 AI-Powered Private Equity Due Diligence Tool")
st.markdown("Enter a company name to generate a due diligence-style report.")

company = st.text_input("Company Name", placeholder="e.g., Spotify")

if st.button("Generate Report") and company:
    st.subheader(f"📄 Due Diligence Report: {company}")
    st.markdown(f"""
    **1. Executive Summary**  
    {company} is a leading company in its industry with strong growth potential.  
    However, profitability and risk factors must be considered.

    **2. Financial Snapshot (Sample)**  
    - Revenue: Estimated based on public data  
    - Profitability: To be assessed  
    - Growth: Varies by region

    **3. Market Overview**  
    - Industry trends  
    - Competitor landscape  
    - Positioning

    **4. Risk Factors**  
    - Competitive threats  
    - Market volatility  
    - Regulatory pressure

    **5. Investment Outlook**  
    - Strengths: Brand, scale, reach  
    - Weaknesses: Costs, margins  
    - Verdict: AI suggests further review
    """)


