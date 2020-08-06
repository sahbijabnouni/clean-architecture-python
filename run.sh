#!/bin/bash
gunicorn --reload --bind 0.0.0.0:8070  wsgi --chdir app