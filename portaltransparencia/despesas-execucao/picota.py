#!/usr/local/bin/python3


import sys
import re
import pandas as pd


def grafico(source):

    arquivo = pd.read_csv(source, delimiter=";", low_memory=False)
    colunas = filter(
        lambda c: re.search(r'^código', c, re.I) is None, arquivo.columns
    )
    arquivo[list(colunas)].to_csv('graficos/' + source, index=False)


source = sys.argv[1]
grafico(source)
