from typing import Any
from xapi_app.types.common import XAPIObjectBase

class XAPIObject(XAPIObjectBase):
    def __init__(self, objectType, id, definition):
        self.objectType: str = objectType
        self.id: str = id
        self.definition: dict = definition


# {
#   "수업명": [
#     "창의적 문제 해결",
#     "사회학적 상상력 개발",
#     "디지털 아트와 미디어",
#     "지속 가능한 라이프스타일 디자인",
#     "현대 비즈니스 전략",
#     "세계 문화와 다양성 이해",
#     "자기 관리와 웰빙",
#     "철학과 인간 삶의 의미",
#     "과학 기술과 사회",
#     "인간-로봇 상호작용",
#     "인공지능과 머신 러닝 기초",
#     "글로벌 건강 문제",
#     "스포츠 심리학과 성과 최적화",
#     "환경 보호와 지속 가능성",
#     "현대 문학과 소설 분석",
#     "디지털 마케팅 전략",
#     "금융 기초와 투자 전략",
#     "식품과 영양 과학",
#     "공공 정책과 시민 참여",
#     "미래의 에너지와 기후 변화"
#   ]
# }


