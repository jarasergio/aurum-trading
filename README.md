AURUM TRADING

Plataforma modular de análisis cuantitativo y trading algorítmico.

Aurum Trading es un proyecto de desarrollo de una plataforma propia de análisis de mercados financieros y trading algorítmico, construida con Python, FastAPI y PostgreSQL.

El objetivo es desarrollar una arquitectura modular, escalable y multi-instrumento que permita gestionar datos de mercado, desarrollar estrategias cuantitativas, realizar backtesting, administrar riesgos y, en una etapa futura, integrar diferentes brokers.

El proyecto contempla una interfaz web profesional para visualizar y controlar el sistema desde un único lugar.

Estado actual: backend inicial funcional. Infraestructura, conexión con PostgreSQL, migraciones y API REST CRUD de instrumentos implementadas y verificadas.
1. Objetivos del proyecto

Aurum Trading está diseñado para evolucionar progresivamente desde una plataforma de gestión de instrumentos y datos financieros hasta un sistema completo de trading algorítmico.

Instrumentos financieros

La arquitectura está diseñada para trabajar con diferentes mercados:

XAU/USD: oro.
EUR/USD: Forex.
NASDAQ: índices.
DOW JONES: índices.
BTC/USD: criptomonedas.
Otros instrumentos financieros que se incorporen posteriormente.

La incorporación de nuevos instrumentos no debe requerir modificaciones estructurales importantes en el sistema.

Funcionalidades previstas
Gestión de instrumentos financieros.
Obtención de datos de mercado.
Cotizaciones y precios en tiempo real.
Almacenamiento de datos históricos.
Gestión de temporalidades.
Validación y normalización de datos.
Indicadores técnicos.
Análisis cuantitativo.
Estrategias algorítmicas.
Backtesting.
Gestión de posiciones y órdenes.
Gestión de riesgo.
Trading simulado.
Integración futura con brokers.
Dashboard web.
Estadísticas y seguimiento del rendimiento.
2. Estado actual del desarrollo

El proyecto se encuentra en la fase inicial de construcción del backend.

Módulo	Estado
Infraestructura de desarrollo	Completado
Repositorio Git y GitHub	Completado
Entorno Python	Completado
PostgreSQL	Completado
SQLAlchemy	Completado
Configuración de FastAPI	Completado
Pydantic Settings	Completado
Alembic y migraciones	Completado
Modelo de instrumentos	Completado
API REST CRUD de instrumentos	Completado y verificado
Arquitectura Market Data	Pendiente
Cotizaciones de mercado	Pendiente
Datos históricos OHLCV	Pendiente
Validación de datos financieros	Pendiente
Indicadores técnicos	Pendiente
Estrategias algorítmicas	Pendiente
Backtesting	Pendiente
Gestión de riesgo	Pendiente
Trading simulado	Pendiente
Frontend React	Pendiente
Integración con brokers	Pendiente

Las funcionalidades pendientes forman parte de la hoja de ruta y no deben considerarse implementadas.

3. Tecnologías utilizadas
Backend
Tecnología	Función
Python 3.14	Lenguaje principal
FastAPI	Framework de API REST
Uvicorn	Servidor ASGI
SQLAlchemy	ORM y acceso a datos
Psycopg	Conexión con PostgreSQL
Alembic	Migraciones de base de datos
Pydantic 2	Validación de datos
Pydantic Settings	Configuración de la aplicación
Análisis cuantitativo y datos
Tecnología	Función
Pandas	Procesamiento de datos
NumPy	Cálculo numérico
pandas-ta u otra biblioteca compatible	Indicadores técnicos
backtesting.py (previsto)	Backtesting
Base de datos
PostgreSQL 18.6.
Frontend previsto
React.
TypeScript.
Vite.
TradingView Lightweight Charts o una alternativa compatible.
WebSockets para actualizaciones en vivo.
Desarrollo y control de calidad
Git.
GitHub.
Visual Studio Code.
NVM.
Node.js 26.
npm.
Pytest.
HTTPX.
Ruff.
4. Entorno de desarrollo

El entorno principal de desarrollo está preparado sobre Ubuntu.

Componente	Configuración
Sistema operativo	Ubuntu 26.04.1 LTS
Arquitectura	x86_64
Equipo	mini-PC
Editor	Visual Studio Code Portable
Python	3.14.4
Node.js	26.13.0
npm	11.20.0
PostgreSQL	18.6
Git	2.53.0
Entorno virtual	.venv
Ubicación del proyecto
text
/home/sergio/AURUM-DEV/Projects/aurum-trading/

Repositorio GitHub

https://github.com/jarasergio/aurum-trading

Rama principal: main.

5. Arquitectura actual

La arquitectura del backend está organizada por responsabilidades, separando API, configuración, acceso a datos, modelos, esquemas y servicios.

text
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


La estructura mostrada recoge los componentes principales y las carpetas previstas para el crecimiento del proyecto. Los módulos todavía no implementados se incorporarán progresivamente.

