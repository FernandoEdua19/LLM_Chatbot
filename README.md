# Tutor Virtual Inteligente ✍️(◔◡◔)

El proyecto consiste en crear un tutor inteligente que pueda ayudar a los estudiantes con sus tareas dando ejemplos parecidos a lo que ellos buscan resolver sin darles la respuesta de su tarea. Esta desarrollado la API de Google Gemini AI con el modelo gratuito de "gemini-3.5-flash" para que los interesados en el proyecto puedan poner en practica la IA

## 🚀 Funcionalidades

Las funcionalidades del tutor virtual son las siguientes:

1. **Explicacion acerca de una tarea**: Esta funcion permite que el usuario ingrese informacion acerca de la tarea donde necesita ayuda y la IA devuelve una tarea similar con una explicacion para que el usuario a traves de ese ejemplo pueda resolver su tarea original.
2. **Sugerir tecnicas de estudio**: Esta funcionalidad permite que el usuario pueda recibir consejos acerca de cual es la mejor tecnica de estudio basada en su forma de aprendizaje y que pueda mejorar su desempeño escolar con esos consejos.
3. **Orientacion acerca de un tema**: En esta opcion le permite al usuario recibir una orientacion de un tema enfocado en una materia en especifico. Es decir, puede recibir informacion acerca de los futuros tecnologicos basados enfocado al tema filosofico.

## 🛠 Requisitos Previos

Para utilizar esta aplicación necesitas:

- Python 3.8 o superior instalado en tu sistema.
- Una **API Key de Google Gemini** (Puedes obtenerla gratuitamente en [Google AI Studio](https://aistudio.google.com/)).

## 📦 Instalación

1. Clona el repositorio o navega hasta la carpeta del proyecto en tu terminal

2. (Recomendado) Crea un entorno virtual para instalar las dependencias sin afectar tu sistema:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Mac/Linux
   # venv\Scripts\activate   # En Windows
   ```

3. Instala las dependencias requeridas usando el archivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Uso

Para iniciar la aplicación, asegúrate de tener tu entorno virtual activado y ejecuta el siguiente comando:

```bash
streamlit run app.py
```

- Al ejecutarlo por primera vez, Streamlit podría preguntarte tu correo electrónico. Puedes simplemente presionar **Enter** para omitir ese paso.
- La aplicación se abrirá automáticamente en tu navegador web predeterminado (usualmente en `http://localhost:8501`).
- En la interfaz, **ingresa tu API Key de Gemini** en el campo correspondiente para comenzar a usar todas las funcionalidades.

## 📚 Tecnologías Utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/) (Interfaz de usuario web)
- [Google Generative AI](https://ai.google.dev/) (Modelo de IA)
