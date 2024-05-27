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

st.markdown('# Αλγόριθμος Yager - Θεωρία')

with st.expander("Βήματα αλγορίθμου"): 
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
  
    
with st.expander("1. Απλός αλγόριθμος Yager"):  
  st.markdown('Ο αλγόριθμος ξεκινάει με τη λιγότερο προτιμώμενη λύση, σύμφωνα με την πιο σημαντική συνάρτηση προτίμησης (σημαντικότερος αποφασίζων) και την τοποθετεί στο τέλος της συνάρτησης προτίμησης P. Στη συνέχεια, μεταβαίνει στη δεύτερη πιο σημαντική συνάρτηση προτίμησης (επόμενος πιο σημαντικός αποφασίζων). ')
  st.image('https://github.com/JohnKotsif/Yager/blob/main/sreamlit/Εικόνες/Εικόνα1.png?raw=true')  
  st.markdown('Εάν το λιγότερο προτιμώμενο στοιχείο του σημαντικότερου αποφασίζων δεν έχει ήδη τοποθετηθεί στην λίστα Ρ, τότε το τοποθετεί στην επόμενη χαμηλότερη θέση (στην κορυφή της τρέχουσας P), εάν όμως έχει ήδη τοποθετηθεί στην Ρ τότε παραλείπει αυτή τη συνάρτηση προτίμησης και μεταβαίνει στην επόμενη πιο σημαντική συνάρτηση προτίμησης.')
  st.markdown('Συνεχίζει με αυτόν τον τρόπο για όλες τις συναρτήσεις προτίμησης, κάνοντας περάσματα και μετακινώντας τις συναρτήσεις προτίμησης. Ο αλγόριθμος αυτός σταματά, όταν τελικά όλα τα στοιχεία τοποθετούνται στην λίστα Ρ, δηλαδή όταν η λίστα S δεν έχει άλλα στοιχεία.')  
  st.image('https://github.com/JohnKotsif/Yager/blob/main/sreamlit/Εικόνες/Εικόνα2.png?raw=true') 

  
with st.expander(" 2. Yager algorithm που περιλαμβάνει συνδυασμό ασθενών διατάξεων μεταξύ επιλογών"):  
  st.markdown('Ο Αλγόριθμος του Yager που περιλαμβάνει συνδυασμό ασθενών διατάξεων μεταξύ επιλογών (Fusing weak orderings) είναι μια εξέλιξη του απλού αλγόριθμου του Yager. Σε αυτή την περίπτωση, δύο οι περισσότερες επιλογές μπορεί να έχουν το ίδιο βάρος – χρησιμότητα για έναν πράκτορα – αποφασίζοντα. Αυτό σημαίνει ότι για τον συγκεκριμένο πράκτορα οι επιλογές αυτές δεν διαφέρουν μεταξύ τους.')
  st.image('https://github.com/JohnKotsif/Yager/blob/main/sreamlit/Εικόνες/Εικόνα3.png?raw=true')
  st.markdown('Στην παραπάνω εικόνα διακρίνεται ότι ο πράκτορας P1 έχει κατατάξει την επιλογή a και b στην 6η θέση. Ο πράκτορας P3 έχει κατατάξει την επιλογή f και e στην 1η θέση και ο πράκτορας P4 έχει κατατάξει την επιλογή a και b στην 5η θέση. Κατά την υλοποίηση του αλγορίθμου, τα βήματα ακολουθούνται κανονικά όπως τον απλό αλγόριθμο του Yager. Η διαφοροποίηση είναι ότι στην λίστα κοινής διάταξης προτίμησης οι επιλογές που έχουν ασθενή διάταξη μεταξύ τους, τοποθετούνται στην ίδια θέση κατάταξης. Κατά την επανάληψη 1 στην παρακάτω εικόνα του παραδείγματος, τα στοιχεία a και b τοποθετούνται μαζί στην ίδια θέση της λίστας κοινής διάταξης προτίμησης.')
  st.image('https://github.com/JohnKotsif/Yager/blob/main/sreamlit/Εικόνες/Εικόνα4.png?raw=true')
  st.markdown('Επιπρόσθετα, στην επανάληψη 8 τα στοιχεία d και e τοποθετούνται στην λίστα κοινής διάταξης προτίμησης μαζί. Η διαδικασία συνεχίζεται κανονικά έως ότου η λίστα S δεν έχει άλλα στοιχεία')
  st.image('https://github.com/JohnKotsif/Yager/blob/main/sreamlit/Εικόνες/Εικόνα5.png?raw=true')

  

