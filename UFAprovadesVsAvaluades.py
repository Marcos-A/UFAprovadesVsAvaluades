#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import re
from sys import argv
from tika import parser

PATTERN = re.compile('UF\d\d - \d{2,3} \d{1,2}')


def convert_pdf_to_txt(filename):
    raw = parser.from_file(filename)
    return raw['content']


def parse_text(text):
    return PATTERN.findall(text)


def calculate_passed_uf_ratio(uf_list):
    avaluades = len(uf_list)
    aprovades = len([uf.rsplit(" ",1)[1] for uf in uf_list if int(uf.rsplit(" ",1)[1])>=5])

    print(f"UF avaluades: {avaluades}\nUF aprovades: {aprovades}\nRatio d'UF aprovades: {((aprovades/avaluades)*100):.2f}%")


if __name__ == "__main__":
    if len(argv)==2:
        try:
            extracted_text = convert_pdf_to_txt(argv[1])
            uf_list = parse_text(extracted_text)
            calculate_passed_uf_ratio(uf_list)
        except FileNotFoundError as e:
            print(f"No existeix el fitxer {argv[1]}.")
    else:
        print("Falta el PDF.")