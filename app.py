import streamlit as st

st.set_page_config(
    page_title="Escape Room ICOPE",
    page_icon="🏥",
    layout="centered"
)

# ---------- ESTILO ----------
st.markdown("""
<style>
    .main {
        background-color: #fafafa;
    }
    .block-container {
        max-width: 850px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }
    .case-box {
        background: #f4f7fb;
        border: 1px solid #d9e2ef;
        border-radius: 14px;
        padding: 18px 20px;
        margin-bottom: 18px;
    }
    .lock-box {
        background: white;
        border: 1px solid #e6e6e6;
        border-radius: 14px;
        padding: 16px 18px;
        margin: 12px 0;
    }
</style>
""", unsafe_allow_html=True)

# ---------- ENCABEZADO ----------
st.title("🏥 Escape Room Clínico ICOPE")
st.subheader("🔐 El expediente de Julio")
st.caption("Evaluación de la capacidad sensorial: visión y audición")

st.markdown("""
<div class="case-box">
<b>Paciente:</b> Julio, 70 años.<br>
<b>Antecedentes:</b> Diabetes mellitus tipo 2 de 15 años de evolución en tratamiento con insulina,
tabaquismo, gonartrosis con EVA 7/10 y 3 caídas en el último año.<br><br>
🎯 <b>Misión:</b> resuelve los 6 candados clínicos para obtener el <b>Código de Alta ICOPE</b>.
</div>
""", unsafe_allow_html=True)

st.info("💡 Lee con atención. Cada candado aporta una letra o número al código final.")

# ---------- CANDADO 1 ----------
st.markdown("### 🔒 Candado 1 — Visión")
c1 = st.selectbox(
    "¿Por qué Julio no requiere tamizaje inicial de agudeza visual en el Paso 1?",
    [
        "Selecciona una respuesta...",
        "A) Por ser mayor de 65 años",
        "B) Por antecedente de Diabetes Mellitus 2: requiere evaluación ocular dirigida",
        "C) Por historia de caídas"
    ],
    key="c1"
)

# ---------- CANDADO 2 ----------
st.markdown("### 🔒 Candado 2 — Intervenciones visuales")
st.write("Cuenta cuántas de las siguientes intervenciones forman parte del abordaje integral de la capacidad visual:")

intervenciones = [
    "1. Referir para valoración de retina en una persona con diabetes.",
    "2. Mejorar la iluminación del hogar.",
    "3. Reducir obstáculos y riesgos de caída en el piso.",
    "4. Revisar si los lentes actuales son adecuados.",
    "5. Favorecer el control de enfermedades crónicas asociadas.",
]
for item in intervenciones:
    st.write(f"• {item}")

c2 = st.number_input(
    "¿Cuántas intervenciones son correctas?",
    min_value=0, max_value=5, step=1, key="c2"
)

# ---------- CANDADO 3 ----------
st.markdown("### 🔒 Candado 3 — Prescripción de lentes")
st.write("Identifica el número de la afirmación VERDADERA:")

st.write("""
1. Todo adulto mayor debe cambiar sus lentes cada 6 meses aunque vea bien.  
2. Los lentes pueden prescribirse sin valorar la agudeza visual ni la refracción.  
3. La corrección óptica debe individualizarse según la evaluación visual y las necesidades funcionales.  
4. La presbicia contraindica el uso de lentes progresivos.
""")

c3 = st.number_input(
    "Número de la afirmación verdadera:",
    min_value=0, max_value=4, step=1, key="c3"
)

# ---------- CANDADO 4 ----------
st.markdown("### 🔒 Candado 4 — Audición")
c4 = st.selectbox(
    "¿Cuál es la maniobra indispensable previa y cuál es una bandera roja auditiva?",
    [
        "Selecciona una respuesta...",
        "A) Lavado ótico bilateral sistemático // Bandera roja: presbiacusia",
        "B) Otoscopia previa // Bandera roja: asimetría, dolor u otorrea",
        "C) Audiometría tonal inmediata // Bandera roja: uso de auxiliares auditivos"
    ],
    key="c4"
)

