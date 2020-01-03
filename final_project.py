#coding:gbk
"""
����:����Խ
"""

import os, sys
import jieba, codecs, math
import jieba.posseg as pseg
names = {}
relationships = {}
lineNames = []
jieba.load_userdict("dict.txt")
with codecs.open("���������Ľֵ�.txt", "r", "gbk") as a:

	for line in a.readlines():

		poss = pseg.cut(line)

		lineNames.append([])

		for w in poss:

			if w.flag != "nr" or len(w.word) < 2:

				continue

			lineNames[-1].append(w.word)

			if names.get(w.word) is None:

				names[w.word] = 0

				relationships[w.word] = {}

			names[w.word] += 1

for line in lineNames:

	for name1 in line:

		for name2 in line:

			if name1 == name2:

				continue

			if relationships[name1].get(name2) is None:

				relationships[name1][name2]= 1

			else:

				relationships[name1][name2] = relationships[name1][name2]+ 1
with codecs.open("node.txt", "w", "gbk") as a:

	a.write("Id Label Weight\r\n")

	for name, times in names.items():

		a.write(name + " " + name + " " + str(times) + "\r\n")
with codecs.open("edge.txt", "w", "gbk") as a:

	a.write("Source Target Weight\r\n")

	for name, edges in relationships.items():

		for v, w in edges.items():

			if w > 10:
				a.write(name + " " + v + " " + str(w) + "\r\n")
