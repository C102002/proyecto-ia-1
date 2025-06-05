
import pandas as pd
import numpy as np
import os

current_script_dir = os.path.dirname(os.path.abspath(__file__))
project_root_dir = os.path.normpath(os.path.join(current_script_dir, '..', '..'))
csv_path = os.path.join(
    project_root_dir,
    'public', 'data', 'wine+quality', 'winequality-red.csv'
)
output_imputation_file = os.path.join(current_script_dir, 'imputation_constants.py')


try:
    df = pd.read_csv(csv_path, delimiter=';')
    features_df = df.drop(columns=['quality'], errors='ignore')

    imputation_values = {}
    
    print("\nCalculando estadísticas para imputación:")
    for column in features_df.columns:
        if pd.api.types.is_numeric_dtype(features_df[column]):
            mean_val = features_df[column].mean()
            median_val = features_df[column].median()
            skew_val = features_df[column].skew()

            print(f"  - {column}:")
            print(f"    Media: {mean_val:.3f}, Mediana: {median_val:.3f}, Asimetría: {skew_val:.3f}")

            if abs(skew_val) > 0.5:
                imputation_values[column] = median_val
                print(f"    -> Asimetría > 0.5. Imputando con la MEDIANA: {median_val:.3f}")
            else:
                imputation_values[column] = mean_val
                print(f"    -> Asimetría <= 0.5. Imputando con la MEDIA: {mean_val:.3f}")
        else:
            print(f"  - {column}: No es numérica, se omite para imputación.")

    with open(output_imputation_file, 'w') as f:
        f.write("# Contiene los valores de imputación para las características del vino rojo con el dataset actual.\n")
        f.write("\nimputation_values = {\n")
        for k, v in imputation_values.items():
            f.write(f"    '{k}': {v:.6f},\n") 
        f.write("}\n")
    
    print(f"\n Diccionario de imputación guardado en: {output_imputation_file}")
    print("-------------------------------------------------")

except FileNotFoundError:
    print(f"ERROR: El archivo CSV no se encontró en {csv_path}. Verifica la ruta.")
except Exception as e:
    print(f"Ocurrió un error al procesar el CSV: {e}")