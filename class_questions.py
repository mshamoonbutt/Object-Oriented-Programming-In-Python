
##
# A question with a text and an answer.
class Question:
    ## Constructs a question with empty question and answer strings.
    #
    def __init__(self):
        self._text = ""
        self._answer = ""
    ## Sets the question text.
    # @param questionText the text of this question
    #
    def setText(self, questionText):
        self._text = questionText
    ## Sets the answer for this question.
    # @param correctResponse the answer
    #
    def setAnswer(self, correctResponse):
        self._answer = correctResponse
    ## Checks a given response for correctness.
    # @param response the response to check
    # @return True if the response was correct, False otherwise
    ##
    def checkAnswer(self, response):
        return response.lower().strip() == self._answer.lower().strip()
## A question whose answer is a number.
#
class NumericQuestion(Question):
    ## Checks a given response for correctness.
    # @param response the response to check
    # @return True if the response was correct, False otherwise
    def checkAnswer(self, response):
        try:
            response = float(response)
            answer = float(self._answer)
            return abs(response - answer) <= 0.01
        except ValueError:
            return False
    def checkAnswer(self, response):
        return response == self._answer
## Displays this question.
#
    def display(self):
        print(self._text)
        
class AnyCorrectChoiceQuestion(Question):
    ## Constructs a question with empty question and answer strings.
    #
    def __init__(self):
        super().__init__()
        self._choices = []
    ## Adds a choice to this question.
    # @param choice the choice to add
    #
    def addChoice(self, choice):
        self._choices.append(choice)
    ## Sets the answer for this question.
    # @param correctResponses the correct choices
    #
    def setAnswer(self, correctResponses):
        self._answer = correctResponses
    ## Checks a given response for correctness.
    # @param response the response to check
    # @return True if the response was correct, False otherwise
    ##
    def checkAnswer(self, response):
        response = response.lower().strip()
        correct_responses = self._answer.lower().strip().split()
        return response in correct_responses
    ## Displays this question.
    #
    def display(self):
        print(self._text)
        for choice in self._choices:
            print(choice)        
## A question with a text and an answer.
#
## A question with multiple correct choices.
class MultiChoiceQuestion(Question):
    ## Constructs a question with empty question and answer strings.
    def __init__(self):
        super().__init__()
        self._choices = []
    ## Adds a choice to this question.
    # @param choice the choice to add
    #
    def addChoice(self, choice):
        self._choices.append(choice)
    ## Sets the answer for this question.
    # @param correctResponses the correct choices
    #
    def setAnswer(self, correctResponses):
        self._answer = correctResponses
    ## Checks a given response for correctness.
    # @param response the response to check
    # @return True if the response was correct, False otherwise
    ##
    def checkAnswer(self, response):
        response = response.lower().strip().split()
        correct_responses = self._answer.lower().strip().split()
        return set(response) == set(correct_responses)
    ## Displays this question.
    #
    def display(self):
        print(self._text)
        for choice in self._choices:
            print(choice)
# A question with a text and an answer.
class Question:
    ## Constructs a question with empty question and answer strings.
    def __init__(self):
        self._text = ""
        self._answer = ""
        
    ## Sets the question text.
    # @param questionText the text of this question
    def setText(self, questionText):
        self._text = questionText
        
    ## Sets the answer for this question.
    # @param correctResponse the answer
    def setAnswer(self, correctResponse):
        self._answer = correctResponse
        
    ## Checks a given response for correctness.
    # @param response the response to check
    # @return True if the response was correct, False otherwise
    def checkAnswer(self, response):
        return response == self._answer
    
    ## Adds text to this question.
    # @param text the text to add
    def addText(self, text):
        self._text += text

## A question whose answer is a number.
class NumericQuestion(Question):
    ## Checks a given response for correctness.
    # @param response the response to check
    # @return True if the response was correct, False otherwise
    def checkAnswer(self, response):
        return response == self._answer

## A question with multiple correct choices.
class MultiChoiceQuestion(Question):
    ## Constructs a question with empty question and answer strings.
    def __init__(self):
        super().__init__()
        self._choices = []
        
    ## Adds a choice to this question.
    # @param choice the choice to add
    def addChoice(self, choice):
        self.addText(choice)
        
    ## Sets the answer for this question.
    # @param correctResponses the correct choices
    def setAnswer(self, correctResponses):
        self._answer = correctResponses
        
    ## Checks a given response for correctness.
    # @param response the response to check
    # @return True if the response was correct, False otherwise
    def checkAnswer(self, response):
        return response == self._answer

## A question with any correct choice.
class AnyCorrectChoiceQuestion(Question):
    ## Constructs a question with empty question and answer strings.
    def __init__(self):
        super().__init__()
        
    ## Adds a choice to this question.
    # @param choice the choice to add
    def addChoice(self, choice):
        self.addText(choice)
        
    ## Sets the answer for this question.
    # @param correctResponses the correct choices
    def setAnswer(self, correctResponses):
        self._answer = correctResponses
        
    ## Checks a given response for correctness.
    # @param response the response to check
    # @return True if the response was correct, False otherwise
    def checkAnswer(self, response):
        response = response.lower().strip()
        correct_responses = self._answer.lower().strip().split()
        return response in correct_responses
    def __repr__(self):
            return f"Question(text={self._text}, answer={self._answer})"

    def __repr__(self):
            return f"ChoiceQuestion(text={self._text}, answer={self._answer}, choices={self._choices})"