<h1 align="center">AURUM TRADING</h1>

<h3 align="center">Plataforma modular de análisis cuantitativo y trading algorítmico</h3>

<p align="center">
<strong>QUANTITATIVE ANALYSIS · ALGORITHMIC TRADING · MARKET DATA</strong>
</p>

<p align="center">
<a href="https://github.com/jarasergio/aurum-trading">Repositorio oficial en GitHub</a>
</p>

<hr>

<h2>1. OBJETIVOS DEL PROYECTO</h2>

<p>Aurum Trading es un proyecto de desarrollo de una plataforma propia de análisis de mercados financieros y trading algorítmico, construida con Python, FastAPI y PostgreSQL.</p>

<p>El objetivo es desarrollar una arquitectura modular, escalable y multi-instrumento que permita gestionar datos de mercado, desarrollar estrategias cuantitativas, realizar backtesting, administrar riesgos y, en una etapa futura, integrar diferentes brokers.</p>

<p>El proyecto contempla una interfaz web profesional para visualizar y controlar el sistema desde un único lugar.</p>

<h3>Instrumentos financieros</h3>

<p>La arquitectura está diseñada para trabajar con diferentes mercados:</p>

<ul>
<li><strong>XAU/USD:</strong> oro.</li>
<li><strong>EUR/USD:</strong> Forex.</li>
<li><strong>NASDAQ:</strong> índices.</li>
<li><strong>DOW JONES:</strong> índices.</li>
<li><strong>BTC/USD:</strong> criptomonedas.</li>
<li><strong>Otros instrumentos:</strong> posibilidad de incorporar nuevos mercados e instrumentos financieros.</li>
</ul>

<p>La incorporación de nuevos instrumentos no debe requerir modificaciones estructurales importantes en el sistema.</p>

<h3>Funcionalidades previstas</h3>

<ul>
<li>Gestión de instrumentos financieros.</li>
<li>Obtención de datos de mercado.</li>
<li>Cotizaciones y precios en tiempo real.</li>
<li>Almacenamiento de datos históricos.</li>
<li>Gestión de temporalidades.</li>
<li>Validación y normalización de datos.</li>
<li>Indicadores técnicos.</li>
<li>Análisis cuantitativo.</li>
<li>Estrategias algorítmicas.</li>
<li>Backtesting.</li>
<li>Gestión de posiciones y órdenes.</li>
<li>Gestión de riesgo.</li>
<li>Trading simulado.</li>
<li>Integración futura con brokers.</li>
<li>Dashboard web.</li>
<li>Estadísticas y seguimiento del rendimiento.</li>
</ul>

<hr>

<h2>2. ESTADO ACTUAL DEL DESARROLLO</h2>

<p>El proyecto se encuentra en la fase inicial de construcción del backend.</p>

<table>
<thead>
<tr>
<th>Módulo</th>
<th>Estado</th>
</tr>
</thead>
<tbody>
<tr><td>Infraestructura de desarrollo</td><td>Completado</td></tr>
<tr><td>Repositorio Git y GitHub</td><td>Completado</td></tr>
<tr><td>Entorno Python</td><td>Completado</td></tr>
<tr><td>PostgreSQL</td><td>Completado</td></tr>
<tr><td>SQLAlchemy</td><td>Completado</td></tr>
<tr><td>Configuración de FastAPI</td><td>Completado</td></tr>
<tr><td>Pydantic Settings</td><td>Completado</td></tr>
<tr><td>Alembic y migraciones</td><td>Completado</td></tr>
<tr><td>Modelo de instrumentos</td><td>Completado</td></tr>
<tr><td>API REST CRUD de instrumentos</td><td>Completado y verificado</td></tr>
<tr><td>Arquitectura Market Data</td><td>Pendiente</td></tr>
<tr><td>Cotizaciones de mercado</td><td>Pendiente</td></tr>
<tr><td>Datos históricos OHLCV</td><td>Pendiente</td></tr>
<tr><td>Validación de datos financieros</td><td>Pendiente</td></tr>
<tr><td>Indicadores técnicos</td><td>Pendiente</td></tr>
<tr><td>Estrategias algorítmicas</td><td>Pendiente</td></tr>
<tr><td>Backtesting</td><td>Pendiente</td></tr>
<tr><td>Gestión de riesgo</td><td>Pendiente</td></tr>
<tr><td>Trading simulado</td><td>Pendiente</td></tr>
<tr><td>Frontend React</td><td>Pendiente</td></tr>
<tr><td>Integración con brokers</td><td>Pendiente</td></tr>
</tbody>
</table>

