#!/usr/local/bin/python3
# -*- coding: iso-8859-15 -*-

import sys
import re
import pandas as pd


def grafico(source):
    arquivo = pd.read_csv(source, delimiter=";")
    colunas = list(filter(
        lambda c: re.search(r'código', c, re.I) is None, list(arquivo.columns)
    ))
    arquivo[colunas].to_csv('graficos/' + source, index=False)


source = sys.argv[1]
grafico(source)
