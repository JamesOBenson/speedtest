#!/bin/sh

# pip install speedtest-cli
# Create a free ubidots.com account:
#  - If edu, they have free edu accounts
# Be sure to update DEVICE-NAME & TOKEN
# https://app.ubidots.com/ubi/getchart/page/DbZuR6ultCCGuNaDN9JCsiw753Y

OUTPUT="$(speedtest-cli --simple)"
PING="$(echo "${OUTPUT}" | grep Ping | awk '{print $2}')"
DOWNLOAD="$(echo "${OUTPUT}" | grep Download| awk '{print $2}')"
UPLOAD="$(echo "${OUTPUT}" | grep Upload | awk '{print $2}')"

TOKEN="PLACE TOKEN HERE"

test="${DEVICE-NAME|POST|$TOKEN|mydevice=>Download:$DOWNLOAD,Upload:$UPLOAD,Ping:$PING|end}"

nc -u translate.ubidots.com 9012 -w 2 << EOF
$test
EOF
