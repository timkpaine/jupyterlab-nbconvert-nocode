from jupyter_core.paths import jupyter_path
from nbconvert.exporters.html import HTMLExporter
from nbconvert.exporters.pdf import PDFExporter
from nbconvert.exporters.webpdf import WebPDFExporter

__all__ = (
    "HTMLHideCodeExporter",
    "PDFHideCodeExporter",
    "WebPDFHideCodeExporter",
)


class HTMLHideCodeExporter(HTMLExporter):
    export_from_notebook = "HTML - No Code"

    def _template_name_default(self):
        return "html_nocode"


class PDFHideCodeExporter(PDFExporter):
    export_from_notebook = "PDF - No Code"

    def _template_data_paths_default(self):
        return jupyter_path("nbconvert", "templates", "pdf_nocode")

    def _template_name_default(self):
        return "pdf_nocode"


class WebPDFHideCodeExporter(WebPDFExporter):
    export_from_notebook = "WebPDF - No Code"

    def _template_data_paths_default(self):
        return jupyter_path("nbconvert", "templates", "webpdf_nocode")

    def _template_name_default(self):
        return "webpdf_nocode"
