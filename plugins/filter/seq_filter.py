from collections.abc import Iterable


class FilterModule:

    def filters(self):
        return {
            "to_list": self.to_list,
        }

    def to_list(self, var):
        if isinstance(var, str) or not isinstance(var, Iterable):
            return [var]
        return list(var)
