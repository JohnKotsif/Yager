import streamlit as st
import pandas as pd
import time

# Ανάπτυξη διαδικτυακού συστήματος υποστήριξης ομαδικών αποφάσεων με χρήση του αλγόριθμου Yager
# Ιωάννης Κοτσιφάκης 02/2024
# ikotsifakis@tuc.gr
#4_📤_Upload

st.set_page_config(page_title='Yager Algorithm',page_icon=':books:')
st.title('📤 Upload your cvs')


# url τών παραδειγμάτων
url1 = 'C:\\Users\\kotsifakis\\Desktop\\sreamlit\\Test Examples\Example1.xlsx'
url4 = 'C:\\Users\\kotsifakis\\Desktop\\sreamlit\\Test Examples\Example3.1.xlsx'

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

with st.expander("Οδηγίες ενότητας 'Upload' "):   
    st.write('Σε αυτό το πεδίο ο χρήστης μπορεί να ανεβάσει το αρχείο του σε μορφή xlsm.') 
    st.write('Παράδειγμα του αρχείου φαίνεται στην δεξια πλευρά της σελίδας ή στο πεδίο "Examples" του sidebar.') 
    st.write('Το σύστημα θα επιλύσει τα δεδομένα με τον αλγόριθμο Yager.') 
    st.write('Θα εμφανιστεί ενα γράφημα με τις επιλογές του κάθε πράκτορα-αποφασίζοντα.')
    st.write('Τα αποτελέσματα της τελικής λίστας κοινής διάταξης προτίμησης παρέχουν την επιλογή αποθήκευσης.')  

a1 , a2 = st.columns(2)

with a2:
    with open(url1,'rb') as f:
        st.download_button(label=':floppy_disk: Download Example 1',
                       data=f,
                       mime='xlsx',
                       key='4',
                       file_name='Example1.xlsx')
        
    with open(url4,'rb') as f:
        st.download_button(label=':floppy_disk: Download Example 3.1',
                       data=f,
                       mime='xlsx',
                       key='5',
                       file_name='Example3.1.xlsx')
with a1:
    uploaded_file = st.file_uploader('📤 Upload your xlsx or cvs',
                                     disabled=  False,
                                     label_visibility='visible',
                                     )
    if uploaded_file is not None:
        st.write("File uploaded:", uploaded_file.name)

# Έλεγχος στα εισαγόμενα δεδομένα
#Το αρχικό Value είναι True, ο χρήστης επιλέγει False όταν δεν χρειάζεται έλεγχος
check = st.toggle('Έλεγχος δεδομένων εισαγωγής', value=True, 
                  help='Δίνει την δυνατότητα να ελεγχθούν τα δεδομένα εισαγωγής σε περίπτωση που κάποιος αποφασίζων δεν έχει τοποθετήσει κάποια εναλλακτική επιλογή')
check2= True  # Αλλάζει αυτόματα όταν δεν μπορεί να γίνει έλεγχος

#Κουμπί για την εκκίνηση του αλγορίθμου
result = st.button('Ready ✅')

# Sleep μέχρι να πατηθεί του κουμπί 'Ready ✅'
while result == False: 
    time.sleep(2)
    
#Export τα δεδομένα απο το excel φύλλο
Dp=pd.read_excel(uploaded_file, usecols= range(2,20))
print(Dp)

#ΠΙΝΑΚΑΣ ΔΕΔΟΜΕΝΩΝ
st.markdown("<p style='text-align: center; border: 6px solid #4CAF50; padding: 10px;'>Πίνακας δεδομένων</p>", unsafe_allow_html=True)
st.table(Dp)

print('Ο Πίνακας των δεδομένων :')
print(Dp)

# Export την πρώτη στήλη (Εναλλακτικές επιλογές)
Dp2 = pd.read_excel(uploaded_file, usecols=("A"), skiprows=1)

# Μετατροπή των δεδομένων σε λίστα
lista = Dp.values.tolist()

# Οι γραμμές και οι στήλες των δεδομένων εισαγωγής
rows , columnss = Dp.shape

# Δημιουργία πίνακα που να περιέχει τα δεδομένα εισαγωγής απο το Dp2
D = ['']
for i in Dp2[Dp2.columns[0]]:
    D.append(i)

# Αφαίρεση κενών στοιχείων του πίνακα απο την αρχική δημιουργία
D.remove('')

# Εκτύπωση σημαντικότητας αποφασιζόντων σε φθίνουσα σειρά
simantikotita = []
apofasizontes = []
for i in range(columnss):
    if int(lista[0][i]) > 0:
        print(lista[0][i],Dp.columns[i])
        simantikotita.append(lista[0][i])
    else:
        simantikotita.append(-lista[0][i])
        check2 = False
    apofasizontes.append(Dp.columns[i])

