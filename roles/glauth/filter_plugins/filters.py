# https://www.iops.tech/blog/generate-toml-using-ansible-template/

import json
import toml


class FilterModule:

    def filters(self):
        return {
            "to_toml": self.to_toml,
        }

    def to_toml(self, variable):
        serialized_json = json.dumps(dict(variable))
        return toml.dumps(json.loads(serialized_json))
