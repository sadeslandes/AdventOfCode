#!/bin/bash

read year day < <(date '+%Y %-d')

python -m pytest -m "y$year and d$day" -v