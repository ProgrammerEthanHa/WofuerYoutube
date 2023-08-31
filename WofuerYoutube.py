import streamlit as st
import pandas as pd
import altair as alt

st.header("Für viele gehören Youtube und Schule zusammen")
st.subheader("Nutzung von Youtube Videos im schulischen Kontext")

source = pd.DataFrame({
        'Anteil(%)': [73, 70, 66, 60, 58, 46, 37, 35],
        'Wofür?': ['Zur Wiederholung von Unterricht, den ich nicht verstanden habe', 'Für Hausaufgaben/Hausarbeiten', 'Zur Vertiefung meines Wissens aus der Schule', 'Für Prüfungen', 'Für die Vor- und Nachbereitung des Unterrichts', 'Für den Musik-, Kunst-, und Theaterunterricht', 'Für den Deutsch- und Sprachunterricht', 'Für Ags, den Chor und, die Schulband etc.']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Wofür?:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis: 520 Befragten; Deutschland; (12 bis 19 Jahre); 2019
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Rat für Kulturelle Bildung")