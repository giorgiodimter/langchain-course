from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()
def main():
    print("Hello from langchain-course!")
    information = """ 
    Project Risk Quantification by John K. Hollmann
A Practitioner's Guide to Realistic Cost and Schedule Risk Management
Are you tired of project cost overruns and missed deadlines? Project Risk Quantification delivers the missing piece in project risk management: a proven, data-driven approach to forecasting cost and schedule outcomes with confidence. Written by John Hollmann, a globally recognized expert in cost engineering and risk quantification, this essential guide bridges the gap between traditional risk management practices and real-world project performance.

Drawing on decades of experience, Hollmann introduces a step-by-step framework for identifying, analyzing, and mitigating project risks in capital-intensive industries. This book breaks down complex statistical and analytical concepts into practical tools that project managers, estimators, risk analysts, and decision-makers can immediately apply.

Inside, you will discover:

* How to move beyond guesswork with empirically-based cost and schedule risk models,
* The importance of risk drivers over simplistic "range estimating" techniques,
* Ways to use probabilistic methods to set realistic contingencies and expectations,
* Real-world case studies that show the consequences of flawed risk approaches and how to fix them, and
* Guidance on integrating quantitative risk analysis into the project planning lifecycle.

Whether you are managing a multi-billion-dollar infrastructure initiative or a more modest capital project, Project Risk Quantification will change the way you think about uncertainty and give you the tools to make more informed, defensible decisions.

This book is not just theory. It is a practical manual for transforming how organizations predict and manage risk. It is time to replace false precision and gut feel with sound data and proven methods.

Equip yourself with the insights that leading organizations worldwide are using to improve predictability, accountability, and results. Project Risk Quantification is your blueprint for mastering project risk with clarity and confidence.
"""


    summary_template = """
    Given the information {information} about the book i want you to give me:
    1. A short summary
    2. what can i discover in it
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model='gpt-5')
    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information":information})
    print(response.content)

if __name__ == "__main__":
    main()
