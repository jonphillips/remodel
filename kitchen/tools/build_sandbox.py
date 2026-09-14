#!/usr/bin/env python3
"""Build the direct-manipulation kitchen sandbox from the canonical model.

Reads the current geometry snapshot and inlines it into the template, so the
sandbox opens with real dimensions but never reads or writes the source files
at runtime. Re-run this whenever the canonical model changes.

    python3 kitchen/tools/build_sandbox.py

Outputs (next to this script):
    sandbox.html           standalone page, open by double-click
    sandbox.fragment.html  head/body-less fragment for publishing as an Artifact
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
MODEL = REPO / "kitchen" / "studies" / "02-purposeful" / "explorations-model.json"
TEMPLATE = HERE / "sandbox.template.html"


def main() -> None:
    model = json.loads(MODEL.read_text())
    template = TEMPLATE.read_text()
    # Compact JSON keeps the inlined snapshot small; separators avoid stray spaces.
    payload = json.dumps(model, separators=(",", ":"))
    html = template.replace("__MODEL_JSON__", payload)

    standalone = HERE / "sandbox.html"
    standalone.write_text(html)

    # Artifact fragment: strip the document skeleton, keep <link>/<style>/markup/<script>.
    start = html.index("<link ")
    end = html.rindex("</script>") + len("</script>")
    fragment = "<title>Kitchen Layout Sandbox</title>\n" + html[start:end] + "\n"
    (HERE / "sandbox.fragment.html").write_text(fragment)

    print(f"model version: {model.get('version')}")
    print(f"wrote {standalone.relative_to(REPO)} ({len(html):,} bytes)")
    print(f"wrote {(HERE / 'sandbox.fragment.html').relative_to(REPO)} ({len(fragment):,} bytes)")


if __name__ == "__main__":
    main()
