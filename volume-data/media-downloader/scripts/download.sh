#! /usr/bin/env bash

download_from_folder() {
  tmpdir=$(/usr/bin/mktemp -d -p /mnt/media/tmp)
  /usr/bin/putio "$PUTIO_OAUTH_TOKEN" "$1" 5 | /usr/bin/xargs /usr/bin/aria2c -d "$tmpdir" -x 5 --auto-file-renaming=false --allow-overwrite=false
  /usr/bin/putio "$PUTIO_OAUTH_TOKEN" "$1" 5
  /usr/bin/mv "$tmpdir"/* /mnt/media/downloads/
  /usr/bin/rm -r "$tmpdir"
  sleep_sec=120
  echo "Sleeping for $sleep_sec seconds"
  sleep "$sleep_sec"
}

cd /mnt/media/downloads/
while true; do
  download_from_folder "$PUTIO_SICKCHILL_FOLDER_ID"
  download_from_folder "$PUTIO_CHILL_INSTITUTE_FOLDER_ID"
done

