
import sys
from anytree import Node, RenderTree
import pathlib
import subprocess


def find_children(parent, root):
    cmd = "grep -r -l '%s' %s" % (parent, root)
    out = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    lines = out.stdout.readlines()
    children = [pathlib.Path(dep.strip().decode()).stem for dep in lines]
    return children

def graph(name, regex, root):
    root = pathlib.Path(root)
    out = dict()
    out[name] = Node(name)  # parent
    _viewed = []
    _remains = [name]

    while len(_remains):
        _parent = _remains.pop(0)
        if _parent in _viewed: continue

        _parent_ptrn = regex % _parent
        children = find_children(_parent_ptrn, root)

        _viewed.append(_parent)
        _remains.extend(children)

        for child in children:
            out[child] = Node(child, parent=out[_parent])

    return out


if __name__ == '__main__':
    try:
        name, regex, root = sys.argv[1:]
    except ValueError:
        print("""
        python dag.py mord2pord "=\s*%s(" "/home/mgreco/matlab/ets"
            name = "mord2pord"
            regex = "=\s*%s("
            root = "/home/mgreco/matlab/ets"

        This will return something like:

            mord2pord
            └── pmodelsgeneration
                ├── simulateiom
                │   └── simulateiom
                ├── generatetoday
                └── pmodelsgeneration
        """)
    n = graph(name, regex, root)
    for pre, fill, node in RenderTree(n[name]):
        print("%s%s" % (pre, node.name))
