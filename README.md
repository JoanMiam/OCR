### Documentación del Procesador de PDFs con OCR

##### Planteamiento del Problema

Se cuenta con una colección de documentos físicos organizados en carpetas. Estos documentos abarcan una variedad de tipos, incluyendo identificaciones oficiales como INEs y recibos de servicios públicos como la luz. Para facilitar su manejo y acceso, estos documentos se están convirtiendo a formato digital, específicamente a archivos PDF.

El proceso no se detiene ahí. La meta principal es identificar y extraer datos clave de estos documentos digitalizados. Esto implica un enfoque detallado en información específica como los nombres de los clientes, sus CURPs, y otros datos relevantes que varían según el tipo de documento.

Una vez extraída, esta información se someterá a un proceso de clasificación. El objetivo es categorizar los datos de manera eficiente para su inclusión en una base de datos. Este almacenamiento estructurado no solo garantizará la seguridad de la información, sino que también permitirá un acceso y una búsqueda rápidos y sencillos. De esta manera, se optimiza la gestión documental, transformando un sistema físico y posiblemente desordenado en una solución digital integrada y fácil de navegar.

#### Requisitos Funcionales (Atributos Funcionales)
- **Extracción de Texto e Imágenes: **Capacidad para identificar y extraer texto e imágenes de cada página de un archivo PDF.
- **Detección de Entidades:** Habilidad para detectar y aislar entidades específicas (por ejemplo, nombres, fechas, identificaciones) en el texto extraído.
- **Guardado y Organización de Datos: **El software debe clasificar y almacenar el texto y las imágenes extraídas en carpetas designadas para una fácil referencia y acceso.
- **Optimización de Imágenes para OCR:** Procesamiento de imágenes para mejorar la precisión del reconocimiento óptico de caracteres.
- **Manejo De Errores:** Identificación y manejo efectivo de posibles errores durante el procesamiento del PDF.

------------


#### Requisitos No Funcionales (Atributos de Calidad)


- **Rendimiento: **Eficiencia en el procesamiento de archivos PDF, incluso con documentos de gran tamaño o alta complejidad.
- **Fiabilidad: **Precisión y consistencia en la extracción de texto e imágenes.
- **Facilidad de Uso:** Interfaz sencilla y documentación clara que permita a los usuarios finales utilizar el software sin problemas.
- **Seguridad:** Asegurar que la manipulación de documentos PDF se realice sin comprometer la integridad del archivo original.
- **Mantenibilidad:** El código está bien organizado y documentado, facilitando futuras actualizaciones o modificaciones.

-------------

##### Escalabilidad, Robustez, Portabilidad
- **Escalabilidad: **El diseño del software permite ajustarse a diferentes volúmenes de trabajo, desde documentos individuales hasta lotes de archivos.
- **Robustez:** El software maneja adecuadamente situaciones anormales o imprevistas durante el procesamiento, sin interrupciones ni fallos.
- **Portabilidad:** El script puede ejecutarse en distintos entornos operativos donde estén disponibles sus dependencias.


------------


##### Características de un Funcionamiento Funcional
- **Descripción Integral y Detallada:** Cada función del software está explicada con detalle, incluyendo ejemplos de uso y posibles casos de aplicación.
- **No Ambigüedad: **Las instrucciones y descripciones evitan la ambigüedad, ofreciendo claridad y precisión en su interpretación.
- **Consistencia y Relaciones:** Las funciones están interrelacionadas de manera lógica y coherente, evitando conflictos o contradicciones en su operación.
- **Documentación de API:** Si el software expone una API, esta está documentada detalladamente, incluyendo descripciones de endpoints, parámetros y formatos de respuesta.


------------


##### Descripción del Diseño 

**1. PDFProcessor:** Encargada de gestionar la apertura, lectura y procesamiento de archivos PDF. Esta clase es responsable de la extracción de texto e imágenes, detectando entidades específicas y guardando la información extraída en formatos organizados.
**2. ImageProcessor: **Esta clase se especializa en el procesamiento de imágenes extraídas del PDF. Implementa técnicas de procesamiento de imágenes para optimizar la calidad y legibilidad de las imágenes antes de pasarlas a OCR.
Las clases están diseñadas para ser extensibles y modificables, permitiendo adaptar el software a diferentes tipos de documentos PDF y requisitos de extracción de datos.
