import streamlit as st
import pandas as pd

# Ανάπτυξη διαδικτυακού συστήματος υποστήριξης ομαδικών αποφάσεων με χρήση του αλγόριθμου Yager
# Ιωάννης Κοτσιφάκης 02/2024
# ikotsifakis@tuc.gr
#5_🈹_Examples.py

st.runtime.legacy_caching.clear_cache()
st.set_page_config(page_title='Yager Algorithm',page_icon=':books:')
st.title(':balloon: Examples')

# Backround και css
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://img.freepik.com/free-vector/elegant-white-background-with-shiny-lines_1017-17580.jpg?w=1380&t=st=1708010802~exp=1708011402~hmac=ccf513f49d0c22903053a9c9115a44659220a4750bfde6209725f83263d1b13f");
background-size: 200%;
background-position: top left;
background-repeat: yes-repeat;
background-attachment: local;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image: url("https://img.freepik.com/free-vector/smooth-white-wave-background_52683-55288.jpg?w=1380&t=st=1708011236~exp=1708011836~hmac=a10050b2ccdc394ce67b34ee4751e598657c9c0c1bd0e4b7d9ed90046058fbd0");
background-position: top; 
background-repeat: yes-repeat;
background-size: 120%;
background-attachment: fixed;
}}

[data-testid="stHeader"] {{
visibility: hidden;
}}

[class="st-emotion-cache-h5rgaw ea3mdgi1"] {{
visibility: hidden;
}}

</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


#url of examples
url1 = 'C:\\Users\\kotsifakis\\Desktop\\sreamlit\\Test Examples\Example1.xlsx'
url2 = 'C:\\Users\\kotsifakis\\Desktop\\sreamlit\\Test Examples\Example1.1.xlsx'
url3 = 'C:\\Users\\kotsifakis\\Desktop\\sreamlit\\Test Examples\Example2.xlsx'
url4 = 'C:\\Users\\kotsifakis\\Desktop\\sreamlit\\Test Examples\Example3.xlsx'
url5 = 'C:\\Users\\kotsifakis\\Desktop\\sreamlit\\Test Examples\Example3.1.xlsx'
url6 = 'C:\\Users\\kotsifakis\\Desktop\\sreamlit\\Test Examples\Example4.xlsx'

#url of results
url7 = 'C:\\Users\\kotsifakis\\Desktop\\sreamlit\\Test Results\ExampleResult1.csv'
url8 = 'C:\\Users\\kotsifakis\\Desktop\\sreamlit\\Test Results\\ExampleResult1.1.csv'
url9 = 'C:\\Users\\kotsifakis\\Desktop\\sreamlit\\Test Results\\ExampleResult2.csv'
url10 = 'C:\\Users\\kotsifakis\\Desktop\\sreamlit\\Test Results\\ExampleResult3.csv'
url11 = 'C:\\Users\\kotsifakis\\Desktop\\sreamlit\\Test Results\\ExampleResult3.1.csv'
url12 = 'C:\\Users\\kotsifakis\\Desktop\\sreamlit\\Test Results\\ExampleResult4.csv'

# header 2 τιτλος 1. Απλός αργόριθμος Yager(Περιλαμβάνει input checks)
st.markdown('## 1. Απλός αργόριθμος Yager(Περιλαμβάνει input checks)')
with st.expander("1. Απλός αργόριθμος Yager"):   
    st.write('Στο πεδίο εναλλακτικές επιλογές τοποθετούνται όλες οι ενναλακτικές επιλογές') 
    st.write('Προσοχή: Η σημαντικότητα των αποφασιζόντων πρέπει πάντα να είναι σε αύξουσα σειρά') 

    Dp1 = pd.read_excel(url4)
    st.write(Dp1)

    c1 , c2 = st.columns(2)
    with c1:
        with open(url1,'rb') as f:
            st.download_button(label=':floppy_disk: Download Example1',
                       data=f,
                       mime='xlsx',
                       key='1',
                       file_name='Example1.xlsx')
    with c2:    
        with open(url7,'rb') as f:
            st.download_button(label=':floppy_disk: Download Example1 results',
                       data=f,
                       mime='csv',
                       key='2',
                       file_name='Example1results.csv')
        
    Dp2 = pd.read_excel(url2)
    st.write(Dp2)
    c1 , c2 = st.columns(2)
    with c1:
        with open(url2,'rb') as f:
            st.download_button(label=':floppy_disk: Download Example1.1',
                       data=f,
                       mime='xlsx',
                       key='3',
                       file_name='Example1.1.xlsx')
    with c2:    
        with open(url8,'rb') as f:
            st.download_button(label=':floppy_disk: Download Example1.1 results',
                       data=f,
                       mime='csv',
                       key='4',
                       file_name='Example1.1results.csv')

