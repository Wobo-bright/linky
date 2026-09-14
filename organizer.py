from datetime import datetime


class LinkOrganizer:
    """Manages a collection of links in memory."""

    def __init__(self):
        self._links: list[dict] = []
        self._next_id: int = 1

    def add_link(self, url: str, title: str, category: str, tags: list[str]) -> dict:
        """Create and store a new link. Raises ValueError for invalid or duplicate input."""
        if not url.strip():
            raise ValueError("URL must not be empty.")
        if not title.strip():
            raise ValueError("Title must not be empty.")
        if not category.strip():
            raise ValueError("Category must not be empty.")
        if any(link["url"] == url for link in self._links):
            raise ValueError(f"Duplicate URL: {url}")

        link = {
            "id": self._next_id,
            "url": url,
            "title": title,
            "category": category,
            "tags": [tag.strip() for tag in tags],
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self._links.append(link)
        self._next_id += 1
        return link

    def get_all_links(self) -> list[dict]:
        """Return all stored links."""
        return self._links

    def get_link(self, link_id: int) -> dict | None:
        """Return the link with the given ID, or None if not found."""
        return next((link for link in self._links if link["id"] == link_id), None)

    def delete_link(self, link_id: int) -> bool:
        """Delete the link with the given ID. Returns True if deleted, False if not found."""
        link = self.get_link(link_id)
        if link is None:
            return False
        self._links.remove(link)
        return True

    def search_links(self, query: str) -> list[dict]:
        """Case-insensitive search across url, title, category, and tags."""
        q = query.lower()
        return [
            link for link in self._links
            if q in link["url"].lower()
            or q in link["title"].lower()
            or q in link["category"].lower()
            or any(q in tag.lower() for tag in link["tags"])
        ]

    def filter_by_category(self, category: str) -> list[dict]:
        """Return all links matching the given category (case-insensitive)."""
        return [link for link in self._links if link["category"].lower() == category.lower()]

    def filter_by_tag(self, tag: str) -> list[dict]:
        """Return all links containing the given tag (case-insensitive)."""
        return [link for link in self._links if any(tag.lower() == t.lower() for t in link["tags"])]
