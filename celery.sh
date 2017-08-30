#!/usr/bin/env bash
export DJANGO_SETTINGS_MODULE=testImport.settings
celery -A testImport worker -l info