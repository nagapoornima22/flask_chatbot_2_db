from __future__ import annotations
import nltk
from nltk.stem.lancaster import LancasterStemmer
import numpy as np
import tflearn
import random
import pickle
import json
import json_path
from utils.app_util import getModuleClass
from app.main.dto.api_response import ApiResponse

nltk.download('punkt')


class ChatBot(object):
    instance = None

    @classmethod
    def getBot(cls):
        if cls.instance is None:
            cls.instance = ChatBot()
        return cls.instance

    def __init__(self):
        if self.instance is not None:
            raise ValueError("Did you forgot to call getBot function ? ")

        self.stemmer = LancasterStemmer()
        data = pickle.load(open(json_path.getPath('trained_data'), "rb"))
        self.words = data['words']
        self.classes = data['classes']
        train_x = data['train_x']
        train_y = data['train_y']
        with open(json_path.getJsonPath()) as json_data:
            self.intents = json.load(json_data)
        net = tflearn.input_data(shape=[None, len(train_x[0])])
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, 8)
        net = tflearn.fully_connected(net, len(train_y[0]), activation='softmax')
        net = tflearn.regression(net)
        self.model = tflearn.DNN(net, tensorboard_dir=json_path.getPath('train_logs'))
        self.model.load(json_path.getPath('model.tflearn'))

    def clean_up_sentence(self, sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [self.stemmer.stem(word.lower()) for word in sentence_words]
        return sentence_words

    def bow(self, sentence, words, show_details=False):
        sentence_words = self.clean_up_sentence(sentence)
        bag = [0] * len(words)
        for s in sentence_words:
            for i, w in enumerate(words):
                if w == s:
                    bag[i] = 1
                    if show_details:
                        print("found in bag: %s" % w)
        return np.array(bag)

    def classify(self, sentence):
        context = {}
        ERROR_THRESHOLD = 0.65
        results = self.model.predict([self.bow(sentence, self.words)])[0]
        results = [[i, r] for i, r in enumerate(results) if r > ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append((self.classes[r[0]], r[1]))
        return return_list

    def response(self, sentence, userID='123', show_details=False):
        results = self.classify(sentence)
        responseType = ""
        context = {}
        if results:
            while results:
                for i in self.intents['intents']:
                    if i['tag'] == results[0][0]:
                        if 'context_set' in i:
                            if show_details: print('context:', i['context_set'])
                            context[userID] = i['context_set']

                        if not 'context_filter' in i or \
                                (userID in context and 'context_filter' in i and i['context_filter'] == context[
                                    userID]):
                            if show_details:
                                print('tag:', i['tag'])

                        if "Questions" in i:
                            question = random.choice(i["Questions"][0]["pattern"])
                            #print(ApiResponse("Question : " , question).__dict__)
                            res = ApiResponse("Question", question).__dict__
                            #return res

                            #if "command" in i:
                            if (i["command"] != None):
                                que = input(question)         # input(question)
                                commandToExecute = random.choice(i['command'])
                                commandClassObj = getModuleClass(commandToExecute)
                                #print(commandClassObj)
                                return ApiResponse("Array", commandClassObj.execute(que)).__dict__

                        else:
                            responses = random.choice(i['responses'])
                            return ApiResponse("Text", responses).__dict__


        else:
            return ApiResponse("Text", "Sorry i didnot understand your question").__dict__
