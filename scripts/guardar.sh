#!/bin/bash

python3 "/media/TPI/programa/conversor de numeros.py" 2>&1 | tee  "/media/TPI/resultado_$(date +%Y-%m-%d_%H-%M-%S).txt"
