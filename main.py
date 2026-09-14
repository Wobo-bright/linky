from metadata import extract_metadata


def main():
    url = input("Enter a URL: ").strip()

    try:
        meta = extract_metadata(url)
    except ValueError as e:
        print(f"Error: {e}")
        return

    print(f"\n-----------------------------")
    print(f"URL:          {meta['url']}")
    print(f"Domain:       {meta['domain']}")
    print(f"Platform:     {meta['platform']}")
    print(f"Content Type: {meta['content_type']}")
    print(f"-----------------------------\n")


if __name__ == "__main__":
    main()
