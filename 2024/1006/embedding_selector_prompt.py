# 使用 MMR 来检索相关示例，以使用示例尽量符合输入
from langchain.prompts.example_selector import MaxMarginalRelevanceExampleSelector
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
import os

# 使用千问模型的API密钥
api_key = os.getenv("QIANWEN_API_KEY")

# 假设已经有这么多的提示词示例组：
examples = [
    {"input":"happy","output":"sad"},
    {"input":"tall","output":"short"},
    {"input":"sunny","output":"gloomy"},
    {"input":"windy","output":"calm"},
    {"input":"高兴","output":"悲伤"}
]

example_prompt = PromptTemplate(
    input_variables = ["input", "output"],
    template = "原词: {input}\n 反义：{output}",
)

# 调用 MMR 
model_name = "Qwen/Qwen2.5-7B-Instruct"
example_selector = MaxMarginalRelevanceExampleSelector.from_examples(
    # 传入示例组
    examples,
    # 使用千问模型的嵌入来做相似性搜索
    HuggingFaceEmbeddings(model_name=model_name),
    # 设置使用向量数据库是什么
    FAISS,
    # 结果条数
    K=2
)

# 使用小样本模板
mmr_prompt = FewShotPromptTemplate(
    example_selector = example_selector,
    example_prompt = example_prompt,
    prefix = "给出每个输入词的反义词",
    suffix = "原词: {adjective}\n 反义:",
    input_variables = ["adjective"]
)

# 当我们输入一个描述情绪的词语的时候，应该筢同样是描述情绪的一对示例组来填充提示词模板
print(mmr_prompt.format(adjective="难过"))






