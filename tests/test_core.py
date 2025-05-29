from pklxml import dump, load
import io

def test_basic_roundtrip():
    data = {"a": 1, "b": [2, 3]}
    buf = io.StringIO()
    dump(data, buf)
    buf.seek(0)
    loaded = load(buf)
    assert data == loaded
