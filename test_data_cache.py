import builtins

import return_entries


def test_return_all_entries_uses_memory_cache(monkeypatch):
    return_entries.refresh_data_cache()

    def fail_open(*args, **kwargs):
        raise AssertionError("Disk read should not happen while cache is warm")

    monkeypatch.setattr(builtins, "open", fail_open)

    rows = return_entries.return_all_entries()
    assert isinstance(rows, list)
    assert len(rows) >= 0
