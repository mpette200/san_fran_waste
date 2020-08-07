#!/bin/bash
set -x
docker run -d -p 127.0.0.1:8050:8050 -e PORT=8050 uwsgi_mp:0.03
