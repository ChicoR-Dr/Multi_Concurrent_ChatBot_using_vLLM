#!/bin/bash

python3 -m vllm.entrypoints.openai.api_server \
  --model /app/models/TinyLlama-1.1B-Chat-v1.0 \
  --dtype float16 \
  --gpu-memory-utilization 0.2 \
  --disable-log-stats \
  --swap-space 4