Principios arquitectónicos
Separación de responsabilidades.
Arquitectura modular y escalable.
Independencia entre instrumentos financieros.
Separación entre proveedores de datos, estrategias y brokers.
Normalización de los datos antes de utilizarlos.
Separación entre lógica de negocio y API.
Persistencia mediante PostgreSQL.
Migraciones de base de datos controladas mediante Alembic.
Pruebas automatizadas para las funcionalidades principales.
Separación estricta entre simulación y ejecución real.
6. Base de datos

La base de datos principal es PostgreSQL.

Configuración actual:

Elemento	Valor
Motor	PostgreSQL
Versión	18.6
Base de datos	aurum_trading
Usuario	aurum_app
ORM	SQLAlchemy
Migraciones	Alembic

La conexión se configura mediante variables de entorno y Pydantic Settings.

Las credenciales deben permanecer en .env y nunca deben subirse al repositorio.

Modelo implementado: Instrument

La primera entidad del sistema es Instrument.

Representa los instrumentos financieros que podrá gestionar Aurum Trading.

Campo	Tipo
id	Integer
symbol	String(32)
name	String(120)
asset_class	String(30)
market	String(30)
base_currency	String(12)
quote_currency	String(12)
is_active	Boolean
created_at	DateTime

El campo symbol tiene una restricción de unicidad.

La desactivación de instrumentos es lógica: los registros no se eliminan físicamente de la base de datos.

Instrumentos registrados actualmente
ID	Símbolo	Nombre	Estado
1	EURUSD	Euro / US Dollar Spot	Activo
3	GBPUSD	British Pound / US Dollar	Activo
7. API REST implementada

Actualmente está implementada la gestión CRUD de instrumentos.

Método	Endpoint	Descripción
GET	/instruments/	Listar instrumentos activos
POST	/instruments/	Crear instrumento
GET	/instruments/{instrument_id}	Consultar instrumento
PATCH	/instruments/{instrument_id}	Modificar instrumento
DELETE	/instruments/{instrument_id}	Desactivar instrumento
Comportamientos verificados
Creación de instrumentos.
Consulta por identificador.
Listado de instrumentos activos.
Modificación de datos.
Desactivación lógica.
Reactivación mediante PATCH.
Exclusión de instrumentos inactivos del listado.
Rechazo de símbolos duplicados mediante HTTP 409 Conflict.

La API utiliza esquemas Pydantic para validar los datos recibidos.

8. Instalación y ejecución

Los siguientes pasos corresponden al entorno de desarrollo preparado sobre Ubuntu.

Requisitos
Ubuntu.
Python 3.14.
PostgreSQL 18.
Git.
Entorno virtual Python.
Clonar el repositorio
bash
git clone git@github.com:jarasergio/aurum-trading.git

cd aurum-trading

Activar el entorno virtual
bash
source .venv/bin/activate

Configurar las variables de entorno

El proyecto utiliza .env.example como plantilla de configuración.

bash
cp .env.example .env


Completar los valores necesarios para la conexión a PostgreSQL y la configuración de la aplicación.

No introducir credenciales reales en archivos versionados.

Migraciones de base de datos

Desde la raíz del proyecto:

bash
alembic upgrade head


Este comando aplica las migraciones pendientes.

Ejecutar el backend

Desde el directorio backend, con el entorno virtual activado:

bash
uvicorn app.main:app --reload


La dirección local habitual de desarrollo será:

text
http://127.0.0.1:8000


La documentación interactiva de FastAPI estará disponible en:

text
http://127.0.0.1:8000/docs


Nota: la configuración de arranque, las variables de entorno y los comandos de ejecución deberán mantenerse sincronizados con los archivos reales del proyecto.

9. Seguridad y gestión del riesgo

La seguridad es un principio fundamental del desarrollo de Aurum Trading.

Se establecen las siguientes reglas:

Las credenciales nunca se almacenan en GitHub.
Los archivos .env permanecen excluidos del control de versiones.
La ejecución real permanece deshabilitada inicialmente.
El sistema debe distinguir claramente entre simulación y trading real.
Las operaciones deberán respetar límites de riesgo configurables.
Los datos de mercado deben validarse antes de utilizarse.
Se deben registrar las decisiones y los errores del sistema.
Deben existir mecanismos de protección frente a desconexiones y órdenes duplicadas.
Las operaciones deberán poder reconciliarse con el estado del broker cuando exista integración.
Configuración inicial de trading
env
TRADING_MODE=simulation
TRADING_ENABLED=false


Estos valores representan la política prevista para el proyecto y deberán mantenerse de acuerdo con la configuración real de la aplicación.

Importante: Aurum Trading es un proyecto de desarrollo tecnológico y análisis financiero. Ninguna estrategia garantiza rentabilidad y los resultados históricos no aseguran resultados futuros.

10. Hoja de ruta

