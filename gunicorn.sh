#!/bin/sh
gunicorn rest:app -w 2 -b 0.0.0.0:8001 --keyfile cloud_interface.key --certfile cloud_interface.crt