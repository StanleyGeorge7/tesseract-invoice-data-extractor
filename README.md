# tesseract-invoice-extractor

A Python project for automated extraction of data from invoice images using Tesseract OCR, with custom parsing logic based on input format and a user-friendly Streamlit interface.

---

## Overview

**tesseract-invoice-extractor** streamlines the process of converting invoice images into structured text data. Built on Python and Tesseract OCR, it features a simple Streamlit web interface and customizable parsing logic tailored to your invoice layouts.

---

## Features

- Accurate text recognition using Tesseract OCR
- Parsing logic adapted to your sample invoice formats
- Streamlit web UI for quick testing and demo
- Support for various image formats (JPG, PNG, TIFF, etc.)
- Sample input images included for reference and testing

---

## Input Samples

Sample invoice images are provided in the `input/` directory. The data extraction and parsing logic are specifically designed around these samples’ layouts. If you add new invoice formats, update the parsing logic accordingly.

**Examples:**

- `input/invoice1.jpg`
- `input/invoice2.png`

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Krithika-AiDev/tesseract-invoice-extractor.git
   cd tesseract-invoice-extractor
   ```

2. **Set up a virtual environment** (optional but recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Tesseract OCR**

   - Download and install Tesseract from the [official repo](https://github.com/tesseract-ocr/tesseract).
   - Note the installation path (e.g., `C:\Program Files\Tesseract-OCR\tesseract.exe` on Windows).

5. **Configure the Tesseract path**

   In your code or environment, specify the Tesseract executable path:

   ```python
   import pytesseract
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

   Update this path according to your system.

---

## Usage

### Run the Streamlit App

```bash
streamlit run app.py
```

- Upload an invoice image via the UI.
- The app will display extracted and parsed invoice data.

---

## Parsing Logic

The invoice parsing logic is defined in `parsing.py`, tailored to extract key information (like invoice number, date, total, etc.) based on the structure of sample invoices in the `input/` directory.  
New or different invoice formats may require updates to the parsing rules.

---

## Contributing

- Add new invoice samples to the `input/` directory.
- If you introduce new invoice formats, please update the parsing logic in `parsing.py`.
- Pull requests and suggestions are welcome!

---

## License

This project is licensed under the MIT License.

---

## Contact

For questions or feedback, please open an issue or contact [Stanley George](https://github.com/StanleyGeorge7).
