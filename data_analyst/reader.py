import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    'marketing_sample_for_naukri_com-jobs__20190701_20190830__30k_data.csv')


def rename_column_val(val=' 3 - 7 Years'):
    try:
        val = val.strip()
        val = val.split('-')[0].strip()
        return 'Exp > ' + val
    except Exception as e:
        return 'Exp > 0'


def preprocess_data():
    # 对 'Job Experience Required' 列进行 lambda 转换
    df['Job Experience Required'] = df['Job Experience Required'].apply(
        lambda x: rename_column_val(str(x)))
    plot_pie()


def plot_pie():
    # 根据 'Role Category' 进行分组并统计人数
    role_counts = df['Job Experience Required'].value_counts()

    # 绘制饼状图
    plt.figure(figsize=(8, 6))
    plt.pie(role_counts, labels=role_counts.index, autopct='%1.1f%%',
            startangle=140)
    plt.title('Job Experience Required')
    plt.axis('equal')  # 使饼图为圆形
    plt.show()


preprocess_data()
