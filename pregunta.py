"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd
import re


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0, encoding='utf-8')
    df = df.dropna()

    # pd.set_option('display.max_rows', 500)
    # print(df.barrio.value_counts())
    df.comuna_ciudadano = df.comuna_ciudadano.astype('string').replace('.0$', '', regex=True)

    # Limpieza de la columna sexo
    df.sexo = df.sexo.str.lower()

    # Limpieza de la columna tipo de emprendimiento
    df.tipo_de_emprendimiento = df.tipo_de_emprendimiento.str.lower()

    df.barrio = df.barrio.str.lower()
    df.barrio = df.barrio.str.replace('[ |-]', '_', regex=True).replace('\.','', regex=True)

    # Limpieza idea de negocio
    df.idea_negocio = df.idea_negocio.map(lambda x : x.strip())
    df.idea_negocio = df.idea_negocio.str.lower()
    df.idea_negocio = df.idea_negocio.str.replace('[_| |-]$', '', regex=True).replace(' ', '-', regex=True).replace('_', '-', regex=True)
    # print(df.idea_negocio.value_counts())

    # Limpieza de monto del crédito
    df.monto_del_credito = df.monto_del_credito.str.replace('\.00$', '', regex=True).replace('[\$ |,|.]', '', regex=True)
    # print(df.monto_del_credito.value_counts())

    # Limpieza de la fecha de beneficio al format día-mes-año
    df.fecha_de_beneficio = pd.to_datetime(
            df.fecha_de_beneficio,
            infer_datetime_format=True,
            errors='ignore',
            dayfirst=True
    )
    df.fecha_de_beneficio = pd.to_datetime(
            df.fecha_de_beneficio,
            infer_datetime_format=True,
            errors='ignore',
            yearfirst=True
    )
    df.fecha_de_beneficio = df.fecha_de_beneficio.dt.strftime('%d-%m-%Y')

    # Limpieza de la línea de crédito
    df.línea_credito = df.línea_credito.str.lower()
    df.línea_credito = df.línea_credito.map(lambda x : x.replace('-', '_').strip().replace(' ', '_'))
    df.línea_credito = df.línea_credito.str.replace('[_| |-]$', '', regex=True)
    # print(df.línea_credito.value_counts())

    # Elimina los repetidos en todas sus columnas
    df = df.drop_duplicates()

    return df

clean_data()
