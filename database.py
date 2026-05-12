

ANTES (búsqueda + pre-adopción)

Pasan:

Fundaciones publican animales en Instagram/Facebook y responden DMs manualmente.

Adoptantes navegan múltiples webs/redes y guardan capturas.

Formularios de adopción se envían por Google Forms/email.

Intentan (workarounds):

Fundaciones usan Excel + WhatsApp para trackear interesados.

Adoptantes crean listas/notas para comparar mascotas.

Momento emocional:

Frustración al repetir datos y no recibir respuesta (adivinanza: 2-5 días sin feedback).

DURANTE (proceso de adopción + match)

Pasan:

Entrevistas por teléfono/WhatsApp sin registro estructurado.

Intercambio de documentos (DNI, contrato) por email/Drive.

Coordinación de visitas y entrega del animal manualmente.

Intentan:

Fundaciones copian/pegan historiales en chats para no perder contexto.

Adoptantes preguntan en foros/Reddit sobre comportamiento de la raza.

Momento emocional:

Ansiedad al no saber si “van bien” en el proceso (silencios largos).

DESPUÉS (post-adopción + seguimiento)

Pasan:

Fundaciones piden fotos/videos por WhatsApp cada X semanas.

Adoptantes buscan en YouTube/Google cómo entrenar o adaptar al animal.

Casos problemáticos (conducta/salud) se comunican tarde.

Intentan:

Fundaciones crean recordatorios manuales en calendarios.

Adoptantes envían audios largos describiendo problemas.

Momento emocional:

Estrés cuando surgen problemas de conducta y no hay guía clara.

Momento más doloroso: DURANTE → falta de visibilidad y coordinación del proceso (estado + documentos + comunicación fragmentada).

Por qué ahí el MVP: Es donde se caen adopciones y se generan malos matches; impacta directamente en conversión y confianza.

MVP podría hacer: Un “pipeline de adopción” compartido tipo Kanban con estado en tiempo real + checklist de documentos + chat centralizado por caso.


<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Mapa de Viaje del Usuario</title>
<style>
  body {
    margin: 0;
    font-family: system-ui, sans-serif;
    color: #1A1A1A;
    background: #FAF7F2;
  }
  .topbar {
    display: flex;
    align-items: center;
    background: #1E2761;
    color: white;
    padding: 16px 24px;
    font-family: Georgia, serif;
    font-size: 18px;
  }
  .topbar::before {
    content: "";
    width: 8px;
    height: 100%;
    background: #F96167;
    margin-right: 16px;
  }
  .container {
    display: flex;
    padding: 24px;
    gap: 16px;
  }
  .column {
    flex: 1;
    background: #FAF7F2;
    border: 1px solid #eee;
    padding: 16px;
  }
  .card {
    background: #FAF7F2;
    padding: 16px;
    border: 1px solid #ddd;
  }
  h2 {
    font-family: Georgia, serif;
    color: #1E2761;
    border-bottom: 2px solid #F96167;
    padding-bottom: 4px;
  }
  h3 {
    margin-top: 12px;
    font-size: 14px;
    color: #1E2761;
  }
  ul {
    margin: 4px 0 12px 16px;
  }
  .feels {
    font-style: italic;
    color: #6B6B6B;
  }
  .break {
    color: #F96167;
  }
  .bar {
    height: 10px;
    background: #eee;
    position: relative;
  }
  .bar span {
    display: block;
    height: 100%;
    background: #F96167;
  }
  .mvp {
    margin: 24px;
    padding: 16px;
    background: #1E2761;
    color: white;
    font-family: Georgia, serif;
  }
  .footer {
    text-align: center;
    font-size: 12px;
    color: #6B6B6B;
    margin: 16px;
  }
  @media print {
    body { zoom: 0.9; }
  }
</style>
</head>
<body>

<div class="topbar">
  Sofía, 32, adoptante primeriza — altas devoluciones por mala adaptación y falta de seguimiento
</div>

