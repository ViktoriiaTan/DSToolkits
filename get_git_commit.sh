#!/bin/bash

# Check for uncommitted changes
if git diff-index --quiet HEAD --; then
    # No changes
    echo "No uncommitted changes found."
else
    # Uncommitted changes exist
    echo "Error: Please commit all changes before running this script."
    exit 1
fi

# Get the current Git commit hash
COMMIT_HASH=$(git rev-parse HEAD)

# Export the commit hash as an environment variable
export GIT_COMMIT_HASH=$COMMIT_HASH

