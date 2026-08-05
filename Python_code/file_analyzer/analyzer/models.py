from dataclasses import dataclass, field, asdict
from typing import Dict, Any, List, Optional


@dataclass
class BasicInfo:
    file_name: str
    absolute_path: str
    extension: str
    size_bytes: int
    size_human: str


@dataclass
class Timestamps:
    created_utc: str
    modified_utc: str
    accessed_utc: str


@dataclass
class Permissions:
    octal_permissions: str
    readable: bool
    writable: bool
    executable: bool
    owner_id: int
    group_id: int


@dataclass
class Hashes:
    md5: str
    sha1: str
    sha256: str


@dataclass
class ContentPreview:
    format_class: str
    encoding: Optional[str] = None
    total_lines: Optional[int] = None
    first_few_lines: Optional[str] = None
    hex_dump_sample: Optional[str] = None


@dataclass
class AnalysisReport:
    basic_info: BasicInfo
    timestamps: Timestamps
    permissions: Permissions
    hashes: Hashes
    content_preview: ContentPreview
    type_specific_metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert nested dataclasses into a plain dictionary for JSON serialization."""
        return asdict(self)