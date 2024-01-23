#!/bin/bash

# Login to Weights & Biases
wandb login $WANDB_TOKEN

# Get commit hash
/get_git_commit.sh


# Execute the passed command
exec "$@"