El desarrollo se realizará progresivamente, validando cada módulo antes de continuar.

Etapa 1 — Infraestructura

Estado: COMPLETADA

Preparación de Ubuntu.
VS Code Portable.
Python y entorno virtual.
Node.js y NVM.
Git y GitHub.
PostgreSQL.
Etapa 2 — Backend y persistencia

Estado: COMPLETADA

FastAPI.
SQLAlchemy.
Psycopg.
Pydantic Settings.
Alembic.
Modelo Instrument.
Migración inicial.
Etapa 3 — API de instrumentos

Estado: COMPLETADA

CRUD de instrumentos.
Validaciones.
Control de duplicados.
Desactivación lógica.
Reactivación.
Verificación de operaciones.
Etapa 4 — Market Data

Estado: SIGUIENTE ETAPA

Diseño de la arquitectura de proveedores.
Integración de fuentes de datos.
Cotizaciones de mercado.
Datos históricos OHLCV.
Gestión de temporalidades.
Validación de precios.
API de datos de mercado.
Etapa 5 — Análisis cuantitativo
Indicadores técnicos.
Procesamiento de series temporales.
Señales de mercado.
Herramientas de análisis.
Etapa 6 — Estrategias y backtesting
Arquitectura de estrategias.
Generación de señales.
Simulación de operaciones.
Backtesting histórico.
Comisiones y costes.
Métricas de rendimiento.
Etapa 7 — Gestión del riesgo
Tamaño de posiciones.
Stop-loss y take-profit.
Límites de pérdidas.
Control de exposición.
Protección del capital.
Etapa 8 — Dashboard web
React y TypeScript.
Diseño oscuro con detalles dorados.
Identidad visual Aurum Trading.
Gráficos financieros.
Estadísticas.
Posiciones e historial.
Estado del motor de trading.
Etapa 9 — Integración en tiempo real
WebSockets.
Actualizaciones de cotizaciones.
Alertas.
Monitorización del sistema.
Etapa 10 — Integración con brokers
Evaluación de proveedores.
Integración mediante API.
Gestión de órdenes.
Sincronización de posiciones.
Controles de seguridad.
Pruebas antes de cualquier ejecución real.
11. Control de versiones

El proyecto utiliza Git y GitHub.

Repositorio remoto:

text
git@github.com:jarasergio/aurum-trading.git


Rama principal:

text
main


Se utilizarán commits pequeños y descriptivos.

Ejemplos:

text
feat: add market data module
feat: implement historical candles
fix: correct instrument validation
refactor: improve database services
test: add market data tests
docs: update project documentation


Antes de cada commit se recomienda comprobar:

bash
git status


Y después de los cambios:

bash
git add .
git commit -m "descriptive commit message"
git push origin main

Archivos que no deben subirse
.env
.venv/
node_modules/
Archivos de caché.
Logs.
Bases de datos locales.
Datos históricos voluminosos.
Credenciales.
Archivos temporales.
12. Documentación del proyecto

La documentación deberá evolucionar junto con el código.

Se contempla incorporar:

text
docs/
├── architecture.md
├── risk-management.md
├── market-data.md
├── database.md
└── development-guide.md


Cada módulo importante deberá documentar:

Objetivo.
Arquitectura.
Responsabilidades.
Modelos de datos.
Endpoints.
Configuración.
Pruebas.
Decisiones técnicas.
13. Estado de seguridad del proyecto

Aurum Trading se encuentra actualmente en fase de desarrollo.

No existe todavía un motor de trading completo ni una integración operativa con brokers.

El objetivo inmediato es desarrollar y validar la infraestructura de datos y análisis antes de implementar cualquier funcionalidad de ejecución.

La ejecución real no forma parte de la fase actual.

14. Próximo paso de desarrollo

El siguiente objetivo es implementar el módulo Market Data.

Antes de escribir código se definirá:

La arquitectura de proveedores de datos.
La estructura de cotizaciones.
El modelo de almacenamiento histórico OHLCV.
La gestión de temporalidades.
Las reglas de validación de precios.
Los servicios de consulta.
Los endpoints de la API.

El diseño deberá permitir incorporar diferentes proveedores de datos sin modificar la lógica central de Aurum Trading.

15. Filosofía del proyecto

Aurum Trading se desarrollará siguiendo estos principios:

Arquitectura modular.
Código limpio y mantenible.
Separación de responsabilidades.
Escalabilidad multi-instrumento.
Datos fiables y reproducibles.
Pruebas antes de incorporar nuevas funcionalidades.
Seguridad desde el diseño.
Gestión del riesgo como prioridad.
Documentación actualizada.
Desarrollo incremental y controlado.

La prioridad no es desarrollar rápidamente un bot que opere, sino construir una plataforma sólida, verificable y preparada para evolucionar.

AURUM TRADING

Quantitative Analysis · Algorithmic Trading · Market Data

Repositorio: https://github.com/jarasergio/aurum-trading