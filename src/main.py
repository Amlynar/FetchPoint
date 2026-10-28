
import sys

print("FetchPoint started")
print("Arguments received:", repr(sys.argv))

if len(sys.argv) > 1:
    shared_url = sys.argv[1]
    print("Shared URL:", shared_url)
else:
    print("No URL argument received.")
