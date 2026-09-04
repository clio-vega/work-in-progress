"""trace.py -- session-stable wrapper around tracecheck.emit: appends to the ONE
log file opened at session start, continuing the sequence across processes."""
import sys, os, glob, json
sys.path.insert(0, '/home/clio/projects')
import tracecheck.emit as E

def attach():
    logs = sorted(glob.glob("/home/clio/projects/state/trajectory/clio-prove-*.jsonl"), key=os.path.getmtime)
    E._LOG = logs[-1]; E._AGENT = 'clio'
    E._SEQ = sum(1 for _ in open(E._LOG))
    return E._LOG

def emit(*a, **k):
    if E._LOG is None: attach()
    return E.emit(*a, **k)
