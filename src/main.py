
import sys
import requests

from framework.network.home_lab_session import PYIHomeLabSession

# Replace this with your DownloadHub server's reachable address.
API_URL = "https://downloadhub.home.arpa/api/v1/add-download"


def submit_download(url):
    try:
        response = PYIHomeLabSession().post(
            API_URL,
            json={"url": url},
            timeout=15,
        )

        response.raise_for_status()
        result = response.json()

        task_id = result.get("task_id")
        print("Download submitted successfully!")
        print("Task ID:", task_id)
        return result

    except RuntimeError as e:
        # Raised when the home-lab CA certificate hasn't been downloaded yet.
        print(e)
    except requests.RequestException as e:
        print("Request failed:", e)
    except ValueError:
        print("The server returned an invalid JSON response.")

    return None


def main():
    # URL passed as an argument by Shortcuts/Pythonista.
    if len(sys.argv) > 1:
        shared_url = sys.argv[1].strip()
    else:
        print("No URL argument received.")
        return

    if not shared_url.startswith(("http://", "https://")):
        print("Invalid URL:", shared_url)
        return

    print("Submitting:", shared_url)
    submit_download(shared_url)

def test():
    shared_url = ""
    submit_download(shared_url)

if __name__ == "__main__":
    #main()
    test()
