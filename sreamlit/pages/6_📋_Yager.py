import streamlit as st
import pandas as pd

# Ανάπτυξη διαδικτυακού συστήματος υποστήριξης ομαδικών αποφάσεων με χρήση του αλγόριθμου Yager
# Ιωάννης Κοτσιφάκης 02/2024
# ikotsifakis@tuc.gr
#6_📋_Yager-steps

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

[class="styles_terminalButton__JBj5T"] {{
visibility: hidden;
}}

</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.markdown('# Αλγόριθμος Yager')
st.markdown('O αλγόριθμος έχει ως εξής:')
st.markdown('1. Θέτουμε το σύνολο των πιθανών λύσεων S = X')
st.markdown('2. Θέτουμε μια λίστα P=∅ Αρχικοποιούμε τη συνάρτηση προτιμήσεων P ως κενό σύνολο. Σε αυτήν θα περιλαμβάνονται οι συγχωνευμένες συναρτήσεις προτίμησης')
st.markdown('3. Θέτουμε: k=1; i=n και j=n')
st.markdown('4. Βρίσκουμε τον u αποφασίζοντα τέτοιο ώστε L(k) = Du(Βρίσκουμε ποιος αποφασίζων βρίσκεται στην 1η θέση της λίστας L. Δηλαδή ξεκινάμε από τον πιο ισχυρό αποφασίζοντα)')
st.markdown('5. Ανακτούμε την Pu(Για τον u αποφασίζοντα βρίσκουμε την εναλλακτική που βρίσκεται στην I θέση της λίστας προτιμήσεων του u. Ξεκινάμε με τη λιγότερο προτιμητέα εναλλακτική του ισχυρότερου αποφασίζοντα)')
st.markdown('6. Εάν Pu(i) ∄ S τότε πήγαινε στο βήμα 9 (Ελέγχει αν το όνομα της εναλλακτικής υπάρχει ή την έχουμε τοποθετήσει ήδη)')
st.markdown('7. Εάν Pu(i) ∈ S τότε')
st.markdown('$~~~~~~~~$(i) θέτουμε P(j) = Pu(i) (Τοποθετεί την Pu(i) στην θέση j της λίστας P, ξεκινώντας από τη λιγότερο προτιμώμενη την οποία τοποθετεί στο τέλος')
st.markdown('$~~~~~~~~$(ii) j = j -1')
st.markdown('$~~~~~~~~$(iii) Διαγράφουμε την Pu(i) από την S.')
st.markdown('8. Εάν j = 0 τότε ΤΕΛΟΣ')
st.markdown('9. Εάν k ≠ m τότε θέτουμε k = k + 1 (ελέγχει τον αριθμό των αποφασιζόντων)Εάν k = m τότε θέτουμε k = 1 και i = i – 1 (Ο τελευταίος αποφασίζων)')
st.markdown('10. Επιστρέφουμε στο βήμα 4')

