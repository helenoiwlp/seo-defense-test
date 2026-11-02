import random
import string
import os

def read_file_safely(file_path):
    """
    智能检测并读取不同编码的文本文件，防止 UnicodeDecodeError
    """
    # 优先检测二进制前缀 (BOM)
    with open(file_path, 'rb') as f:
        raw = f.read(4)
        if raw.startswith(b'\xff\xfe') or raw.startswith(b'\xfe\xff'):
            return open(file_path, 'r', encoding='utf-16').read().splitlines()
        if raw.startswith(b'\xef\xbb\xbf'):
            return open(file_path, 'r', encoding='utf-8-sig').read().splitlines()

    # 如果没有标准BOM头，尝试常见编码解析
    encodings = ['utf-8', 'gbk', 'gb18030']
    for enc in encodings:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                return f.read().splitlines()
        except (UnicodeDecodeError, LookupError):
            continue
            
    # 最后的保底方案：强行读取并忽略无法解析的畸形字符
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read().splitlines()


def mutate_existing_urls(input_file, output_file, mutations_per_url=1, string_length=5):
    """
    读取现有的 URL 列表文件，为每个 URL 批量生成 ?/lllll 形式的变形
    """
    if not os.path.exists(input_file):
        print(f"❌ 错误：找不到输入文件 '{input_file}'，请检查文件名是否正确。")
        return

    print(f"📖 正在从 '{input_file}' 读取原始 URL...")
    raw_lines = read_file_safely(input_file)
    
    # 过滤掉空行和纯空格行
    urls = [line.strip() for line in raw_lines if line.strip()]

    if not urls:
        print("⚠️ 警告：读取到的 URL 列表为空，请检查原始文件内容。")
        return

    mutated_urls = []
    print(f"⚡ 开始为 {len(urls)} 个 URL 生成变形...")
    
    for url in urls:
        base_url = url.rstrip('/')
        current_url_set = set()
        
        while len(current_url_set) < mutations_per_url:
            # 生成随机后缀
            random_str = ''.join(random.choices(string.ascii_lowercase, k=string_length))
            mutated_format = f"{base_url}/?/{random_str}"
            current_url_set.add(mutated_format)
            
        mutated_urls.extend(list(current_url_set))

    print(f"💾 正在将 {len(mutated_urls)} 条结果写入 '{output_file}'...")
    # 输出时统一规范为标准的 UTF-8 编码，方便你的 pipeline.py 或 url_fuzzer.py 后续读取
    with open(output_file, 'w', encoding='utf-8') as f:
        for m_url in mutated_urls:
            f.write(m_url + '\n')

    print(f"✅ 处理完成！变形字典已成功保存至: {os.path.abspath(output_file)}")


# --- 执行脚本 ---
if __name__ == "__main__":
    INPUT_TXT = "all_seo_urls.txt"       # 你的原始 SEO URL 文件
    OUTPUT_TXT = "mutated_seo_urls.txt"   # 变形后的输出文件
    MUTATIONS_COUNT = 3                   # 每个 URL 生成的随机变形数量
    
    mutate_existing_urls(
        input_file=INPUT_TXT, 
        output_file=OUTPUT_TXT, 
        mutations_per_url=MUTATIONS_COUNT, 
        string_length=5
    )
