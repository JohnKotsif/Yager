import streamlit as st
import pandas as pd

# Ανάπτυξη διαδικτυακού συστήματος υποστήριξης ομαδικών αποφάσεων με χρήση του αλγόριθμου Yager
# Ιωάννης Κοτσιφάκης 02/2024
# ikotsifakis@tuc.gr
#1_📨_Info


st.set_page_config(page_title='Yager Algorithm',page_icon=':books:')

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

st.image('https://github.com/JohnKotsif/Yager/blob/main/sreamlit/Εικόνες/logo.jpg?raw=true')


st.markdown('# ΔΠΜΣ')
st.markdown('## Επιχειρησιακή Έρευνα και Λήψη Αποφάσεων')

st.write('Αυτη η ιστοσελίδα δημιουργήθηκε στα πλαίσια μεταπτυχιακής διπλωματικής με θέμα :')
st.markdown('**Ανάπτυξη διαδικτυακού συστήματος υποστήριξης ομαδικών αποφάσεων με χρήση του αλγόριθμου Yager**')

st.markdown('')
st.write('Μεταπτυχιακός Φοιτητής: Κοτσιφάκης Ιωάννης')
st.markdown('Email: ikotsifakis@tuc.gr')
st.write('Ημερομηνία: Φεβρουάριος 2024')
st.write('Επιβλέπων: Καθηγητής Ματσατσίνης Νικόλαος')
