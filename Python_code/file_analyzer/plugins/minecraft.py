from pathlib import Path
from typing import Dict, Any
from analyzer.registry import BaseHandler


class MinecraftNBTHandler(BaseHandler):
    supported_extensions = [".nbt", ".dat", ".mca"]

    def analyze(self, path: Path) -> Dict[str, Any]:
        # Minimal signature check for GZip compressed NBT structures
        with open(path, "rb") as f:
            header = f.read(2)
            is_gzipped = header == b"\x1f\x8b"

        return {
            "minecraft_format": "NBT Compound / Region Data",
            "is_gzip_compressed": is_gzipped,
            "plugin_source": "plugins/minecraft.py",
        }