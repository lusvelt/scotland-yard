import xml.etree.ElementTree as ET
import csv

TRANSPORTATIONS = ['taxi', 'bus', 'underground', 'boat']

graph = {}

def add_edge(start, end, transportation):
    if start not in graph.keys():
        graph[start] = []
    if end not in graph.keys():
        graph[end] = []
    graph[start].append((end, transportation))
    graph[end].append((start, transportation))


if __name__ == '__main__':
    boardPositions = ET.Element('boardPositions')
    with open('edges.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        for rawEdge in spamreader:
            start = int(rawEdge[0])
            end = int(rawEdge[1])
            transportation = TRANSPORTATIONS[int(rawEdge[2]) - 1]
            add_edge(start, end, transportation)
    for node in graph.keys():
        boardPosition = ET.SubElement(boardPositions, 'boardPosition')
        boardPosition.attrib['id'] = str(node)
        for edge in graph[node]:
            action = ET.SubElement(boardPosition, 'action')
            end, transportation = edge
            tr = ET.SubElement(action, 'transportation')
            tr.text = transportation
            destination = ET.SubElement(action, 'destination')
            destination.text = str(end)
    tree = ET.ElementTree(boardPositions)
    ET.indent(tree, space='\t')
    tree.write('board_file_ita.xml', encoding='utf-8')



