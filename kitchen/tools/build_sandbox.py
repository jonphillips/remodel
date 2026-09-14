#!/usr/bin/env python3
"""Build the direct-manipulation kitchen sandbox(es) from the canonical model.

Reads the current geometry snapshot and inlines it into the template, so each
sandbox opens with real dimensions but never reads or writes the source files
at runtime. Re-run this whenever the canonical model changes.

    python3 kitchen/tools/build_sandbox.py

Two scopes are produced from the one template:
    sandbox.html         kitchen only (stay focused on the kitchen)
    sandbox-porch.html   kitchen + the reclaimable old porch (161 x 111)

Each also gets a head/body-less *.fragment.html for publishing as an Artifact.
All generated files are gitignored; edit sandbox.template.html, not them.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
MODEL = REPO / "kitchen" / "studies" / "02-purposeful" / "explorations-model.json"
TEMPLATE = HERE / "sandbox.template.html"

VARIANTS = [
    {"scope": "kitchen", "title": "Kitchen Layout Sandbox", "out": "sandbox"},
    {"scope": "full", "title": "Kitchen + Porch Sandbox", "out": "sandbox-porch"},
]


def main() -> None:
    model = json.loads(MODEL.read_text())
    template = TEMPLATE.read_text()
    # Compact JSON keeps the inlined snapshot small; separators avoid stray spaces.
    payload = json.dumps(model, separators=(",", ":"))
    print(f"model version: {model.get('version')}")

    for v in VARIANTS:
        html = (
            template
            .replace("__MODEL_JSON__", payload)
            .replace("__SCOPE__", v["scope"])
            .replace("__TITLE__", v["title"])
        )
        standalone = HERE / f"{v['out']}.html"
        standalone.write_text(html)

        # Artifact fragment: strip the document skeleton; keep the head title.
        start = html.index("<link ")
        end = html.rindex("</script>") + len("</script>")
        fragment = f"<title>{v['title']}</title>\n" + html[start:end] + "\n"
        (HERE / f"{v['out']}.fragment.html").write_text(fragment)

        print(f"  [{v['scope']:>7}] wrote {standalone.name} ({len(html):,} bytes) + {v['out']}.fragment.html")


if __name__ == "__main__":
    main()
