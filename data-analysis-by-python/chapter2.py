import pandas as pd
import numpy as np

def analysis_movie_data():
    unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
    users = pd.read_table('../data/ml-1m/users.dat', sep='::', header=None, names=unames, engine='python')

    rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
    ratings = pd.read_table('../data/ml-1m/ratings.dat', sep='::', header=None, names=rnames, engine='python')

    mnames = ['movie_id', 'title', 'genres']
    movies = pd.read_table('../data/ml-1m/movies.dat', sep='::', header=None, engine='python', names=mnames)

    # print(users[:5])
    # print(ratings[:5])
    # print(movies[:5])

    data = pd.merge(pd.merge(users, ratings), movies)
    # print(data)
    # print(data.ix[0])

    mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
    # print(mean_ratings[:5])

    ratings_by_title = data.groupby('title').size()
    # print(ratings_by_title[:10])
    active_titles = ratings_by_title.index[ratings_by_title >= 250]
    # print(active_titles)

    mean_ratings = mean_ratings.ix[active_titles]
    # print(mean_ratings)

    # top_female_ratings = mean_ratings.sort_index(by='F',ascending=False)
    top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)
    # print(top_female_ratings[:10])

    mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
    sorted_by_diff = mean_ratings.sort_values(by='diff')
    # print(sorted_by_diff[:10])
    # print(sorted_by_diff[::-1][:15])

    rating_std_by_title = data.groupby('title')['rating'].std()
    rating_std_by_title = rating_std_by_title.ix[active_titles]
    # print(rating_std_by_title.sort_values(ascending=False)[:10])

def add_prop(group):
    births = group.births
    group['prop'] = births/births.sum()
    return group

def analysis_child_name_data():
    # names1880 = pd.read_csv('../data/names/yob1880.txt',names=['name','sex','births'])
    # print(names1880)

    # births_sum_by_sex = names1880.groupby('sex').births.sum()
    # print(births_sum_by_sex)

    years = range(1880,2011)
    columns = ['name','sex','births']
    pieces = []
    for year in years:
        path = '../data/names/yob%d.txt' % year
        frame = pd.read_csv(path,names=columns)

        frame['year'] = year
        pieces.append(frame)

    # 按行将多个dataframe组合到一起,ignore_index忽略原始行号
    names = pd.concat(pieces,ignore_index=True)
    # print(names)

    # pivot_table:参数1,对该参数进行计算,index:行,columns:列,aggfunc:计算的函数
    total_births = names.pivot_table('births',index='year',columns='sex',aggfunc=sum)
    # print(total_births)

    total_births.plot(title='Total births by sex and year')

    names = names.groupby(['year','sex']).apply(add_prop)
    # print(names)

    print(np.allclose(names.groupby(['year','sex']).prop.sum(),1))

if __name__ == '__main__':
    # analysis_movie_data()

    analysis_child_name_data()

    pass