#! /usr/bin/env bash

cd /mnt/media/downloads/
while true; do
  tmpdir=$(/usr/bin/mktemp -d -p /mnt/media/tmp)
  /usr/bin/putio "$PUTIO_OAUTH_TOKEN" "$PUTIO_SICKCHILL_FOLDER_ID" 5 | /usr/bin/xargs /usr/bin/aria2c -d "$tmpdir" -x 5 --auto-file-renaming=false --allow-overwrite=false
  /usr/bin/putio "$PUTIO_OAUTH_TOKEN" "$PUTIO_SICKCHILL_FOLDER_ID" 5
  /usr/bin/mv "$tmpdir"/* /mnt/media/downloads/
  /usr/bin/rm -r "$tmpdir"

  sleep_sec=120
  echo "Sleeping for $sleep_sec seconds"
  sleep "$sleep_sec"
done
