from ruamel.yaml.comments import CommentedMap, CommentedSeq
_copy = {'image':'image', 'environment':'env'}
def transform(dc_data):
    res = CommentedMap()
    services = dc_data["services"]
    for name, props in services.items():
        res[name] = CommentedMap()
        for copy_from, copy_to in _copy.items():
            if copy_from in props:
                #if isinstance(props[copy_from], (str,int)):
                if hasattr(props[copy_from], 'copy1'):
                    res[name][copy_to] = props[copy_from].copy()
                else:
                    res[name][copy_to] = props[copy_from]
    return res

def act_copy(_from,_to):
    _to = _from.copy()
    return _to

_rules = [
    {'from':'image', 'to':'image', 'action': act_copy}
]

