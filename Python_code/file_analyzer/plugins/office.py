from pathlib import Path
from typing import Dict, Any
from analyzer.registry import BaseHandler


class OfficeHandler(BaseHandler):
    supported_extensions = [".docx", ".xlsx", ".pptx", ".doc", ".xls", ".ppt"]

    def analyze(self, path: Path) -> Dict[str, Any]:
        metadata = {}
        with open(path, "rb") as f:
            header = f.read(8)

        # OpenXML Formats (.docx, .xlsx) are ZIP archives starting with PK\x03\x04
        if header.startswith(b"PK\x03\x04"):
            metadata["office_format"] = "Modern Office OpenXML (ZIP Container)"
            metadata["is_legacy"] = False
        # Legacy binary Office formats (.doc, .xls) start with OLE Header \xD0\xCF\x11\xE0
        elif header.startswith(b"\xd0\xcf\x11\xe0"):
            metadata["office_format"] = "Legacy Office Binary (OLE Compound Document)"
            metadata["is_legacy"] = True
        else:
            metadata["office_format"] = "Unknown / Non-standard Office Document"

        return metadata