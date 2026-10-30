import os
import random
import subprocess
import requests

# ==================== 1. 核心配置区域 ====================
TARGET_REPO_PATH = os.path.dirname(os.path.abspath(__file__)) 
MY_AD_HEADER = """
站✅ 【—网：m j 3 8 3 8.cc—】✅网址复制浏览器打开，✅【as112113】，优网推引UWTY首家永久担保平台！✅✅✅【新客专属 存款3送】【首存返利100%】【首存最高可领88888】【二存最高再送16888】【存款赠送3%】 【每周六充值最高返利15%】【代理返佣最高55%】 ✅✅✅【as112113】✅【—网：# 【独家推荐】澳洲幸运5开奖直播网站-360访谈
> 澳洲幸运5开奖直播网站✅ 【—薇：7948079—】网 m j 3 8 3 8.cc—】✅
✅100%精准出码规律👉👉 mj3838.cc 点击开户
> 🔗 官100%精准出码规律👉👉 mj3838.cc 点击开户
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
    file_name = f"澳洲幸运5开奖直播网站_{random.randint(1000, 9999)}.md"
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
        commit_message = f"2026第一认知:澳洲幸运5开奖结果走势图 mj3838.cc~ -光华财经 ~ 《{news_title}》"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("[====== 🚀 自动化流水线执行完毕 🚀 ======]")
    except Exception as e:
        print(f"[!] Git 自动化命令执行失败: {e}")

if __name__ == "__main__":
    title, body = step_1_fetch_real_content()
    step_2_generate_template(title, body)
    step_3_git_automation_push(title)
