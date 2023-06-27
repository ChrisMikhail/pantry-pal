#!/bin/bash
source /home/my-VM/pantry-pal-redo/myenv/bin/activate
cd /home/my-VM/pantry-pal-redo
/home/my-VM/pantry-pal-redo/myenv/bin/waitress-serve --host=0.0.0.0 --port=80 app:app
