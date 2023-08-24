#!/usr/bin/python3
import json 
import uuid 



test = {
    "id": str(uuid.uuid4()),
    "context": {
      "registration": "969c110a-d3bc-427b-b91e-28c2839968a2",
      "contextActivities": {
        "category": [
          {
            "objectType": "Activity",
            "id": "http://class.whalespace.io/xapi/profile/video"
          }
        ],
        "parent": [
          {
            "objectType": "Activity",
            "id": "https://class.whalespace.io/data2/lectures/455106",
            "definition": {
              "type": "https://class.whalespace.io/definition/type",
              "name": {
                "en-US": "클래스명"
              },
              "description": {
                "en-US": "클래스 설명"
              }
            }
          }
        ]
      },
      "instructor": {
        "objectType": "Group",
        "account": {
          "homePage": "https://class.whalespace.io/userInfo/base-info/",
          "name": "학교 정보"
        },
    "member": [
            {
                "mbox": "mailto:998@class.whalespace.io",
                "name": "웨일클래스 교수자 1"
            }
        ]
},
"revision": "1.0",
"platform": "https://class.whalespace.io",
"extensions": {
    "https://w3id.org/xapi/cmi5/context/extensions/sessionid": str(uuid.uuid4()),
    "https://w3id.org/xapi/cmi5/context/extensions/launchurl": "https://cne-player.bubblecon.co.kr/?endpoint=https%3A%2F%2Fcne-lrs.bubblecon.co.kr%2FxAPI&fetch=https%3A%2F%2Fcne-lrs.bubblecon.io%2FxAPI%2Ftoken&actor=%7B%22objectType%22%3A%22Agent%22%2C%22name%22%3A%22jsh123%22%2C%22account%22%3A%7B%22homePage%22%3A%22https%3A%2F%2Fclass.whalespace.io%2FuserInfo%2Fbase-info%2F%22%2C%22name%22%3A%22%EC%A1%B0%EC%88%98%ED%98%84%22%7D%7D&activityId=https%3A%2F%2Fclass.whalespace.io%2Fbubblecon-guide%2Flecture%2F1639588&registration=969c110a-d3bc-427b-b91e-28c2839968a2",
    "https://w3id.org/xapi/cmi5/context/extensions/launchmode": "Normal",
    "https://w3id.org/xapi/cmi5/context/extensions/moveon": "Completed",
    "https://class.whalespace.io/classes/class/id": 1281368,
    "https://class.whalespace.io/classes/class/name": "웨일 클래스 사용자 가이드",
    "https://class.whalespace.io/classes/class/type": "group",
    "https://class.whalespace.io/classes/class/period/startdate": "2023-01-01",
    "https://class.whalespace.io/classes/class/period/enddate": "2023-01-20",
    "https://class.whalespace.io/classes/class/certificate": false,
    "https://class.whalespace.io/classes/class/address": "가나다",
    "https://class.whalespace.io/classes/class/school-level": "초등학교",
    "https://class.whalespace.io/classes/class/subject": "국어",
    "https://class.whalespace.io/classes/class/subject-progress": 0.8,
    "https://class.whalespace.io/classes/class/subject-progress-type": "rate",
    "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/period-set/startdate": "2023-01-01",
    "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/period-set/enddate": "2023-01-13",
    "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/tag-subject": "수학",
    "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/tag": "첫 학기",
    "https://class.whalespace.io/classes/class/chapters/chapter/lectures/lecture/comment": 3
},
"team": {
    "objectType": "Group",
    "account": {
        "homePage": "https://class.whalespace.io/userInfo/base-info/",
        "name": "학교 정보"
    }
}
},
"object": {
"objectType": "Activity",
"definition": {
    "name": {
        "en-US": "definition name"
    },
    "description": {
        "en-US": "definition description"
    },
    "type": "http://activitystrea.ms/schema/1.0/collection",
    "extensions": {
        
    }
},
"id": "https://class.whalespace.io/bubblecon-guide/lecture/1639588"
},
"verb": {
"id": "http://adlnet.gov/expapi/verbs/launched",
"display": {
    "en-US": "launched"
}
},
"actor": {
      "objectType": "Agent",
      "name": "jsh123",
      "account": {
        "homePage": "https://class.whalespace.io/userInfo/base-info/",
        "name": "조미현"
      }
    },
}

test = test.encode("ascii")