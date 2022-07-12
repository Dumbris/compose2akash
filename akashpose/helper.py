from collections.abc import Mapping

def traverse(data, path):
        for k,v in data.items():
            if isinstance(v, Mapping):
                yield from traverse(v, path+[k])
            else:
                yield path+[k],v