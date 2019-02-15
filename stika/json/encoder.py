import json
import dataclasses


class JSONEncoder(json.JSONEncoder):
    def default(self, o):

        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)

        return super().default(o)
