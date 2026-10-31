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

<p>Aurum Trading es una plataforma propia en desarrollo para el análisis de mercados financieros, procesamiento de datos cuantitativos y trading algorítmico, construida con Python, FastAPI y PostgreSQL.</p>

<p>El objetivo es desarrollar una arquitectura modular, escalable y multi-instrumento que permita gestionar datos de mercado, desarrollar estrategias cuantitativas, realizar backtesting, administrar riesgos y, en una etapa futura, integrar diferentes brokers.</p>

<p>El proyecto contempla una interfaz web profesional para visualizar y controlar el sistema desde un único lugar.</p>

<h3>Instrumentos financieros</h3>

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
<li>Gestión de cotizaciones.</li>
<li>Almacenamiento de ticks.</li>
<li>Almacenamiento histórico OHLCV.</li>
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

<p>El proyecto se encuentra en la fase de construcción y validación del backend. Ya dispone de infraestructura, persistencia PostgreSQL, gestión de instrumentos, modelos de datos de mercado y pruebas automatizadas iniciales.</p>

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
<tr><td>Base de datos de pruebas</td><td>Preparada</td></tr>
<tr><td>SQLAlchemy</td><td>Completado</td></tr>
<tr><td>Configuración de FastAPI</td><td>Completado</td></tr>
<tr><td>Pydantic Settings</td><td>Completado</td></tr>
<tr><td>Alembic y migraciones</td><td>Completado</td></tr>
<tr><td>Modelo de instrumentos</td><td>Completado</td></tr>
<tr><td>API REST CRUD de instrumentos</td><td>Completado y verificado</td></tr>
<tr><td>Modelos Market Quote</td><td>Implementado</td></tr>
<tr><td>Modelos Market Tick</td><td>Implementado</td></tr>
<tr><td>Modelos Market Candle</td><td>Implementado</td></tr>
<tr><td>Migración de tablas Market Data</td><td>Aplicada y verificada</td></tr>
<tr><td>Esquemas Pydantic de Market Data</td><td>Implementados</td></tr>
<tr><td>Servicio de persistencia de cotizaciones</td><td>Implementado</td></tr>
<tr><td>Consulta de últimas cotizaciones</td><td>Implementada</td></tr>
<tr><td>Consulta de ticks históricos</td><td>Implementada</td></tr>
<tr><td>Eliminación de ticks antiguos</td><td>Implementada</td></tr>
<tr><td>Pruebas automatizadas Market Data</td><td>4 pruebas superadas</td></tr>
<tr><td>API REST de Market Data</td><td>Pendiente</td></tr>
<tr><td>Integración con proveedores externos</td><td>Pendiente</td></tr>
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
<tr><td>Python 3.14.4</td><td>Lenguaje principal</td></tr>
<tr><td>FastAPI</td><td>Framework de API REST</td></tr>
<tr><td>Uvicorn</td><td>Servidor ASGI</td></tr>
<tr><td>SQLAlchemy</td><td>ORM y acceso a datos</td></tr>
<tr><td>Psycopg 3</td><td>Conexión con PostgreSQL</td></tr>
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
<tr><td>pandas-ta u otra biblioteca compatible</td><td>Indicadores técnicos previstos</td></tr>
<tr><td>backtesting.py</td><td>Backtesting previsto</td></tr>
</tbody>
</table>

<h3>Base de datos</h3>

<ul>
<li>PostgreSQL 18.6.</li>
<li>SQLAlchemy ORM.</li>
<li>Alembic.</li>
<li>Base de datos independiente para pruebas automatizadas.</li>
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
<li>Node.js 26.13.0.</li>
<li>npm 11.20.0.</li>
<li>Pytest 9.2.0.</li>
<li>HTTPX 0.28.1.</li>
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

<pre>/home/sergio/AURUM-DEV/Projects/aurum-trading/</pre>

<h3>Repositorio GitHub</h3>

<p><a href="https://github.com/jarasergio/aurum-trading">https://github.com/jarasergio/aurum-trading</a></p>

<p><strong>Rama principal:</strong> main.</p>

<p><strong>Rama de desarrollo actual:</strong> feature/market-data.</p>

