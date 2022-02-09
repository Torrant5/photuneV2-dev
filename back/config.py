from dotenv import load_dotenv
load_dotenv()

import os
USE_AI = os.getenv('USE_AI') == 'True'
# Trueで計算, Falseでランダム
# パワーがあればTrue