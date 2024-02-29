#!/bin/bash

URL="https://raw.githubusercontent.com/MilenaValentini/TRM_Dati/main/Nemo_6670.dat"
OUTPUT_FILE="Nemo_6670.dat"

curl -o "$OUTPUT_FILE" "$URL"

python3 prova_finale.py "$OUTPUT_FILE"
