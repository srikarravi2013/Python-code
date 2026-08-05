from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any
from analyzer.registry import BaseHandler

try:
    import pefile
    HAS_PEFILE = True
except ImportError:
    HAS_PEFILE = False


class ExecutableHandler(BaseHandler):
    supported_extensions = [".exe", ".dll", ".sys"]

    def analyze(self, path: Path) -> Dict[str, Any]:
        metadata = {}
        with open(path, "rb") as f:
            metadata["has_mz_header"] = f.read(2) == b"MZ"

        if not HAS_PEFILE:
            metadata["warning"] = "Install 'pefile' for deep binary analysis."
            return metadata

        try:
            pe = pefile.PE(str(path))
            machine = pe.FILE_HEADER.Machine
            metadata["architecture"] = pefile.MACHINE_TYPE.get(machine, f"Unknown (0x{machine:x})")

            compile_time = datetime.fromtimestamp(pe.FILE_HEADER.TimeDateStamp, tz=timezone.utc)
            metadata["compile_timestamp_utc"] = compile_time.strftime("%Y-%m-%d %H:%M:%S UTC")
            metadata["section_count"] = pe.FILE_HEADER.NumberOfSections

            if hasattr(pe, "DIRECTORY_ENTRY_IMPORT"):
                metadata["imported_dll_count"] = len(pe.DIRECTORY_ENTRY_IMPORT)
            return metadata
        except Exception as e:
            metadata["pe_parse_error"] = str(e)
            return metadata