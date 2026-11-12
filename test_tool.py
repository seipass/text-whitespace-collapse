import json
from text_whitespace_collapse import transform
def test_transform():
    value='a  b\nc'
    if True: result=transform(value)
    else: result=transform(json.loads(value))
    assert 'a b c' in json.dumps(result,ensure_ascii=False)
