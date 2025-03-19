from dotenv import load_dotenv

load_dotenv()

import controlflow as cf


@cf.flow
def my_flow(x: int) -> int:
    y = cf.run("5を足してください", result_type=int, context=dict(x=x))
    z = cf.run("結果を2倍してください", result_type=int)
    return z


print(my_flow(10))
