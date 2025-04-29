from typing import TypedDict, Dict, Any
from langgraph.graph import StateGraph # 导入 StateGraph
# from langgraph.prebuilt import conditional_edge  # 移除旧的导入
from typing import List, Dict
from typing_extensions import TypedDict
import asyncio

# ---------------
# Langgraph version 3.0.30
# Python 3.11.11
# ---------------


# 假设的第三方 SDK 和工具函数
class SurveySDK:
    def __init__(self):
      self.questions = {
          "user1": [
              {"question": "请输入您的身高(cm):", "question_id": 1, "status": 1, "result": ""},
              {"question": "请输入您的体重(kg):", "question_id": 2, "status": 1, "result": ""},
              {"question": "请输入您的年龄:", "question_id": 3, "status": 1, "result": ""},
              {"question": "", "question_id": None, "status": 2, "result": "Evaluation completed."},
          ]
      }

    async def get_question(self, user_id: str) -> Dict:
        # 模拟从 SDK 获取问题
        # 实际应用中需要替换为真实的 SDK 调用
        if user_id in self.questions:
            if self.questions[user_id]:
              return self.questions[user_id].pop(0)
            else:
              return {"question": "", "question_id": None, "status": 2, "result": "Evaluation completed."}
        else:
            return {"question": "", "question_id": None, "status": 2, "result": "User not found."}

    async def submit(self, question_id: int, answer: str) -> None:
        # 模拟提交答案
        # 实际应用中需要替换为真实的 SDK 调用和状态更新
        print(f"Answer submitted for question {question_id}: {answer}")

async def send_form(form_data: Dict) -> None:
    # 模拟发送表单到客户端
    print(f"Sending form to client: {form_data}")
    # 这里需要实现向客户端发送表单数据的逻辑
    # 在实际应用中，可能需要使用 HTTP 请求或其他通信方式
    await asyncio.sleep(1) # 模拟网络请求

# 问卷 SDK 实例
survey = SurveySDK()


