#!/usr/bin/env python

import sys

sys.path.append('/var/www/update_monitor_server/venv/lib64/python3.6/site-packages')

sys.path.insert(0, '/var/www/recepie_book')

from server import app as application