<hr>

<h2>5. ARQUITECTURA DEL PROYECTO</h2>

<p>La arquitectura del backend está organizada por responsabilidades, separando API, configuración, acceso a datos, modelos, esquemas y servicios.</p>

<h3>Estructura actual</h3>

<pre>
aurum-trading/
│
├── .env
├── .env.example
├── .gitignore
├── alembic.ini
├── pytest.ini
├── README.md
│
├── backend/
│ │
│ ├── alembic/
│ │ ├── versions/
│ │ │ ├── 3e9d19027571_create_instruments_table.py
│ │ │ └── fde942f0c117_add_market_data_tables.py
│ │ ├── env.py
│ │ ├── README
│ │ └── script.py.mako
│ │
│ ├── app/
│ │ ├── __init__.py
│ │ ├── main.py
│ │ │
│ │ ├── api/
│ │ │ ├── __init__.py
│ │ │ └── instruments.py
│ │ │
│ │ ├── core/
│ │ │ └── config.py
│ │ │
│ │ ├── db/
│ │ │ ├── base.py
│ │ │ └── session.py
│ │ │
│ │ ├── models/
│ │ │ ├── __init__.py
│ │ │ ├── instrument.py
│ │ │ ├── market_quote.py
│ │ │ ├── market_tick.py
│ │ │ └── market_candle.py
│ │ │
│ │ ├── schemas/
│ │ │ ├── __init__.py
│ │ │ ├── instrument.py
│ │ │ └── market_data.py
│ │ │
│ │ ├── services/
│ │ │ ├── __init__.py
│ │ │ ├── instrument_service.py
│ │ │ └── market_data_service.py
│ │ │
│ │ └── tests/
│ │
│ └── tests/
│ ├── conftest.py
│ └── test_market_data_service.py
│
├── frontend/
├── docs/
├── research/
├── scripts/
└── .github/
└── workflows/
</pre>

<p>La estructura recoge los módulos implementados y las carpetas previstas para el crecimiento del proyecto. Las rutas y archivos de módulos futuros se incorporarán progresivamente.</p>

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
<tr><td>Base de datos principal</td><td>aurum_trading</td></tr>
<tr><td>Base de datos de pruebas</td><td>aurum_trading_test</td></tr>
<tr><td>Usuario</td><td>aurum_app</td></tr>
<tr><td>ORM</td><td>SQLAlchemy</td></tr>
<tr><td>Migraciones</td><td>Alembic</td></tr>
</tbody>
</table>

<p>La conexión se configura mediante variables de entorno y Pydantic Settings.</p>

<p>Las credenciales deben permanecer en .env y nunca deben subirse al repositorio.</p>

<h3>Modelo implementado: Instrument</h3>

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

<p>El campo symbol tiene una restricción de unicidad.</p>

<p>La desactivación de instrumentos es lógica: los registros no se eliminan físicamente de la base de datos.</p>

<h3>Modelo implementado: MarketQuote</h3>

<p>Almacena la última cotización disponible por instrumento y proveedor.</p>

<table>
<thead>
<tr><th>Campo</th><th>Tipo</th></tr>
</thead>
<tbody>
<tr><td>id</td><td>Integer</td></tr>
<tr><td>instrument_id</td><td>ForeignKey</td></tr>
<tr><td>provider</td><td>String(50)</td></tr>
<tr><td>bid</td><td>Numeric(28,12), nullable</td></tr>
<tr><td>ask</td><td>Numeric(28,12), nullable</td></tr>
<tr><td>last</td><td>Numeric(28,12), nullable</td></tr>
<tr><td>market_timestamp</td><td>DateTime(timezone=True)</td></tr>
<tr><td>received_at</td><td>DateTime(timezone=True)</td></tr>
</tbody>
</table>

<p>Existe una restricción de unicidad para instrument_id y provider, garantizando una cotización actual por proveedor e instrumento.</p>

<p>También existe una restricción que impide almacenar cotizaciones sin ningún precio.</p>

<h3>Modelo implementado: MarketTick</h3>

<p>Almacena el histórico de actualizaciones de precios recibidas.</p>

