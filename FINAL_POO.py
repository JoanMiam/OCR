import fitz  # Importa PyMuPDF para trabajar con archivos PDF
import pytesseract  # Importa pytesseract para OCR (Reconocimiento Óptico de Caracteres)
from PIL import Image  # Importa Image de PIL para manejar imágenes
import io  # Importa io para manejar flujos de bytes
import os  # Importa os para manejar funcionalidades del sistema operativo, como archivos y directorios
import re  # Importa re para trabajar con expresiones regulares

# Clase para procesar y manejar PDFs
class PDFProcessor:
    def __init__(self, pdf_path, image_folder, text_output_folder, names_output_folder):
        # Constructor de la clase, inicializa las rutas y crea los directorios necesarios
        self.pdf_path = pdf_path  # Ruta del archivo PDF
        self.image_folder = image_folder  # Directorio para guardar imágenes extraídas
        self.text_output_folder = text_output_folder  # Directorio para guardar texto extraído
        self.names_output_folder = names_output_folder  # Directorio para guardar nombres extraídos
        # Crea los directorios si no existen
        self._create_folder_if_not_exists(self.image_folder)
        self._create_folder_if_not_exists(self.text_output_folder)
        self._create_folder_if_not_exists(self.names_output_folder)

    def _create_folder_if_not_exists(self, folder_path):
        # Método para crear un directorio si no existe
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def _page_has_images(self, page):
        # Método para verificar si una página contiene imágenes
        return len(page.get_images(full=True)) > 0

    def _extract_and_save_text(self, page, doc, page_num):
        # Método para extraer y guardar texto de una página
        if self._page_has_images(page):
            # Si la página tiene imágenes, procesa cada imagen
            for img_index, img in enumerate(page.get_images(full=True)):
                xref = img[0]
                base_image = fitz.Pixmap(doc, xref)
                # Convierte la imagen a RGB si es necesario
                if base_image.n - base_image.alpha < 4:
                    pix = fitz.Pixmap(fitz.csRGB, base_image)
                    base_image = pix
                # Carga la imagen para procesamiento
                image = Image.open(io.BytesIO(base_image.tobytes()))
                # Procesa la imagen para OCR
                processed_image = ImageProcessor.process_image_for_ocr(image)
                # Extrae texto de la imagen
                text = pytesseract.image_to_string(processed_image)
                # Guarda el texto y nombres extraídos, y guarda la imagen procesada
                self._save_text(text, img_index, page_num)
                self._extract_and_save_names(text, img_index, page_num)
                ImageProcessor.save_extracted_image(processed_image, self.image_folder, img_index, page_num)

                # Funcionalidad específica para detectar texto relacionado con INE
                if "INSTITUTO NACIONAL ELECTORAL" in text:
                    self._save_ine_detected(page_num, img_index)

                base_image = None  # Libera la memoria de la imagen base

    def _save_text(self, text, img_index, page_num):
        # Método para guardar el texto extraído en un archivo
        text_file_name = f"page_{page_num + 1}_image_{img_index + 1}.txt"
        text_file_path = os.path.join(self.text_output_folder, text_file_name)
        with open(text_file_path, "w") as text_file:
            text_file.write(text)

    def _extract_and_save_names(self, text, img_index, page_num):
        # Método para extraer y guardar nombres del texto
        names = re.findall(r'\bNombre:\s*(\w+)', text, re.IGNORECASE)
        if names:
            text_file_name = f"page_{page_num + 1}_image_{img_index + 1}.txt"
            names_file_path = os.path.join(self.names_output_folder, text_file_name)
            with open(names_file_path, "a") as names_file:
                for name in names:
                    names_file.write(f"Nombre: {name}\n")

    def _save_ine_detected(self, page_num, img_index):
        # Método para indicar la detección de INE en un archivo
        ine_file_name = f"page_{page_num + 1}_image_{img_index + 1}_INE_detected.txt"
        ine_file_path = os.path.join(self.text_output_folder, ine_file_name)
        with open(ine_file_path, "w") as ine_file:
            ine_file.write("INE (Credencial para Votar) detectada en esta imagen.\n")

    def process_pdf(self):
        # Método principal para procesar el PDF
        try:
            doc = fitz.open(self.pdf_path)  # Intenta abrir el archivo PDF
        except Exception as e:
            print(f"Error al abrir el archivo PDF: {e}")  # Manejo de excepción si falla la apertura
            return
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)  # Carga cada página del PDF
            self._extract_and_save_text(page, doc, page_num)  # Extrae y guarda el texto de cada página
        doc.close()  # Cierra el documento PDF

# Clase para procesar y manejar imágenes
class ImageProcessor:
    @staticmethod
    def process_image_for_ocr(image):
        # Método estático para procesar imágenes para OCR, convierte a escala de grises
        return image.convert('L')

    @staticmethod
    def save_extracted_image(image, image_folder, img_index, page_num):
        # Método estático para guardar una imagen procesada
        image_format = "jpeg"
        image_file_path = os.path.join(image_folder, f"page_{page_num + 1}_image_{img_index + 1}.{image_format}")
        image.save(image_file_path, image_format.upper())  # Guarda la imagen en el formato y ruta especificados
        return image_file_path

# Configuración de Tesseract
try:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Joan Miam Chan\AppData\Local\Programs\Tesseract-OCR\tesseract'
    # Establece la ruta del ejecutable de Tesseract
except Exception as e:
    print(f"Error al configurar Tesseract: {e}")  # Manejo de excepción en caso de error
    exit(1)

# Rutas y carpetas para el procesamiento
pdf_path = 'Hola como estás.pdf'  # Ruta del archivo PDF a procesar
image_folder = 'imagenes_extraidas'  # Nombre de la carpeta para guardar imágenes
text_output_folder = 'textos_extraidos'  # Nombre de la carpeta para guardar textos
names_output_folder = 'nombres_extraidos'  # Nombre de la carpeta para guardar nombres

# Procesamiento del PDF
processor = PDFProcessor(pdf_path, image_folder, text_output_folder, names_output_folder)
processor.process_pdf()  # Llama al método para procesar el PDF

print("Extracción completada. Texto, imágenes y nombres guardados.")  # Mensaje de finalización