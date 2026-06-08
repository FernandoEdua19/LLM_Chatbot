import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="Tutor Virtual", page_icon="🧑‍🏫", layout="centered")

st.title("✍️(◔◡◔) Tutor Virtual Inteligente")
st.write("¡Hola! Soy tu Tutor Virtual Inteligente. Puedo ayudarte con temas relacionados a cualquier materia escolar, explicarte como hacer tu tarea, darte consejos para mejorar tu tecnica de estudio u orientarte en lo que necesites.")

api_key = st.text_input("Ingresa tu Google Gemini API Key para empezar:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    
    tarea = st.selectbox(
        "¿En qué te puedo ayudar hoy?",
        ("Explicacion acerca de una tarea", "Sugerir tecnicas de estudio", "Orientacion acerca de un tema")
    )
    
    if tarea == "Explicacion acerca de una tarea":
        texto_usuario = st.text_area("Dime acerca de que es tu tarea:", height=150)
        if st.button("Explicar tarea"):
            if texto_usuario:
                with st.spinner("Revisando tu tarea..."):
                    try:
                        model = genai.GenerativeModel('gemini-3.5-flash')
                        prompt = f"Da una explicacion breve si es posible acerca de la tarea. Devuelve una tarea similar con otro ejemplo:\n\n{texto_usuario}"
                        response = model.generate_content(prompt)
                        st.subheader("Explicacion:")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Error: {e}")
            else:
                st.warning("Por favor, dime como te puedo ayudar con tu tarea.")
                
    elif tarea == "Sugerir tecnicas de estudio":
        texto_usuario = st.text_area("Dime cual es tu forma favorita de aprender? (visual, auditivo o kinestésico):", height=150)
        if st.button("Sugerir tecnica basada en forma de aprendizaje"):
            if texto_usuario:
                with st.spinner("Buscando la mejor tecnica de aprendizaje..."):
                    try:
                        model = genai.GenerativeModel('gemini-3.5-flash')
                        prompt = f"Da la mejor tecnica de estudio con la forma de aprendizaje:\n\n{texto_usuario}"
                        response = model.generate_content(prompt)
                        st.subheader("Sugerencia:")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Error: {e}")
            else:
                st.warning("Por favor, ingresa tu tecnica de aprendizaje favorita" \
                
                "")
                
    elif tarea == "Orientacion acerca de un tema":
        tema = st.text_input("¿Acerca de que tema ocupas ayuda? (Ej. como aplicar la IA de forma etica, como realizar una tesis, etc.)")
        tono = st.selectbox("Elige el tema", ("Matematicas", "Filosofia", "Ciencia", "Otros"))
        
        if st.button("Generar texto"):
            if tema:
                with st.spinner("Escribiendo..."):
                    try:
                        model = genai.GenerativeModel('gemini-3.5-flash')
                        prompt = f"Da una orientacion corta acerca: '{tema}'. debe ser enfocado acerca de {tono.lower()}."
                        response = model.generate_content(prompt)
                        st.subheader("Texto Generado:")
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Error: {e}")
            else:
                st.warning("Por favor, ingresa un tema.")
else:
    st.info("Para usar el asistente, necesitas una API Key de Google Gemini. Puedes obtenerla en Google AI Studio.")
