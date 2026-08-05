from pathlib import Path
from typing import Dict, Any
from analyzer.registry import BaseHandler

try:
    import pypdf
    HAS_PDF = True
except ImportError:
    HAS_PDF = False


class PDFHandler(BaseHandler):
    supported_extensions = [".pdf"]

    def analyze(self, path: Path) -> Dict[str, Any]:
        if not HAS_PDF:
            return {"warning": "Install 'pypdf' for PDF metadata parsing."}

        try:
            reader = pypdf.PdfReader(path)
            meta = {
                "pages": len(reader.pages),
                "encrypted": reader.is_encrypted,
            }
            if reader.metadata:
                meta["author"] = reader.metadata.get("/Author", "Unknown")
                meta["creator"] = reader.metadata.get("/Creator", "Unknown")
            return meta
        except Exception as e:
            return {"pdf_error": str(e)}