import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

sprint_sheets = ['CW 2-3', 'CW 4-5', 'CW 6-7', 'CW 8-9']

data_jira = {
    'sprint_name': sprint_sheets,
    'commited_jira': [256, 222, 205, 231],
    'complited': [205, 170, 123, 177],
    'ad_hoc_sp': [21, 19, 52, 44],
    'ad_hoc_number': [10, 6, 15, 10]
}
# List1
Name = ['commited excel', 'commited Jira', 'complited', 'ad-hoc']


data = {
    'sprint_name': None,
    'commited_excel': [],
    'commited_jira': None,
    'complited': None,
    'ad_hoc_sp': None,
    'working_days': [],
    'planned_abs': [],
    'unplanned_abs': [],
    'capacity_before_sprint': [],
    'capacity_after_sprint': [],
    'ad_hoc_number': [],
    'target_capacity': [],
    'commited_jira_plus_ad_hoc_sp': []
}


def get_commited_excel(max=0):
    for value in df['Unnamed: 19'][:16]:
        try:
            assert (isinstance(value, int))
            if value > max:
                max = value
        except:
            continue
    return max


def working_days(sum=0):
    for value in df['Unnamed: 18'][:16]:
        try:
            assert (isinstance(value, int))
        except:
            continue
        sum += value
    return sum


# for i in range(1, 8):

def unplanned_abs(sum=0):
    for i in range(18, 27):
        unnamed = 'Unnamed: ' + str(i)
        for value in df[unnamed][19:33]:
            try:
                assert (value == 'UO')
            except:
                continue
            sum += 1
    return sum


def capacity_before_sprint(max=0):
    for value in df['Unnamed: 20'][:16]:
        try:
            assert (isinstance(value, int))
            if value > max:
                max = value
        except:
            continue
    return max
def add_two_keys(a,b):
    return a + b
df = pd.read_excel(r'C:\Users\matejko\Documents\A_wycieczka\Excel\PLANNING SHEET - Copy.xlsx', sheet_name='CW 8-9')
print('commited', df['Unnamed: 19'][:15])

print('unplanned', working_days())

for sprint_name in sprint_sheets:
    df = pd.read_excel(r'C:\Users\matejko\Documents\A_wycieczka\Excel\PLANNING SHEET - Copy.xlsx',
                       sheet_name=sprint_name)
    data['commited_excel'].append(get_commited_excel())
    data['working_days'].append(working_days())
    data['planned_abs'].append(get_commited_excel())
    data['unplanned_abs'].append(unplanned_abs())
    data['capacity_before_sprint'].append(capacity_before_sprint())
    data['capacity_after_sprint'].append(get_commited_excel())
    data['target_capacity'].append(df['Unnamed: 21'][1])
data['commited_jira'] = data_jira['commited_jira']
data['complited'] = data_jira['complited']
data['ad_hoc_sp'] = data_jira['ad_hoc_sp']
data['sprint_name'] = data_jira['sprint_name']
data['ad_hoc_number'] = data_jira['ad_hoc_number']


print(data['commited_jira_plus_ad_hoc_sp'])

new_df = pd.concat({k: pd.Series(v) for k, v in data.items()}, axis=1)
new_df['commited_jira_plus_ad_hoc_sp'] = new_df['ad_hoc_sp'] + new_df['commited_jira']

print('sprint x: ', new_df.loc[new_df['sprint_name'] == 'CW 8-9'])


new = new_df[['sprint_name', 'commited_excel', 'commited_jira', 'ad_hoc_sp']]

g = sns.catplot(x="sprint_name", y="commited_jira", data=new)



print('----------------------------------------------')
new_df.plot('sprint_name', y=['commited_excel', 'commited_jira', 'complited', 'ad_hoc_sp'])
new_df.plot.bar('sprint_name', y=['commited_excel', 'commited_jira', 'complited', 'ad_hoc_sp'])


new_df.plot.bar('sprint_name', y=['ad_hoc_sp', 'ad_hoc_sp'])
new_df.plot.bar('sprint_name', y=['commited_excel', 'commited_jira'])
new_df.plot.bar('sprint_name', y=['complited', 'capacity_before_sprint','commited_jira'])
new_df.plot.bar('sprint_name', y=['complited', 'commited_jira_plus_ad_hoc_sp','capacity_before_sprint'])

plt.show()

print(new_df)
print(data)




