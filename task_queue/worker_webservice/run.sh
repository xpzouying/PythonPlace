#!/bin/bash

exec gunicorn --paste task_queue.ini
# exec gunicorn --paste task_queue.ini -b :9001 --chdir $(pwd)
