import json
from sentence_transformers import SentenceTransformer, util
import torch

def load_data():
    """加载数据文件"""
    # 加载标准指标模板
    with open('data/indicator_template.json', 'r', encoding='utf-8') as f:
        database_indicators = json.load(f)

    # 加载原始实验室指标数据
    with open('data/raw_lab_indicator.json', 'r', encoding='utf-8') as f:
        raw_indicators = json.load(f)

    return database_indicators, raw_indicators

def find_best_semantic_match(query: str, indicators: list, model: SentenceTransformer, score_threshold: float = 0.8):
    """
    在指标库中为查询找到最佳的语义匹配。

    Args:
        query (str): 用户的输入查询。
        indicators (list): 包含指标对象的列表。
        model (SentenceTransformer): 已加载的 sentence-transformer 模型。
        score_threshold (float): 用于判断是否匹配成功的相似度阈值。

    Returns:
        dict: 包含最佳匹配信息的字典，如果没有找到则返回 None。
    """

    # --- 步骤 1: 数据展平和建立映射 ---
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

def batch_match_indicators():
    """批量匹配指标"""
    print("正在加载语义模型...")
    model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
    print("模型加载完毕。")

    # 加载数据
    database_indicators, raw_indicators = load_data()

    # 存储匹配结果
    match_results = []
    unmatched_indicators = []

    print(f"\n开始批量匹配 {len(raw_indicators)} 个指标...")

    for i, raw_indicator in enumerate(raw_indicators):
        query = raw_indicator['name']
        print(f"正在处理 ({i+1}/{len(raw_indicators)}): {query}")

        # 进行语义匹配
        match_result = find_best_semantic_match(query, database_indicators, model, score_threshold=0.8)

        if match_result:
            # 添加原始指标信息到匹配结果中
            match_result['original_indicator'] = raw_indicator
            match_results.append(match_result)
            print(f"  ✓ 匹配成功: {match_result['matched_term']} (得分: {match_result['score']:.3f})")
        else:
            # 计算最接近的匹配项及其分数
            # 重新编码和计算分数
            all_terms = []
            term_to_indicator_map = []
            for indicator in database_indicators:
                all_terms.append(indicator['name'])
                term_to_indicator_map.append(indicator)
                if indicator.get('alias'):
                    aliases = [alias.strip() for alias in indicator['alias'].split(',')]
                    for alias in aliases:
                        if alias:
                            all_terms.append(alias)
                            term_to_indicator_map.append(indicator)
            query_embedding = model.encode(query, convert_to_tensor=True)
            terms_embeddings = model.encode(all_terms, convert_to_tensor=True)
            cosine_scores = util.cos_sim(query_embedding, terms_embeddings)
            best_match_index = torch.argmax(cosine_scores).item()
            best_score = cosine_scores[0][best_match_index].item()
            matched_term = all_terms[best_match_index]
            matched_indicator = term_to_indicator_map[best_match_index]
            unmatched_indicators.append({
                'name': query,
                'original_indicator': raw_indicator,
                'best_match_term': matched_term,
                'best_match_score': best_score,
                'best_match_indicator': matched_indicator
            })
            print(f"  ✗ 未匹配或得分低于0.8，最接近: {matched_term} (得分: {best_score:.3f})")

    # 保存匹配结果到文件
    with open('data/match_result.json', 'w', encoding='utf-8') as f:
        json.dump(match_results, f, ensure_ascii=False, indent=2)

    print(f"\n匹配完成!")
    print(f"成功匹配: {len(match_results)} 个指标")
    print(f"未匹配: {len(unmatched_indicators)} 个指标")
    print(f"匹配结果已保存到: data/match_result.json")

    # 打印未匹配的指标
    if unmatched_indicators:
        print(f"\n=== 未匹配或得分低于0.8的指标 ===")
        for i, unmatched in enumerate(unmatched_indicators, 1):
            print(f"{i}. {unmatched['name']}")

    return match_results, unmatched_indicators

if __name__ == "__main__":
    batch_match_indicators()