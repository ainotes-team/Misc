import json
import attr
import regipy
import pathlib

path = str(pathlib.Path.home()) + "/AppData/Local/Packages/1875vincentscode.AINotes_xnbggcnkvqcny/Settings/settings.dat"

reg = regipy.registry.RegistryHive(path)
for entry in reg.recurse_subkeys(reg.root, as_json=True):
	print(json.dumps(attr.asdict(entry), sort_keys=True, indent=4, separators=(',', ': ')))