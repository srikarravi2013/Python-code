from pathlib import Path
from typing import Dict, Any
from analyzer.registry import BaseHandler


class UnityHandler(BaseHandler):
    supported_extensions = [".unitypackage", ".unity3d", ".asset", ".prefab", ".unity"]

    def analyze(self, path: Path) -> Dict[str, Any]:
        metadata = {}
        with open(path, "rb") as f:
            header = f.read(32)

        # Check for Unity Web/AssetBundle Magic Signatures
        if b"UnityRaw" in header or b"UnityWeb" in header or b"UnityFS" in header:
            metadata["unity_file_type"] = "Unity AssetBundle"
            metadata["signature"] = header.split(b"\x00")[0].decode("ascii", errors="replace")
        elif path.suffix.lower() == ".unitypackage":
            metadata["unity_file_type"] = "Unity Package Archive (GZipped Tar)"
        else:
            metadata["unity_file_type"] = "Unity Asset / YAML Serialized Scene"

        return metadata