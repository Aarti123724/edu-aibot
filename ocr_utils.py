import easyocr
import numpy as np
from pdf2image import convert_from_bytes

reader = easyocr.Reader(
    ['en'],
    gpu=False
)

def extract_text_from_scanned_pdf(pdf_file):

    text = ""

    images = convert_from_bytes(
        pdf_file.read()
    )

    for image in images:

        # PIL Image → NumPy Array
        image_np = np.array(image)

        results = reader.readtext(
            image_np
        )

        for result in results:

            text += result[1] + "\n"

    return text