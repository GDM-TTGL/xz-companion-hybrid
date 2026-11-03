# XZ Companion Hybrid — integración real v0.1 (fuentes)

Este código parte de `JaviLabarumDJ/mixxx-android` e integra el selector de **seis Sound Color FX** procedente de `thanhtonvk/Vynix-DJ` en la aplicación **QML** Android.

## Implementado en el código

- `src/qml/qmlapplication.cpp`: port de controles `[Skin],color_fx_select_1..6` al motor QML; cargan el efecto en `QuickEffectChain` de cada deck (Filter, Reverb/SPACE, Echo/DUB ECHO, Moog Ladder/SWEEP, White Noise, Bitcrusher/CRUSH); se mantiene un único EffectsManager. Los ajustes de parámetros siguen el código de Vynix.
- `src/qml/qmlapplication.h`: almacenamiento del ciclo de vida de los controles.
- `res/qml/XZColorFxPanel.qml`: botones para seleccionar efectos y knobs para CH1/CH2.
- `res/qml/MainWindow.qml`: botón XZ FX y panel superpuesto.
- `third_party/VynixDJ_skin/`: skin XML original preservada para trabajo futuro y referencia; **no es ejecutada por la interfaz QML de Android**.
- Se conserva el sistema de biblioteca, audio USB, STEMS ya separados y apariencia Booth/Classic de Javier.

## No implementado o no validado

- **NO es un APK**; la compilación con Qt/Android SDK y las pruebas en teléfono están pendientes. Los controles QML/C++ son una integración de código, no una prueba de funcionamiento real.
- La skin XML Vynix no es un layout QML: portarla visualmente necesita traducir componentes o crear una interfaz QML nueva.
- La separación automática por IA de archivos MP3 no viene implementada por este merge.
- El soporte de XDJ-XZ en modo standalone con canales CH3/4 no está verificado.
- Android 13 puede no iniciar con las dependencias ARM64 compiladas para Android 14+; requiere reconstruir libs, no solo bajar minSdk.
- iPadOS requiere otro port, este archivo es Android.

## Revisión en Antigravity

Abrir `XZCompanion_Hybrid_source/` como proyecto. Compilar según `packaging/android/README.md` y la documentación del proyecto base, usando Qt 6.8 y sus dependencias precompiladas. Si la compilación falla, revisar primero `src/qml/qmlapplication.cpp` y la disponibilidad de `XZColorFxPanel.qml` en recursos empaquetados de Android. No sustituir implementaciones del audio USB existentes.

## Procedencia / licencias

Basado en Mixxx y Mixxx Android (GPL-2.0) y parcialmente en Vynix DJ (GPL, archivo LICENSE incluido en skin). Conservar avisos originales y publicar el código fuente correspondiente al distribuir binarios GPL.
