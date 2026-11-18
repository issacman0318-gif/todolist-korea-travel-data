"""讀取本機交通資料，輸出指定條件的旅程比較。"""
import argparse
import csv
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description='首爾住宿站點與仁川 AREX 比較')
    parser.add_argument("condition", nargs="?", help='輸入直達車或站站停')
    args = parser.parse_args()
    with Path(__file__).with_name("travel-data.csv").open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    matches = [row for row in rows if not args.condition or args.condition in row["方式"].split("、")]
    if not matches:
        parser.error("沒有符合的資料。省略條件可列出所有項目。")
    for index, row in enumerate(matches, 1):
        print(f"{row['分類']}（{row['站點']}）｜{row['方式']}")
        print(f"    {row['出發前核對']}")
        print(f"    來源 {row['來源']}")

if __name__ == "__main__":
    main()
