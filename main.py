from metadata import extract_metadata
from organizer import LinkOrganizer
from extractor import extract_content


organizer = LinkOrganizer()

def main():
    while True: 
        url = input("Enter a URL or 'q' to quit: ").strip()

        if url.lower() in ("q","quit"):
            break

        try:
            meta = extract_metadata(url)
            page = extract_content(url)
        except ValueError as e:
            print(f"Error: {e}")
            return

        print(f"\n-----------------------------")
        print("Metadata")
        print(f"URL:          {meta['url']}")
        print(f"Domain:       {meta['domain']}")
        print(f"Platform:     {meta['platform']}")
        print(f"Content Type: {meta['content_type']}")
        print(f"-----------------------------\n")

        print(f"\n-----------------------------")
        print("Page information")
        print(f"page title:          {page['title']}")
        print(f"\ncontent preview:       \n{page['content']}")
        print(f"-----------------------------\n")



if __name__ == "__main__":
    main()
