#!/bin/bash

set -e

# Define new branch name
NEW_BRANCH="data-clean"
EXCLUDE_DIR="datasets/processed"

# Fetch and update main branch
git checkout main
git pull

# Create new branch
git checkout -b "$NEW_BRANCH"

# Remove all files and folders except .git and .gitignore (.env, etc. can be added below if needed)
find . -mindepth 1 -maxdepth 1 ! -name ".git" ! -name ".gitignore" -exec rm -rf {} +

# Copy everything from previous working dir except datasets/processed
rsync -av --exclude="$EXCLUDE_DIR" ../sas-curiosity-cup-2026/ .  # Update source path as needed!

# Add everything except excluded folder
git add .
git commit -m "Fresh start: all current files except datasets/processed/"

echo "Done! Now push with: git push -u origin $NEW_BRANCH"