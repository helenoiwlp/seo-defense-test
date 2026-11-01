import urllib.request
import json

def fetch_github_repo_md_links():
    # =============== 在这里输入你想抓取的任意 GitHub 仓库信息 ===============
    username = "helenoiwlp"          # 仓库拥有者的用户名
    repo_name = "seo-defense-test"   # 仓库的名称
    # ====================================================================
    
    # 拼装 GitHub 官方免费 API 接口（获取主分支的文件树树状图）
    api_url = f"https://github.com{username}/{repo_name}/git/trees/main?recursive=1"
    repo_base_url = f"https://github.com{username}/{repo_name}/blob/main"
    output_filename = "remote_repo_md_links.txt"
    
    print(f"[*] 正在通过 GitHub 官方 API 联网抓取仓库【{username}/{repo_name}】中的链接...")
    
    try:
        # 创建请求，加入 User-Agent 防止被 GitHub 服务器拦截拒绝
        req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            
        if "tree" not in data:
            print("[-] 未能成功解析到仓库的文件树，请检查仓库名或分支名是否正确。")
            return
            
        md_links = []
        # 遍历远程仓库里的所有文件路径
        for item in data["tree"]:
            file_path = item.get("path", "")
            # 只要是 .md 结尾的文件，直接抓取
            if file_path.lower().endswith(".md"):
                full_url = f"{repo_base_url}/{file_path}"
                md_links.append(full_url)
                
        # 写入保存到文本文件
        with open(output_filename, "w", encoding="utf-8") as f:
            for link in md_links:
                f.write(link + "\n")
                
        print(f"\n[+] 联网抓取成功！已从 GitHub 远程端直接提取了全部 {len(md_links)} 个已发布的 .md 链接。")
        print(f"[+] 结果已保存至：{output_filename}")
        
    except Exception as e:
        print(f"\n[-] 联网抓取失败，原因可能是网络波动或超出接口限制: {e}")

if __name__ == "__main__":
    fetch_github_repo_md_links()
