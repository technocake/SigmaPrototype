#!/bin/sh
inkscape favicon.svg --export-png=favicon.png -w 120 && convert favicon.png favicon.ico