<table>
<thead>
<tr><th>Campo</th><th>Tipo</th></tr>
</thead>
<tbody>
<tr><td>id</td><td>Integer</td></tr>
<tr><td>instrument_id</td><td>ForeignKey</td></tr>
<tr><td>provider</td><td>String(50)</td></tr>
<tr><td>bid</td><td>Numeric(28,12), nullable</td></tr>
<tr><td>ask</td><td>Numeric(28,12), nullable</td></tr>
<tr><td>last</td><td>Numeric(28,12), nullable</td></tr>
<tr><td>market_timestamp</td><td>DateTime(timezone=True)</td></tr>
<tr><td>received_at</td><td>DateTime(timezone=True)</td></tr>
</tbody>
</table>

<p>Se han incorporado índices para optimizar consultas por instrumento, fecha de mercado y fecha de recepción.</p>

<p>La política inicial de retención del histórico es de siete días.</p>

<h3>Modelo implementado: MarketCandle</h3>

<p>Representa velas OHLCV de diferentes temporalidades.</p>

<table>
<thead>
<tr><th>Campo</th><th>Tipo</th></tr>
</thead>
<tbody>
<tr><td>id</td><td>Integer</td></tr>
<tr><td>instrument_id</td><td>ForeignKey</td></tr>
<tr><td>provider</td><td>String(50)</td></tr>
<tr><td>timeframe</td><td>String(10)</td></tr>
<tr><td>open_time</td><td>DateTime(timezone=True)</td></tr>
<tr><td>close_time</td><td>DateTime(timezone=True)</td></tr>
<tr><td>open</td><td>Numeric(28,12)</td></tr>
<tr><td>high</td><td>Numeric(28,12)</td></tr>
<tr><td>low</td><td>Numeric(28,12)</td></tr>
<tr><td>close</td><td>Numeric(28,12)</td></tr>
<tr><td>volume</td><td>Numeric(28,12), nullable</td></tr>
</tbody>
</table>

<p>Se han incorporado restricciones de integridad para validar la relación entre los valores high, low, open y close.</p>

<p>Existe una restricción de unicidad por instrumento, proveedor, temporalidad y hora de apertura.</p>

<h3>Migraciones implementadas</h3>

<table>
<thead>
<tr><th>Revisión</th><th>Descripción</th></tr>
</thead>
<tbody>
<tr><td>3e9d19027571</td><td>Creación de la tabla instruments</td></tr>
<tr><td>fde942f0c117</td><td>Creación de las tablas de Market Data</td></tr>
</tbody>
</table>

<p>La última migración fue aplicada correctamente mediante Alembic.</p>

<p>La verificación alembic check confirmó que no existen operaciones de migración adicionales pendientes.</p>

<hr>

<h2>7. API REST IMPLEMENTADA</h2>

<h3>Gestión de instrumentos</h3>

<table>
<thead>
<tr><th>Método</th><th>Endpoint</th><th>Descripción</th></tr>
</thead>
<tbody>
<tr><td>GET</td><td>/instruments/</td><td>Listar instrumentos activos</td></tr>
<tr><td>POST</td><td>/instruments/</td><td>Crear instrumento</td></tr>
<tr><td>GET</td><td>/instruments/{instrument_id}</td><td>Consultar instrumento</td></tr>
<tr><td>PATCH</td><td>/instruments/{instrument_id}</td><td>Modificar instrumento</td></tr>
<tr><td>DELETE</td><td>/instruments/{instrument_id}</td><td>Desactivar instrumento</td></tr>
</tbody>
</table>

<h3>Endpoints generales</h3>

<table>
<thead>
<tr><th>Método</th><th>Endpoint</th><th>Descripción</th></tr>
</thead>
<tbody>
<tr><td>GET</td><td>/</td><td>Información general de la aplicación</td></tr>
<tr><td>GET</td><td>/health</td><td>Estado de la aplicación</td></tr>
<tr><td>GET</td><td>/health/database</td><td>Comprobación de conexión a PostgreSQL</td></tr>
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

<p><strong>Nota:</strong> Los modelos y servicios de Market Data están implementados, pero todavía no se han incorporado sus endpoints REST a FastAPI.</p>

<hr>

