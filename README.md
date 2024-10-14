# Cálculo de Duración de UPS

Este programa en Python calcula el tiempo aproximado que un aparato eléctrico puede permanecer encendido al estar conectado a un UPS (Sistema de Alimentación Ininterrumpida). El usuario debe proporcionar la capacidad del UPS en volt-amperios (VA), el factor de potencia del UPS, y el consumo del aparato en vatios (W).

## Funcionalidades

1. **Entrada de datos del usuario**:
    - **Capacidad del UPS (VA)**: El usuario introduce la capacidad nominal del UPS en volt-amperios.
    - **Factor de Potencia**: Un valor que oscila entre 0.6 y 0.9, proporcionado por el usuario. El factor de potencia convierte VA a vatios-hora (Wh), que es la energía útil del UPS.
    - **Consumo del aparato eléctrico (W)**: Potencia consumida por el aparato que estará conectado al UPS.

2. **Cálculo de la duración**:
    - Se convierte la capacidad del UPS de VA a Wh multiplicando por el factor de potencia.
    - Se calcula la duración en horas dividiendo la capacidad en Wh entre el consumo del aparato en W.

3. **Manejo de errores**:
    - El programa valida que los valores proporcionados sean números válidos.
    - Verifica que la capacidad del UPS, el factor de potencia, y el consumo sean mayores a 0 y que el factor de potencia esté dentro del rango esperado (0.6 a 0.9).

## Ejemplo de Uso

Si el usuario proporciona los siguientes datos:

- Capacidad del UPS: `1500 VA`
- Factor de Potencia: `0.8`
- Consumo del aparato eléctrico: `300 W`

El programa calculará la duración aproximada de funcionamiento del aparato como:

$\text{Conversión VA a Wh} = 1500 \text{ VA} \times 0.8 = 1200 \text{ Wh}$
$\text{Duración} = 1200 \text{ Wh} \div 300 \text{ W} = 4 \text{horas}$

Por lo tanto, el aparato podría funcionar aproximadamente 4 horas con esa configuración.

## Requisitos

- **Python 3.x**

## Cómo Ejecutar el Programa

1. Clona este repositorio o descarga el archivo Python.
2. Ejecuta el archivo desde una terminal o entorno de desarrollo de Python.
3. Introduce los valores solicitados para realizar el cálculo.

## Licencia

Este proyecto está bajo la [Licencia MIT](./LICENSE).
