#!/bin/bash

uvicorn app.server:app --host 0.0.0.0 --port 4080
