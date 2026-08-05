import hashlib
from pathlib import Path
from analyzer.models import Hashes


def compute_hashes(path: Path) -> Hashes:
    """Calculates MD5, SHA-1, and SHA-256 hashes in memory-safe chunks."""
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()

    chunk_size = 65536
    with open(path, "rb") as f:
        while chunk := f.read(chunk_size):
            md5.update(chunk)
            sha1.update(chunk)
            sha256.update(chunk)

    return Hashes(
        md5=md5.hexdigest(),
        sha1=sha1.hexdigest(),
        sha256=sha256.hexdigest(),
    )