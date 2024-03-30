#find duplicated rows sum
rating.duplicated().sum()
#merge two df
dfp = rating.merge(books,on='ISBN')

#grouping and renaming the columns
num_rating_df=dfp.groupby('Book-Title').count()['Book-Rating'].reset_index()
num_rating_df.rename(columns={'Book-Rating':'num_ratings'},inplace=True)

#remove non alphabets
def pre(txt):
    txt = re.sub('[^a-zA-Z]',' ',txt)
    return txt
num_rating_df['Book-Title'] = num_rating_df['Book-Title'].apply(pre)

#rating greater than 250 sorted values
popular_df = popular_df[popular_df['num_ratings']>=250].sort_values('avg_ratings',ascending=True)

#merge and drop duplicate values
popular_df = popular_df.merge(books,on='Book-Title').drop_duplicates('Book-Title')[['Book-Title','Book-Author','Image-URL-M','num_ratings','avg_ratings']]
