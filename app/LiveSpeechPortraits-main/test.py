import pickle
f = open(r'E:\final_work\work\app\LiveSpeechPortraits-main\data\May\checkpoints\Audio2Feature.pkl','rb')
content=pickle.load(f)

print(content)