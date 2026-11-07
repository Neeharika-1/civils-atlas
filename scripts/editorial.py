"""Compatibility entry point: refresh ledgers only; never overwrite source provenance."""
import runpy,pathlib
runpy.run_path(str(pathlib.Path(__file__).with_name('reconcile.py')),run_name='__main__')
