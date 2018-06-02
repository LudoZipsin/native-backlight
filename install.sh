#! /usr/bin/env bash

set -e

TARGET="/opt/native-backlight"

mkdir "$TARGET"
cp -r . "$TARGET"

cp native-backlight.service /etc/systemd/system/

