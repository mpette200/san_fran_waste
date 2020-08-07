#!/bin/bash
set -x
# heroku login
heroku container:login

docker tag uwsgi_mp:0.03 registry.heroku.com/sf-waste/web
docker push registry.heroku.com/sf-waste/web
heroku container:release web --app sf-waste

heroku container:logout
# heroku logout