class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        user_id: The ID of the user taking the survey.
        question_id: The ID of the current question.
        question: The current question being asked.
        answer: The user's answer to the current question.
        all_answers: A list of all the user's answers.
        status: The status of the survey (1: ongoing, 2: completed).
        result: The final evaluation result.
    """
    user_id: str
    question_id: int | None
    question: str
    answer: str
    all_answers: List[Dict]
    status: int
    result: str

# 1. 定义节点

async def greeting_node(state: GraphState) -> Dict:
    """显示问卷的欢迎语和说明"""
    print("\n===== 健康评估问卷 =====")
    print("欢迎参与健康评估问卷调查！")
    print("本问卷将收集您的身高、体重和年龄信息，")
    print("用于计算BMI指数并提供健康建议。")
    print("请根据提示输入相关信息。")
    print("=======================\n")
    return {}

async def get_question_node(state: GraphState) -> Dict:
    """获取问题"""
    question_data = await survey.get_question(state["user_id"])
    return {
        "question": question_data["question"],
        "question_id": question_data["question_id"],
        "status": question_data["status"],
        "result": question_data["result"],
    }


async def send_form_node(state: GraphState) -> Dict:
    """发送表单给客户端，等待用户输入"""
    # 检查是否已经没有题目了
    if state["question_id"] is None and state["status"] == 2:
        return {"answer": ""}  # 不需要用户输入，直接返回空答案
        
    form_data = {
        "question": state["question"],
        "question_id": state["question_id"],
    }
    await send_form(form_data)
    # 模拟中断等待用户输入，实际应用中需要替换为中断机制
    # 这里只是为了让流程暂停，等待用户输入
    answer = input(f"Please answer the question: {state['question']}\n") # 阻塞进程, 模拟interrupt
    return {"answer": answer}


async def process_answer_node(state: GraphState) -> Dict:
    """处理答案，更新状态"""
    question_id = state["question_id"]
    answer = state["answer"]
    
    # 检查问题是否已结束，避免处理空答案
    if question_id is None:
        return {}  # 不更新all_answers
        
    await survey.submit(question_id, answer)  # 调用 submit 方法提交答案

    return {
        "all_answers": state["all_answers"] + [{"question_id": question_id, "answer": answer}]
    }


async def evaluate_node(state: GraphState) -> Dict:
    """生成评估结果，计算BMI并给出建议"""
    all_answers = state["all_answers"]
    
    # 提取用户输入的数据
    height_cm = 0
    weight_kg = 0
    age = 0
    
    for answer in all_answers:
        if answer["question_id"] == 1:  # 身高
            try:
                height_cm = float(answer["answer"])
            except ValueError:
                height_cm = 170  # 默认值
        elif answer["question_id"] == 2:  # 体重
            try:
                weight_kg = float(answer["answer"])
            except ValueError:
                weight_kg = 60  # 默认值
        elif answer["question_id"] == 3:  # 年龄
            try:
                age = int(answer["answer"])
            except ValueError:
                age = 30  # 默认值
    
    # 计算BMI (体重kg/身高m的平方)
    height_m = height_cm / 100
    bmi = weight_kg / (height_m * height_m) if height_m > 0 else 0
    bmi = round(bmi, 2)
    
    # 根据BMI评估健康状况
    health_status = ""
    if bmi < 18.5:
        health_status = "体重过轻"
        advice = "建议适当增加饮食量，增加蛋白质摄入，开展力量训练。"
    elif bmi < 24:
        health_status = "体重正常"
        advice = "继续保持健康的生活习惯，均衡饮食和适当运动。"
    elif bmi < 28:
        health_status = "超重"
        advice = "建议控制饮食热量摄入，增加有氧运动频率，如慢跑、游泳等。"
    else:
        health_status = "肥胖"
        advice = "建议在医生指导下制定减重计划，控制饮食并增加运动量。"
    
    # 生成综合评估结果
    result = f"BMI评估结果:\n身高: {height_cm}cm\n体重: {weight_kg}kg\n年龄: {age}岁\n\nBMI值: {bmi}\n健康状态: {health_status}\n\n健康建议:\n{advice}"
    
    return {"result": result}


async def output_node(state: GraphState) -> Dict:
    """输出结果"""
    print("Final Result:", state["result"])
    return {}


# 3. 构建图
agent = StateGraph(GraphState) # 使用 StateGraph

# 添加节点
agent.add_node("greeting", greeting_node)
agent.add_node("get_question", get_question_node)
agent.add_node("send_form", send_form_node)
agent.add_node("process_answer", process_answer_node)
agent.add_node("evaluate", evaluate_node)
agent.add_node("output", output_node)

# 添加边
agent.add_edge("greeting", "get_question")  # 先显示欢迎语，然后获取问题
agent.add_edge("get_question", "send_form") # 获取问题后发送表单

# 使用条件边连接 send_form 和 evaluate
def should_evaluate(state: GraphState):
    if state["status"] == 2:
        return "evaluate"
    else:
        return "process_answer"

agent.add_conditional_edges(
    "send_form",  # 从 send_form 节点开始
    should_evaluate,  # 使用 should_evaluate 函数判断
    {
        "process_answer": "process_answer",  # 如果 should_evaluate 返回 "process_answer"，则连接到 process_answer
        "evaluate": "evaluate"  # 如果 should_evaluate 返回 "evaluate"，则连接到 evaluate
    }
)

agent.add_edge("process_answer", "get_question")
agent.add_edge("evaluate", "output")

# 设置入口点
agent.set_entry_point("greeting")  # 修改入口点为欢迎节点

# 构建图
workflow = agent.compile() #  这里也要改成 agent.compile()

def draw_graph(graph):
    try:
        # Save image to a file in the current folder
        import os
        current_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(current_dir, "survey_demo_diagram.png")
        graph.get_graph().draw_png(output_path)
    except Exception:
        # This requires some extra dependencies and is optional
        import traceback
        print(traceback.format_exc())
        pass

# 4. 运行 workflow
# 初始化状态
inputs = {"user_id": "user1", "question_id": None, "question": "", "answer": "", "all_answers": [], "status": 1, "result": ""}

# 运行
async def run_workflow():
  result = await workflow.ainvoke(inputs)
  print(result)

# Main entry point
if __name__ == "__main__":
    # 绘制图
    # draw_graph(workflow)
    asyncio.run(run_workflow())  
