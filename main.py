import pandas as pd
import streamlit as st

st.set_page_config(
   page_title="Tokyo Marine Insuarance",
   page_icon="Compunnel-Digital-Logo.png",
   layout="wide",
   initial_sidebar_state="expanded",
)

def main():

    col1, col2, col3 = st.columns([1, 6, 1])
    with col1:
        st.sidebar.image(['Compunnel-Digital-Logo.png'], width=125)

    st.sidebar.title('''**Tokio Marine Insurance Analytics**''')
    st.markdown("""<style>[data-testid="stSidebar"][aria-expanded="true"] 
    > div:first-child {width: 450px;}[data-testid="stSidebar"][aria-expanded="false"] 
    > div:first-child {width: 450px;margin-left: -400px;}</style>""",
    unsafe_allow_html=True)

    options= st.sidebar.selectbox('Please Select',['Data','Power BI'])

    if options == 'Power BI':
        st.markdown('<iframe title="Tokio Analytics" width="750" height="1060" src="https://app.powerbi.com/view?r=eyJrIjoiNTAzODQ4NjAtMDljZC00NWUxLTlmYzQtOWZlM2Q5MGQyNTFiIiwidCI6ImE2MTdlYzYwLTBhYjMtNDBiZS05MjhmLWJmMzY1MzA4NDkxYSIsImMiOjF9&pageName=ReportSection" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html = True)

    if options == 'Data':

        File_name = st.selectbox('Select File Name to preview',['AliBaba','Amazon','Apple','BAC','Google','Meta','Nvida','Paypal','Salesforce','Tesla'])
        st.info(File_name)
        df=pd.read_excel(File_name+'.xlsx')
        st.dataframe(df.head())



if __name__ == '__main__':
    main()

