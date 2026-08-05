from pathlib import Path
from typing import Dict, Any
from analyzer.registry import BaseHandler

try:
    import mutagen
    HAS_MUTAGEN = True
except ImportError:
    HAS_MUTAGEN = False


class MP3Handler(BaseHandler):
    supported_extensions = [".mp3"]

    def analyze(self, path: Path) -> Dict[str, Any]:
        if not HAS_MUTAGEN:
            return {"warning": "Install 'mutagen' for audio tag parsing."}

        try:
            audio = mutagen.File(path)
            metadata = {}
            if audio and audio.info:
                metadata["duration_seconds"] = round(audio.info.length, 2)
                metadata["bitrate_kbps"] = int(audio.info.bitrate / 1000) if hasattr(audio.info, "bitrate") else "N/A"
                metadata["sample_rate_hz"] = getattr(audio.info, "sample_rate", "N/A")

            if audio and audio.tags:
                metadata["title"] = str(audio.tags.get("TIT2", "Unknown"))
                metadata["artist"] = str(audio.tags.get("TPE1", "Unknown"))
                metadata["album"] = str(audio.tags.get("TALB", "Unknown"))
            return metadata
        except Exception as e:
            return {"audio_error": str(e)}