<h2>8. SERVICIO MARKET DATA</h2>

<p>Se ha creado el servicio market_data_service.py para centralizar la persistencia y consulta de información de mercado.</p>

<h3>Funcionalidades implementadas</h3>

<ul>
<li><strong>save_market_quote:</strong> comprueba la existencia del instrumento, guarda la cotización y registra un nuevo tick.</li>
<li><strong>get_latest_quotes:</strong> obtiene las últimas cotizaciones de un instrumento, ordenadas por proveedor.</li>
<li><strong>get_market_ticks:</strong> recupera los ticks históricos de un instrumento con límite configurable.</li>
<li><strong>delete_expired_ticks:</strong> elimina los ticks cuya fecha de recepción supera el período de retención establecido.</li>
</ul>

<h3>Reglas de negocio implementadas</h3>

<ul>
<li>Una cotización debe contener al menos un precio entre bid, ask y last.</li>
<li>Los precios deben ser positivos.</li>
<li>Bid no puede ser superior a ask cuando ambos están presentes.</li>
<li>La fecha de mercado debe incluir información de zona horaria.</li>
<li>Una cotización antigua no debe reemplazar una cotización más reciente.</li>
<li>Todos los ticks recibidos se registran en el histórico.</li>
<li>Las operaciones de escritura utilizan transacciones y rollback ante errores.</li>
<li>El límite de consulta de ticks está restringido entre 1 y 5000 registros.</li>
<li>La retención inicial de ticks es de siete días.</li>
</ul>

<p>El servicio está preparado para evolucionar hacia una arquitectura de proveedores de datos independientes.</p>

<hr>

<h2>9. PRUEBAS AUTOMATIZADAS</h2>

<p>Se ha configurado Pytest para ejecutar las pruebas automatizadas del backend.</p>

<h3>Infraestructura de pruebas</h3>

<ul>
<li>Pytest 9.2.0.</li>
<li>HTTPX 0.28.1.</li>
<li>Base de datos PostgreSQL independiente: aurum_trading_test.</li>
<li>Configuración de pruebas mediante pytest.ini.</li>
<li>Fixtures compartidas mediante backend/tests/conftest.py.</li>
</ul>

<h3>Pruebas implementadas</h3>

<table>
<thead>
<tr><th>Prueba</th><th>Resultado</th></tr>
</thead>
<tbody>
<tr><td>test_save_market_quote</td><td>PASS</td></tr>
<tr><td>test_newer_quote_updates_current_quote</td><td>PASS</td></tr>
<tr><td>test_older_quote_does_not_replace_current_quote</td><td>PASS</td></tr>
<tr><td>test_delete_expired_ticks</td><td>PASS</td></tr>
</tbody>
</table>

<p><strong>Resultado de la última ejecución:</strong></p>

<pre>
4 passed, 1 warning
</pre>

<p>También se verificó la ejecución completa de la suite mediante:</p>

<pre><code>pytest -v</code></pre>

<p>Las cuatro pruebas fueron superadas correctamente.</p>

<p>Se observó una advertencia de compatibilidad relacionada con HTTPX y Starlette TestClient. No impidió la ejecución de las pruebas.</p>

<h3>Verificación de sintaxis</h3>

<p>Se ejecutó correctamente la compilación de los módulos Python:</p>

<pre><code>python -m compileall -q backend/app</code></pre>

<p>También se comprobó la importación del servicio Market Data mediante un comando Python independiente.</p>

<hr>

<h2>10. INSTALACIÓN Y EJECUCIÓN</h2>

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

<pre><code>cp .env.example .env</code></pre>

<p>Completar los valores necesarios para la conexión a PostgreSQL y la configuración de la aplicación.</p>

<p>No introducir credenciales reales en archivos versionados.</p>

<h3>Migraciones de base de datos</h3>

<pre><code>alembic upgrade head</code></pre>

<p>Comprobar la revisión actual:</p>

<pre><code>alembic current</code></pre>

<p>Comprobar diferencias entre modelos y base de datos:</p>

<pre><code>alembic check</code></pre>

<h3>Ejecutar el backend</h3>

<p>Desde el directorio backend, con el entorno virtual activado:</p>

