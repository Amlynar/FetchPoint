
import appex
import console


def main():
    if not appex.is_running_extension():
        print("Run FetchPoint from the iOS Share Sheet.")
        return

    # Try to get the shared URL directly.
    url = appex.get_url()

    # Chrome may provide the URL as shared text instead.
    if not url:
        text = appex.get_text()
        if text:
            url = text.strip()

    if url:
        print("FetchPoint received:")
        print(url)

        # Temporary prototype: show the received URL.
        console.alert("FetchPoint", url, "OK")
    else:
        console.alert(
            "FetchPoint",
            "No URL was received.",
            "OK"
        )

import sys
if __name__ == "__main__":
    # main()
    print("=== FetchPoint Debug ===")
    print("Extension:", appex.is_running_extension())
    print("URL:", appex.get_url())
    print("Text:", appex.get_text())
    print("Input:", appex.get_input())
    print("Arguments:", sys.argv)
    print("=========================")
