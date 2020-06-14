""" script to batch process a directory of svgs """

from subprocess import Popen
from os.path import isfile, join
from os import listdir

from pathlib import Path
THISDIR = str(Path(__file__).resolve().parent)

files = [
file.replace(".svg", "") for file in listdir(THISDIR)
if isfile(join(THISDIR, file)) and file.endswith(".svg")]
for file in files:
	with Popen(f"inkscape.com {file}.svg -w 160 -y 255 -o {file}.png;convert {file}.png {file}.bmp;potrace {file}.bmp -s -o {file}.svg;rm {file}.png;rm {file}.bmp", shell=True) as process:
		exitCode = process.wait()
	if exitCode > 0:
		print(f"error for file: {file}")
	else:
		print(f"success for file: {file}")