<p>Las funcionalidades pendientes forman parte de la hoja de ruta y no deben considerarse implementadas.</p>

<hr>

<h2>3. TECNOLOGÍAS UTILIZADAS</h2>

<h3>Backend</h3>

<table>
<thead>
<tr><th>Tecnología</th><th>Función</th></tr>
</thead>
<tbody>
<tr><td>Python 3.14</td><td>Lenguaje principal</td></tr>
<tr><td>FastAPI</td><td>Framework de API REST</td></tr>
<tr><td>Uvicorn</td><td>Servidor ASGI</td></tr>
<tr><td>SQLAlchemy</td><td>ORM y acceso a datos</td></tr>
<tr><td>Psycopg</td><td>Conexión con PostgreSQL</td></tr>
<tr><td>Alembic</td><td>Migraciones de base de datos</td></tr>
<tr><td>Pydantic 2</td><td>Validación de datos</td></tr>
<tr><td>Pydantic Settings</td><td>Configuración de la aplicación</td></tr>
</tbody>
</table>

<h3>Análisis cuantitativo y datos</h3>

<table>
<thead>
<tr><th>Tecnología</th><th>Función</th></tr>
</thead>
<tbody>
<tr><td>Pandas</td><td>Procesamiento de datos</td></tr>
<tr><td>NumPy</td><td>Cálculo numérico</td></tr>
<tr><td>pandas-ta u otra biblioteca compatible</td><td>Indicadores técnicos</td></tr>
<tr><td>backtesting.py (previsto)</td><td>Backtesting</td></tr>
</tbody>
</table>

<h3>Base de datos</h3>

<ul>
<li>PostgreSQL 18.6.</li>
</ul>

<h3>Frontend previsto</h3>

<ul>
<li>React.</li>
<li>TypeScript.</li>
<li>Vite.</li>
<li>TradingView Lightweight Charts o una alternativa compatible.</li>
<li>WebSockets para actualizaciones en vivo.</li>
</ul>

<h3>Desarrollo y control de calidad</h3>

<ul>
<li>Git.</li>
<li>GitHub.</li>
<li>Visual Studio Code.</li>
<li>NVM.</li>
<li>Node.js 26.</li>
<li>npm.</li>
<li>Pytest.</li>
<li>HTTPX.</li>
<li>Ruff.</li>
</ul>

<hr>

<h2>4. ENTORNO DE DESARROLLO</h2>

<p>El entorno principal de desarrollo está preparado sobre Ubuntu.</p>

<table>
<thead>
<tr><th>Componente</th><th>Configuración</th></tr>
</thead>
<tbody>
<tr><td>Sistema operativo</td><td>Ubuntu 26.04.1 LTS</td></tr>
<tr><td>Arquitectura</td><td>x86_64</td></tr>
<tr><td>Equipo</td><td>mini-PC</td></tr>
<tr><td>Editor</td><td>Visual Studio Code Portable</td></tr>
<tr><td>Python</td><td>3.14.4</td></tr>
<tr><td>Node.js</td><td>26.13.0</td></tr>
<tr><td>npm</td><td>11.20.0</td></tr>
<tr><td>PostgreSQL</td><td>18.6</td></tr>
<tr><td>Git</td><td>2.53.0</td></tr>
<tr><td>Entorno virtual</td><td>.venv</td></tr>
</tbody>
</table>

<h3>Ubicación del proyecto</h3>

<pre>
/home/sergio/AURUM-DEV/Projects/aurum-trading/
</pre>

<h3>Repositorio GitHub</h3>

<p><a href="https://github.com/jarasergio/aurum-trading">https://github.com/jarasergio/aurum-trading</a></p>

<p><strong>Rama principal:</strong> <code>main</code>.</p>

<hr>

<h2>5. ARQUITECTURA DEL PROYECTO</h2>

<p>La arquitectura del backend está organizada por responsabilidades, separando API, configuración, acceso a datos, modelos, esquemas y servicios.</p>

<h3>Estructura actual y prevista</h3>

