from __future__ import annotations

import os
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IGNORED_PARTS = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "__pycache__",
    "node_modules",
    "staticfiles",
}


def joined(*parts: str) -> str:
    return "".join(parts)


legacy_token = joined("I", "D", "A", "C")
FORBIDDEN_PATTERNS = {
    "legacy organization token": re.compile(
        rf"(?<![A-Za-z]){legacy_token}(?![A-Za-z])", re.IGNORECASE
    ),
    "legacy branded identifier": re.compile(
        rf"(?<![A-Za-z]){legacy_token}(?:[-_.]|logo|laboratorios)",
        re.IGNORECASE,
    ),
    "legacy customization repository": re.compile(
        re.escape(joined("kpi", "_", "i", "d", "a", "c")), re.IGNORECASE
    ),
    "legacy infrastructure repository": re.compile(
        re.escape(joined("kobo-docker-", "I", "D", "A", "C")),
        re.IGNORECASE,
    ),
    "unrelated client name": re.compile(
        "|".join(
            (
                re.escape(joined("Cy", "cla")),
                re.escape(joined("Be", "tel", " ", "Bus")),
                re.escape(joined("Andes", "mar")),
                re.escape(joined("Cura", " ", "Calquin")),
                re.escape(joined("Cura", "-", "Calquin")),
                re.escape(joined("Cura", " ", "Calqu", "\u00ed", "n")),
            )
        ),
        re.IGNORECASE,
    ),
}

FORBIDDEN_FILENAMES = {
    joined("kobo", "logo.svg"),
    joined("kobo", "logo_symbol.svg"),
    joined("kobocat", "_logo.png"),
    joined("kobocat", "_photo.png"),
    joined("signup", "_photo.jpg"),
}


def audit_text(label: str, value: str, violations: list[str]) -> None:
    for reason, pattern in FORBIDDEN_PATTERNS.items():
        if pattern.search(value):
            violations.append(f"{label}: {reason}")


def audit_required_contracts(violations: list[str]) -> None:
    if (ROOT / "Dockerfile").exists():
        required = {
            "README.md": ("DataMovin",),
            "NOTICE.md": ("DataMovin",),
            "package.json": (
                "DataMovin",
                "https://github.com/proyectomovin/kpi-datamovin",
            ),
            "kobo/settings/base.py": (
                "DataMovin",
                "hola@movin.com.ar",
                "https://movin.com.ar/product-datos-campo",
            ),
            "static/datamovin.webmanifest": ("DataMovin", "#FF6D4D"),
        }
    else:
        required = {
            "README.md": ("DataMovin",),
            "NOTICE": ("DataMovin",),
            ".env.template": (
                "data.movin.com.ar",
                "hola@movin.com.ar",
                "ghcr.io/proyectomovin/kpi-datamovin",
            ),
            "docker-compose.easypanel.yml": (
                "DATAMOVIN_KF_SUBDOMAIN:-kf",
                "DATAMOVIN_KC_SUBDOMAIN:-kc",
                "DATAMOVIN_EE_SUBDOMAIN:-ee",
                "DATAMOVIN_PUBLIC_DOMAIN:-data.movin.com.ar",
                "datamovin_kobo_nginx",
            ),
        }

    for relative, expected_values in required.items():
        path = ROOT / relative
        if not path.is_file():
            violations.append(f"{relative}: required contract file missing")
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except OSError as error:
            violations.append(f"{relative}: cannot validate contract: {error}")
            continue
        for expected in expected_values:
            if expected not in content:
                violations.append(
                    f"{relative}: required DataMovin contract missing: {expected}"
                )


def main() -> int:
    violations: list[str] = []

    for directory, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [name for name in dirnames if name not in IGNORED_PARTS]
        base = Path(directory)

        for filename in filenames:
            path = base / filename
            relative = path.relative_to(ROOT)
            audit_text(str(relative), str(relative), violations)

            if path.name.lower() in FORBIDDEN_FILENAMES:
                violations.append(f"{relative}: obsolete visible asset")

            try:
                data = path.read_bytes()
            except OSError as error:
                violations.append(f"{relative}: cannot read file: {error}")
                continue

            for encoding in ("utf-8", "utf-16-le", "utf-16-be", "latin-1"):
                audit_text(
                    f"{relative} [{encoding}]",
                    data.decode(encoding, errors="ignore"),
                    violations,
                )

    audit_required_contracts(violations)

    if violations:
        print("\n".join(sorted(set(violations))))
        return 1

    print(f"{ROOT}: brand-boundary audit passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
