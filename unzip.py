import sys
from zipfile import PyZipFile

pzf = PyZipFile('parser_psychology_06082018.zip')
pzf.extractall()