# header 2 τιτλος 2. Yager algorithm που περιλαμβάνει συνδυασμό ασθενών διατάξεων μεταξύ επιλογών (Fusing weak orderings) )
st.markdown('## 2. Yager algorithm που περιλαμβάνει συνδυασμό ασθενών διατάξεων μεταξύ επιλογών (Fusing weak orderings) ')
with st.expander(" 2. Yager algorithm που περιλαμβάνει συνδυασμό ασθενών διατάξεων μεταξύ επιλογών"):
    st.write('Σε αυτή την περίπτωση ο αποφασίζων μπορεί να έχει περισσότερες απο μία επιλογές στην ίδια διάταξη') 
    st.write('Για αυτή την υλοποίηση ο χρήστης τοποθετεί τον ίδιο αποφασίζοντα σε όσες στήλες χρειαστεί') 
    st.write('Πρέπει να προστεθεί τελεία (.) και αύξων αριθμός σε κάθε επιπλέον όνομα') 
    st.write('Πρέπει να προστεθεί το σύμβολο (-) στην σημαντικότητα του αποφασίζοντα μετά απο την πρώτη στήλη') 

    Dp3 = pd.read_excel(url3)
    st.write(Dp3)
    c1 , c2 = st.columns(2)
    with c1:
        with open(url3,'rb') as f:
            st.download_button(label=':floppy_disk: Download Example2',
                       data=f,
                       mime='xlsx',
                       key='5',
                       file_name='Example2.xlsx')
    with c2:    
        with open(url9,'rb') as f:
            st.download_button(label=':floppy_disk: Download Example2 results',
                       data=f,
                       mime='csv',
                       key='6',
                       file_name='Example2results.csv')


# header 2 3. Yager algorithm που περιλαμβάνει συνδυασμό ασθενών διατάξεων μεταξύ πρακτόρων (Περιλαμβάνει input checks)
st.markdown('## 3. Yager algorithm που περιλαμβάνει συνδυασμό ασθενών διατάξεων μεταξύ πρακτόρων(Περιλαμβάνει input checks)')
with st.expander(" 3. Yager algorithm που περιλαμβάνει συνδυασμό ασθενών διατάξεων μεταξύ πρακτόρων(Περιλαμβάνει input checks)"):
    st.write('Σε αυτή την περίπτωση οι πράκτορες ίσως έχουν ίδια σημαντικότητα μεταξύ τους') 
    st.write('Για αυτή την υλοποίηση ο χρήστης τοποθετεί τον ίδιο αριθμό για τους ίδιους πράκτορες στο πεδίο "Σημαντικότητα πρακτόρων" ') 

    Dp4 = pd.read_excel(url4)
    st.write(Dp4)
    c1 , c2 = st.columns(2)
    with c1:
        with open(url4,'rb') as f:
            st.download_button(label=':floppy_disk: Download Example3',
                       data=f,
                       mime='xlsx',
                       key='7',
                       file_name='Example3.xlsx')
    with c2:    
        with open(url10,'rb') as f:
            st.download_button(label=':floppy_disk: Download Example3 results',
                       data=f,
                       mime='csv',
                       key='8',
                       file_name='Example3results.csv')

    Dp5 = pd.read_excel(url5)
    st.write(Dp5)
    c1 , c2 = st.columns(2)
    with c1:
        with open(url5,'rb') as f:
           st.download_button(label=':floppy_disk: Download Example3.1',
                       data=f,
                       mime='xlsx',
                       key='9',
                       file_name='Example3.1.xlsx')
    with c2:    
        with open(url11,'rb') as f:
            st.download_button(label=':floppy_disk: Download Example3.1 results',
                       data=f,
                       mime='csv',
                       key='10',
                       file_name='Example3.1results.csv')
        

# header 2 4. Yager algorithm που περιλαμβάνει συνδυασμό ασθενών διατάξεων μεταξύεπιλογών και πρακτόρων (Fusing weak orderings))
st.markdown('## 4. Yager algorithm που περιλαμβάνει συνδυασμό ασθενών διατάξεων μεταξύ επιλογών και πρακτόρων (Fusing weak orderings)')
with st.expander(" 4. Yager algorithm που περιλαμβάνει συνδυασμό ασθενών διατάξεων μεταξύ επιλογών και πρακτόρων (Fusing weak orderings)"):
    st.write('Σε αυτή την περίπτωση οι πράκτορες ίσως έχουν ίδια σημαντικότητα μεταξύ τους και') 
    st.write(' μπορεί να έχουν περισσότερες απο μία επιλογές στην ίδια διάταξη')
    st.write('Πρέπει να προστεθεί τελεία (.) και αύξων αριθμός σε κάθε επιπλέον όνομα') 
    st.write('Πρέπει να προστεθεί το σύμβολο (-) στην σημαντικότητα του αποφασίζοντα μετά απο την πρώτη στήλη') 

    Dp6 = pd.read_excel(url6)
    st.write(Dp6)  
    c1 , c2 = st.columns(2)
    with c1:
        with open(url6,'rb') as f:
            st.download_button(label=':floppy_disk: Download Example4',
                       data=f,
                       mime='xlsx',
                       key='11',
                       file_name='Example4.xlsx')
    with c2:    
        with open(url12,'rb') as f:
            st.download_button(label=':floppy_disk: Download Example4 results',
                       data=f,
                       mime='csv',
                       key='12',
                       file_name='Example4results.csv')

