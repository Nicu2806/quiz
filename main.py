import streamlit as st
import json
import random
import time

# --- JSON cu Întrebări ---
# Am structurat toate întrebările din documentul dvs. într-un format JSON.
# Acest lucru permite selectarea ușoară și aleatorie a întrebărilor pe categorii.

questions_json = """
{
  "categorii": [
    {
      "nume": "Concepte de bază în informatică",
      "intrebari": [
        {
          "intrebare": "Ce este un algoritm?",
          "optiuni": ["O secvență de pași pentru rezolvarea unei probleme", "Un program care rulează în fundal", "O metodă de a măsura viteza unui computer", "Un limbaj de programare"],
          "corect": 0
        },
        {
          "intrebare": "Ce face un procesor într-un computer?",
          "optiuni": ["Afișează informațiile pe ecran", "Stochează fișierele utilizatorului", "Execută instrucțiunile programelor", "Controlează ventilatorul computerului"],
          "corect": 2
        },
        {
          "intrebare": "Ce este un bit?",
          "optiuni": ["O unitate de măsură pentru viteza internetului", "Cea mai mică unitate de date într-un computer", "Un tip de fișier de imagine", "O parte a tastaturii"],
          "corect": 1
        },
        {
          "intrebare": "Cum sunt stocate informațiile într-un computer?",
          "optiuni": ["În formă de imagini", "În formă de text", "În formă de numere binare", "În formă de coduri de bare"],
          "corect": 2
        },
        {
          "intrebare": "Ce este codul binar?",
          "optiuni": ["Un limbaj de programare pentru aplicații", "Un sistem de numerație care folosește doar cifrele 0 și 1", "Un tip de software antivirus", "Un program pentru editarea video"],
          "corect": 1
        },
        {
          "intrebare": "Care este funcția memoriei RAM?",
          "optiuni": ["Stocarea permanentă a datelor", "Rularea și stocarea temporară a programelor și datelor", "Controlul imaginii afișate pe ecran", "Menținerea securității datelor"],
          "corect": 1
        },
        {
          "intrebare": "Ce este un sistem de operare?",
          "optiuni": ["Un program care permite utilizatorului să navigheze pe internet", "Un software care gestionează toate resursele hardware și software ale unui computer", "Un dispozitiv care controlează mișcările mouse-ului", "O aplicație pentru procesarea textului"],
          "corect": 1
        },
        {
          "intrebare": "Cum se numește dispozitivul care transformă semnalele digitale în semnale video pentru afișare pe monitor?",
          "optiuni": ["Procesor", "Hard disk", "Placa grafică (GPU)", "Router"],
          "corect": 2
        },
        {
          "intrebare": "Ce este un fișier executabil?",
          "optiuni": ["Un fișier care poate fi deschis cu orice program", "Un fișier care rulează instrucțiuni pentru a executa un program", "Un fișier de backup al datelor", "Un fișier care conține doar imagini"],
          "corect": 1
        },
        {
          "intrebare": "Care este diferența dintre un hard disk (HDD) și un SSD?",
          "optiuni": ["HDD-ul este mai rapid decât SSD-ul", "SSD-ul folosește componente mecanice, iar HDD-ul folosește circuite electronice", "SSD-ul este mai rapid și nu are părți mecanice", "HDD-ul are o capacitate de stocare mai mică decât SSD-ul"],
          "corect": 2
        }
      ]
    },
    {
      "nume": "Limbaje de programare",
      "intrebari": [
        {
            "intrebare": "Ce limbaj de programare este adesea folosit pentru dezvoltarea web?",
            "optiuni": ["Python", "Java", "HTML/CSS", "C++"],
            "corect": 2
        },
        {
            "intrebare": "Care este funcția unei variabile într-un program?",
            "optiuni": ["A stoca date temporar", "A afișa un mesaj pe ecran", "A controla viteza programului", "A opri execuția programului"],
            "corect": 0
        },
        {
            "intrebare": "Ce este un if-else într-un program?",
            "optiuni": ["O modalitate de a repeta un bloc de cod", "O structură condițională care controlează fluxul programului", "Un tip de funcție matematică", "Un tip de variabilă"],
            "corect": 1
        },
        {
            "intrebare": "Ce este o buclă while?",
            "optiuni": ["Un tip de variabilă", "O metodă de stocare a datelor", "O structură care repetă un bloc de cod până când o condiție devine falsă", "O metodă de optimizare a memoriei"],
            "corect": 2
        },
        {
            "intrebare": "Ce limbaj de programare este cel mai utilizat pentru dezvoltarea de aplicații mobile Android?",
            "optiuni": ["Swift", "Java", "Python", "HTML"],
            "corect": 1
        },
        {
            "intrebare": "Ce face funcția print() în Python?",
            "optiuni": ["Tipărește documente la imprimantă", "Afișează un mesaj pe ecran", "Salvează date într-un fișier", "Închide programul"],
            "corect": 1
        },
        {
            "intrebare": "Cum poți defini o funcție în Python?",
            "optiuni": ["Cu cuvântul cheie define", "Cu cuvântul cheie func", "Cu cuvântul cheie def", "Cu cuvântul cheie lambda"],
            "corect": 2
        },
        {
            "intrebare": "Ce face un compilator?",
            "optiuni": ["Rulează programul pe computer", "Traducă codul sursă într-un limbaj de nivel inferior", "Salvează codul într-un fișier text", "Corectează erorile din cod"],
            "corect": 1
        },
        {
            "intrebare": "Care este diferența dintre o buclă for și o buclă while?",
            "optiuni": ["For repetă de un număr fix de ori, while repetă până când o condiție devine falsă", "While este mai rapid decât for", "For poate fi utilizată doar pentru numere, while pentru text", "Nu există nicio diferență"],
            "corect": 0
        },
        {
            "intrebare": "Ce este un comentariu în cod?",
            "optiuni": ["Un bloc de cod care se repetă", "O linie de cod care este executată", "O linie de text care explică ce face codul, dar nu este executată", "Un mesaj de eroare"],
            "corect": 2
        }
      ]
    },
    {
      "nume": "Internet și securitate",
      "intrebari": [
        {
            "intrebare": "Ce este o adresă IP?",
            "optiuni": ["Un identificator unic pentru fiecare dispozitiv conectat la o rețea", "O pagină web", "Un fișier text folosit pe internet", "Un cod de eroare pentru conexiuni nereușite"],
            "corect": 0
        },
        {
            "intrebare": "Ce este HTTPS?",
            "optiuni": ["Un protocol de securitate pentru transferul de fișiere", "O versiune securizată a HTTP care protejează datele transmise", "Un limbaj de programare", "O aplicație de chat online"],
            "corect": 1
        },
        {
            "intrebare": "Ce este phishing-ul?",
            "optiuni": ["O metodă de criptare a datelor", "Un atac cibernetic prin care sunt furate informații personale", "Un software antivirus", "O tehnologie pentru îmbunătățirea vitezei internetului"],
            "corect": 1
        },
        {
            "intrebare": "Ce este un firewall?",
            "optiuni": ["Un dispozitiv fizic care blochează accesul la internet", "Un software care controlează traficul de date și protejează împotriva atacurilor", "Un sistem de backup pentru date", "Un tip de server web"],
            "corect": 1
        },
        {
            "intrebare": "Cum te poți proteja împotriva virusurilor informatice?",
            "optiuni": ["Folosind un antivirus și actualizându-l regulat", "Deschizând orice fișier primit pe email", "Dezactivând firewall-ul", "Folosind doar parole simple"],
            "corect": 0
        },
        {
            "intrebare": "Ce este criptarea datelor?",
            "optiuni": ["Procesul de backup al datelor pe un server", "Transformarea datelor într-un format codificat pentru a preveni accesul neautorizat", "Ștergerea permanentă a datelor de pe un hard disk", "O metodă de compresie a fișierelor mari"],
            "corect": 1
        },
        {
            "intrebare": "Cum funcționează un motor de căutare precum Google?",
            "optiuni": ["Caută pe toate site-urile web simultan", "Utilizează algoritmi care sortează și clasifică paginile web pe baza relevanței", "Alege site-urile web în funcție de numărul de imagini", "Caută doar pe paginile populare"],
            "corect": 1
        },
        {
            "intrebare": "Ce este o rețea locală (LAN)?",
            "optiuni": ["O rețea globală de calculatoare", "O rețea de calculatoare care acoperă o zonă restrânsă, cum ar fi o clădire", "O conexiune între telefoanele mobile și internet", "Un tip de conexiune la internet prin cablu"],
            "corect": 1
        },
        {
            "intrebare": "Ce înseamnă 'cloud' în contextul stocării de date?",
            "optiuni": ["Stocarea datelor pe hard disk-ul propriu", "Stocarea datelor pe servere externe accesibile prin internet", "O metodă de criptare a datelor", "Un tip de fișier multimedia"],
            "corect": 1
        },
        {
            "intrebare": "Ce este un virus de computer?",
            "optiuni": ["Un program care protejează computerul", "Un program malițios care se răspândește și poate dăuna sistemului", "O aplicație folosită pentru actualizări software", "Un fișier de backup pentru sistemul de operare"],
            "corect": 1
        }
      ]
    },
    {
      "nume": "Hardware și Software",
      "intrebari": [
        {
            "intrebare": "Ce este un hard disk (HDD)?",
            "optiuni": ["Un dispozitiv de afișare a imaginilor", "Un dispozitiv de stocare a datelor", "Un procesor grafic", "Un software de gestionare a fișierelor"],
            "corect": 1
        },
        {
            "intrebare": "Ce este un server?",
            "optiuni": ["Un computer care furnizează servicii altor computere într-o rețea", "Un software antivirus", "Un dispozitiv de stocare extern", "O aplicație de procesare a textului"],
            "corect": 0
        },
        {
            "intrebare": "Ce înseamnă 'plug and play'?",
            "optiuni": ["Dispozitivul trebuie instalat manual înainte de utilizare", "Dispozitivul funcționează imediat după conectare, fără instalare suplimentară", "O metodă de încărcare a fișierelor multimedia", "O opțiune pentru jocuri video"],
            "corect": 1
        },
        {
            "intrebare": "Care dintre următoarele componente ale unui computer controlează ieșirea video?",
            "optiuni": ["Hard disk", "Placa de bază", "Procesorul", "Placa video (GPU)"],
            "corect": 3
        },
        {
            "intrebare": "Ce este o aplicație?",
            "optiuni": ["Un tip de hardware", "Un software conceput pentru a realiza sarcini specifice pe un dispozitiv", "O metodă de conectare la internet", "O formă de protecție antivirus"],
            "corect": 1
        },
        {
            "intrebare": "Ce este o interfață grafică (GUI)?",
            "optiuni": ["O interfață care folosește doar text pentru a interacționa cu utilizatorul", "O interfață care folosește imagini și pictograme pentru a interacționa cu utilizatorul", "O metodă de criptare a datelor", "Un tip de fișier multimedia"],
            "corect": 1
        },
        {
            "intrebare": "Ce este un router?",
            "optiuni": ["Un dispozitiv care conectează calculatoarele la internet sau la alte rețele", "Un software pentru navigarea pe internet", "Un tip de cablu pentru conectarea dispozitivelor", "Un sistem de backup pentru fișiere"],
            "corect": 0
        },
        {
            "intrebare": "Ce este un touchscreen?",
            "optiuni": ["Un tip de software de editare", "Un ecran care reacționează la atingerea utilizatorului", "O metodă de imprimare", "Un sistem de securitate pentru calculatoare"],
            "corect": 1
        },
        {
            "intrebare": "Ce face un antivirus?",
            "optiuni": ["Instalează aplicații pe computer", "Protejează computerul împotriva virușilor și altor programe malițioase", "Crește viteza procesorului", "Optimizează grafica jocurilor video"],
            "corect": 1
        },
        {
            "intrebare": "Ce este o unitate de alimentare (PSU)?",
            "optiuni": ["Un dispozitiv care controlează viteza ventilatorului", "Un dispozitiv care furnizează energie electrică computerului", "Un procesor grafic", "O aplicație pentru gestionarea fișierelor"],
            "corect": 1
        }
      ]
    },
    {
      "nume": "Diverse concepte în informatică",
      "intrebari": [
        {
            "intrebare": "Ce este un fișier ZIP?",
            "optiuni": ["Un tip de fișier pentru imagini", "Un fișier comprimat care conține mai multe fișiere sau foldere", "Un program antivirus", "Un tip de fișier pentru documente text"],
            "corect": 1
        },
        {
            "intrebare": "Ce face comanda 'Ctrl + Z'?",
            "optiuni": ["Reface ultima acțiune", "Anulează ultima acțiune", "Salvează documentul", "Copiază textul selectat"],
            "corect": 1
        },
        {
            "intrebare": "Ce este un pixel?",
            "optiuni": ["Un tip de fișier imagine", "Cea mai mică unitate de afișare pe un ecran digital", "O metodă de compresie a fișierelor video", "Un tip de procesor grafic"],
            "corect": 1
        },
        {
            "intrebare": "Ce este o bază de date?",
            "optiuni": ["Un sistem de stocare a informațiilor într-un format organizat", "Un software de editare video", "Un server de internet", "Un program de procesare a textului"],
            "corect": 0
        },
        {
            "intrebare": "Ce este inteligența artificială (AI)?",
            "optiuni": ["Un sistem care imită comportamentul uman și poate lua decizii", "Un program pentru crearea jocurilor video", "O tehnologie de stocare a datelor", "Un tip de memorie RAM"],
            "corect": 0
        },
        {
            "intrebare": "Ce este o adresă de e-mail?",
            "optiuni": ["O metodă de criptare a fișierelor", "O modalitate de a comunica prin mesaje scrise pe internet", "Un tip de fișier multimedia", "Un software pentru procesarea textului"],
            "corect": 1
        },
        {
            "intrebare": "Ce face un program de procesare a textului?",
            "optiuni": ["Creează și editează imagini", "Creează și editează documente text", "Protejează fișierele împotriva virușilor", "Stochează date pe servere externe"],
            "corect": 1
        },
        {
            "intrebare": "Ce este un algoritm de sortare?",
            "optiuni": ["Un proces de afișare a datelor pe ecran", "Un set de instrucțiuni pentru organizarea datelor într-o anumită ordine", "O metodă de compresie a fișierelor mari", "Un software pentru crearea jocurilor"],
            "corect": 1
        },
        {
            "intrebare": "Ce este un IP static?",
            "optiuni": ["O adresă IP care se schimbă la fiecare conexiune la internet", "O adresă IP care rămâne aceeași pentru o perioadă lungă de timp", "O metodă de criptare a fișierelor", "O adresă IP utilizată doar pentru rețele mobile"],
            "corect": 1
        },
        {
            "intrebare": "Ce este un QR code?",
            "optiuni": ["O imagine utilizată pentru criptarea datelor", "Un cod de bare bidimensional utilizat pentru stocarea informațiilor", "Un program de editare grafică", "Un tip de fișier multimedia"],
            "corect": 1
        }
      ]
    }
  ]
}
"""

