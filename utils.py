import concurrent.futures  # <-- Import concurrent.futures
import json
import logging
import os
import threading
import time
import traceback
import uuid
from typing import Any, Optional

import requests

DEFAULT_TIMEOUT = 10  # Default compile and run timeout
MAX_RETRIES = 3
INITIAL_RETRY_DELAY = 1
API_TIMEOUT = 10

logger = logging.getLogger(__name__)

# Define supported languages list (optional, for documentation or validation)
SUPPORTED_LANGUAGES = [
    "python",
    "cpp",
    "nodejs",
    "go",
    "go_test",
    "java",
    "php",
    "csharp",
    "bash",
    "typescript",
    "sql",
    "rust",
    "cuda",
    "lua",
    "R",
    "perl",
    "D_ut",
    "ruby",
    "scala",
    "julia",
    "pytest",
    "junit",
    "kotlin_script",
    "jest",
    "verilog",
    "python_gpu",
    "lean",
    "swift",
    "racket",
]
