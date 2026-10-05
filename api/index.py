import os
import sys

# Add Backend directory to module search path
backend_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Backend')
if backend_dir not in sys.path:
    sys.path.append(backend_dir)

from app import app
