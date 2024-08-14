# https://www.iops.tech/blog/generate-toml-using-ansible-template/

import json
import toml

# FIXME: should move this to a top-level collection plugin.


class FilterModule:

    def filters(self):
        return {
            "to_toml": self.to_toml,
            "from_toml": self.from_toml,
        }

    def to_toml(self, variable):
        serialized_json = json.dumps(dict(variable))
        return toml.dumps(json.loads(serialized_json))

    def from_toml(self, data):
        toml_data = toml.loads(data)
        return json.loads(json.dumps(dict(toml_data)))
