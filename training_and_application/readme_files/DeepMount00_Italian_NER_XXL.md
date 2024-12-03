---
tags:
- legal
- finance
- privacy
model-index:
- name: Italin_NER_XXL
  results: []
widget:
- text: >-
    Mario Rossi, nato il 15 marzo 1975, residente in Via delle Rose 123, 50122
    Firenze, ha inviato un'email a info@example.com per richiedere informazioni
    sulla legge N. 123/2021, indicando il suo numero di telefono +39 0551234567
    e il codice fiscale RSSMRA75C15D612K.
- text: >-
    La ditta Giardini Belli S.p.A., con partita IVA 01234567890, ha emesso una
    fattura di 500€ per la consulenza giuridica fornita dall'avvocato Giulia
    Bianchi, il cui studio si trova in Piazza del Duomo, Milano, dal giorno
    01/04/2024.
- text: >-
    Il cliente ha effettuato un pagamento di 1500€ tramite bonifico bancario
    (IBAN: IT60X0542811101000000123456) dalla banca Banca di Roma, per
    l'acquisto di un veicolo con targa AB123CD, registrando la transazione alle
    14:00 del 10/01/2024, come evidenziato nel suo estratto conto numero 7890.
language:
- it
license: apache-2.0
---


# Italian_NER_XXL

## Model Overview
This is the initial release of our artificial intelligence model on Hugging Face. It is important to note that this version is just the beginning; the model will be constantly improved over time. <u>**Currently, the model boasts an accuracy of 79%, but we plan to increase this regularly through monthly updates.**</u>

## Uniqueness of the Model in Italy
We are proud to announce that our model is currently the only one in Italy capable of identifying a wide range of **52** different categories. This capability distinctly sets it apart from other models available in the Italian landscape, offering an unprecedented level of versatility and breadth in entity recognition.

## Technology and Innovation
The model is based on the BERT architecture, one of the most advanced technologies in the field of Natural Language Processing (NLP). State-of-the-art techniques have been employed for its training, ensuring high-level accuracy and efficiency. This technological choice ensures a deep and sophisticated understanding of natural language.

## Recognized Categories
The model is capable of identifying the following categories:
- **INDIRIZZO**: Identifica un indirizzo fisico.
- **VALUTA**: Rappresenta una valuta.
- **CVV**: Codice di sicurezza della carta di credito.
- **NUMERO_CONTO**: Numero di un conto bancario.
- **BIC**: Codice identificativo di una banca (Bank Identifier Code).
- **IBAN**: Numero di conto bancario internazionale.
- **STATO**: Identifica un paese o una nazione.
- **NOME**: Riferito al nome di una persona.
- **COGNOME**: Riferito al cognome di una persona.
- **CODICE_POSTALE**: Codice postale di un'area geografica.
- **IP**: Indirizzo IP di un dispositivo in rete.
- **ORARIO**: Riferito a un orario specifico.
- **URL**: Indirizzo web (Uniform Resource Locator).
- **LUOGO**: Identifica un luogo geografico.
- **IMPORTO**: Riferito a una somma di denaro.
- **EMAIL**: Indirizzo di posta elettronica.
- **PASSWORD**: Parola chiave per l'accesso a sistemi protetti.
- **NUMERO_CARTA**: Numero di una carta di credito o debito.
- **TARGA_VEICOLO**: Numero di targa di un veicolo.
- **DATA_NASCITA**: Data di nascita di una persona.
- **DATA_MORTE**: Data di decesso di una persona.
- **RAGIONE_SOCIALE**: Nome legale di un'azienda o entità commerciale.
- **ETA**: Età di una persona.
- **DATA**: Riferita a una data generica.
- **PROFESSIONE**: Occupazione o lavoro di una persona.
- **PIN**: Numero di identificazione personale.
- **NUMERO_TELEFONO**: Numero telefonico.
- **FOGLIO**: Riferito a un foglio di documentazione.
- **PARTICELLA**: Riferito a una particella catastale.
- **CARTELLA_CLINICA**: Documentazione medica di un paziente.
- **MALATTIA**: Identifica una malattia o condizione medica.
- **MEDICINA**: Riferito a un farmaco o trattamento medico.
- **CODICE_FISCALE**: Codice fiscale personale o aziendale.
- **NUMERO_DOCUMENTO**: Numero di un documento ufficiale.
- **STORIA_CLINICA**: Registro delle condizioni mediche di un paziente.
- **AVV_NOTAIO**: Identifica un avvocato o notaio.
- **P_IVA**: Partita IVA di un'azienda o professionista.
- **LEGGE**: Riferito a una legge specifica.
- **TASSO_MUTUO**: Tasso di interesse di un mutuo.
- **N_SENTENZA**: Numero di una sentenza legale.
- **MAPPALE**: Riferito a un mappale catastale.
- **SUBALTERNO**: Riferito a un subalterno catastale.
- **REGIME_PATRIMONIALE**: Stato patrimoniale in ambito legale.
- **STATO_CIVILE**: Stato civile di una persona.
- **BANCA**: Identifica una banca o istituto di credito.
- **BRAND**: Marchio o brand commerciale.
- **NUM_ASSEGNO_BANCARIO**: Numero di un assegno bancario.
- **IMEI**: Numero di identificazione internazionale di un dispositivo mobile.
- **N_LICENZA**: Numero di una licenza specifica.
- **IPV6_1**: Indirizzo IP versione 6.
- **MAC**: Indirizzo MAC di un dispositivo di rete.
- **USER_AGENT**: Identifica il software usato per accedere a una rete.
- **TRIBUNALE**: Identifica un tribunale specifico.
- **STRENGTH**: Riferito alla forza o intensità di del medicinale.
- **FREQUENZA**: Riferito alla frequenza di un trattamento medico.
- **DURATION**: Durata di un evento o trattamento.
- **DOSAGGIO**: Quantità di un medicinale da assumere.
- **FORM**: Forma del medicinale, ad esempio compresse.

## How to Use
To utilize this model:

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import torch

tokenizer = AutoTokenizer.from_pretrained("DeepMount00/Italian_NER_XXL")
model = AutoModelForTokenClassification.from_pretrained("DeepMount00/Italian_NER_XXL", ignore_mismatched_sizes=True)
nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = """Il commendatore Gianluigi Alberico De Laurentis-Ponti, con residenza legale in Corso Imperatrice 67,  Torino, avente codice fiscale DLNGGL60B01L219P, è amministratore delegato della "De Laurentis Advanced Engineering Group S.p.A.",  che si trova in Piazza Affari 32, Milano (MI); con una partita IVA di 09876543210, la società è stata recentemente incaricata  di sviluppare una nuova linea di componenti aerospaziali per il progetto internazionale di esplorazione di Marte."""
ner_results = nlp(example)
print(ner_results)
```
---

## Conclusion
The primary goal of this model is to provide effective and accurate identification of a wide range of entities, surpassing the limits of traditional models. Being the only model in Italy to recognize so many entities, we are confident that it will be an invaluable tool for numerous application areas. Constant evolution and improvement of the model is our top priority to ensure always top-notch performance.

## Contribution and Contact

If you are interested in contributing to this project, have suggestions for improvement, or require a specific named entity recognizer for your use case, please feel free to reach out. Your input and collaboration can significantly enhance the model's capabilities and applications. For any inquiries or to discuss potential contributions, please contact Michele Montebovi at [montebovi.michele@gmail.com](mailto:montebovi.michele@gmail.com). Your support and participation are highly appreciated as we aim to continuously improve and expand the functionalities of the Italian_NER_XXL model.