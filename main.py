import numpy as np 
import pandas as pd 

import streamlit as st 


df = pd.read_csv('drug200.csv')

#---------------------
#streamlit 

st.set_page_config(layout='wide')
st.title("Decision Tree: Creating a Stump")
st.write('By : Hawar Dzaee')


#--------------------------------------
#root
# Custom CSS to center the table
st.markdown("""
<style>
.centered-table {
    display: flex;
    justify-content: center;
}
</style>
""", unsafe_allow_html=True)

# Create three columns
col1, col2, col3 = st.columns([1,2,1])

# Use the middle column to display the table
with col2:
    # st.markdown('<div class="centered-table">', unsafe_allow_html=True)
    st.dataframe(df)
    # st.markdown('</div>', unsafe_allow_html=True)
    st.write(f'Data samples : {len(df)}')
    st.write(dict(df['Drug'].value_counts()))
    st.latex(r"Gini\ impurity = 1 - [(\frac{91}{200})^2 + (\frac{54}{200})^2 + (\frac{23}{200})^2 + (\frac{16}{200})^2 +(\frac{16}{200})^2]")

st.write('-----------')

#------------------------------------------------------
# # block one 

st.markdown("<h1 style='text-align: center;'>is it F ?</h1>", unsafe_allow_html=True)

female_true = df[df['Sex'] == 'F']
female_false = df[df['Sex'] != 'F']

col1, col2 = st.columns([1,1])


with col1:
    st.write('True')
    st.dataframe(female_true)
    st.write(f'Data samples : {len(female_true)}')
    st.write(dict(female_true['Drug'].value_counts()))
    f_t_b_d = list(female_true['Drug'].value_counts()) # f_t_b_d : feamle_true_binning_drugs 
    st.latex(r"\footnotesize{" + fr"Gini\ impurity = 1 - [(\frac{{{f_t_b_d[0]}}}{{{200}}})^2 + (\frac{{{f_t_b_d[1]}}}{{{200}}})^2 + (\frac{{{f_t_b_d[2]}}}{{{200}}})^2 + (\frac{{{f_t_b_d[3]}}}{{{200}}})^2 +(\frac{{{f_t_b_d[4]}}}{{{200}}})^2]"+ "}")


with col2:
    st.write('False')
    st.dataframe(female_false)
    st.write(f'Data samples : {len(female_false)}')
    st.write(dict(female_false['Drug'].value_counts()))
    f_f_b_d = list(female_false['Drug'].value_counts()) # f_f_b_d : feamle_true_binning_drugs
    st.latex(r"\footnotesize{" + fr"Gini\ impurity = 1 - [(\frac{{{f_f_b_d[0]}}}{{{200}}})^2 + (\frac{{{f_f_b_d[1]}}}{{{200}}})^2 + (\frac{{{f_f_b_d[2]}}}{{{200}}})^2 + (\frac{{{f_f_b_d[3]}}}{{{200}}})^2 +(\frac{{{f_f_b_d[4]}}}{{{200}}})^2]"+ "}")
