import random
from xapi_app.actions.contents.actions import lecture, quiz


class ContentsActionTemplate:
    def __init__(self):
        self._actions = []

    def actions(self):
        self._actions.append(self._initialize())
        self._actions.extend(self._add_actions())
        self._actions.append(self._complated())
        self._actions.extend(self._hooks())
        return self._actions
    
    def _add_actions(self):
        raise NotImplementedError

    def _initialize(self):
        raise NotImplementedError

    def _complated(self):
        raise NotImplementedError
    
    def _hooks(self):
        return []


class ContentsFactory:
    def __init__(self):
        types = ["lecture", "task", "peer", "quiz", "survey"]
        self._builders = {}
        for type_ in types:
            self._builders[type_] = {}

    def regist(self, class_, *args):
        dict_ = self._builders
        for idx, key in enumerate(args):
            if idx == len(args) -1:
                dict_[key] = class_
            else:
                dict_ = dict_[key]
        
    def get_template(self, *args) -> ContentsActionTemplate:
        dict_ = self._builders
        for key in args:
            dict_ = dict_[key]
        return dict_
    

class LectureActionTemplate(ContentsActionTemplate):
    def _initialize(self):
        return lecture.Initialized
    
    def _complated(self):
        return lecture.Completed

# NOTE: 완료 
class LectureTextTemplate(LectureActionTemplate):
    def __init__(self): 
        super().__init__()

    def _add_actions(self):
        items = [lecture.Read]
        return items

# TODO: 각각의 result 정의할 것, Movie 기간 동안의 동작을 랜더믹하게 돌리면 완성될 듯?
class LectureMovieTemplate(LectureActionTemplate):
    def __init__(self): 
        super().__init__()

    def _add_actions(self):
        items = list(
            lecture.MoviePlayed,
            lecture.MoviePaused,
            lecture.MovieInteracted,
            lecture.MovieSeeked,
        )
        return items
    
    def _complated(self):
        return lecture.MovieCompleted

class LectureImageTemplate(LectureActionTemplate):
    def __init__(self): 
        super().__init__()

    def _add_actions(self):
        return [lecture.Viewed]
    

class LectureExercTemplate(LectureActionTemplate):
    def __init__(self): 
        super().__init__()

    def _add_actions(self):
        items = []
        interacted_num = random.randint(1, 5)

        for x in range(interacted_num):
            items.append(lecture.ExercInteracted)
        items.append(lecture.ExercAnswered)
        return items
    

class LectureDocTemplate(LectureActionTemplate):
    def __init__(self): 
        super().__init__()

    def _add_actions(self):
        items = list(
            lecture.Donwloaded
        )
        return items

class LectureUrlTemplate(LectureActionTemplate):
    def __init__(self): 
        super().__init__()

    def _add_actions(self):
        items = list(
            lecture.Opened
        )
        return items   

# TODO: 시도횟수에 대한 것이 필요할 것 
class LecturePollTemplate(LectureActionTemplate):
    def __init__(self): 
        super().__init__()

    def _add_actions(self):
        items = list(
            lecture.PollAnswered
        )
        return items   


# TODO: 완료해야 할 것 
class LectureLiveTemplate(LectureActionTemplate):
    def __init__(self): 
        super().__init__()

    def _add_actions(self):
        items = list(
            lecture.PollAnswered
        )
        return items   


# factory.regist(LectureTextTemplate, "lecture", "text")
# factory.regist(LectureMovieTemplate, "lecture", "movie")
# factory.regist(LectureMovieTemplate, "lecture", "image")
# factory.regist(LectureExercTemplate, "lecture", "exerc")
# factory.regist(LectureDocTemplate, "lecture", "doc")
# factory.regist(LectureUrlTemplate, "lecture", "url")
# factory.regist(LecturePollTemplate, "lecture", "poll")
# factory.regist(LecturePollTemplate, "lecture", "live")


class QuizChoiceTemplate(ContentsActionTemplate):
    def __init__(self): 
        super().__init__()
    
    def _initialize(self):
        return quiz.ChoiceInitialized
    
    def _complated(self):
        return quiz.ChoiceCompleted

    def _add_actions(self):
        items = [quiz.ChoiceAnswered]
        return items   

    def _hooks(self):
        return [quiz.ChoiceChecked]


class QuizFillinTemplate(ContentsActionTemplate):
    def __init__(self): 
        super().__init__()

    def _initialize(self):
        return quiz.FillInInitialized
    
    def _complated(self):
        return quiz.FillInCompleted

    def _hooks(self):
        return [quiz.FillInChecked]
    
    def _add_actions(self):
        items = [quiz.FillInCompleted]
        return items   

class QuizLongFillinTemplate(ContentsActionTemplate):
    def __init__(self): 
        super().__init__()

    def _initialize(self):
        return quiz.LongFillInInitialized
    
    def _complated(self):
        return quiz.LongFillInCompleted

    def _hooks(self):
        items = [quiz.LongFillInChecked, quiz.LongFillInScored]
        return items
                 
    def _add_actions(self):
        items = [quiz.LongFillInAnswered]
        return items 
        
factory = ContentsFactory()
factory.regist(QuizChoiceTemplate, "quiz", "choice")
factory.regist(QuizFillinTemplate, "quiz", "fill-in")
factory.regist(QuizLongFillinTemplate, "quiz", "long-fill-in")

# factory.regist(SurveyFillinTemplate, "survey", "fill-in")
# factory.regist(SurveyLongFillinTemplate, "survey", "long-fiil-in")