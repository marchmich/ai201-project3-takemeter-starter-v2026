"""
No-login, no-API-key version. Uses only the Python standard library (nothing to install).

Pulls posts from a subreddit's public .json feed into a CSV: text,label,note

Usage examples:
  python reddit_json_to_csv.py -s YourSubreddit --limit 200
  python reddit_json_to_csv.py -s YourSubreddit --sort top --time month --limit 300 --label my_label
"""
import argparse
import csv
import json
import time
import urllib.error
import urllib.request


def fetch(url):
    req = urllib.request.Request(
        url, headers={"User-Agent": "post-collector/0.1 (personal research script)"}
    )
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 429:  # rate limited: wait and retry
                wait = 10 * (attempt + 1)
                print(f"Rate limited, waiting {wait}s...")
                time.sleep(wait)
                continue
            raise
    raise RuntimeError("Still rate limited after retries; try again later.")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("-s", "--subreddit", required=True)
    p.add_argument("--sort", default="new", choices=["new", "hot", "top", "rising"])
    p.add_argument("--time", default="all", choices=["hour", "day", "week", "month", "year", "all"],
                   help="only used with --sort top")
    p.add_argument("--limit", type=int, default=100, help="max posts to write")
    p.add_argument("--label", default="your_label_here")
    p.add_argument("--note", default="cold")
    p.add_argument("--include-title", action="store_true")
    p.add_argument("-o", "--out", default="posts.csv")
    args = p.parse_args()

    seen, rows, after = set(), 0, None
    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["text", "label", "note"])
        while rows < args.limit:
            url = f"https://www.reddit.com/r/{args.subreddit}/{args.sort}.json?limit=100&raw_json=1"
            if args.sort == "top":
                url += f"&t={args.time}"
            if after:
                url += f"&after={after}"
            data = fetch(url)["data"]
            children = data["children"]
            if not children:
                break
            for c in children:
                post = c["data"]
                body = (post.get("selftext") or "").strip()
                if not body or body in ("[removed]", "[deleted]"):
                    continue
                text = f"{post['title']}\n\n{body}" if args.include_title else body
                if text in seen:
                    continue
                seen.add(text)
                w.writerow([text, args.label, args.note])  # full text, not trimmed
                rows += 1
                if rows >= args.limit:
                    break
            after = data.get("after")
            if not after:
                break
            time.sleep(2)  # be polite

    print(f"Wrote {rows} posts to {args.out}")


if __name__ == "__main__":
    main()