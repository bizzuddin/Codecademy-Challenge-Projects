import pandas as pd
pd.set_option('display.max_colwidth', -1)

jeopardy = pd.read_csv('jeopardy.csv')
#print(jeopardy.columns)
#Mengganti format judul kolom dan menyimpan ke dataframe baru 
jeopardy_new = jeopardy.rename(columns= {'Show Number':'Show Number', ' Air Date':'Air Date', ' Round':'Round', ' Category':'Category', ' Value':'Value',' Question':'Question',' Answer':'Answer'})
#print(jeopardy_new.columns)

def filter_question(data,words):
    #Value pada kolom 'Question' dibuat lowercase, begitu pula dengan kata kunci yang ingin difilter
    filter = lambda x: all(word.lower() in x.lower() for word in words)
    # Menerapkan fungsi lambda ke kolom 'Question' sehingga nilai return merupakan row di mana nilai lambda adalah True
    return data.loc[data["Question"].apply(filter)]
#king_england_jeopardy = filter_question(jeopardy_new,['King','England'])

king_questions = filter_question(jeopardy_new,'king')
#print(king_questions['Value'].head())

#Mengubah nilai pada column Value dari tipe string ke tipe Float 
king_questions['Only Value']= king_questions['Value'].apply(lambda x: float(x[1:].replace(',','')) if x != "None" else 0)
#print(king_questions['Only Value'].head())
#Mencari rata-rata nilai dari pertanyaan yang mengandung kata 'king'
king_questions_value_mean = king_questions['Only Value'].mean()
#print(king_questions_value_mean)

#Mencari jumlah jawaban unik dari pertanyaan yang mengandung kata 'king'
unique_answer = king_questions['Answer'].value_counts()
print(unique_answer)
















