import importlib.metadata
from pathlib import Path
from typing import Dict, Final, Optional

_metadata = importlib.metadata.metadata("nuklear")

__metadata_version__: Final[Optional[str]] = _metadata.get("metadata-version", None)

__title__: Final[Optional[str]] = _metadata.get("name", None)
__version__: Final[Optional[str]] = _metadata.get("version", None)
__summary__: Final[Optional[str]] = _metadata.get("summary", None)
__author__: Final[Optional[str]] = _metadata.get("author", None)
__maintainer__: Final[Optional[str]] = _metadata.get("maintainer", __author__)
__license__: Final[Optional[str]] = _metadata.get("license", None)
__url__: Final[Optional[str]] = _metadata.get("home-page", None)
__download_url__: Final[Optional[str]] = _metadata.get("download-url", None)
__project_urls__: Final[Dict[str, str]] = {
    values[0].strip(): values[1].strip()
    for url_str in _metadata.get_all("project-url", tuple())
    if (values := url_str.split(","))
}

__copyright__: Final[str] = f"Copyright 2022 {__author__}"

__bin_dir__: Final[Path] = (Path(__file__).parent / "bin").resolve()
