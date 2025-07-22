import json
import os
from sentence_transformers import SentenceTransformer, util
import torch

# --- 1. 模拟数据库中的标准指标 ---
database_indicators = []
with open('data/indicator_template.json', 'r', encoding='utf-8') as f:
    database_indicators = json.load(f)

# --- 2. 加载预训练的语义模型 ---
# 'paraphrase-multilingual-MiniLM-L12-v2' 是一个轻量且高效的多语言模型，非常适合中文。
# 模型在首次运行时会自动下载，后续会直接从缓存加载。
print("正在加载语义模型...")
model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
print("模型加载完毕。")

def find_best_semantic_match(query: str, indicators: list, model: SentenceTransformer, score_threshold: float = 0.6):
    """
    在指标库中为查询找到最佳的语义匹配。

    Args:
        query (str): 用户的输入查询。
        indicators (list): 包含指标对象的列表 (如 database_indicators)。
        model (SentenceTransformer): 已加载的 sentence-transformer 模型。
        score_threshold (float): 用于判断是否匹配成功的相似度阈值。

    Returns:
        dict: 包含最佳匹配信息的字典，如果没有找到则返回 None。
    """

    # --- 步骤 1: 数据展平和建立映射 ---
    # all_terms: 包含所有 name 和 alias 的扁平化列表
    # term_to_indicator_map: 映射列表，其索引与 all_terms 对应，值为原始的指标对象
    all_terms = []
    term_to_indicator_map = []

    for indicator in indicators:
        # 添加 name
        all_terms.append(indicator['name'])
        term_to_indicator_map.append(indicator)

        # 添加所有 alias
        if indicator.get('alias'):
            aliases = [alias.strip() for alias in indicator['alias'].split(',')]
            for alias in aliases:
                if alias:
                    all_terms.append(alias)
                    term_to_indicator_map.append(indicator)

    if not all_terms:
        return None

    # --- 步骤 2: 编码与计算 ---
    # 将用户查询和所有待匹配词条转换为向量
    query_embedding = model.encode(query, convert_to_tensor=True)
    terms_embeddings = model.encode(all_terms, convert_to_tensor=True)

    # 计算余弦相似度
    cosine_scores = util.cos_sim(query_embedding, terms_embeddings)

    # --- 步骤 3: 找到最佳匹配 ---
    # torch.argmax() 找到最高得分的索引
    best_match_index = torch.argmax(cosine_scores).item()
    best_score = cosine_scores[0][best_match_index].item()

    if best_score >= score_threshold:
        matched_term = all_terms[best_match_index]
        matched_indicator = term_to_indicator_map[best_match_index]

        return {
            "query": query,
            "matched_term": matched_term,
            "score": best_score,
            "hit_indicator": matched_indicator
        }
    else:
        return None

# --- 4. 运行 Demo ---
if __name__ == "__main__":
    # 测试用例 1: 输入一个别名
    query1 = "平均血小板体积"
    result1 = find_best_semantic_match(query1, database_indicators, model)
    print(f"\n--- 测试1: 精确匹配别名 ---")
    print(result1)

    # 测试用例 2: 输入一个与 name 意思相近但不完全相同的词
    query2 = "PG I/PG IPG I/PGII"
    result2 = find_best_semantic_match(query2, database_indicators, model)
    print(f"\n--- 测试2: 语义模糊匹配 ---")
    print(result2)
    os._exit(0)

    # 测试用例 3: 另一个领域的指标
    query3 = "查血糖"
    result3 = find_best_semantic_match(query3, database_indicators, model, score_threshold=0.5) # 适当降低阈值
    print(f"\n--- 测试3: 另一个指标的模糊匹配 ---")
    print(result3)

    # 测试用例 4: 一个完全不相关的查询
    query4 = "体重"
    result4 = find_best_semantic_match(query4, database_indicators, model)
    print(f"\n--- 测试4: 无匹配项 ---")
    print(result4)

    # 测试用例 5: 测试另一个指标
    query5 = "平均血小板体test"
    result5 = find_best_semantic_match(query5, database_indicators, model)
    print(f"\n--- 测试5: 另一个指标配项 ---")
    print(result5)
