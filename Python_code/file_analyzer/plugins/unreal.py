import struct
from pathlib import Path
from typing import Dict, Any
from analyzer.registry import BaseHandler


class UnrealEngineHandler(BaseHandler):
    supported_extensions = [".uasset", ".umap", ".uexp", ".ubulk"]

    def analyze(self, path: Path) -> Dict[str, Any]:
        metadata = {}
        with open(path, "rb") as f:
            header = f.read(4)

        if len(header) == 4:
            # Check for Unreal Engine Package Magic Signature (0x9E2A83C1)
            magic = struct.unpack("<I", header)[0]
            metadata["has_valid_unreal_magic"] = magic == 0x9E2A83C1
            metadata["raw_magic_hex"] = hex(magic)

        metadata["engine_target"] = "Unreal Engine 4/5"
        return metadata