# ---------- CANDADO 5 ----------
st.markdown("### 🔒 Candado 5 — Grado de hipoacusia")
st.write("La audiometría de Julio reporta un promedio de **48 dB HL**.")

c5 = st.number_input(
    "Escribe el número romano convertido a arábigo de la categoría asignada en este ejercicio (I = 1, II = 2, III = 3, etc.):",
    min_value=0, max_value=5, step=1, key="c5"
)

# ---------- CANDADO 6 ----------
st.markdown("### 🔒 Candado 6 — Entorno auditivo")
st.write("¿Cuántas afirmaciones son VERDADERAS para favorecer la comunicación con Julio?")

st.write("""
1. Hablarle de frente y procurar que pueda ver el rostro de quien habla.  
2. Aumentar el ruido de fondo para estimular la discriminación auditiva.  
3. Disminuir el ruido ambiental y hablar con claridad, sin gritar.  
4. Hablar únicamente desde detrás del paciente para evitar distracciones.
""")

c6 = st.number_input(
    "Cantidad total de afirmaciones verdaderas:",
    min_value=0, max_value=4, step=1, key="c6"
)

st.divider()

# ---------- VERIFICACIÓN ----------
if st.button("🔓 Verificar Código de Salida", use_container_width=True):
    letra1 = "B" if "Diabetes" in c1 else ""
    num1 = str(c2)
    num2 = str(c3)
    letra2 = "B" if "Otoscopia" in c4 else ""
    num3 = str(c5)
    num4 = str(c6)

    codigo_ingresado = f"{letra1}{num1}{num2}{letra2}{num3}{num4}"

    if codigo_ingresado == "B53B32":
        st.success(
            "🎉 ¡Felicidades! Has descifrado el Código de Alta ICOPE: **B53B32**. "
            "El plan de atención de Julio está validado."
        )
        st.balloons()

        with st.expander("🩺 Ver razonamiento de los candados"):
            st.markdown("""
**Candado 1 — B:** la diabetes obliga a una evaluación ocular dirigida por el riesgo de enfermedad ocular asociada.

**Candado 2 — 5:** las cinco medidas propuestas contribuyen a proteger la función visual, reducir riesgos y atender causas modificables.

**Candado 3 — 3:** la corrección óptica debe individualizarse con base en la evaluación visual y las necesidades funcionales de la persona.

**Candado 4 — B:** la otoscopia permite detectar causas tratables u obstrucciones; la asimetría marcada, el dolor o la otorrea requieren valoración específica.

**Candado 5 — 3:** para este escape room, 48 dB HL corresponde a la categoría III definida por el ejercicio.

**Candado 6 — 2:** son correctas las afirmaciones 1 y 3: contacto visual, menor ruido ambiental y comunicación clara.
""")
    else:
        st.error(
            f"❌ Código incorrecto: **{codigo_ingresado or 'incompleto'}**. "
            "Revisa los fundamentos clínicos y vuelve a intentarlo."
        )

        # Retroalimentación sin revelar todo el código de golpe
        pistas = []
        if "Diabetes" not in c1:
            pistas.append("Candado 1: revisa qué antecedente obliga a una valoración ocular dirigida.")
        if c2 != 5:
            pistas.append("Candado 2: piensa en prevención, seguridad del entorno y atención de causas tratables.")
        if c3 != 3:
            pistas.append("Candado 3: la prescripción óptica debe ser individualizada.")
        if "Otoscopia" not in c4:
            pistas.append("Candado 4: antes de valorar audición, inspecciona el oído.")
        if c5 != 3:
            pistas.append("Candado 5: revisa la categoría asignada a 48 dB HL en este ejercicio.")
        if c6 != 2:
            pistas.append("Candado 6: prioriza contacto visual, claridad y poco ruido ambiental.")

        if pistas:
            st.warning("💡 **Pistas:**\n\n" + "\n\n".join(f"- {p}" for p in pistas))

st.divider()
st.caption("Escape Room educativo — ICOPE | Capacidad sensorial: visión y audición")
