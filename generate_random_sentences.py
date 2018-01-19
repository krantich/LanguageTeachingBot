import os
import random

dataset_file = "yestu hottige\nyaavaga meeting\nyelli bartire meeting ge\nyaaru bartire class ge\nenu maditiri\nyaake class\nyestu meeting hottige\nyaake meeting\nyaavaga bartire\nyelli ide class\nyaaru avaru\nyestu togottiri"
model = {}
generated = []
predicted = []

def save_data_to_file(filename):
    f = open(fileName, "w+")
    f.write(dataset_file)
    f.close()


def set_corpus(filename):
    with open(filename) as f:
        for line in f:
            line = line.split()
            for i, word in enumerate(line):
                if i == len(line)-1:
                    model['END'] = model.get('END', []) + [word]
                else:
                    if(i == 0):
                        model['START'] = model.get('START', []) + [word]                    
                    model[word] = model.get(word, []) + [line[i+1]] 
                i+= 1

def get_sentence(startWord, predicted):
    words = []
    output = ""
    while True:
        if len(predicted) == 0:
            words = startWord
        elif predicted[-1] in model['END']:
            break
        else:
            try:
                words = model[predicted[-1]]
            except KeyError:
                predicted = []
                break

        if(len(predicted) == 0):
            predicted.append(words)
        else:
            predicted.append(random.SystemRandom().choice(words))
        #print("Data in Predicted list = ",predicted)

    if(len(predicted) == 0):
        output = "No corpus available to generate sentence for the given word"
    else:
        output = ' '.join(predicted)

    return(output)


eng_trans = {"yestu hottige": "What time?", "yaavaga meeting": "What time is the meeting?", "yelli bartire meeting ge": "Where do you come for meeting?",
             "yaaru bartire class ge": "Who will come for the class?", "enu maditiri": "What are you doing?", "yaake class": "Why there is a class?", "yestu meeting hottige": "What time will you go for meeting?",
             "yaake meeting": "Why is the meeting for?", "yaavaga bartire": "When will you come?", "yelli ide class": "Where is the class?", "yaaru avaru": "Whoz that?", "yestu togottiri": "How much is it?"}

def get_english_translation(kannada):
    output = ""
    try:
        output = eng_trans[kannada]
    except KeyError:
        for key in eng_trans:
            if kannada in key:
                output = eng_trans[key]
        if(len(output) == 0):
            output = "No translation available for the generated Kannada Sentence"
    return output



fileName = os.getcwd()+"\datafile.txt"
save_data_to_file(fileName)
set_corpus(fileName)

while(True):
    print("Enter the word to generate sentence: Example words: Yestu, Enu, Yaavaga, Yaaru, Yelli, Yaake")
    print("Enter quit to quit from the learning")
    line = input()
    line = line.lower()
    if(line != 'quit'):
        kannada_sentence = get_sentence(line,predicted)
        if(kannada_sentence != "No corpus available to generate sentence for the given word"):
            print ("Example usage for the word: ",line)
            eng_sentence = get_english_translation(kannada_sentence)
            print(kannada_sentence, ", Loosely translated to: ", eng_sentence)
        else:
            print ("No corpus available to generate sentence for the given word: ", line)
        predicted=[]
        print("\n")
    else:
        print ("Hope you had fun, while learning Kannada :)")
        break