<pre>
aurum-trading/
│
├── .env
├── .env.example
├── .gitignore
├── alembic.ini
│
├── backend/
│   │
│   ├── alembic/
│   │   ├── versions/
│   │   │   └── 3e9d19027571_create_instruments_table.py
│   │   ├── env.py
│   │   ├── README
│   │   └── script.py.mako
│   │
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   │
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── instruments.py
│   │   │
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   └── config.py
│   │   │
│   │   ├── db/
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   └── session.py
│   │   │
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── instrument.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   └── instrument.py
│   │   │
│   │   └── services/
│   │       ├── __init__.py
│   │       └── instrument_service.py
│   │
│   └── tests/
│
├── frontend/
├── docs/
├── research/
├── scripts/
└── .github/
    └── workflows/
</pre>

<p>La estructura mostrada recoge los componentes principales y las carpetas previstas para el crecimiento del proyecto. Los módulos todavía no implementados se incorporarán progresivamente.</p>

<h3>Principios arquitectónicos</h3>

<ol>
<li>Separación de responsabilidades.</li>
<li>Arquitectura modular y escalable.</li>
<li>Independencia entre instrumentos financieros.</li>
<li>Separación entre proveedores de datos, estrategias y brokers.</li>
<li>Normalización de los datos antes de utilizarlos.</li>
<li>Separación entre lógica de negocio y API.</li>
<li>Persistencia mediante PostgreSQL.</li>
<li>Migraciones de base de datos controladas mediante Alembic.</li>
<li>Pruebas automatizadas para las funcionalidades principales.</li>
<li>Separación estricta entre simulación y ejecución real.</li>
</ol>

<hr>

<h2>6. BASE DE DATOS</h2>

<p>La base de datos principal es PostgreSQL.</p>

<h3>Configuración actual</h3>

<table>
<thead>
<tr><th>Elemento</th><th>Valor</th></tr>
</thead>
<tbody>
<tr><td>Motor</td><td>PostgreSQL</td></tr>
<tr><td>Versión</td><td>18.6</td></tr>
<tr><td>Base de datos</td><td><code>aurum_trading</code></td></tr>
<tr><td>Usuario</td><td><code>aurum_app</code></td></tr>
<tr><td>ORM</td><td>SQLAlchemy</td></tr>
<tr><td>Migraciones</td><td>Alembic</td></tr>
</tbody>
</table>

<p>La conexión se configura mediante variables de entorno y Pydantic Settings.</p>

<p>Las credenciales deben permanecer en <code>.env</code> y nunca deben subirse al repositorio.</p>

<h3>Modelo implementado: Instrument</h3>

<p>La primera entidad del sistema es <strong>Instrument</strong>.</p>

<p>Representa los instrumentos financieros que podrá gestionar Aurum Trading.</p>

<table>
<thead>
<tr><th>Campo</th><th>Tipo</th></tr>
</thead>
<tbody>
<tr><td>id</td><td>Integer</td></tr>
<tr><td>symbol</td><td>String(32)</td></tr>
<tr><td>name</td><td>String(120)</td></tr>
<tr><td>asset_class</td><td>String(30)</td></tr>
<tr><td>market</td><td>String(30)</td></tr>
<tr><td>base_currency</td><td>String(12)</td></tr>
<tr><td>quote_currency</td><td>String(12)</td></tr>
<tr><td>is_active</td><td>Boolean</td></tr>
<tr><td>created_at</td><td>DateTime</td></tr>
</tbody>
</table>

<p>El campo <code>symbol</code> tiene una restricción de unicidad.</p>

<p>La desactivación de instrumentos es lógica: los registros no se eliminan físicamente de la base de datos.</p>

<h3>Instrumentos registrados actualmente</h3>

<table>
<thead>
<tr><th>ID</th><th>Símbolo</th><th>Nombre</th><th>Estado</th></tr>
</thead>
<tbody>
<tr><td>1</td><td>EURUSD</td><td>Euro / US Dollar Spot</td><td>Activo</td></tr>
<tr><td>3</td><td>GBPUSD</td><td>British Pound / US Dollar</td><td>Activo</td></tr>
</tbody>
</table>

<hr>

<h2>7. API REST IMPLEMENTADA</h2>

<p>Actualmente está implementada la gestión CRUD de instrumentos.</p>

