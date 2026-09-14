from pathlib import Path
import json
r=Path(__file__).parent
s=(r/'explorations.template.html').read_text().replace('__MODEL__',json.dumps(json.loads((r/'explorations-model.json').read_text()),separators=(',',':')))
(r/'explorations-fragment.html').write_text(s)
