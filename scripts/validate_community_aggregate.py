import json
import sys
from pathlib import Path

ALLOWED = {
    "platform_family": {"web", "windows", "macos", "android", "ios-ipados", "work-project", "other", "unknown"},
    "intermittent": {"yes", "no", "unknown"},
    "recovered_after_wait": {"yes", "no", "unknown"},
    "remained_visible": {"yes", "no", "unknown"},
    "terminal_class": {"429", "other-4xx", "5xx", "cancellation", "timeout", "other", "unknown"},
    "evidence_grade": {"S0", "S1", "S2", "S3", "unknown"},
}
REQUIRED = {"symptom_family", "platform_family", "terminal_class", "evidence_grade", "report_count"}
ALLOWED_KEYS = REQUIRED | {"intermittent", "recovered_after_wait", "remained_visible"}


def validate(path: Path) -> None:
    rows = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(rows, list):
        raise ValueError("top level must be an array")
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            raise ValueError(f"row {i}: object required")
        missing = REQUIRED - row.keys()
        extra = row.keys() - ALLOWED_KEYS
        if missing or extra:
            raise ValueError(f"row {i}: missing={sorted(missing)} extra={sorted(extra)}")
        if not isinstance(row["symptom_family"], str) or not row["symptom_family"].strip():
            raise ValueError(f"row {i}: invalid symptom_family")
        if not isinstance(row["report_count"], int) or isinstance(row["report_count"], bool) or row["report_count"] < 1:
            raise ValueError(f"row {i}: report_count must be integer >= 1")
        for key, values in ALLOWED.items():
            if key in row and row[key] not in values:
                raise ValueError(f"row {i}: invalid {key}={row[key]!r}")
    print(f"PASS: {len(rows)} aggregate row(s) validated from {path}")


if __name__ == "__main__":
    validate(Path(sys.argv[1] if len(sys.argv) > 1 else "data/community-aggregate.example.json"))
