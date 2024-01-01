#!/bin/bash
# wait-for-it.sh

set -e

HOST_PORT="$1"
shift
COMMAND="$@"

# Extract HOST and PORT from HOST_PORT
HOST="$(echo $HOST_PORT | cut -d : -f 1)"
PORT="$(echo $HOST_PORT | cut -d : -f 2)"

# Wait for the specified host and port to become available
until nc -z "$HOST" "$PORT"; do
  >&2 echo "Waiting for $HOST:$PORT - service is not up yet"
  sleep 1
done

>&2 echo "$HOST:$PORT is up - executing command"
exec $COMMAND

