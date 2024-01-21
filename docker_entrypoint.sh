#!/bin/bash

# Load .env variables
source .env

# Login to Weights & Biases
wandb login $WANDB_TOKEN

# Execute the passed command
exec "$@"