print('Η σημαντικότητα των αποφασιζόντων ',simantikotita)
print('Οι αποφασίζοντες : ',apofasizontes)
print('Η Λίστα εναλλακτικών επιλογών :',D)

# Έλεγχος ο χρήστης να έχει τοποθετήσει όλα τα δεδομένα εισαγωγής σωστά
def elegxos():
    error1 = False
    for j in range(columnss):
        D2 = D.copy()
        for i in range(rows-2):
            if (lista[i+2][j] in D2):
                D2.remove(lista[i+2][j])
                continue
            else:
                error1 = True
                st.error(f'Δεν υπάρχουν όλες οι εναλλακτικές στα δεδομένα του:  {Dp.columns[j]}', icon="🚨")

    # Έλεγχος να μην υπάρχει το ίδιο δεδομένο 2 φορές στην ίδια στήλη
    error2 = False
    for i in range(columnss):
        D1 = D.copy()
        for j in range(rows-2):
            if (lista[j+2][i] in D1) and lista[j+2][i] in D:
                D1.remove(lista[j+2][i])
                continue
            else: 
                if lista[j+2][i] in D:
                   error2 = True
                   st.error(f'Υπάρχει παραπάνω απο 1 φόρα μια εναλλακτική στα δεδομένα του: {Dp.columns[i]}', icon="🚨")

    return error1,error2

# 'Εναρξη διαδικασίας ελέγχου αν ο χρήστης έχει επιλέξει check = True
if check == True and check2== True:
    print('Θα πραγματοποιηθεί έλεγχος στα δεδομένα εισαγωγής')
    error1,error2 = elegxos()
    if error1 == False and error2 == False:
        st.success('Ο έλεγχος των εισαγόμενων δεδομένων ήταν επιτυχής', icon="✅")
else:
    print('Δεν πραγματοποιήθηκε έλεγχος των εισαγόμενων δεδομένων')

# Chartframe που δείχνει τις επιλογές κάθε χρήστη
def ChartFrame():
    L = pd.DataFrame(
      {
       'Επιλογές' : D,
      })

    for i in range(len(apofasizontes)):
        EMPTY =[]
        EMPTY2 =[]
        for j in range(rows):
            EMPTY2.append(lista[j][i])
        print(EMPTY2)
        for j in range(rows-1):
            EMPTY.append(EMPTY2.index(D[j]))
        L[apofasizontes[i]] = EMPTY
    return L

# Chart
if check2 == True:
    A =  ChartFrame()
    st.bar_chart(
       A, x="Επιλογές",  # Optional
       )
else:
    print('Chart not available')


# Δημιουργία λίστας κοινής διάταξης προτίμησης
Diataksi = []

proigoumeni_simantikotita = simantikotita[0]

# Τοποθέτηση των δεδομένων στην λίστα
for i in range(rows-1,0,-1):
    Diataksi.append([])
    for j in range(columnss):
            if (lista[i][j] in D):
                if simantikotita[j] == proigoumeni_simantikotita:
                  Diataksi[-1].append(lista[i][j])
                else:
                  if [] in Diataksi:
                    Diataksi.remove([])
                  Diataksi.append([])
                  Diataksi[-1].append(lista[i][j])
                  proigoumeni_simantikotita = simantikotita[j]
                D.remove(lista[i][j])
                
# Η επανάληψη σταματάει όταν αδειάσει το D (λίστα S)         
            if len(D)== 0 :
                break        
    if len(D)== 0 :
        break

# Αφαίρεση τυχών κενών στοιχείων
    if [] in Diataksi:
       Diataksi.remove([])

# Reverse την λίστα
Diataksi.reverse()

# ΑΠΟΤΕΛΕΣΜΑΤΑ
st.markdown("<p style='text-align: center; border: 5px solid #4CAF50; padding: 10px;'>Αποτελέσματα</p>", unsafe_allow_html=True)

print('Η Λίστα κοινής διάταξης προτίμισης :',Diataksi)

# Εισαγώγη των αποτελεσμάτων στο excel φύλλο για να γίνει save
file2 = pd.DataFrame({'Kοινή διάταξη προτίμησης:':Diataksi})
file = pd.DataFrame({'Koini diataksi protimisis:':Diataksi})

# Convert το cvs σε UTF-8
# IMPORTANT: Cache the conversion to prevent computation on every rerun
@st.cache_data
def convert_df(df):
    return df.to_csv().encode('utf-8')

csv = convert_df(file)

#Εμφάνιση αποτελεσμάτων και επιλογής για download
c1 , c2 = st.columns(2)

with c1:
    st.write(file2)
csv = convert_df(file)
with c2:
    st.download_button(
        label=':floppy_disk: Download results',
        data=csv,
        file_name='results.csv',
        mime='text/csv',
        )
    