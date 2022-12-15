#!/usr/bin/env python3
import sys
from typing import Any
import networkx as nx


def printPaths(path: "dict[Any, dict[Any, list]] | dict | dict[Any, list] | list[None] | list"):
    printArr = []
    for i in path:
        printArr.append(int(i) + 1)
    print(printArr)


def main(path, fromNode, toNode):
    G = nx.Graph(nx.nx_pydot.read_dot(path))
    shPathList = nx.shortest_path(
        G,
        source=str(int(fromNode) - 1),
        target=str(int(toNode) - 1)
    )
    printPaths(shPathList)


if __name__ == "__main__":
    args = sys.argv
    main(args[1], args[2], args[3])
