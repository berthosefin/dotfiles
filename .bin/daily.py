#!/usr/bin/env python3
"""
Daily
=====

Mijery ny Teny vakina epub dia mampiseho ny andininteny androany.
"""

from xml.etree import ElementTree
from zipfile import ZipFile
from datetime import date
from textwrap import wrap
from pathlib import Path
import sys

today = date.today()


DAILY_FILENAME = f"es{str(today.year)[2:4]}_MG.epub"

# Apetrao ao amin'ny ~/JW/Document/epub ny boky epub"es20_MG.epub" sy "es21_MG.epub"
# na afaka solinao eo amin'ny ilay oe <PATH> ny tokony hisy azy

# Download link: 
# https://download-a.akamaihd.net/files/media_publication/11/es20_MG.epub
# https://download-a.akamaihd.net/files/media_publication/04/es21_MG.epub

PATH = Path.home() / "JW/Document/epub" / DAILY_FILENAME


DAILY_FILE = ZipFile(PATH)

# Soloy teny hafa ireto raha epub amin'ny teny hafa no ampiasainao

MONTH_SHORT2LONG = [
    'janoary',
    'febroary',
    'martsa',
    'aprily',
    'may',
    'jona',
    'jolay',
    'aogositra',
    'septambra',
    'oktobra',
    'novambra',
    'desambra', ]


def parse(file):
    """
    Mijery ny fichier anaty epub (zip)
    """

    with DAILY_FILE.open(f"OEBPS/{file}") as fp:
        parsed = ElementTree.fromstring(fp.read())

    return parsed


def get_month_file():
    """
    Maka ny fichier misy ny andininteny androany.
    """

    month = MONTH_SHORT2LONG[today.month - 1].title()
    day = today.day

    for element in parse("toc.xhtml").iter():
        if element.text == month:
            begin = element.attrib["href"]

    if day == 1:
        return begin
    else:
        part = begin.split(".")
        part[0] += f"-split{day}"

        return ".".join(part)


def get_text():
    """
    Maka ny soratra misy ny andininteny androany.
    """

    i = 0
    text_list = list()

    for element in parse(get_month_file()).iter():
        if i >= 2:
            break
        if element.tag == '{http://www.w3.org/1999/xhtml}em':
            text_list.append(element)
            i += 1

    result_text = text_list[0].text[:-1]
    result_chap = list(text_list[1].iter())[1].text

    result_text = "".join(list(result_text))

    return [result_text, result_chap]


def main():

    result = get_text()

    # Soloy isa hafa akotran'ny 70 eto raha tiana ho lavalava kokoa ny teny

    default_width = 70

    try:
        width = int(sys.argv[1])
    except IndexError:
        width = default_width
    except ValueError:
        width = default_width


    print("\n".join(wrap(result[0], width)))
    print(f"—{result[1]}")


if __name__ == '__main__':
    main()
