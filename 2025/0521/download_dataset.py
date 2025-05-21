from modelscope import MsDataset

# 加载训练集
dataset = MsDataset.load('swift/zh_cls_fudan-news', split='train')

# 加载测试集（注意：原代码中的subset_name参数可能有误）
test_dataset = MsDataset.load('swift/zh_cls_fudan-news', split='test')

print(dataset)
print(test_dataset)

