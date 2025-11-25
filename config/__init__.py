"""Configuration package for the Message Board app.

This package exposes configuration modules. Typical usage in `app.py`:

    from config import default as config
    app.config.from_object(config)

You can import a different module for development/production, or set
`FLASK_APP_CONFIG` / `APP_CONFIG` environment variable and load accordingly.
"""

from . import default  # keep a simple default import available
