#!/bin/sh
gunicorn rest:app -w 2 --threads 2 -b 0.0.0.0:8001