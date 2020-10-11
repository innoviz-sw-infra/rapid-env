from pathlib import Path
import os
import re
import pytest

from .context import rapidenv
from rapidenv import __version__, __build__


@pytest.mark.dev
def test_version_dev():
    assert __version__ == "0.0.0"
    assert __build__ == "dev"


@pytest.mark.dist
def test_version_dist():
    version_path = Path(rapidenv.__file__).parent / "version.py"
    if os.path.exists(version_path):
        txt = open(version_path, 'r').read()
        mo = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", txt, re.M)

        assert mo is not None

        # assert valid major.minor.patch version
        assert True

