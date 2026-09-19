import streamlit as st

# Definición de la clase Actividad
class Actividad:
    def __init__(self, nombre, tipo, presupuesto, gasto_real):
        self.nombre = nombre
        self.tipo = tipo
        self.presupuesto = presupuesto
        self.gasto_real = gasto_real

    def esta_en_presupuesto(self):
        return self.gasto_real <= self.presupuesto

    def mostrar_info(self):
        estado = "✅ OK" if self.esta_en_presupuesto() else "❌ Excedido"
        return f"{self.nombre} - Tipo: {self.tipo} | Presupuesto: ${self.presupuesto} | Gasto Real: ${self.gasto_real} | Estado: {estado}"

# Inicialización de estado en Streamlit
if "actividades" not in st.session_state:
    st.session_state.actividades = []

st.title("📊 CRUD de Actividades - Streamlit")

# Menú de navegación
opcion = st.sidebar.selectbox("Selecciona una acción", ["Agregar Actividad", "Ver Actividades", "Actualizar Gasto", "Eliminar Actividad"])

# Agregar nueva actividad
if opcion == "Agregar Actividad":
    st.subheader("➕ Agregar Nueva Actividad")
    nombre = st.text_input("Nombre")
    tipo = st.text_input("Tipo")
    presupuesto = st.number_input("Presupuesto", min_value=0.0)
    gasto_real = st.number_input("Gasto Real", min_value=0.0)
    if st.button("Agregar"):
        nueva = Actividad(nombre, tipo, presupuesto, gasto_real)
        st.session_state.actividades.append(nueva)
        st.success("✅ Actividad agregada con éxito.")

# Ver actividades
elif opcion == "Ver Actividades":
    st.subheader("📋 Lista de Actividades")
    if st.session_state.actividades:
        for act in st.session_state.actividades:
            st.write(act.mostrar_info())
    else:
        st.info("No hay actividades registradas.")

# Actualizar gasto real
elif opcion == "Actualizar Gasto":
    st.subheader("🔄 Actualizar Gasto Real")
    nombres = [a.nombre for a in st.session_state.actividades]
    if nombres:
        seleccion = st.selectbox("Selecciona una actividad", nombres)
        nuevo_gasto = st.number_input("Nuevo gasto real", min_value=0.0)
        if st.button("Actualizar"):
            for act in st.session_state.actividades:
                if act.nombre == seleccion:
                    act.gasto_real = nuevo_gasto
                    st.success("Gasto actualizado correctamente.")
    else:
        st.info("No hay actividades para actualizar.")

# Eliminar actividad
elif opcion == "Eliminar Actividad":
    st.subheader("🗑️ Eliminar Actividad")
    nombres = [a.nombre for a in st.session_state.actividades]
    if nombres:
        seleccion = st.selectbox("Selecciona una actividad para eliminar", nombres)
        if st.button("Eliminar"):
            st.session_state.actividades = [a for a in st.session_state.actividades if a.nombre != seleccion]
            st.success("Actividad eliminada correctamente.")
    else:
        st.info("No hay actividades para eliminar.")