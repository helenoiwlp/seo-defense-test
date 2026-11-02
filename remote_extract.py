import os
import re
import sys
from urllib.parse import urlparse, urlunparse
import urllib.request
from urllib.error import URLError

# ========================================================
# 1. 自动挂载本地代理配置（核心：解决 Errno 11001 报错）
# ========================================================
# 💡 请根据你电脑上的代理软件（如 Clash、V2ray 等）的实际本地端口进行修改。
# 常见默认端口：Clash 通常为 7890，v2rayN 通常为 10809，科学上网助手通常为 1080
PROXY_PORT = "7890"  

os.environ['HTTP_PROXY'] = f'http://127.0.0.1:{PROXY_PORT}'
os.environ['HTTPS_PROXY'] = f'http://127.0.0.1:{PROXY_PORT}'

# ========================================================
# 2. 变体自动净化模块（核心：防范黑产裂变尾巴）
# ========================================================
def clean_and_purify_url(url):
    """
    逆向识别黑产变体特征。如果命中，自动裁剪掉问号后面的垃圾参数（如 ?/llwqq），只保留主干
    """
    # 编译黑产裂变特征正则：匹配 ?/ 或者 ?.*.html 或者带有灰色长尾关键词传参
    blackhat_pattern = re.compile(r'(\?\/)|(\?.*\.s?html?)|(\?[a-zA-Z0-9_\-]+=\d+)')
    
    if blackhat_pattern.search(url):
        parsed = urlparse(url)
        # 将 query 字段清空，重新组合成不带变体尾巴的干净主干 URL
        clean_url = urlunparse((parsed.scheme, parsed.netloc, parsed.path, parsed.params, '', parsed.fragment))
        return clean_url, True
    return url, False

# ========================================================
# 3. 远程抓取与流水线调度主函数
# ========================================================
def main():
    # 示例目标仓库（对应你终端里显示的测试仓库）
    target_repo = "helenoiwlp/seo-defense-test"
    # 构建请求的远程数据接口（此处以 RAW 源码内容为例，黑产通常抓取 .md 或 .txt 中的链接）
    url = f"https://githubusercontent.com{target_repo}/main/remote_repo_md_links.txt"
    
    print(f"[*] 正在通过全局安全代理 127.0.0.1:{PROXY_PORT} 联网抓取仓库中的链接...")
    
    try:
        # 显式加入 timeout=10 超时控制，防止脚本无限死等断流
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read().decode('utf-8')
            print("[+] 远程数据下载成功！开始解析并进行防御性净化...")
            
            # 假设远程文件每行是一个链接，将其提取
            raw_links = content.splitlines()
            cleaned_pool = set()
            garbage_count = 0
            
            for link in raw_links:
                link = link.strip()
                if not link:
                    continue
                # 调用净化算法，边提取边清洗
                purified_url, is_garbage = clean_and_purify_url(link)
                cleaned_pool.add(purified_url)
                if is_garbage:
                    garbage_count += 1
            
            # 将清洗干净、去重后的高质量主干数据，写入到你的数据文件中
            output_file = "all_seo_urls.txt"
            with open(output_file, "w", encoding="utf-8") as f:
                for clean_url in sorted(cleaned_pool):
                    f.write(clean_url + "\n")
                    
            print(f"--- [流水线处理完成] ---")
            print(f"[安全拦截] 累计识别并粉碎黑产裂变尾巴: {garbage_count} 条")
            print(f"[数据入库] 干净的白名单数据已安全导入 {output_file}，共计 {len(cleaned_pool)} 条")
            
    except URLError as e:
        print(f"\n[-] 联网抓取失败，原因为: {e}")
        print("[-] 【排查提示】:")
        print(f"    1. 请确保你已经打开了代理软件（梯子）。")
        print(f"    2. 请检查代理软件当前的本地端口是否确实为 {PROXY_PORT}。若不是，请修改脚本第 14 行的 PROXY_PORT。")
        sys.exit(1)

if __name__ == "__main__":
    main()