# --- Funcții Helper ---

def initialize_quiz():
    """Inițializează sau resetează starea quiz-ului."""
    data = json.loads(questions_json)
    
    # Selectează câte o întrebare aleatorie din fiecare categorie
    st.session_state.questions = [random.choice(cat["intrebari"]) for cat in data["categorii"]]
    st.session_state.current_question_index = 0
    st.session_state.score = 0
    st.session_state.user_answers = {}
    st.session_state.quiz_started = True
    st.session_state.quiz_completed = False

def display_results():
    """Afișează rezultatele finale și un mesaj personalizat."""
    st.header("🎉 Rezultate Finale 🎉", anchor=False)
    
    score = st.session_state.score
    total = len(st.session_state.questions)
    
    # Baloanele apar mereu la final
    st.balloons()

    # Mesaj și efect suplimentar în funcție de scor
    if score == total:
        st.success(f"Excelent! Ai răspuns corect la toate cele {total} întrebări!")
        st.markdown("<h2 style='color:gold;'>🏆 Super Campion! 🏆</h2>", unsafe_allow_html=True)
        st.toast("Perfect! Felicitări!", icon="🎊")
    elif score >= total / 2:
        st.info(f"Felicitări! Ai răspuns corect la {score} din {total} întrebări.")
        st.snow()
        st.toast("Destul de bine! Mai exersează!", icon="👍")
    else:
        st.warning(f"Ai răspuns corect la {score} din {total}. Mai exersează și vei deveni un expert!")
        st.snow()
        st.toast("Poți mai mult! Încearcă din nou!", icon="💪")

    # Buton pentru a reîncepe quiz-ul
    if st.button("Reîncepe Quiz-ul", type="primary"):
        initialize_quiz()
        st.rerun()

