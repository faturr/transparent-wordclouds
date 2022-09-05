from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
Peran_MOT = data_all[['column']]
wordcloud = WordCloud(
    width = 3000,
    height = 1400,
    background_color="rgba(255, 255, 255, 0)", 
    mode= "RGBA",
    colormap = 'tab10',
    stopwords=[],
    max_words=10000,
    min_word_length=5,).generate(str(column))
fig = plt.figure(
figsize = (20, 10),
edgecolor = 'k')
plt.imshow(wordcloud, interpolation = 'bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.savefig('output.png', dpi=200)