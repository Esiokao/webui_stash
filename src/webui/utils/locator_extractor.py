import re
import os
import argparse

def extract_arguments(input_file, output_file):
    try:
        # 讀取輸入檔案
        with open(input_file, "r", encoding="utf-8") as f:
            code = f.read()

        # 正則表達式匹配 `find_element(...)` 並保留括號
        pattern = r'(\(By.*"\))'  # 只捕獲小括號及內部內容
        matches = re.findall(pattern, code, re.M)

        # 確保目錄存在
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # 存入 txt 檔案
        with open(output_file, "w", encoding="utf-8") as f:
            for match in matches:
                f.write(match.strip() + "\n")  # 只寫入括號內的內容

        print(f"已成功提取 {len(matches)} 個 `find_element()` 內的參數，並儲存到 {output_file}")

    except FileNotFoundError:
        print(f"錯誤：找不到檔案 {input_file}")
    except Exception as e:
        print(f"發生錯誤：{e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="從 Python 代碼中提取 find_element() 內的內容")
    parser.add_argument("-f", "--file", required=True, help="輸入的 Python 檔案")
    parser.add_argument("-o", "--output", default="extract_locators/selectors.txt", help="輸出檔案 (預設為 extract_locators/selectors.txt)")
    
    args = parser.parse_args()
    extract_arguments(args.file, args.output)