<pre><code>uvicorn app.main:app --reload</code></pre>

<p>La dirección local habitual de desarrollo será:</p>

<pre>http://127.0.0.1:8000</pre>

<p>La documentación interactiva de FastAPI estará disponible en:</p>

<pre>http://127.0.0.1:8000/docs</pre>

<h3>Ejecutar las pruebas</h3>

<p>Desde la raíz del proyecto:</p>

<pre><code>pytest -v</code></pre>

<h3>Comprobar la sintaxis del backend</h3>

<pre><code>python -m compileall -q backend/app</code></pre>

<hr>

<h2>11. SEGURIDAD Y GESTIÓN DEL RIESGO</h2>

<p>La seguridad es un principio fundamental del desarrollo de Aurum Trading.</p>

<ul>
<li>Las credenciales nunca se almacenan en GitHub.</li>
<li>Los archivos .env permanecen excluidos del control de versiones.</li>
<li>La ejecución real permanece deshabilitada inicialmente.</li>
<li>El sistema debe distinguir claramente entre simulación y trading real.</li>
<li>Las operaciones deberán respetar límites de riesgo configurables.</li>
<li>Los datos de mercado deben validarse antes de utilizarse.</li>
<li>Se deben registrar las decisiones y los errores del sistema.</li>
<li>Deben existir mecanismos de protección frente a desconexiones y órdenes duplicadas.</li>
<li>Las operaciones deberán poder reconciliarse con el estado del broker cuando exista integración.</li>
</ul>

<h3>Configuración inicial prevista</h3>

<pre><code>TRADING_MODE=simulation
TRADING_ENABLED=false</code></pre>

<p>Estos valores representan la política prevista para el proyecto y deberán mantenerse de acuerdo con la configuración real de la aplicación.</p>

<p><strong>Importante:</strong> Aurum Trading es un proyecto de desarrollo tecnológico y análisis financiero. Ninguna estrategia garantiza rentabilidad y los resultados históricos no aseguran resultados futuros.</p>

<hr>

<h2>12. HOJA DE RUTA</h2>

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

<h3>ETAPA 4 — Arquitectura Market Data</h3>

<p><strong>Estado: IMPLEMENTADA PARCIALMENTE</strong></p>

<ul>
<li>Modelos MarketQuote, MarketTick y MarketCandle.</li>
<li>Migraciones de base de datos.</li>
<li>Esquemas Pydantic.</li>
<li>Servicio de persistencia de cotizaciones.</li>
<li>Consulta de cotizaciones actuales.</li>
<li>Consulta de histórico de ticks.</li>
<li>Retención de datos históricos.</li>
<li>Validaciones de precios.</li>
<li>Pruebas automatizadas iniciales.</li>
<li>Endpoints REST de Market Data pendientes.</li>
<li>Integración de proveedores externos pendiente.</li>
<li>Generación y almacenamiento de velas pendiente.</li>
</ul>

<h3>ETAPA 5 — Proveedores de datos</h3>

<ul>
<li>Diseño de arquitectura de proveedores.</li>
<li>Evaluación de fuentes de datos.</li>
<li>Integración de proveedores externos.</li>
<li>Normalización de cotizaciones.</li>
<li>Gestión de conexiones.</li>
<li>Reconexión automática.</li>
<li>Control de calidad de datos.</li>
</ul>

<h3>ETAPA 6 — Análisis cuantitativo</h3>

<ul>
<li>Indicadores técnicos.</li>
<li>Procesamiento de series temporales.</li>
<li>Señales de mercado.</li>
<li>Herramientas de análisis.</li>
</ul>

<h3>ETAPA 7 — Estrategias y backtesting</h3>

<ul>
<li>Arquitectura de estrategias.</li>
<li>Generación de señales.</li>
<li>Simulación de operaciones.</li>
<li>Backtesting histórico.</li>
<li>Comisiones y costes.</li>
<li>Métricas de rendimiento.</li>
</ul>

<h3>ETAPA 8 — Gestión del riesgo</h3>

