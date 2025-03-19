from dotenv import load_dotenv

load_dotenv()

import controlflow as cf

color = cf.run(
    "Get the user's favorite color",
    interactive=True,
)

print(f"The user's favorite color is: {color}")
