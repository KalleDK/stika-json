import json
import typing
import dataclasses


class JSONDecoder(json.JSONDecoder):

    __slots__ = ['data_cls']

    def __init__(self, data_cls, **kwargs):
        super().__init__(**kwargs)
        if not dataclasses.is_dataclass(data_cls):
            raise ValueError
        self.data_cls = data_cls

    def _encode_field(self, cls: dataclasses.Field, obj):

        t: type = cls.type

        # If the field is a Dataclass encode it
        if dataclasses.is_dataclass(t):
            try:
                return self._encode_dataclass(t, obj)
            except ValueError:
                raise ValueError("{} has to be a dict".format(cls.name))

        origin = getattr(t, '__origin__', None)
        if origin == typing.Union:
            if type(obj) in t.__args__:
                return obj
            for arg in t.__args__:
                if dataclasses.is_dataclass(arg):
                    try:
                        return self._encode_dataclass(arg, obj)
                    except ValueError:
                        raise ValueError("{} has to be a dict".format(cls.name))

        # Verify that the object is the correct type
        if isinstance(obj, t):
            return obj

        raise ValueError("invalid type for object")

    def _encode_dataclass(self, cls, dct: dict):
        cls_fields = cls.__dataclass_fields__

        if not isinstance(dct, dict):
            raise ValueError("invalid dict")

        # Get get the set of all the dict's keys and Dataclass keys
        fields = {*dct.keys(), *cls_fields.keys()}

        # If the dict has keys not in the dataclass, raise an exception
        if not set(dct.keys()).issubset(cls_fields.keys()):
            difference = fields.difference(cls_fields.keys())
            raise ValueError("dataclass {} does not contain the fields {}".format(cls, difference))

        # Encode all the fields to the correct type
        kwargs = {name: self._encode_field(cls_fields[name], dct.get(name)) for name in fields}

        # Return the new dataclass object
        return cls(**kwargs)

    def raw_decode(self, s, idx=0):
        dct, edx = super().raw_decode(s, idx=idx)
        return self._encode_dataclass(self.data_cls, dct), edx
