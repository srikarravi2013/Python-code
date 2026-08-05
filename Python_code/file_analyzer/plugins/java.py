import struct
from pathlib import Path
from typing import Dict, Any
from analyzer.registry import BaseHandler


class JavaHandler(BaseHandler):
    supported_extensions = [".class", ".jar", ".war"]

    # Java major class version mapping
    CLASS_VERSIONS = {
        52: "Java 8",
        55: "Java 11",
        61: "Java 17",
        65: "Java 21",
    }

    def analyze(self, path: Path) -> Dict[str, Any]:
        metadata = {}
        ext = path.suffix.lower()

        if ext == ".class":
            with open(path, "rb") as f:
                header = f.read(8)
                if len(header) == 8:
                    magic, minor, major = struct.unpack(">IHH", header)
                    metadata["valid_java_class"] = magic == 0xCAFEBABE
                    metadata["major_version"] = major
                    metadata["java_target"] = self.CLASS_VERSIONS.get(major, f"JDK Major Version {major}")
        elif ext in [".jar", ".war"]:
            metadata["format"] = "Java Archive (ZIP Compressed)"
            with open(path, "rb") as f:
                metadata["valid_zip_header"] = f.read(4) == b"PK\x03\x04"

        return metadata