# --- Interfața Principală a Aplicației ---

st.set_page_config(page_title="Quiz FCIM", layout="centered")

# --- Aici înlocuiți cu calea către logo-ul dumneavoastră ---
st.image("Logo_inscript_horizontal-fcim-m.png")

st.title("🚀Quiz Interactiv de Informatică🚀", anchor=False)

# Inițializarea stării la prima rulare
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
    st.session_state.quiz_completed = False

# Pagina de start
if not st.session_state.quiz_started:
    st.markdown("### Testează-ți cunoștințele de informatică! Ești pregătit?")
    if st.button("START", type="primary", use_container_width=True):
        initialize_quiz()
        st.rerun()

# Logica de desfășurare a quiz-ului
elif not st.session_state.quiz_completed:
    index = st.session_state.current_question_index
    question_data = st.session_state.questions[index]
    
    # Afișează progresul
    st.progress((index + 1) / len(st.session_state.questions), text=f"Întrebarea {index + 1}/{len(st.session_state.questions)}")
    
    st.subheader(f"Întrebarea {index + 1}:", anchor=False)
    st.markdown(f"**{question_data['intrebare']}**")

    # Folosim un form pentru a preveni re-rularea la fiecare click pe radio
    with st.form(key=f"question_{index}"):
        user_choice = st.radio(
            "Alege răspunsul corect:",
            options=question_data["optiuni"],
            index=None, # Nicio opțiune nu este selectată implicit
            label_visibility="collapsed"
        )
        
        submit_button = st.form_submit_button("Trimite Răspunsul", use_container_width=True)

        if submit_button:
            if user_choice is not None:
                # Verifică răspunsul și actualizează scorul
                correct_option_index = question_data["corect"]
                if question_data["optiuni"].index(user_choice) == correct_option_index:
                    st.session_state.score += 1
                    st.success("Corect! 🎉")
                else:
                    st.error(f"Greșit! 😟 Răspunsul corect era: **{question_data['optiuni'][correct_option_index]}**")
                
                # Așteaptă puțin pentru ca utilizatorul să vadă feedback-ul
                time.sleep(1.5) 
                
                # Treci la următoarea întrebare sau finalizează quiz-ul
                if index + 1 < len(st.session_state.questions):
                    st.session_state.current_question_index += 1
                else:
                    st.session_state.quiz_completed = True
                
                st.rerun()
            else:
                st.warning("Te rog să selectezi un răspuns!")

# Afișează rezultatele la final
else:
    display_results()