<table>
<thead>
<tr><th>Método</th><th>Endpoint</th><th>Descripción</th></tr>
</thead>
<tbody>
<tr><td>GET</td><td><code>/instruments/</code></td><td>Listar instrumentos activos</td></tr>
<tr><td>POST</td><td><code>/instruments/</code></td><td>Crear instrumento</td></tr>
<tr><td>GET</td><td><code>/instruments/{instrument_id}</code></td><td>Consultar instrumento</td></tr>
<tr><td>PATCH</td><td><code>/instruments/{instrument_id}</code></td><td>Modificar instrumento</td></tr>
<tr><td>DELETE</td><td><code>/instruments/{instrument_id}</code></td><td>Desactivar instrumento</td></tr>
</tbody>
</table>

<h3>Comportamientos verificados</h3>

<ul>
<li>Creación de instrumentos.</li>
<li>Consulta por identificador.</li>
<li>Listado de instrumentos activos.</li>
<li>Modificación de datos.</li>
<li>Desactivación lógica.</li>
<li>Reactivación mediante PATCH.</li>
<li>Exclusión de instrumentos inactivos del listado.</li>
<li>Rechazo de símbolos duplicados mediante HTTP 409 Conflict.</li>
</ul>

<p>La API utiliza esquemas Pydantic para validar los datos recibidos.</p>

<hr>

<h2>8. INSTALACIÓN Y EJECUCIÓN</h2>

<p>Los siguientes pasos corresponden al entorno de desarrollo preparado sobre Ubuntu.</p>

<h3>Requisitos</h3>

<ul>
<li>Ubuntu.</li>
<li>Python 3.14.</li>
<li>PostgreSQL 18.</li>
<li>Git.</li>
<li>Entorno virtual Python.</li>
</ul>

<h3>Clonar el repositorio</h3>

<pre><code>git clone git@github.com:jarasergio/aurum-trading.git

cd aurum-trading</code></pre>

<h3>Activar el entorno virtual</h3>

<pre><code>source .venv/bin/activate</code></pre>

<h3>Configurar las variables de entorno</h3>

<p>El proyecto utiliza <code>.env.example</code> como plantilla de configuración.</p>

<pre><code>cp .env.example .env</code></pre>

<p>Completar los valores necesarios para la conexión a PostgreSQL y la configuración de la aplicación.</p>

<p>No introducir credenciales reales en archivos versionados.</p>

<h3>Migraciones de base de datos</h3>

<p>Desde la raíz del proyecto:</p>

<pre><code>alembic upgrade head</code></pre>

<p>Este comando aplica las migraciones pendientes.</p>

<h3>Ejecutar el backend</h3>

<p>Desde el directorio <code>backend</code>, con el entorno virtual activado:</p>

<pre><code>uvicorn app.main:app --reload</code></pre>

<p>La dirección local habitual de desarrollo será:</p>

<pre>http://127.0.0.1:8000</pre>

<p>La documentación interactiva de FastAPI estará disponible en:</p>

<pre>http://127.0.0.1:8000/docs</pre>

<p><strong>Nota:</strong> la configuración de arranque, las variables de entorno y los comandos de ejecución deberán mantenerse sincronizados con los archivos reales del proyecto.</p>

<hr>

<h2>9. SEGURIDAD Y GESTIÓN DEL RIESGO</h2>

<p>La seguridad es un principio fundamental del desarrollo de Aurum Trading.</p>

<ul>
<li>Las credenciales nunca se almacenan en GitHub.</li>
<li>Los archivos <code>.env</code> permanecen excluidos del control de versiones.</li>
<li>La ejecución real permanece deshabilitada inicialmente.</li>
<li>El sistema debe distinguir claramente entre simulación y trading real.</li>
<li>Las operaciones deberán respetar límites de riesgo configurables.</li>
<li>Los datos de mercado deben validarse antes de utilizarse.</li>
<li>Se deben registrar las decisiones y los errores del sistema.</li>
<li>Deben existir mecanismos de protección frente a desconexiones y órdenes duplicadas.</li>
<li>Las operaciones deberán poder reconciliarse con el estado del broker cuando exista integración.</li>
</ul>

<h3>Configuración inicial de trading</h3>

<pre><code>TRADING_MODE=simulation
TRADING_ENABLED=false</code></pre>

