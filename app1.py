import streamlit as st

st.set_page_config(page_title="Sumador de Números", layout="centered")

st.title("🔢 Suma de números consecutivos")
st.markdown("""
Esta aplicación te permite ingresar un número entero positivo y suma todos los números consecutivos desde 1 hasta ese valor.

Por ejemplo:  
Si ingresas `5`, se calculará `1 + 2 + 3 + 4 + 5 = 15`.
""")

# Entrada del número
n = st.number_input("Ingresa un número entero positivo:", min_value=1, step=1, value=1)

if st.button("Calcular suma"):
    suma = sum(range(1, n + 1))
    st.success(f"La suma de los números del 1 al {n} es: {suma}")

    # Fórmula opcional
    st.markdown("También puedes calcularlo con la fórmula:")
    st.latex(r"S = \frac{n(n+1)}{2}")
