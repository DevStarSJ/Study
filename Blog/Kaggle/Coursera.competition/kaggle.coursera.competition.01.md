---
title: Coursera Kaggle 강의(How to win a data science competition) week 1 요약
date: 2018-10-20 17:00:00
categories:
- DataScience
tags:
- DataScience
- MachineLearning
- Kaggle
---

# Coursera Kaggle 강의(How to win a data science competition) week 1 요약

참고로 Kaggle 대회에 대한 소개, HW/SW 이야기 등은 모두 생략하였으며, Machine Learning 모델 개발에 관련된 내용들만을 정리했음

## 02.Competition mechanics

### 03.Recap of main ML algorithms

#### 1. Linear Model
* 공간을 나누어서 구분
* ex) Logistic regression, SVM
  * ![](https://raw.githubusercontent.com/DevStarSJ/Study/master/Blog/Kaggle/Coursera.competition/image/coursera.competition.01.01.png)
* 하지만 원형으로 모여있는 경우에는 선형모델의 적용이 힘듬
    * ![](https://raw.githubusercontent.com/DevStarSJ/Study/master/Blog/Kaggle/Coursera.competition/image/coursera.competition.01.02.png)

#### 2. Tree-based Model
* Decision tree를 좀 더 복잡하게 구성하는 것이 기본 아이디어
* Divide-and-conquer 접근 방법
    * ![](https://raw.githubusercontent.com/DevStarSJ/Study/master/Blog/Kaggle/Coursera.competition/image/coursera.competition.01.03.png)
    * 먼저 선하나로 devide한 다음 위쪽은 더 이상 나눌필요가 없으니 아래쪽만 다시 devide
    * ![](https://raw.githubusercontent.com/DevStarSJ/Study/master/Blog/Kaggle/Coursera.competition/image/coursera.competition.01.04.png)
* 하지만 선형으로 쉽게 해결 되는 문제에 적용할 경우 훨씬 복잡해지며, 정확성도 더 떨어질 수 있음
    * ![](https://raw.githubusercontent.com/DevStarSJ/Study/master/Blog/Kaggle/Coursera.competition/image/coursera.competition.01.05.png)
* Random forest는 sklearn의 것이 가장 효과적이고, Gradient boosting은 XGBoost, LGBM이 좋음
* 대회에서 상위 랭킹자들이 많이 사용하는 알고리즘

#### 3. k-NN (k-Nearest Neighbors)
![](https://raw.githubusercontent.com/DevStarSJ/Study/master/Blog/Kaggle/Coursera.competition/image/coursera.competition.01.06.png)
* 가장 가까운 것을 따라가는 방식
* missing value를 채울때 유용
* sklearn의 kNN이 좋음. (custom distance funtion 지원)

#### 4. Neural Nets
* 이미지, 사운드, 텍스트 시퀀스에 적합
* TensorFlow, Keras, MXNet, PyTorch

