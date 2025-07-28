import pandas as pd

# Definimos los datos de las tarifas
tarifas = [
    {
        "Proveedor": "Naturgy",
        "Tarifa": "Noche",
        "Potencia Punta (€/kW*día)": 0.108163,
        "Potencia Valle (€/kW*día)": 0.033392,
        "Energía Punta (€/kWh)": 0.185461,
        "Energía Llano (€/kWh)": 0.116414,
        "Energía Valle (€/kWh)": 0.082334
    },
    {
        "Proveedor": "Naturgy",
        "Tarifa": "Uso",
        "Potencia Punta (€/kW*día)": 0.108163,
        "Potencia Valle (€/kW*día)": 0.033392,
        "Energía Punta (€/kWh)": 0.119166,
        "Energía Llano (€/kWh)": 0.119166,
        "Energía Valle (€/kWh)": 0.119166
    },
    {
        "Proveedor": "Iberdrola",
        "Tarifa": "3 Periodos",
        "Potencia Punta (€/kW*día)": 0.086301,
        "Potencia Valle (€/kW*día)": 0.013014,
        "Energía Punta (€/kWh)": 0.176576,
        "Energía Llano (€/kWh)": 0.113892,
        "Energía Valle (€/kWh)": 0.083904
    },
    {
        "Proveedor": "Iberdrola",
        "Tarifa": "Ahorro Inteligente",
        "Potencia Punta (€/kW*día)": 0.108192,
        "Potencia Valle (€/kW*día)": 0.046548,
        "Energía Punta (€/kWh)": 0.223294,
        "Energía Llano (€/kWh)": 0.223294,
        "Energía Valle (€/kWh)": 0.111647
    },
    {
        "Proveedor": "Endesa",
        "Tarifa": "One Luz",
        "Potencia Punta (€/kW*día)": 40.930548 / 365,
        "Potencia Valle (€/kW*día)": 14.697588 / 365,
        "Energía Punta (€/kWh)": 0.133783,
        "Energía Llano (€/kWh)": 0.133783,
        "Energía Valle (€/kWh)": 0.133783
    },
    {
        "Proveedor": "Endesa",
        "Tarifa": "Conecta",
        "Potencia Punta (€/kW*día)": 37.930548 / 365,
        "Potencia Valle (€/kW*día)": 11.697588 / 365,
        "Energía Punta (€/kWh)": 0.100848,
        "Energía Llano (€/kWh)": 0.100848,
        "Energía Valle (€/kWh)": 0.100848
    },
    {
        "Proveedor": "Endesa",
        "Tarifa": "One Luz 3 Periodos",
        "Potencia Punta (€/kW*día)": 40.150296 / 365,
        "Potencia Valle (€/kW*día)": 13.917336 / 365,
        "Energía Punta (€/kWh)": 0.200113,
        "Energía Llano (€/kWh)": 0.123560,
        "Energía Valle (€/kWh)": 0.092084
    }
]

# Consumos estimados para el cálculo
potencia_contratada = 5  # kW
dias_marzo = 31  # días en marzo
consumo_kwh_punta = 194  # Consumo estimado en horas punta (kWh)
consumo_kwh_llano = 142  # Consumo estimado en horas llano (kWh)
consumo_kwh_valle = 200  # Consumo estimado en horas valle (kWh)

# Cálculo de costes
resultados = []
for tarifa in tarifas:
    coste_potencia = (
        tarifa["Potencia Punta (€/kW*día)"] * potencia_contratada * dias_marzo +
        tarifa["Potencia Valle (€/kW*día)"] * potencia_contratada * dias_marzo
    )
    coste_energia = (
        tarifa["Energía Punta (€/kWh)"] * consumo_kwh_punta +
        tarifa["Energía Llano (€/kWh)"] * consumo_kwh_llano +
        tarifa["Energía Valle (€/kWh)"] * consumo_kwh_valle
    )
    coste_total = coste_potencia + coste_energia
    resultados.append({
        "Proveedor": tarifa["Proveedor"],
        "Tarifa": tarifa["Tarifa"],
        "Coste Potencia (€)": round(coste_potencia, 2),
        "Coste Energía (€)": round(coste_energia, 2),
        "Coste Total (€)": round(coste_total, 2)
    })

# Crear un DataFrame y mostrar resultados
df_resultados = pd.DataFrame(resultados)
df_resultados.to_excel("resultados.xlsx", index=False, sheet_name="Tarifas")

