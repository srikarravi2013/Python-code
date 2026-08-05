from pathlib import Path
from typing import Dict, Any
from analyzer.registry import BaseHandler

try:
    import exifread
    HAS_EXIF = True
except ImportError:
    HAS_EXIF = False


class ImageHandler(BaseHandler):
    supported_extensions = [".jpg", ".jpeg", ".tiff"]

    def analyze(self, path: Path) -> Dict[str, Any]:
        if not HAS_EXIF:
            return {"warning": "Install 'exifread' for EXIF metadata parsing."}

        metadata = {}
        with open(path, "rb") as f:
            tags = exifread.process_file(f, details=False)
            metadata["exif_tags_count"] = len(tags)
            for tag in ["Image Make", "Image Model", "EXIF DateTimeOriginal"]:
                if tag in tags:
                    metadata[tag] = str(tags[tag])
        return metadata