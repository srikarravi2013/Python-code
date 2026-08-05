import zipfile
from pathlib import Path
from typing import Dict, Any
from analyzer.registry import BaseHandler


class APKHandler(BaseHandler):
    supported_extensions = [".apk", ".aab"]

    def analyze(self, path: Path) -> Dict[str, Any]:
        metadata = {"is_valid_zip": False}

        try:
            with zipfile.ZipFile(path, "r") as zip_ref:
                metadata["is_valid_zip"] = True
                file_list = zip_ref.namelist()

                # Search for essential Android manifest & DEX code files
                metadata["contains_android_manifest"] = "AndroidManifest.xml" in file_list
                metadata["contains_resources"] = "resources.arsc" in file_list
                metadata["dex_file_count"] = sum(1 for name in file_list if name.endswith(".dex"))

        except Exception as e:
            metadata["apk_parse_error"] = str(e)

        return metadata