<div class="container">

  <div class="column">
    <div class="card">
      <h2>ANTES</h2>

      <h3>Qué HACE</h3>
      <ul>
        <li>Busca adoptar con intención de “hacer algo bueno”</li>
        <li>Se informa superficialmente sobre cuidado</li>
        <li>Contacta con fundaciones</li>
      </ul>

      <h3>Qué SIENTE</h3>
      <div class="feels">
        <p>*Ilusión por adoptar*</p>
        <p>*Subestima la dificultad*</p>
      </div>

      <h3>Qué se ROMPE</h3>
      <ul class="break">
        <li>Falta de educación previa clara</li>
      </ul>

      <h3>PUNTAJE DE DOLOR</h3>
      <div class="bar"><span style="width:40%"></span></div>
    </div>
  </div>

  <div class="column">
    <div class="card">
      <h2>DURANTE</h2>

      <h3>Qué HACE</h3>
      <ul>
        <li>Adopta y lleva al animal a casa</li>
        <li>Intenta adaptarlo sin guía estructurada</li>
        <li>Contacta a la fundación de forma puntual</li>
      </ul>

      <h3>Qué SIENTE</h3>
      <div class="feels">
        <p>*“Nadie me dijo que sería tan difícil”*</p>
        <p>*Frustración en el día a día*</p>
      </div>

      <h3>Qué se ROMPE</h3>
      <ul class="break">
        <li>Falta de guía clara de adaptación</li>
        <li>Comunicación inconsistente</li>
      </ul>

      <h3>PUNTAJE DE DOLOR</h3>
      <div class="bar"><span style="width:90%"></span></div>
    </div>
  </div>

  <div class="column">
    <div class="card">
      <h2>DESPUÉS</h2>

      <h3>Qué HACE</h3>
      <ul>
        <li>La fundación intenta hacer seguimiento</li>
        <li>Gestionan casos en herramientas dispersas</li>
        <li>Algunos casos terminan en devolución</li>
      </ul>

      <h3>Qué SIENTE</h3>
      <div class="feels">
        <p>*“Queremos hacer seguimiento, pero no nos da el tiempo”*</p>
        <p>*Agotamiento operativo*</p>
      </div>

      <h3>Qué se ROMPE</h3>
      <ul class="break">
        <li>Pérdida de seguimiento</li>
        <li>Carga operativa insostenible</li>
      </ul>

      <h3>PUNTAJE DE DOLOR</h3>
      <div class="bar"><span style="width:100%"></span></div>
    </div>
  </div>

</div>

<div class="mvp">
  <strong>ZONA DE OPORTUNIDAD MVP</strong><br><br>
  DURANTE: Momento donde Sofía se siente desbordada → aquí ocurre la falta de guía que dispara devoluciones.<br>
  DESPUÉS: Seguimiento fallido por carga operativa → aquí se pierde visibilidad y control del proceso.
</div>

<div class="footer">
  DESIGNING INTELLIGENCE · MAPA DE VIAJE DEL USUARIO
</div>

</body>
</html>

# ROL
Eres un prompt engineer que ha armado 1,000+ builds de vibecoding.
Tu trabajo: convertir mi research de Sesión 1 en el bloque V + I
perfecto — la base de cada build prompt que voy a usar después.
# QUÉ SIGNIFICAN V + I
V = VISION · mi contexto vivido. Qué construyo, para quién, por qué
importa, dónde vive el MVP, qué constraints de stack tengo.
I = IDENTITY · la expertise técnica de build que la IA necesita para
mandar MI producto exacto. Stack mastery, librerías nombradas,
features hard, failure modes. NO 'un developer' — un builder de ESTO.
# CONTEXTO DOWNSTREAM — cada prompt posterior es SOLO-BROWSER
Después de este V+I, la estudiante corre Build → Functionality → Branding →
Refine en 3 tabs solo: chat del LLM · github.com · share.streamlit.io.
SIN terminal · SIN VS Code · SIN Python local. El párrafo IDENTITY debe
anclarse a un stack que corra en Streamlit Community Cloud free tier:
Streamlit + Python stdlib + libs pip-instalables + Google Fonts CDN. Nada
que requiera npm, binarios nativos o build step.
# MIS INPUTS (usa solo esto — no inventes)
<session_1>
problem: Los refugios de animales se enfrentan a flujos de trabajo fragmentados.

