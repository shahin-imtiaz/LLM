from flask import Flask
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain
import os

os.environ["OPENAI_API_KEY"] = "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"

app = Flask(__name__)

@app.route("/")
def hello():
    llm = OpenAI(temperature=.7)
    template = """Let the following be a powerBI model called demoModel:

In Power BI, I have: A dimension table called Account of:
Account,Account_level1,Account_level2
Default member,Default member,
Undefined,Undefined,
Units Sold,Statistical,Units Sold
Price per Unit,Statistical,Price per Unit
Cost per Unit,Statistical,Cost per Unit
Revenue,Sales Margin,Revenue
Cost,Sales Margin,Cost

A dimension table called Product of:
Product,Product_level1,Product_level2
Default member,Default member,
Undefined,Undefined,
Plant-Based Burger,All Products,Plant-Based Burger
Ice Cream,All Products,Ice Cream
Cola,All Products,Cola
Burger,All Products,Burger

A dimension table called Store of:
Store,Store_level1,Store_level2
Default member,Default member,
Undefined,Undefined,
San Diego,All Stores,San Diego
Los Angeles,All Stores,Los Angeles
New York,All Stores,New York
Dallas,All Stores,Dallas
Toronto,All Stores,Toronto
Vancouver,All Stores,Vancouver

A dimension table called Year of:
Year,Year_level1,Year_level2
Default member,Default member,
Undefined,Undefined,
2023,All Years,2023
2022,All Years,2022
2021,All Years,2021
2020,All Years,2020

A dimension table called Period of:
Period,Period_level1,Period_level2
Default member,Default member,
Undefined,Undefined,
1,Full Year,1
2,Full Year,2
3,Full Year,3
4,Full Year,4
5,Full Year,5
6,Full Year,6
7,Full Year,7
8,Full Year,8
9,Full Year,9
10,Full Year,10
11,Full Year,11
12,Full Year,12


There are next relationships between the tables:
values.Account is mapped many-to-one to Account.Account
values.Product is mapped many-to-one to Product.Product
values.Store is mapped many-to-one to Store.Store
values.Year is mapped many-to-one to Year.Year
values.Period is mapped many-to-one to Period.Period

A fact table called values of:
Account,Product,Store,Year,Period,value
Assume the Year dimension in the fact table is numeric. The fact table is as follows:

Revenue.Plant-Based Burger.San Diego.2022.1.4870.28
Revenue.Cola.Los Angeles.2022.7.41350.3
Revenue.Cola.Los Angeles.2022.8.40798.54
Revenue.Cola.Los Angeles.2022.9.38985.87
Revenue.Cola.Los Angeles.2022.10.35252.57
Revenue.Cola.Los Angeles.2022.11.32448.43
Revenue.Cola.Los Angeles.2022.12.35933.62
Revenue.Cola.Los Angeles.2021.1.24357.18
Revenue.Cola.Los Angeles.2021.2.24054
Revenue.Cola.Los Angeles.2021.3.27390.21
Revenue.Cola.Los Angeles.2021.4.28610.82
Revenue.Cola.Los Angeles.2021.5.30785.1
Revenue.Cola.Los Angeles.2021.6.35805.05
Revenue.Cola.Los Angeles.2020.7.33053.45
Revenue.Cola.Los Angeles.2020.8.32405.59
Revenue.Cola.Los Angeles.2020.9.30539.81
Revenue.Cola.Los Angeles.2020.10.25981.96
Revenue.Cola.Los Angeles.2020.11.24832.9
Revenue.Cola.Los Angeles.2020.12.28123.11
Revenue.Cola.New York.2022.1.22623.62
Revenue.Cola.New York.2022.2.22046.6
Revenue.Cola.New York.2022.3.24960.98
Revenue.Cola.New York.2022.4.25840.45
Revenue.Cola.New York.2022.5.29411.08
Revenue.Cola.New York.2022.6.35816.17
Revenue.Cola.New York.2022.7.35552.44
Revenue.Cola.New York.2022.8.34916.85
Revenue.Cola.New York.2022.9.34743.22
Revenue.Cola.New York.2022.10.28217.15
Revenue.Cola.New York.2022.11.24887.88
Revenue.Cola.New York.2022.12.28919.08
Revenue.Cola.New York.2021.1.19388.88
Revenue.Cola.New York.2021.2.20942.37
Revenue.Cola.New York.2021.3.22780.33
Revenue.Cola.New York.2021.4.23662.87
Revenue.Cola.New York.2021.5.26508.87
Revenue.Cola.New York.2021.6.30820.16
Revenue.Cola.New York.2021.7.28249.72
Revenue.Cola.New York.2021.8.29042.47
Revenue.Cola.New York.2021.9.27366.65
Revenue.Cola.New York.2021.10.25663.26
Revenue.Cola.New York.2021.11.23032.69
Revenue.Cola.New York.2021.12.25150.83
Revenue.Cola.New York.2020.1.17095.43
Revenue.Cola.New York.2020.2.18149.91
Revenue.Cola.New York.2020.3.19569.29
Revenue.Cola.New York.2020.4.20615.96
Revenue.Cola.New York.2020.5.22998.39
Revenue.Cola.New York.2020.6.28547.18
Revenue.Cola.New York.2020.7.26623.06
Revenue.Cola.New York.2020.8.26567.98
Revenue.Cola.New York.2020.9.25868.22
Revenue.Cola.New York.2020.10.20583.35
Revenue.Cola.New York.2020.11.19802.46
Revenue.Cola.New York.2020.12.23817.13
Revenue.Cola.Dallas.2022.1.16919.52
Revenue.Cola.Dallas.2022.2.15679.7
Revenue.Cola.Dallas.2022.3.18730.5
Revenue.Cola.Dallas.2022.4.20209.82
Revenue.Cola.Dallas.2022.5.21270.56
Revenue.Cola.Dallas.2022.6.24861.38
Revenue.Cola.Dallas.2022.7.24216.12
Revenue.Cola.Dallas.2022.8.24257.7
Revenue.Cola.Dallas.2022.9.23912.33
Revenue.Cola.Dallas.2022.10.20815.46
Revenue.Cola.Dallas.2022.11.19303.15
Revenue.Cola.Dallas.2022.12.20278.99
Revenue.Cola.Dallas.2021.1.13728.82
Revenue.Cola.Dallas.2021.2.14372.25
Revenue.Cola.Dallas.2021.3.16615.59
Revenue.Cola.Dallas.2021.4.16171.36
Revenue.Cola.Dallas.2021.5.18449.29
Revenue.Cola.Dallas.2021.6.21862.73
Revenue.Cola.Dallas.2021.7.21366.44
Revenue.Cola.Dallas.2021.8.21634.13
Revenue.Cola.Dallas.2021.9.21417.94
Revenue.Cola.Dallas.2021.10.17750.04
Revenue.Cola.Dallas.2021.11.15576.06
Revenue.Cola.Dallas.2021.12.18027.42
Revenue.Cola.Toronto.2021.1.8092.4
Revenue.Cola.Toronto.2021.2.8899.03
Revenue.Cola.Toronto.2021.3.10653.88
Revenue.Cola.Toronto.2021.4.11489.13
Revenue.Cola.Toronto.2021.5.11293.28
Revenue.Cola.Toronto.2021.6.13589.91
Revenue.Cola.Toronto.2021.7.13097.81
Revenue.Cola.Toronto.2021.8.13343.16
Revenue.Cola.Toronto.2021.9.14551.34
Revenue.Cola.Toronto.2021.10.11607.63
Revenue.Cola.Toronto.2021.11.9325.46
Revenue.Cola.Toronto.2021.12.11506.69
Question: {text}
Answer:
    """
    prompt_template = PromptTemplate(input_variables=["text"], template=template)
    answer_chain = LLMChain(llm=llm, prompt=prompt_template)
    answer = answer_chain.run("In that case, given the information of demoModel above, what is the year over year growth in revenue of the New York store? tell me the exact number given the info above?")
    return answer
