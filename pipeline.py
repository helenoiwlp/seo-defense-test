import os
import random
import subprocess
import time
import requests

# ==================== 1. 核心配置区域 ====================
TARGET_REPO_PATH = os.path.dirname(os.path.abspath(__file__)) 
MY_AD_HEADER = """
# 澳洲幸运5开奖直播网站✅—✅【—网：m j 3 8 3 8.cc—】
> 💡 ✅澳洲幸运5开奖直播网站✅ 【—薇：7948079—】✅澳洲幸运5开奖直播网站✅ 【—网：m j 3 8 3 8.cc—】✅网址复制浏览器打开，
> 🔗 ✅【as112113】，优网推引UWTY首家永久担保平台！✅✅✅【新客专属 存款3送】【首存返利100%】【首存最高可领88888】【二存最高再送16888】【存款赠送3%】 【每周周六充值最高返利15%】【代理返佣最高55%】 ✅✅✅【as112113】✅【—网：m j 3 8 3 8.cc—】✅
---
"""

# 🎯【配置库】：用于批量组合的前缀、尾缀词库以及连接符
SEO_PREFIXES = ["一手指南", "一线专栏", "一线专访", "一线动向", "一线动态", "一线周刊", "一线呼声", "一线回应", "一线专题"]
SEO_SUFFIXES = ["银瑞财经", "鸿图财经", "行业观察", "港口财经", "鼎信财经", "东京财经", "葡萄财经", "投资参考"]
SEO_CONNECTORS = ["—", "—", "··", "!", "-", "："]
# =======================================================

def step_1_fetch_real_content():
    """自动化爬取实时内容"""
    url = "https://hitokoto.cn"
    try:
        response = requests.get(url, timeout=5).json()
        return response.get("from", "全球数码动态"), response.get("hitokoto", "网络安全是一场持久的攻防战。")
    except Exception:
        return "2027年全球科技前瞻", f"人工智能领域取得第 {random.randint(100,999)} 号新突破。"


def step_2_generate_template(news_title, news_body):
    """动态拼接并生成全新的 Markdown 文件到 Git 仓库中"""
    sub_dir = os.path.join(TARGET_REPO_PATH, "tech_digest_batch")
    if not os.path.exists(sub_dir):
        os.makedirs(sub_dir)
        
    # 严格清洗文件名，防止包含系统保留或不允许的特殊字符导致报错
    safe_file_title = news_title
    for char in ["<", ">", ":", '"', "/", "\\", "|", "?", "*", "!", "：", "·"]:
        safe_file_title = safe_file_title.replace(char, "")

    file_name = f"{safe_file_title}_{random.randint(10000, 99999)}.md"
    file_path = os.path.join(sub_dir, file_name) 

    # 写入生成的文章，采用 utf-8-sig 确保本地查看不乱码
    markdown_content = f"{MY_AD_HEADER}\n\n## 📊 今日更新：{news_title}\n\n{news_body}"
    with open(file_path, "w", encoding="utf-8-sig") as f:
        f.write(markdown_content)
    print(f"[+] 成功生成新文件：{file_name}")


def step_3_git_automation_push(news_title):
    """自动化 Git 提交流水线与链接提取并自动导出"""
    print("[*] 正在向 GitHub 服务器持续同步变动...")
    try:
        os.chdir(TARGET_REPO_PATH)
        subprocess.run(["git", "add", "."], check=True)
        
        # 缩短后的 Commit 提交信息
        commit_message = f" 《{news_title}》"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # 获取当前最新的有效哈希
        sha_result = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True)
        current_sha = sha_result.stdout.strip()
        
        # 推送到远程 GitHub
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("[====== 🚀 单次自动化同步已成功完成 🚀 ======]")
        
        # 动态获取当前 Git 仓库的真实远程 URL
        remote_url_result = subprocess.run(["git", "config", "--get", "remote.origin.url"], capture_output=True, text=True, check=True)
        remote_url = remote_url_result.stdout.strip()
        
        if "github.com" in remote_url:
            repo_path = remote_url.split("github.com")[-1].replace(":", "/").replace(".git", "").strip("/")
        else:
            repo_path = "helenoiwlp/seo-defense-test"
        
        # 动态拼接出公开 Commit 永久链接
        file_url = f"https://github.com{repo_path}/commit/{current_sha}"
        print(f"[ 🔗 提取成功！本次生成的独立 SEO 链接为 ]:\n{file_url}\n")
        
        # 🎯【终极修复点】：改用 utf-8-sig 编码追加写入，强行压制 Windows 记事本的乱码识别
        log_file_path = os.path.join(TARGET_REPO_PATH, "all_seo_urls.txt")
        with open(log_file_path, "a", encoding="utf-8-sig") as f:  
            f.write(file_url + "\n")
            f.flush()  
        print(f"[💾 导出成功] 链接已追加写入本地文件：{log_file_path}")
            
    except Exception as e:
        print(f"[!] 本次推送失败（可能没有文件实质更改或触发风控）: {e}\n")


if __name__ == "__main__":
    print("[=== 开启安全演练：自动流水线模拟 ===]")
    print("[提示] 想要停止时，请在黑色终端里按下键盘上的 Ctrl + C 强行终止。\n")
    
    count = 1
    filename = os.path.join(TARGET_REPO_PATH, "词.txt")
    
    while True:
        print(f"================ 正在执行第 {count} 次自动推送 ================")
        
        # 1. 抓取默认数据
        default_title, body = step_1_fetch_real_content()
        final_title = ""

        # ========================================================
        # 2. 核心控制：从 词.txt 提取核心词并随机拼装组合前尾缀
        # ========================================================
        # 💡 采用 errors='ignore' 容错，防止“词.txt”本身带有奇怪的编码导致程序崩溃
        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            try:
                with open(filename, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()
            except Exception:
                with open(filename, "r", encoding="gbk", errors="ignore") as f:
                    lines = f.readlines()

            if lines:
                core_keyword = lines[0].strip()  # 精准取出第一个词作为核心词
                
                # 写回剩余行
                with open(filename, "w", encoding="utf-8") as f:
                    f.writelines(lines[1:])
                
                # 拼装复合标题
                p = random.choice(SEO_PREFIXES)
                s = random.choice(SEO_SUFFIXES)
                c1 = random.choice(SEO_CONNECTORS)
                c2 = random.choice(SEO_CONNECTORS)
                
                final_title = f"2026{c1}{p}{c2}{core_keyword}-{s}"
                print(f"[➔] 成功从 词.txt 提取核心词并装配复合标题: {final_title}")
        
        # 如果没有读到有效行，则降级使用默认标题
        if not final_title:
            final_title = default_title
            print("[⚠️] 词.txt 为空或不存在，将使用网络抓取的默认内容。")
        # ========================================================

        # 3. 统一执行生成和推送
        step_2_generate_template(final_title, body)
        step_3_git_automation_push(final_title)
        
        count += 1
        print("[*] 等待 30 秒后将自动执行下一次抓取与推送...\n")
        time.sleep(30)
