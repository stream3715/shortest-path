#!/usr/bin/env python3
import sys
import networkx as nx


def main(path, fromNode, toNode):
    G = nx.Graph(nx.nx_pydot.read_dot(path))
    shPathList = nx.shortest_path(
        G,
        source=str(int(fromNode) - 1),
        target=str(int(toNode) - 1)
    )
    print(shPathList)


if __name__ == "__main__":
    args = sys.argv
    main(args[1], args[2], args[3])
