name: Decode spamv3.py

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  decode-job:
    runs-on: ubuntu-latest

    steps:
      # Step 1: Checkout code
      - name: Checkout code
        uses: actions/checkout@v2

      # Step 2: Set up Python
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'

      # Step 3: Install dependencies (if any)
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          # Nếu có thư viện phụ thuộc, có thể cài đặt tại đây

      # Step 4: Run the Python script to decode spamv3.py
      - name: Decode spamv3.py
        run: |
          python unspamv3.py
