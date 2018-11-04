---
title: Coursera Kaggle 강의(How to win a data science competition) week 3-2 Advanced Feature Engineering 요약
date: 2018-11-04 11:04:00
categories:
- DataScience
tags:
- DataScience
- MachineLearning
- Kaggle
---

# Coursera Kaggle 강의(How to win a data science competition) week 3-2 Advanced Feature Engineering 요약

## 1. Mean encodings

- Categorical feature로 **groupby**하여 `target의 mean` 값을 feature로 추가
  - mean뿐 아니라 median, std, min, max 등 해당 데이터의 성격을 잘 나타내는 통계 연산

ex)
![](https://raw.githubusercontent.com/DevStarSJ/Study/master/Blog/Kaggle/Coursera.competition/image/coursera.competition.03.15.png)

위 그림의 경우
- Moscow : 1 2개, 0 3개 -> 0.4
- Tver : 1 4개, 0 1개 -> 0.8
- Klin : 0 all -> 0.0

![](https://raw.githubusercontent.com/DevStarSJ/Study/master/Blog/Kaggle/Coursera.competition/image/coursera.competition.03.16.png)

Label encoding의 경우 단순히 순서에 의해 부여된 숫자일뿐 target과의 관련성이 전혀 없지만, `Mean encoding`의 경우 0 ~ 1 사이 값으로 target값과 연관성이 있이 있다. 특히 0인 것과 아닌 것은 완전히 구분이 된다.

![](https://raw.githubusercontent.com/DevStarSJ/Study/master/Blog/Kaggle/Coursera.competition/image/coursera.competition.03.17.png)

더 짧은 tree로도 더 좋은 성능을 발휘한다.

적용 방법들
- Likelihood : Goods / (Goods + Bads) = mean(target)
- Weight of Evidence = ln(Goods / Bads) * 100
- Count = Goods = sum(target)
- Diff = Goods - Bads

cf. Goods : 1의 개수, Bads : 0의 개수

tree 개수가 증가하면면서 정확도가 계속 증가한다면 아직 overfitting이 아니라는 뜻이다.
이럴 때 `mean encoding`을 적용하여 더 빨리 정확도를 올릴 수 있다.
하지만 overfitting은 항상 주의해야 한다.
왜냐면 train, validation의 비율이 다를 경우 overfitting된 상태라면 결과가 좋지 않다.

## 2. Regularization (정규화)

### 2.1 CV Loop regularization

- 매주 직관적이고 강력한(robust)한 방법

```python
y_tr = df_tr['target'].values
skf = StratifiedKFold(y_tr, 5, shuffle=True, random_state=123)

for tr_ind, val_ind in skf:
    X_tr, X_val = df_tr.iloc[tr_ind], df_tr.iloc[val_ind]
    for col in cols:
        means = X_val[col].map(X_tr.groupby(col).target.mean())
        X_val[col+'_mean_target'] = means
    train_new.iloc[val_ind] = X_val

prior = df_tr['target'].mean() # global mean
train_new.fillna(prior, inplace=True)
```
- Fold를 나누어서 validation set의 feature를 train set의 `mean encoding`으로 설정 (보통 4~5 정도면 충분)
  - NA값은 global mean으로 설정

단 LOO (Leave one out)같은 극단적인 경우는 주의

### 2.2 Smoothing

다른 regularization을 얼만큼 적용시킬지를 `Alpha`값을 이용하여 설정

$$ \frac{mean(target)*nrows + globalmean*alpha}{nrows + alpha} $$

### 2.3 Noise

통상적으로 노이즈를 추가하면 encoding의 품질이 저하되어서 얼마나 넣어야 할지 고민을 많이 해야 한다. LOO와 함께 사용하면 효과적이다. (자세한 설명이 없음)

### 2.4 Expanding mean

```python
cumsum = df_tr.groupby(col)['target'].cumsum() - df_tr['target']
cumcnt = df_tr.groupby(col).cumcount()
train_new[col+'_mean_target'] = cumsum/cumcnt
```
- CatBoost애는 내장된 방식
- Leakage를 줄일 수 있으나 품질이 불규칙적이다.

## 3. Generalizations and extensions

### 3.1 Regression과 Multiclass

- Regression : percentile, std, distribution bin등의 통계함수를 추가
- Multiclass : 각각의 class별로 encoding

### 3.2 Many-to-many relation

- Cross product
- Statistics from vectors

![](https://raw.githubusercontent.com/DevStarSJ/Study/master/Blog/Kaggle/Coursera.competition/image/coursera.competition.03.18.png)

APPS를 각각의 row로 나눔

### 3.3 Time series

time-series 데이터의 경우 앞의 방법들을 사용하는게 의미 없을 수 있다.

![](https://raw.githubusercontent.com/DevStarSJ/Study/master/Blog/Kaggle/Coursera.competition/image/coursera.competition.03.19.png)

위 예제의 경우 `Day-User-전날 Amount 합`과 `Day-Spend-전날 Amount 평균`을 feature로 추가하였다.

### 3.4 Interactions and numerical features

- numeric feature를 bin하여 categorical feature로 만드는 방법이다.
  - EDA 과정을 통해서 숫자상의 어떤 점에서 target값의 분기가 일어나는지를 관찰하는 것이 유용하다.
- feature 2개 이상이 상호작용적으로 동작하는 경우에는 그것들을 합하여 `mean encoding`하는 방법도 있다.


###  Correct validation reminder

- Local experiments:
  ‒ Estimate encodings on X_tr
  ‒ Map them to X_tr and X_val
  ‒ Regularize on X_tr
  ‒ Validate model on X_tr/ X_val split
- Submission:
  ‒ Estimate encodings on whole Train data
  ‒ Map them to Train and Test
  ‒ Regularize on Train
  ‒ Fit on Train

![](https://raw.githubusercontent.com/DevStarSJ/Study/master/Blog/Kaggle/Coursera.competition/image/coursera.competition.03.20.png)

- Main advantages:
  ‒ Compact transformation of categorical variables
  ‒ Powerful basis for feature engineering
- Disadvantages:
  ‒ Need careful validation, there a lot of ways to overfit
  ‒ Significant improvements only on specific datasets