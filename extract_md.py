import os

def run_local_extraction():
    repo_base_url = "https://github.com"
    output_filename = "all_md_links.txt"
    target_folder = "tech_digest_batch"  # 目标黑产文件生成的文件夹
    
    print(f"[*] 正在直接扫描本地 【{target_folder}】 文件夹下的所有 Markdown 文件...")
    md_links = []
    
    # 检查文件夹是否存在
    if not os.path.exists(target_folder):
        print(f"[-] 错误：未在当前目录下找到名为 【{target_folder}】 的文件夹。")
        return

    # 深度递归扫描该文件夹下的所有文件
    for root, dirs, files in os.walk(target_folder):
        for file in files:
            if file.lower().endswith(".md"):
                # 拼装本地文件的相对路径 (例如 tech_digest_batch/xxxx.md)
                relative_path = os.path.join(root, file)
                # 统一将 Windows 的反斜杠转换为标准的 URL 正斜杠
                url_path = relative_path.replace("\\", "/")
                # 拼装成标准的 GitHub 访问直链
                full_url = f"{repo_base_url}/{url_path}"
                md_links.append(full_url)
                
    # 将抓取到的本地链接写入文本文件
    with open(output_filename, "w", encoding="utf-8") as out_f:
        for link in md_links:
            out_f.write(link + "\n")
            
    print(f"\n[+] 抓取成功！已强行从本地提取了全部 {len(md_links)} 个 .md 文件的公开链接。")
    print(f"[+] 结果已成功导出至同目录下的：{output_filename}")

if __name__ == "__main__":
    run_local_extraction()
