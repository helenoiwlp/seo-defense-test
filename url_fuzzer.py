import random
import string
from urllib.parse import urlparse

# 定义一些黑产常用的伪静态目录和垃圾关键词字典（用于安全审计特征分析）
FAKE_FOLDERS = ['news', 'category', 'gov', 'edu', 'detail', 'archive', 'bulletin']
EXTENSIONS = ['.html', '.htm', '.shtml', '.php']
SEO_KEYWORDS = ['amxn5_zhixuan', 'lucky5_plan', 'lottery_numbers', 'caipiao_zx']

def generate_seo_variants(base_url, count_per_mode=5):
    """
    【安全红队演练专用】URL 无限裂变变体生成算法
    :param base_url: 需要被污染或变造的高权重宿主 URL
    :param count_per_mode: 每种裂变模式生成的数量
    :return: 裂变后的变体 URL 列表
    """
    # 严格校验：如果 URL 本身已经带了问号，需要先剥离，确保变体拼接正确
    if '?' in base_url:
        base_url = base_url.split('?')[0]
        
    variants_pool = []
    
    # ==========================================
    # 模式一：纯随机字符串裂变（对应你看到的 ?/llwqq 模式）
    # ==========================================
    for _ in range(count_per_mode):
        # random.choices 从 26 个小写字母中随机抽取 5 个，''.join 组合成字符串
        random_str = ''.join(random.choices(string.ascii_lowercase, k=5))
        # 拼接核心：利用问号 '?' 让 Web 服务器忽略后续内容，利用 '/' 迷惑爬虫
        variant_url = f"{base_url}?/{random_str}"
        variants_pool.append(variant_url)

    # ==========================================
    # 模式二：伪静态路径裂变（欺骗爬虫深层目录权重）
    # ==========================================
    for _ in range(count_per_mode):
        folder = random.choice(FAKE_FOLDERS)      # 随机抽取假目录名
        ext = random.choice(EXTENSIONS)          # 随机抽取假静态后缀
        page_id = random.randint(10000, 99999)   # 随机生成假文章ID
        
        # 拼装出类似 ?/news/88341.html 的怪物结构
        variant_url = f"{base_url}?/{folder}/{page_id}{ext}"
        variants_pool.append(variant_url)

    # ==========================================
    # 模式三：灰产长尾关键词混合裂变（用于霸屏特定搜索词）
    # ==========================================
    for _ in range(count_per_mode):
        kw = random.choice(SEO_KEYWORDS)
        random_suffix = random.randint(1, 100)
        
        # 拼装出类似 ?amxn5_zhixuan=42 的动态传参结构
        variant_url = f"{base_url}?{kw}={random_suffix}"
        variants_pool.append(variant_url)

    return variants_pool

if __name__ == "__main__":
    # 设定演练的目标主链接
    target_link = "https://github.com"
    
    print("--- [安全演练] 启动 Python 裂变算法分析 ---")
    results = generate_seo_variants(target_link, count_per_mode=3)
    
    # 打印生成的指纹，以便我们在 WAF 中编写拦截规则
    for index, url in enumerate(results, 1):
        print(f"变体特征 {index:02d}: {url}")
