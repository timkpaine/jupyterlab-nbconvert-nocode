from pathlib import Path

from nbconvert.nbconvertapp import NbConvertApp

root = Path(__file__).parent


class TestImport:
    def test_convert(self):
        NbConvertApp.launch_instance(
            [
                "--to",
                "html_nocode",
                "jupyterlab_nbconvert_nocode/tests/Test.ipynb",
                "--output",
                "test_html_nocode.html",
            ]
        )

        assert (root / "test_html_nocode.html").exists()

        NbConvertApp.launch_instance(
            [
                "--to",
                "pdf_nocode",
                "jupyterlab_nbconvert_nocode/tests/Test.ipynb",
                "--output",
                "test_pdf_nocode.pdf",
            ]
        )

        assert (root / "test_pdf_nocode.pdf").exists()

        NbConvertApp.launch_instance(
            [
                "--to",
                "webpdf_nocode",
                "jupyterlab_nbconvert_nocode/tests/Test.ipynb",
                "--output",
                "test_webpdf_nocode",
            ]
        )

        assert (root / "test_webpdf_nocode.pdf").exists()