with st.expander(" 3. Yager algorithm που περιλαμβάνει συνδυασμό ασθενών διατάξεων μεταξύ πρακτόρων(Περιλαμβάνει input checks)"):
  st.markdown('Ο Αλγόριθμος του Yager που περιλαμβάνει συνδυασμό ασθενών διατάξεων μεταξύ πρακτόρων είναι ακόμα μια αναβάθμιση του απλού αλγόριθμου του Yager. Σε αυτή την περίπτωση, δύο οι περισσότεροι πράκτορες έχουν την ίδια σημαντικότητα (rank). Οι επιλογές των αποφασιζόντων – πρακτόρων αυτών τοποθετούνται στην ίδια θέση στην λίστα κοινής διάταξης προτίμησης. ')
  st.image('https://github.com/JohnKotsif/Yager/blob/main/sreamlit/Εικόνες/Εικόνα6.png?raw=true')
  st.markdown('Στις εικόνες του παραδείγματος ο πράκτορας P1 και ο πράκτορας P2 έχουν ασθενή διάταξη μεταξύ τους και για αυτό το λόγο οι επιλογές τους έχουν το ίδιο βάρος για την λήψη της ομαδικής απόφασης. Στην επανάληψη 1 ο P1 έχει επιλέξει το στοιχείο b για την τελευταία του επιλογή ενώ ο P2 το στοιχείο a. Τα δύο στοιχεία τοποθετούνται στην λίστα κοινής διάταξης προτίμησης P μαζί.')
  st.image('https://github.com/JohnKotsif/Yager/blob/main/sreamlit/Εικόνες/Εικόνα7.png?raw=true')
  st.markdown('Κατά τις επαναλήψεις του παραδείγματος οι αποφασίζοντες P1 και P2 τοποθετούνται στην ίδια γραμμή μαζί με τα στοιχεία που επέλεξαν. Τα βήματα συνεχίζονται και το τελικό αποτέλεσμα είναι P = f,e,c,d,[b,a]')
  st.image('https://github.com/JohnKotsif/Yager/blob/main/sreamlit/Εικόνες/Εικόνα8.png?raw=true')

  

with st.expander(" 4. Yager algorithm που περιλαμβάνει συνδυασμό ασθενών διατάξεων μεταξύ επιλογών και πρακτόρων (Fusing weak orderings)"):
  st.markdown('Ο Αλγόριθμος του Yager που περιλαμβάνει συνδυασμό ασθενών διατάξεων μεταξύ πρακτόρων και επιλογών είναι ο συνδυασμός των δύο προηγούμενων περιπτώσεων. Σε αυτή την περίπτωση, δύο οι περισσότεροι πράκτορες έχουν την ίδια σημαντικότητα (rank) καθώς και δύο οι περισσότερες επιλογές μπορεί να έχουν το ίδιο βάρος – χρησιμότητα για έναν ή περισσότερους πράκτορες – αποφασίζοντες.')
  st.image('https://github.com/JohnKotsif/Yager/blob/main/sreamlit/Εικόνες/Εικόνα9.png?raw=true')
  st.markdown('Στο παράδειγμα, οι αποφασίζοντες P2 και P3 έχουν ασθενή διάταξη μεταξύ τους. Επίσης, οι επιλογές b-c-d και e-a του P1, οι επιλογές b-e και c-d του P2 καθώς και οι επιλογές c-d και b-a του P4 έχουν το ίδιο βάρος – χρησιμότητα για τους παραπάνω πράκτορες.')
  st.image('https://github.com/JohnKotsif/Yager/blob/main/sreamlit/Εικόνες/Εικόνα10.png?raw=true')
  st.markdown('Κατά την επανάληψη 2 του παραδείγματος, ο αποφασίζων P2 έχει επιλέξει τα στοιχεία c-d ενώ ο αποφασίζων P3 έχει επιλέξει το στοιχείο e. Τα στοιχεία τοποθετούνται στην τελική λίστα κοινής διάταξης προτίμησης P μαζί, ενώ η διαδικασία συνεχίζεται κανονικά μέχρι το τέλος των επαναλήψεων')
  st.image('https://github.com/JohnKotsif/Yager/blob/main/sreamlit/Εικόνες/Εικόνα11.png?raw=true')

