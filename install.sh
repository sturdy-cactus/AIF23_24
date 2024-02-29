#!/bin/bash

mkdir prova_finale_abramo

curl -o prova_finale_abramo/launch.sh https://raw.githubusercontent.com/sturdy-cactus/AIF23_24/master/launch
curl -o prova_finale_abramo/prova_finale.py https://raw.githubusercontent.com/sturdy-cactus/AIF23_24/master/prova_finale.py

chmod +x prova_finale_abramo/launch.sh

export PYTHONPATH="$PYTHONPATH:/prova_finale_abramo"
export PATH="$PATH:/prova_finale_abramo"