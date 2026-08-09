import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

from analyzer.hashes import compute_hashes
from analyzer.models import (
    AnalysisReport,
    BasicInfo,
    ContentPreview,
    Permissions,
    Timestamps,
)
from analyzer.registry import registry


def initialize_framework():
    """Locate and auto-register internal handlers and external drop-in plugins."""
    handlers_dir = Path(__file__).parent / "analyzer" / "handlers"
    registry.load_builtins(str(handlers_dir), "analyzer.handlers")

    plugins_dir = Path(__file__).parent / "plugins"
    registry.load_external_plugins(plugins_dir)


def format_size(size_bytes: int) -> str:
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} PB"


def extract_content_preview(path: Path) -> ContentPreview:
    with open(path, "rb") as f:
        raw_sample = f.read(1024)
        if b"\x00" in raw_sample:
            return ContentPreview(
                format_class="Binary", hex_dump_sample=raw_sample[:64].hex(" ")
            )

    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            lines = [f.readline() for _ in range(10)]
            line_count = sum(1 for _ in f) + len(lines)
        return ContentPreview(
            format_class="Text",
            encoding="UTF-8 (assumed)",
            total_lines=line_count,
            first_few_lines="".join(lines).strip(),
        )
    except Exception as e:
        return ContentPreview(format_class="Unknown", hex_dump_sample=str(e))


def analyze_file(file_path: str) -> AnalysisReport:
    path = Path(file_path).resolve()
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    st = path.stat()

    basic_info = BasicInfo(
        file_name=path.name,
        absolute_path=str(path),
        extension=path.suffix.lower() or "None",
        size_bytes=st.st_size,
        size_human=format_size(st.st_size),
    )

    timestamps = Timestamps(
        created_utc=datetime.fromtimestamp(st.st_ctime, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        modified_utc=datetime.fromtimestamp(st.st_mtime, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        accessed_utc=datetime.fromtimestamp(st.st_atime, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
    )

    permissions = Permissions(
        octal_permissions=oct(st.st_mode)[-3:],
        readable=os.access(path, os.R_OK),
        writable=os.access(path, os.W_OK),
        executable=os.access(path, os.X_OK),
        owner_id=st.st_uid,
        group_id=st.st_gid,
    )

    hashes = compute_hashes(path)
    preview = extract_content_preview(path)

    # Handlers registry lookup
    handler = registry.get_handler(path.suffix)
    type_metadata = handler.analyze(path) if handler else {"note": "No handler registered for this extension"}

    return AnalysisReport(
        basic_info=basic_info,
        timestamps=timestamps,
        permissions=permissions,
        hashes=hashes,
        content_preview=preview,
        type_specific_metadata=type_metadata,
    )


def print_report(report: AnalysisReport):
    data = report.to_dict() 
    print(f" FILE ANALYSIS REPORT: {report.basic_info.file_name}")
    for section_name, section_data in data.items():
        print(f"\n🔹 [{section_name.replace('_', ' ').upper()}]")
        if isinstance(section_data, dict):
            for k, v in section_data.items():
                if k == "first_few_lines":
                    print(f"  • Preview:\nSTART:\n{v}\nEND:")
                else:
                    print(f"  • {k}: {v}")
    


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_file>")
        sys.exit(1)

    initialize_framework()
    report_obj = analyze_file(sys.argv[1])
    print_report(report_obj)

    # Save output as JSON using dataclass conversion
    output_path = f"{sys.argv[1]}_analysis.json"
    with open(output_path, "w") as f:
        json.dump(report_obj.to_dict(), f, indent=4)
    print(f"\n[+] Full report exported to: {output_path}")
