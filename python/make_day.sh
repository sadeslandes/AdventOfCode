#!/bin/bash

DIR="`dirname $0`"

read year day < <(date '+%Y %-d')

if [ ! -z "$1" ]
then
    day=$1
fi

if [ ! -z "$2" ]
then
    year=$2
fi

mkdir -p "$DIR/aoc/aoc$year/day$day" &&
    ([ -f "$DIR/aoc/aoc$year/day$day/day$day.py" ] ||
    (
        cp "$DIR/template.py" "$DIR/aoc/aoc$year/day$day" &&
        mv "$DIR/aoc/aoc$year/day$day/template.py" "$DIR/aoc/aoc$year/day$day/day$day.py" &&
        sed -i -e "s/url_template/https:\/\/adventofcode.com\/$year\/day\/$day/g" "$DIR/aoc/aoc$year/day$day/day$day.py" &&
        touch "$DIR/aoc/aoc$year/day$day/__init__.py"
    )) &&
    mkdir -p "$DIR/tests/$year/$day" &&
    ([ -f "$DIR/tests/$year/$day/s0.txt" ] || echo -e "${year}_$day\n<sample here>\n-\n-" > "$DIR/tests/$year/$day/s0.txt") &&
    echo "https://adventofcode.com/$year/day/$day" &&
    # reset_wsl2_interop > /dev/null &&
    # powershell.exe -c Start-Process "https://adventofcode.com/$year/day/$day" > /dev/null &&
    curl "https://adventofcode.com/$year/day/$day/input" --cookie "session=$AOC_SESSION" -o "$DIR/aoc/aoc$year/day$day/input.txt" --silent