La mayoría de los procesos de adopción se llevan a cabo mediante hojas de cálculo, mensajes de WhatsApp, formularios en papel, mensajes directos en redes sociales y sistemas desconectados. Esto genera caos operativo en los refugios e incertidumbre para los adoptantes.

Además, los adoptantes suelen sentirse desamparados tras llevar una mascota a casa, lo que provoca ansiedad, problemas de adaptación y adopciones fallidas.

Petto se propuso rediseñar todo el proceso de adopción, desde el descubrimiento de una mascota hasta el cuidado a largo plazo posterior a la adopción.  user: Refugios/Fundaciones y Adoptantes
idea: Crear una plataforma digital que en lugar de diseñar experiencias aisladas, creamos una plataforma interconectada donde cada producto respalda una etapa diferente del proceso de adopción.
industry: industria de las mascotas y animales
why_me: porque quiero ayudar a mitigar el abandono animal
mvp_focus: no poder ayudar a adaptar a la nueva mascota al estilo de vida y nuevo hogar technical_constraint: [Streamlit free + GitHub web + free LLM] [Streamlit free + GitHub web + free LLM]
</session_1>
# PROCESO — corre en orden
## /diagnose — razonamiento silencioso (NO lo imprimas)
Antes de generar V + I, decide en silencio:
· ¿Cuál es la industria REAL detrás del problema? (ej. 'ilustración'
es 'workflow freelance creativo')
· ¿Qué 2-3 FEATURES HARD requiere este MVP para funcionar?
(ej. version diff · trail PDF de aprobación · trigger de email)
· ¿Qué LIBRERÍAS / FRAMEWORKS debe dominar la IA al pelo para
mandarlas?
· ¿Qué FAILURE MODES van a morder este stack exacto (ej. Streamlit
session_state en rerun · 200MB upload · sleep de free tier)?
· ¿Qué valores + sesgo de ingeniería caben con un founder no-técnico?
## /vision — produce el bloque V
Un párrafo Vision completo, listo para pegar, que:
· Diga qué estoy construyendo (1 frase)
· Nombre al usuario específico de <session_1>.user
· Explique por qué importa usando <session_1>.why_me
· Cierre el scope MVP a <session_1>.mvp_focus
· Mencione el constraint técnico
Formato: 4-6 frases. Primera persona. Sin relleno.
## /identity — produce el bloque I
Un Identity listo para pegar que ARMA a la IA con las skills exactas
de build para mandar MI producto. Incluye:
· ROL DE INGENIERÍA ESPECÍFICO (NO 'un developer'). Formato: 'un
[tipo de ingeniero] de clase mundial que ha mandado [N] [tipo
exacto de producto]'
· STACK MASTERY — 3 librerías/frameworks nombrados que la IA debe
dominar al pelo (ej. 'Streamlit forms · migraciones SQLite ·
ReportLab para firma PDF'). Sale de tu /diagnose.
· EXPERTISE DE FEATURES — las 2-3 partes HARD de MI build, nombradas
(ej. 'version diff de assets · flujo aprobar-y-bloquear de un
clic · confirmaciones SMTP por email')
· FAILURE MODES — 1-2 edge cases que maneja por default (ej.
'Streamlit session_state se resetea en rerun → SQLite es la verdad')
· 3 VALORES DE INGENIERÍA (ej. 'mandar antes que perfecto · cortar
scope · deploy diario')
· 1 SESGO EXPLÍCITO (ej. 'en duda, corta una feature')
· 1 LÍNEA sobre cómo le habla a MÍ, founder no-técnico
Formato: 6-9 frases. Directo. Listo para construir.
## /scaffold — produce los 3 archivos starter para GitHub web
Imprime 3 archivos que la estudiante creará en github.com ANTES de Build.
Estos son el mínimo para que el <current_state> de Build sea real:
· /app.py — Streamlit hello de 4 líneas con nombre de proyecto
· /requirements.txt — streamlit==1.39.0 (pineado; Build agregará más)
· /runtime.txt — python-3.11 (CRÍTICO: sin él Cloud se cuelga al instalar)
## /test — verifica cada output
· ¿V tiene los 5 elementos (idea/user/por-qué/scope/constraint)?
· ¿I nombra 3 librerías + 2-3 features hard + 1-2 failure modes?
· ¿Un Identity 'developer' genérico pudo producirlo? Si sí, afila.
· ¿Los 3 archivos scaffold están, son pegables, runtime.txt = python-3.11?
# CONTRATO DE OUTPUT
Imprime exactamente:
# VISION
[tu párrafo V · pega arriba de cada prompt posterior]
# IDENTITY
[tu párrafo I · pega arriba de cada prompt posterior]
# STARTER SCAFFOLD — 3 archivos, créalos en GitHub web ANTES de Build
## NEW · CREATE FILE: /app.py
[Streamlit hello world de 4 líneas con nombre del proyecto]
## NEW · CREATE FILE: /requirements.txt
streamlit==1.39.0
## NEW · CREATE FILE: /runtime.txt
python-3.11
Luego: --- END ---
Palabras prohibidas: leverage · unlock · seamless · synergy · vanguardia.
Máx 350 palabras de prosa V+I. Archivos scaffold como bloques de código.
Sin preámbulo. Sin comentarios.

VISION
Estoy construyendo Petto, una plataforma digital para refugios/fundaciones de animales y adoptantes que reorganiza el proceso de adopción en un solo sistema conectado. Quiero reducir el abandono animal eliminando el caos operativo y ayudando a que las mascotas se adapten mejor a su nuevo hogar. El MVP se enfoca específicamente en el seguimiento post-adopción y en ayudar a los adoptantes primerizos a integrar a su mascota a su estilo de vida mediante guía, check-ins y comunicación centralizada. No estoy intentando resolver toda la operación del refugio desde el día uno; el foco es reducir ansiedad, devoluciones y pérdida de seguimiento después de la adopción. El producto debe correr únicamente con Streamlit Community Cloud free tier, GitHub web y herramientas gratuitas basadas en LLM, sin terminal local ni build steps complejos.

IDENTITY
Eres un ingeniero de producto para plataformas de operaciones y onboarding de usuarios de clase mundial que ha lanzado más de 50 herramientas SaaS internas construidas solo con Streamlit y Python para founders no técnicos. Dominas Streamlit forms y session_state, SQLite con sqlite3 del stdlib, y pandas para tablas editables y seguimiento de datos persistentes dentro del free tier de Streamlit Cloud. Sabes construir flujos críticos como seguimiento post-adopción con timelines, formularios multipaso persistentes, dashboards básicos de riesgo de devolución y mensajería/check-ins simulados sin depender de servicios externos pagos. Manejas por defecto los failure modes típicos del stack: session_state se pierde en cada rerun → SQLite es la fuente de verdad; el free tier entra en sleep → persistencia mínima y arranque rápido. Priorizas shipping rápido, scope pequeño y UX extremadamente clara para usuarios no técnicos como fundaciones saturadas y adoptantes ansiosos. En duda, cortas features y mantienes una sola experiencia crítica funcionando de punta a punta antes de agregar más módulos. Escribes código simple, legible y desplegable desde GitHub web sin terminal ni configuraciones manuales. Le hablas al founder como un socio técnico práctico: explicas decisiones en lenguaje simple y siempre propones el camino más corto hacia un MVP usable.

STARTER SCAFFOLD — 3 archivos, créalos en GitHub web ANTES de Build
NEW · CREATE FILE: /app.py
import streamlit as st

st.title("Petto")
st.write("Seguimiento post-adopción para refugios y adoptantes.")
NEW · CREATE FILE: /requirements.txt
streamlit==1.39.0
NEW · CREATE FILE: /runtime.txt
python-3.11
--- END ---


Dame el código comprensivo o detallado de todos los files

Petto Streamlit Mvp Full Scaffold

Petto — MVP Scaffold Completo
Estructura de Archivos
/
├── app.py
├── requirements.txt
├── runtime.txt
├── database.py
├── seed.py
├── utils.py
├── styles.css
├── README.md
└── .streamlit/
    └── config.toml
/app.py
            st.success("Mascota registrada correctamente")
            st.rerun()

elif menu == "Nuevo Adoptante":
    st.subheader("Registrar Adoptante")

    with st.form("adopter_form"):
        full_name = st.text_input("Nombre completo")
        city = st.text_input("Ciudad")
        experience = st.selectbox(
            "Experiencia previa",
            ["Primerizo", "Intermedio", "Experto"]
        )

        submitted = st.form_submit_button("Guardar")

        if submitted:
            add_adopter(full_name, city, experience)
            st.success("Adoptante registrado")
            st.rerun()

elif menu == "Seguimiento":
    st.subheader("Seguimiento Post-Adopción")

    pets = get_pets()
    adopters = get_adopters()

    if not pets or not adopters:
        st.warning("Debes crear mascotas y adoptantes primero")
    else:
        with st.form("followup_form"):
            pet = st.selectbox(
                "Mascota",
                pets,
                format_func=lambda x: x["name"]
            )

            adopter = st.selectbox(
                "Adoptante",
                adopters,
                format_func=lambda x: x["full_name"]
            )

            adaptation_score = st.slider(
                "Nivel de adaptación",
                1,
                10,
                5
            )

            notes = st.text_area("Observaciones")

            submitted = st.form_submit_button("Guardar seguimiento")

            if submitted:
                create_followup(
                    pet["id"],
                    adopter["id"],
                    adaptation_score,
                    notes
                )

                st.success("Seguimiento guardado")
                st.rerun()

    st.divider()

    followups = get_followups()

    if followups:
        df = pd.DataFrame(followups)
        df["risk"] = df["adaptation_score"].apply(risk_label)
        st.dataframe(df, use_container_width=True)
/database.py
    return conn
    cursor.execute(
        "INSERT INTO pets (name, species, age, notes) VALUES (?, ?, ?, ?)",
        (name, species, age, notes)
    )

    conn.commit()
    conn.close()


def add_adopter(full_name, city, experience):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO adopters (full_name, city, experience) VALUES (?, ?, ?)",
        (full_name, city, experience)
    )

    conn.commit()
    conn.close()


def create_followup(pet_id, adopter_id, adaptation_score, notes):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO followups (
            pet_id,
            adopter_id,
            adaptation_score,
            notes
        ) VALUES (?, ?, ?, ?)
        """,
        (pet_id, adopter_id, adaptation_score, notes)
    )

    conn.commit()
    conn.close()


def get_pets():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM pets").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_adopters():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM adopters").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_followups():
    conn = get_connection()

    rows = conn.execute(
        """
        SELECT
            followups.id,
            pets.name AS pet_name,
            adopters.full_name,
            followups.adaptation_score,
            followups.notes
        FROM followups
        JOIN pets ON pets.id = followups.pet_id
        JOIN adopters ON adopters.id = followups.adopter_id
        ORDER BY followups.id DESC
        """
    ).fetchall()

    conn.close()

    return [dict(r) for r in rows]
/utils.py

def risk_label(score):
    if score <= 3:
        return "ALTO"

    if score <= 6:
        return "MEDIO"

    return "BAJO"
/seed.py
from database import init_db, add_pet, add_adopter

init_db()

add_pet("Luna", "Perro", 2, "Ansiedad leve")
add_pet("Milo", "Gato", 1, "Muy sociable")

add_adopter("Sofía Martínez", "Madrid", "Primerizo")
add_adopter("Carlos Pérez", "Barcelona", "Intermedio")

print("Datos demo creados")
/styles.css
.block-container {
    padding-top: 2rem;
}

h1 {
    color: #1E2761;
}

.stButton button {
    background: #F96167;
    color: white;
    border-radius: 10px;
    border: none;
}

.stMetric {
    background: #FAF7F2;
    border-radius: 12px;
    padding: 12px;
}
/requirements.txt
streamlit==1.39.0
pandas==2.2.3
/runtime.txt
python-3.11
/.streamlit/config.toml
[theme]
base="light"
primaryColor="#F96167"
backgroundColor="#FAF7F2"
secondaryBackgroundColor="#FFFFFF"
textColor="#1A1A1A"
font="sans serif"
/README.md
# Petto

Petto es una plataforma de seguimiento post-adopción para refugios y adoptantes.

## Features MVP

- Registro de mascotas
- Registro de adoptantes
- Seguimiento post-adopción
- Dashboard de riesgo de devolución
- Persistencia local con SQLite

## Deploy

1. Subir repositorio a GitHub
2. Ir a Streamlit Community Cloud
3. Conectar repositorio
4. Seleccionar app.py
5. Deploy
Ya tienes el scaffold completo y detallado de Petto listo para copiar a GitHub y desplegar en Streamlit Cloud.


Tengo este error, arreglalo por fa: File "/home/adminuser/venv/lib/python3.11/site-packages/streamlit/runtime/scriptrunner/exec_code.py", line 88, in exec_func_with_error_handling
    result = func()
             ^^^^^^
File "/home/adminuser/venv/lib/python3.11/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 579, in code_to_exec
    exec(code, module.__dict__)
File "/mount/src/petto/app.py", line 3, in <module>
    from database import (

Ese error significa que Streamlit NO está encontrando el archivo database.py.

Normalmente pasa por una de estas 3 razones:

el archivo no existe en GitHub

el nombre está mal escrito (Database.py ≠ database.py)

está dentro de otra carpeta

Haz esto:

En GitHub verifica que tengas EXACTAMENTE esta estructura:

/
├── app.py
├── database.py
├── utils.py
├── requirements.txt
├── runtime.txt
├── styles.css
Verifica que el archivo se llame:

database.py
todo en minúsculas.

Abre database.py y pega esto COMPLETO:

import sqlite3

DB_NAME = "petto.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            species TEXT,
            age INTEGER,
            notes TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS adopters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            city TEXT,
            experience TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS followups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pet_id INTEGER,
            adopter_id INTEGER,
            adaptation_score INTEGER,
            notes TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_pet(name, species, age, notes):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO pets (name, species, age, notes) VALUES (?, ?, ?, ?)",
        (name, species, age, notes)
    )

    conn.commit()
    conn.close()


def add_adopter(full_name, city, experience):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO adopters (full_name, city, experience) VALUES (?, ?, ?)",
        (full_name, city, experience)
    )

    conn.commit()
    conn.close()


def create_followup(pet_id, adopter_id, adaptation_score, notes):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO followups (
            pet_id,
            adopter_id,
            adaptation_score,
            notes
        ) VALUES (?, ?, ?, ?)
        """,
        (pet_id, adopter_id, adaptation_score, notes)
    )

    conn.commit()
    conn.close()


def get_pets():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM pets").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_adopters():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM adopters").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_followups():
    conn = get_connection()

    rows = conn.execute("""
        SELECT
            followups.id,
            pets.name AS pet_name,
            adopters.full_name,
            followups.adaptation_score,
            followups.notes
        FROM followups
        JOIN pets ON pets.id = followups.pet_id
        JOIN adopters ON adopters.id = followups.adopter_id
        ORDER BY followups.id DESC
    """).fetchall()

    conn.close()

    return [dict(r) for r in rows]




