root = 'voice_statistics/'
balance_sentences = 'balance_sentences.txt'
sr = 8000
length = sr * 15
n_category = 100
batchsize = 1
lr = 1e-3
finish_trigger = (100, 'epoch')
report_trigger = (10, 'iteration')