<ul>
<li>Tamaño de posiciones.</li>
<li>Stop-loss y take-profit.</li>
<li>Límites de pérdidas.</li>
<li>Control de exposición.</li>
<li>Protección del capital.</li>
</ul>

<h3>ETAPA 9 — Dashboard web</h3>

<ul>
<li>React y TypeScript.</li>
<li>Diseño oscuro con detalles dorados.</li>
<li>Identidad visual Aurum Trading.</li>
<li>Gráficos financieros.</li>
<li>Estadísticas.</li>
<li>Posiciones e historial.</li>
<li>Estado del motor de trading.</li>
</ul>

<h3>ETAPA 10 — Integración en tiempo real</h3>

<ul>
<li>WebSockets.</li>
<li>Actualizaciones de cotizaciones.</li>
<li>Alertas.</li>
<li>Monitorización del sistema.</li>
</ul>

<h3>ETAPA 11 — Integración con brokers</h3>

<ul>
<li>Evaluación de proveedores.</li>
<li>Integración mediante API.</li>
<li>Gestión de órdenes.</li>
<li>Sincronización de posiciones.</li>
<li>Controles de seguridad.</li>
<li>Pruebas antes de cualquier ejecución real.</li>
</ul>

<hr>

<h2>13. CONTROL DE VERSIONES</h2>

<p>El proyecto utiliza Git y GitHub.</p>

<h3>Repositorio remoto</h3>

<pre>git@github.com:jarasergio/aurum-trading.git</pre>

<p><strong>Rama principal:</strong> main.</p>

<p>Se utilizarán ramas de desarrollo y commits pequeños y descriptivos.</p>

<h3>Rama de trabajo actual</h3>

<pre>feature/market-data</pre>

<h3>Ejemplos de commits</h3>

<pre><code>feat: add market data module
feat: implement historical candles
fix: correct instrument validation
refactor: improve database services
test: add market data tests
docs: update project documentation</code></pre>

<h3>Comandos habituales</h3>

<pre><code>git status

git add .

git commit -m "descriptive commit message"

git push origin feature/market-data</code></pre>

<h3>Archivos que no deben subirse</h3>

<ul>
<li>.env</li>
<li>.venv/</li>
<li>node_modules/</li>
<li>Archivos de caché.</li>
<li>Logs.</li>
<li>Bases de datos locales.</li>
<li>Datos históricos voluminosos.</li>
<li>Credenciales.</li>
<li>Archivos temporales.</li>
</ul>

<hr>

<h2>14. DOCUMENTACIÓN DEL PROYECTO</h2>

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

<h2>15. ESTADO DE SEGURIDAD DEL PROYECTO</h2>

<p>Aurum Trading se encuentra actualmente en fase de desarrollo.</p>

<p>No existe todavía un motor de trading completo ni una integración operativa con brokers.</p>

<p>El objetivo inmediato es desarrollar y validar la infraestructura de datos y análisis antes de implementar cualquier funcionalidad de ejecución.</p>

<p>La ejecución real no forma parte de la fase actual.</p>

<hr>

<h2>16. PRÓXIMO PASO DE DESARROLLO</h2>

<p>El siguiente objetivo es completar la arquitectura Market Data y exponer sus funcionalidades mediante la API REST.</p>

<h3>Orden de trabajo propuesto</h3>

<ol>
<li>Revisar y consolidar las pruebas del servicio Market Data.</li>
<li>Completar las pruebas de validación de esquemas Pydantic.</li>
<li>Implementar los endpoints REST para cotizaciones.</li>
<li>Implementar los endpoints REST para histórico de ticks.</li>
<li>Implementar los endpoints REST para velas OHLCV.</li>
<li>Incorporar las consultas de histórico de velas.</li>
<li>Diseñar la interfaz de proveedores de datos.</li>
<li>Integrar el primer proveedor externo.</li>
<li>Implementar la normalización de datos.</li>
<li>Desarrollar el procesamiento de ticks y generación de velas.</li>
<li>Ampliar las pruebas automatizadas.</li>
</ol>

<p>El diseño deberá permitir incorporar diferentes proveedores de datos sin modificar la lógica central de Aurum Trading.</p>

<hr>

<h2>17. FILOSOFÍA DEL PROYECTO</h2>

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