<p>Estos valores representan la política prevista para el proyecto y deberán mantenerse de acuerdo con la configuración real de la aplicación.</p>

<p><strong>Importante:</strong> Aurum Trading es un proyecto de desarrollo tecnológico y análisis financiero. Ninguna estrategia garantiza rentabilidad y los resultados históricos no aseguran resultados futuros.</p>

<hr>

<h2>10. HOJA DE RUTA</h2>

<p>El desarrollo se realizará progresivamente, validando cada módulo antes de continuar.</p>

<h3>ETAPA 1 — Infraestructura</h3>

<p><strong>Estado: COMPLETADA</strong></p>

<ul>
<li>Preparación de Ubuntu.</li>
<li>VS Code Portable.</li>
<li>Python y entorno virtual.</li>
<li>Node.js y NVM.</li>
<li>Git y GitHub.</li>
<li>PostgreSQL.</li>
</ul>

<h3>ETAPA 2 — Backend y persistencia</h3>

<p><strong>Estado: COMPLETADA</strong></p>

<ul>
<li>FastAPI.</li>
<li>SQLAlchemy.</li>
<li>Psycopg.</li>
<li>Pydantic Settings.</li>
<li>Alembic.</li>
<li>Modelo Instrument.</li>
<li>Migración inicial.</li>
</ul>

<h3>ETAPA 3 — API de instrumentos</h3>

<p><strong>Estado: COMPLETADA</strong></p>

<ul>
<li>CRUD de instrumentos.</li>
<li>Validaciones.</li>
<li>Control de duplicados.</li>
<li>Desactivación lógica.</li>
<li>Reactivación.</li>
<li>Verificación de operaciones.</li>
</ul>

<h3>ETAPA 4 — Market Data</h3>

<p><strong>Estado: SIGUIENTE ETAPA</strong></p>

<ul>
<li>Diseño de la arquitectura de proveedores.</li>
<li>Integración de fuentes de datos.</li>
<li>Cotizaciones de mercado.</li>
<li>Datos históricos OHLCV.</li>
<li>Gestión de temporalidades.</li>
<li>Validación de precios.</li>
<li>API de datos de mercado.</li>
</ul>

<h3>ETAPA 5 — Análisis cuantitativo</h3>

<ul>
<li>Indicadores técnicos.</li>
<li>Procesamiento de series temporales.</li>
<li>Señales de mercado.</li>
<li>Herramientas de análisis.</li>
</ul>

<h3>ETAPA 6 — Estrategias y backtesting</h3>

<ul>
<li>Arquitectura de estrategias.</li>
<li>Generación de señales.</li>
<li>Simulación de operaciones.</li>
<li>Backtesting histórico.</li>
<li>Comisiones y costes.</li>
<li>Métricas de rendimiento.</li>
</ul>

<h3>ETAPA 7 — Gestión del riesgo</h3>

<ul>
<li>Tamaño de posiciones.</li>
<li>Stop-loss y take-profit.</li>
<li>Límites de pérdidas.</li>
<li>Control de exposición.</li>
<li>Protección del capital.</li>
</ul>

<h3>ETAPA 8 — Dashboard web</h3>

<ul>
<li>React y TypeScript.</li>
<li>Diseño oscuro con detalles dorados.</li>
<li>Identidad visual Aurum Trading.</li>
<li>Gráficos financieros.</li>
<li>Estadísticas.</li>
<li>Posiciones e historial.</li>
<li>Estado del motor de trading.</li>
</ul>

<h3>ETAPA 9 — Integración en tiempo real</h3>

<ul>
<li>WebSockets.</li>
<li>Actualizaciones de cotizaciones.</li>
<li>Alertas.</li>
<li>Monitorización del sistema.</li>
</ul>

<h3>ETAPA 10 — Integración con brokers</h3>

<ul>
<li>Evaluación de proveedores.</li>
<li>Integración mediante API.</li>
<li>Gestión de órdenes.</li>
<li>Sincronización de posiciones.</li>
<li>Controles de seguridad.</li>
<li>Pruebas antes de cualquier ejecución real.</li>
</ul>

<hr>

<h2>11. CONTROL DE VERSIONES</h2>

<p>El proyecto utiliza Git y GitHub.</p>

<h3>Repositorio remoto</h3>

<pre>git@github.com:jarasergio/aurum-trading.git</pre>

