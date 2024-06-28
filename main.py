import numpy as np 
import pandas as pd 
import streamlit as st 

import helper_function



df = pd.read_csv('drug200.csv')


#--------------------------------------------------------------
def color_specific_cell(row, target_column):
    color = 'background-color: green' if row[target_column] == 'F' else 'background-color: red'
    return [color if col == target_column else '' for col in row.index]


# df_sex_styled = df.style.apply(color_specific_cell, axis=1, target_column='Sex' )


#--------------------------------------------------------------

#---------------------
#streamlit 

st.set_page_config(layout='wide')
st.title("Decision Tree")
st.write('By : Hawar Dzaee')


#--------------------------------------
#root
st.markdown("""
<style>
.centered-table {
    display: flex;
    justify-content: center;
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col3: 
    selected_feature = st.radio("Select feature to split on:", ["None","Sex","BP" ],horizontal=True)


with col2:
    if selected_feature == "Sex":
        df_styled = df.style.apply(color_specific_cell, axis=1, target_column='Sex')
    else:
        df_styled = df

    st.dataframe(df_styled)
    st.write(f'Data samples : {len(df)}')
    st.write(dict(df['Drug'].value_counts()))

    st.latex(r"Gini\ impurity = 1 - [(\frac{91}{200})^2 + (\frac{54}{200})^2 + (\frac{23}{200})^2 + (\frac{16}{200})^2 +(\frac{16}{200})^2]")

    gini_impurtiy_root = helper_function.gini_impurity(df['Drug'].value_counts().values)
    st.latex(f'Gini\ impurity = {gini_impurtiy_root:.3f}')

st.write('-----------')

#------------------------------------------------------ # # block one 

if selected_feature == "Sex":
    st.markdown("<h1 style='text-align: center;'>is it F ?</h1>", unsafe_allow_html=True)

    female_true = df[df['Sex'] == 'F']
    female_false = df[df['Sex'] != 'F']



    col1, col2 = st.columns([1,1])


    with col1:
        st.write('True')
        st.dataframe(female_true.style.apply(color_specific_cell, axis=1, target_column='Sex' ))
        st.write(f'Data samples : {len(female_true)}')
        st.write(dict(female_true['Drug'].value_counts()))
        f_t_b_d = list(female_true['Drug'].value_counts()) # f_t_b_d : feamle_true_binning_drugs 

        st.latex(r"\footnotesize{" + fr"Gini\ impurity\ female\ true  = 1 - [(\frac{{{f_t_b_d[0]}}}{{{{{len(female_true)}}}}})^2 + (\frac{{{f_t_b_d[1]}}}{{{{{len(female_true)}}}}})^2 + (\frac{{{f_t_b_d[2]}}}{{{{{len(female_true)}}}}})^2 + (\frac{{{f_t_b_d[3]}}}{{{{{len(female_true)}}}}})^2 +(\frac{{{f_t_b_d[4]}}}{{{{{len(female_true)}}}}})^2]" + "}")


        gini_impurity_female_true = helper_function.gini_impurity(female_true['Drug'].value_counts().values)
        st.latex(f'Gini\ impurity\ female\ true = {gini_impurity_female_true:.3f}')
        


    with col2:
        st.write('False')
        st.dataframe(female_false.style.apply(color_specific_cell, axis=1, target_column='Sex' ))
        st.write(f'Data samples : {len(female_false)}')
        st.write(dict(female_false['Drug'].value_counts()))
        f_f_b_d = list(female_false['Drug'].value_counts()) # f_f_b_d : feamle_true_binning_drugs

        st.latex(r"\footnotesize{" + fr"Gini\ impurity\ female\ false = 1 - [(\frac{{{f_f_b_d[0]}}}{{{{{len(female_false)}}}}})^2 + (\frac{{{f_f_b_d[1]}}}{{{{{len(female_false)}}}}})^2 + (\frac{{{f_f_b_d[2]}}}{{{{{len(female_false)}}}}})^2 + (\frac{{{f_f_b_d[3]}}}{{{{{len(female_false)}}}}})^2 +(\frac{{{f_f_b_d[4]}}}{{{{{len(female_false)}}}}})^2]" + "}")


        gini_impurity_female_false = helper_function.gini_impurity(female_false['Drug'].value_counts().values)
        st.latex(f'Gini\ impurity\ female\ false = {gini_impurity_female_false:.3f}')




    st.write('--------------------------------')

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        latex_formula = r'''
        \text{Gini impurity Sex} = 
        (\frac{%d}{%d} \cdot %.3f) + 
        (\frac{%d}{%d} \cdot %.3f)
        ''' % (len(female_true), len(df), gini_impurity_female_true,
            len(female_false), len(df), gini_impurity_female_false)

        # Display the LaTeX formula
        st.latex(latex_formula)

        gini_impurity_sex = ((len(female_true)/len(df))*gini_impurity_female_true) + ((len(female_false)/len(df))*gini_impurity_female_false)
        st.latex(f'Gini\ impurity\ Sex = {gini_impurity_sex:.3f}') 

#------------------------------------------------------------------------- End of block one 
if selected_feature == "BP":


    BP_high = df[['BP','Drug']][df['BP']=='HIGH']
    BP_not_high = df[['BP','Drug']][df['BP']!='HIGH']

    BP_normal = df[df['BP']=='NORMAL']
    BP_not_normal = df[df['BP']!='NORMAL']

    BP_low = df[df['BP']=='LOW']
    BP_not_low = df[df['BP']!='LOW']
    



    col1, col2 , col3, col4,= st.columns([1,1,1,1])


    with col1:
        st.write('High split')
        st.dataframe(BP_high)
        st.write(f'Data samples : {len(BP_high)}')
        st.write(dict(BP_high['Drug'].value_counts()))
        h_t_b_d = list(BP_high['Drug'].value_counts()) # high true binning drug
        gini_impurity_BP_high = helper_function.gini_impurity(BP_high['Drug'].value_counts().values)
        # st.latex(f'G\ I\ BP\ HIGH = {gini_impurity_BP_high:.3f}')
        st.write(f'Gini Impurity BP HIGH = {gini_impurity_BP_high:.3f}')
        


    with col2:
        st.write('not High split')
        st.dataframe(BP_not_high)
        st.write(f'Data samples : {len(BP_not_high)}')
        st.write(dict(BP_not_high['Drug'].value_counts()))
        h_t_b_d = list(BP_not_high['Drug'].value_counts()) # high true binning drug
        gini_impurity_BP_not_high = helper_function.gini_impurity(BP_not_high['Drug'].value_counts().values)
        st.write(f'Gini Impurity BP HIGH = {gini_impurity_BP_high:.3f}')




    # st.write('--------------------------------')

    # col1, col2, col3 = st.columns([1,2,1])
    # with col2:
    #     latex_formula = r'''
    #     \text{Gini impurity Sex} = 
    #     (\frac{%d}{%d} \cdot %.3f) + 
    #     (\frac{%d}{%d} \cdot %.3f)
    #     ''' % (len(female_true), len(df), gini_impurity_female_true,
    #         len(female_false), len(df), gini_impurity_female_false)

    #     # Display the LaTeX formula
    #     st.latex(latex_formula)

    #     gini_impurity_sex = ((len(female_true)/len(df))*gini_impurity_female_true) + ((len(female_false)/len(df))*gini_impurity_female_false)
    #     st.latex(f'Gini\ impurity\ Sex = {gini_impurity_sex:.3f}') 