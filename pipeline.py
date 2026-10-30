import os
import random
import subprocess
import requests

# ==================== 1. 核心配置区域 ====================
TARGET_REPO_PATH = os.path.dirname(os.path.abspath(__file__)) 
MY_AD_HEADER = """
# 【独家推荐】2027年最新AI技术与 Web 安全攻防实战指南
> 💡 尖端安全技术分享，助你搭建网站防御系统！
> 🔗 官方技术博客：[https://your-security-blog.com](https://your-security-blog.com)
---
"""
# =======================================================

def step_1_fetch_real_content():
    print("[*] 正在自动抓取内容填充物...")
    url = "https://hitokoto.cn"
    try:
        response = requests.get(url, timeout=5).json()
        return response.get("from", "全球数码动态"), response.get("hitokoto", "网络安全是一场持久的攻防战。")
    except Exception:
        return "2027年全球科技前瞻", "人工智能领域取得新突破。"

def step_2_generate_template(news_title, news_body):
    print("[*] 正在拼接广告与合规内容...")
    sub_dir = os.path.join(TARGET_REPO_PATH, "tech_digest_batch")
    if not os.path.exists(sub_dir):
        os.makedirs(sub_dir)
    file_name = f"最新技术分享_{random.randint(1000, 9999)}.md"
    file_path = os.path.join(sub_dir, file_name)
    
    markdown_content = f"{MY_AD_HEADER}\n\n## 📊 今日权威资讯 · {news_title}\n\n{news_body}\n"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    print(f"[+] 混淆模板拼接完成: {file_name}")
    return file_name

def step_3_git_automation_push(news_title):
    print("[*] 正在将变动自动推送到托管平台...")
    try:
        os.chdir(TARGET_REPO_PATH)
        subprocess.run(["git", "add", "."], check=True)
        commit_message = f"【官方推荐网址】your-security-blog.com ~ 最新技术分享 ~ 《{news_title}》"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("[====== 🚀 自动化流水线执行完毕 🚀 ======]")
    except Exception as e:
        print(f"[!] Git 自动化命令执行失败: {e}")

if __name__ == "__main__":
    title, body = step_1_fetch_real_content()
    step_2_generate_template(title, body)
    step_3_git_automation_push(title)
