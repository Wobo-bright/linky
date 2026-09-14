import unittest
from metadata import extract_metadata


class TestExtractMetadata(unittest.TestCase):

    def test_youtube_full_url(self):
        result = extract_metadata("https://www.youtube.com/watch?v=abc")
        self.assertEqual(result["platform"], "YouTube")
        self.assertEqual(result["content_type"], "video")

    def test_youtube_short_url(self):
        result = extract_metadata("https://youtu.be/abc")
        self.assertEqual(result["platform"], "YouTube")
        self.assertEqual(result["content_type"], "video")

    def test_github_url(self):
        result = extract_metadata("https://github.com/user/project")
        self.assertEqual(result["platform"], "GitHub")
        self.assertEqual(result["content_type"], "repository")

    def test_reddit_url(self):
        result = extract_metadata("https://www.reddit.com/r/python/")
        self.assertEqual(result["platform"], "Reddit")
        self.assertEqual(result["content_type"], "post")

    def test_unknown_website(self):
        result = extract_metadata("https://example.com/article")
        self.assertEqual(result["platform"], "Unknown")
        self.assertEqual(result["content_type"], "webpage")

    def test_empty_url_raises(self):
        with self.assertRaises(ValueError):
            extract_metadata("")

    def test_malformed_url_raises(self):
        with self.assertRaises(ValueError):
            extract_metadata("not-a-url")

    def test_www_removed_from_domain(self):
        result = extract_metadata("https://www.youtube.com/watch?v=abc")
        self.assertEqual(result["domain"], "youtube.com")


if __name__ == "__main__":
    unittest.main()
