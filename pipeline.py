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
> 🔗 ✅【as112113】，优网推引UWTY首家永久担保平台！✅✅✅【新客专属 存款3送】【首存返利100%】【首存最高可领88888】【二存最高再送16888】【存款赠送3%】 【每周六充值最高返利15%】【代理返佣最高55%】 ✅✅✅【as112113】✅【—网：m j 3 8 3 8.cc—】✅
---
"""
# =======================================================

def step_1_fetch_real_content():
    """自动化爬取实时合规内容（确保每次循环抓取的内容都不同）"""
    url = "https://hitokoto.cn"
    try:
        response = requests.get(url, timeout=5).json()
        return response.get("from", "全球数码动态"), response.get("hitokoto", "网络安全是一场持久的攻防战。")
    except Exception:
        return "2027年全球科技前瞻", f"人工智能领域取得第 {random.randint(100,999)} 号新突破。"

def step_2_generate_template(news_title, news_body):
    """动态拼接并生成全新的 Markdown 文件"""
    sub_dir = os.path.join(TARGET_REPO_PATH, "tech_digest_batch")
    if not os.path.exists(sub_dir):
        os.makedirs(sub_dir)
        
    file_name = f"最新技术分享_{random.randint(10000, 99999)}.md"
    file_path = os.path.join(sub_dir, file_name)
    
    markdown_content = f"{MY_AD_HEADER}\n\n## 📊 今日权威资讯 · {news_title}\n\n{news_body}\n"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    print(f"[+] 成功生成新文件: {file_name}")

def step_3_git_automation_push(news_title):
    """自动化 Git 提交流水线与链接提取"""
    print("[*] 正在向 GitHub 服务器持续同步变动...")
    try:
        os.chdir(TARGET_REPO_PATH)
        subprocess.run(["git", "add", "."], check=True)
        commit_message = f"【官方推荐】最新最稳澳澳洲5幸运彩开奖结果  mj3838.cc ~ 动态更新 ~ 《{news_title}》"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # 🎯 核心自动提取：通过 Git 自动获取本次推送产生的 40 位唯一特征哈希值
        sha_result = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True)
        current_sha = sha_result.stdout.strip()
        
        # 推送到远程 GitHub
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("[====== 🚀 单次自动化同步已成功完成 🚀 ======]")
        
        # 🎯 核心打印输出：动态拼接出单个文件的专属公开永久 URL 并直接在终端打印出来
        file_url = f"https://github.com{current_sha}"
        print(f"\n[🔗 提取成功！本次生成的独立 SEO 链接为 ]:\n{file_url}\n")
        
    except Exception as e:
        print(f"[!] 本次推送失败（可能没有文件实质更改或触发风控）: {e}\n")

if __name__ == "__main__":
    print("[=== 开启安全演练：黑帽 SEO 持续自动引流流水线模拟 ===]")
    print("[提示] 想要停止时，请在黑色终端里按下键盘上的 Ctrl + C 强行终止。\n")
    
    count = 1
    while True:
        print(f"================ 正在执行第 {count} 次自动推送 ================")
        
        # 执行流水线
        title, body = step_1_fetch_real_content()
        step_2_generate_template(title, body)
        step_3_git_automation_push(title)
        
        # 设置自动化推送的间隔时间（每 30 秒全自动循环执行一次）
        sleep_time = 30 
        print(f"[*] 等待 {sleep_time} 秒后将自动执行下一次抓取与推送...")
        time.sleep(sleep_time)
        
        count += 1
