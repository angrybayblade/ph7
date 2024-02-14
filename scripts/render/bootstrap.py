import re
from pathlib import Path

import requests
from black import Mode, format_str

url = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
bootstrap = requests.get(url=url).content.decode()
classes = set()
for spec in bootstrap.split("}.")[1:]:
    name, *_ = spec.split("{")
    name, *_ = name.split(":")
    if "." in name:
        *_, name = name.split(".")
    if "~" in name or " " in name:
        continue
    classes.add(re.sub(r"[\>\*]", "", name))

code = """\"\"\"This file is autogenerate using scripts/render/bootstrap.py\"\"\"

"""

for cls in sorted(classes):
    var = re.sub(r"[\[\]\-=]", "_", cls)
    if "," not in var:
        code += var + "=" + '"' + f"{cls}" + '"\n'
        continue
    code += var + "=" + ",".join(map(lambda x: f'"{x}"', cls.split(","))) + "\n"

Path("contrib/bootstrap/bootstrap/css.py").write_text(format_str(code, mode=Mode()))