<p><strong>Rama principal:</strong> <code>main</code>.</p>

<p>Se utilizarán commits pequeños y descriptivos.</p>

<h3>Ejemplos de commits</h3>

<pre><code>feat: add market data module
feat: implement historical candles
fix: correct instrument validation
refactor: improve database services
test: add market data tests
docs: update project documentation</code></pre>

<h3>Comandos habituales</h3>

<p><strong>Comprobar el estado del repositorio:</strong></p>

<pre><code>git status</code></pre>

<p><strong>Añadir cambios:</strong></p>

<pre><code>git add .</code></pre>

<p><strong>Crear un commit:</strong></p>

<pre><code>git commit -m "descriptive commit message"</code></pre>

<p><strong>Subir los cambios:</strong></p>

<pre><code>git push origin main</code></pre>

<h3>Archivos que no deben subirse</h3>

<ul>
<li><code>.env</code></li>
<li><code>.venv/</code></li>
<li><code>node_modules/</code></li>
<li>Archivos de caché.</li>
<li>Logs.</li>
<li>Bases de datos locales.</li>
<li>Datos históricos voluminosos.</li>
<li>Credenciales.</li>
<li>Archivos temporales.</li>
</ul>

<hr>

<h2>12. DOCUMENTACIÓN DEL PROYECTO</h2>

<p>La documentación deberá evolucionar junto con el código.</p>

<p>Se contempla incorporar:</p>

<pre>
docs/
├── architecture.md
├── risk-management.md
├── market-data.md
├── database.md
└── development-guide.md
</pre>

<p>Cada módulo importante deberá documentar:</p>

<ul>
<li>Objetivo.</li>
<li>Arquitectura.</li>
<li>Responsabilidades.</li>
<li>Modelos de datos.</li>
<li>Endpoints.</li>
<li>Configuración.</li>
<li>Pruebas.</li>
<li>Decisiones técnicas.</li>
</ul>

<hr>

<h2>13. ESTADO DE SEGURIDAD DEL PROYECTO</h2>

<p>Aurum Trading se encuentra actualmente en fase de desarrollo.</p>

<p>No existe todavía un motor de trading completo ni una integración operativa con brokers.</p>

<p>El objetivo inmediato es desarrollar y validar la infraestructura de datos y análisis antes de implementar cualquier funcionalidad de ejecución.</p>

<p>La ejecución real no forma parte de la fase actual.</p>

<hr>

<h2>14. PRÓXIMO PASO DE DESARROLLO</h2>

<p>El siguiente objetivo es implementar el módulo <strong>Market Data</strong>.</p>

<p>Antes de escribir código se definirá:</p>

<ol>
<li>La arquitectura de proveedores de datos.</li>
<li>La estructura de cotizaciones.</li>
<li>El modelo de almacenamiento histórico OHLCV.</li>
<li>La gestión de temporalidades.</li>
<li>Las reglas de validación de precios.</li>
<li>Los servicios de consulta.</li>
<li>Los endpoints de la API.</li>
</ol>

<p>El diseño deberá permitir incorporar diferentes proveedores de datos sin modificar la lógica central de Aurum Trading.</p>

<hr>

<h2>15. FILOSOFÍA DEL PROYECTO</h2>

<p>Aurum Trading se desarrollará siguiendo estos principios:</p>

<ul>
<li>Arquitectura modular.</li>
<li>Código limpio y mantenible.</li>
<li>Separación de responsabilidades.</li>
<li>Escalabilidad multi-instrumento.</li>
<li>Datos fiables y reproducibles.</li>
<li>Pruebas antes de incorporar nuevas funcionalidades.</li>
<li>Seguridad desde el diseño.</li>
<li>Gestión del riesgo como prioridad.</li>
<li>Documentación actualizada.</li>
<li>Desarrollo incremental y controlado.</li>
</ul>

<p><strong>La prioridad no es desarrollar rápidamente un bot que opere, sino construir una plataforma sólida, verificable y preparada para evolucionar.</strong></p>

<hr>

<h2 align="center">AURUM TRADING</h2>

<p align="center">
<strong>Quantitative Analysis · Algorithmic Trading · Market Data</strong>
</p>

<p align="center">
<a href="https://github.com/jarasergio/aurum-trading">GitHub Repository</a>
</p>