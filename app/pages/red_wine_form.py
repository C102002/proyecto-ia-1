import streamlit as st
import pandas as pd
import joblib 
import tensorflow as tf 
import os
from utils.imputation_constants import imputation_values 

current_dir = os.path.dirname(__file__)
scaler_path = os.path.join(current_dir, '..', 'scalers', 'scaler.pkl')
model_path = os.path.join(current_dir, '..', 'models', 'red_wine_model.keras')


st.title(' 🍷 Aplicación de Predicción de  Calidad del Vino Tinto 🍷')

# --- Cargar el Scaler ---
@st.cache_resource
def load_scaler(path):
    try:
        scaler_loaded = joblib.load(path)
        return scaler_loaded
    except FileNotFoundError:
        return None
    except Exception as e:
        return None

scaler = load_scaler(scaler_path)

# --- Cargar el Modelo ---
@st.cache_resource
def load_model(path):
    try:
        model_loaded = tf.keras.models.load_model(path)
        return model_loaded
    except FileNotFoundError:
        return None
    except Exception as e:
        return None

model = load_model(model_path)


if scaler is None or model is None or imputation_values is None:
    st.error("Error crítico: No se pudieron cargar todos los recursos para realizar su predicción, por favor intentelo más tarde.")
    st.stop() 

feature_names = list(imputation_values.keys()) 


st.header("📊 Ingresa los 11 parámetros químicos referentes al vino a predecir su calidad")
st.markdown("Por favor, introduce los valores decimales para cada característica. Deja vacío si el dato es desconocido y se imputará automáticamente.")

user_inputs = {} 

with st.form("prediction_form"):
    cols = st.columns(3) 

    for i, feature_name in enumerate(feature_names):
        with cols[i % 3]: 
         
            user_inputs[feature_name] = st.number_input(
                f"{feature_name.replace('_', ' ').title()}:",
                value=None, 
                min_value=0.0, 
                format="%.3f", 
                placeholder=f"Ej: {imputation_values.get(feature_name, 0.0):.3f}", # Usa .get() para seguridad
                key=f"input_{feature_name}" 
            )

    st.markdown("---")
    predict_button = st.form_submit_button("🔮 Predecir Calidad del Vino")

# --- Lógica de Predicción al presionar el botón ---

if predict_button:

        st.subheader("Resultados de la Predicción")

        input_features_raw = [user_inputs[name] for name in feature_names]
        
        processed_input_features = []
        imputed_fields_info = [] 

        for i, value in enumerate(input_features_raw):
            feature_name = feature_names[i]
            
            if value is None:
                imputed_value = imputation_values[feature_name]
                processed_input_features.append(imputed_value)
                imputed_fields_info.append(f"'{feature_name}' (imputado con {imputed_value:.3f})")
            else:
                processed_input_features.append(value)
        
        if imputed_fields_info:
            st.info(f"ℹ️ Los siguientes campos estaban vacíos y fueron imputados: {', '.join(imputed_fields_info)}")

        input_df = pd.DataFrame([processed_input_features], columns=feature_names)

        st.write("Valores de entrada recibidos (y procesados si hubo vacíos):")
        st.dataframe(input_df)

        try:
            scaled_input = scaler.transform(input_df)
        except Exception as e:
            st.error(f"❌ Error durante la prediccion ")
            st.stop()

        try:
            prediction = model.predict(scaled_input)
            st.markdown("---")

            if prediction.shape == (1, 1):
                predicted_quality_score = round(prediction[0][0]) 
                st.success(f"✨ **La predicción de calidad del vino es: {predicted_quality_score}**")
                if 0 <= predicted_quality_score <= 4:
                    st.error("❌ **Calidad del Vino: ¡Malo!**")
                elif 5 <= predicted_quality_score <= 7:
                    st.warning("⚠️ **Calidad del Vino: Regular**")
                elif 8 <= predicted_quality_score <= 10:
                    st.success("🏆 **Calidad del Vino: ¡Bueno!**")
                else:
                    st.info("❓ **Calidad del Vino: Fuera de rango esperado (0-10).**")
            else:
                st.success(f"✨ **Predicción del modelo:** {prediction}")
            
        except Exception as e:
            st.error(f"❌ Error al realizar la predicción")
    
st.markdown("---")
st.caption("Aplicación de Predicción de Calidad de Vino con Streamlit y TensorFlow/Scikit-learn.")