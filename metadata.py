from urllib.parse import urlparse

_PLATFORMS: dict[str, str] = {
    "youtube.com": "YouTube",
    "youtu.be": "YouTube",
    "github.com": "GitHub",
    "reddit.com": "Reddit",
    "x.com": "X",
    "twitter.com": "X",
    "linkedin.com": "LinkedIn",
    "medium.com": "Medium",
}

_CONTENT_TYPES: dict[str, str] = {
    "YouTube": "video",
    "GitHub": "repository",
    "Reddit": "post",
    "Medium": "article",
    "LinkedIn": "post",
    "X": "post",
}


def _normalize_domain(netloc: str) -> str:
    return netloc.removeprefix("www.")


def _identify_platform(domain: str) -> str:
    return _PLATFORMS.get(domain, "Unknown")


def _identify_content_type(platform: str) -> str:
    return _CONTENT_TYPES.get(platform, "webpage")


def extract_metadata(url: str) -> dict:
    """Parse a URL and return basic metadata: domain, platform, and content type.

    Raises ValueError for empty or unparseable URLs.
    """
    if not url.strip():
        raise ValueError("URL must not be empty.")

    parsed = urlparse(url)
    if not parsed.scheme or not parsed.netloc:
        raise ValueError(f"Invalid URL: {url!r}")

    domain = _normalize_domain(parsed.netloc)
    platform = _identify_platform(domain)
    content_type = _identify_content_type(platform)

    return {
        "url": url,
        "domain": domain,
        "platform": platform,
        "content_type": content_type,
    }
