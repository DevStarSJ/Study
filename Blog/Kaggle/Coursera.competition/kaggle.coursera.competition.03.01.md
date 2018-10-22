---
title: Coursera Kaggle 강의(How to win a data science competition) week 3-1 Metrics 요약
date: 2018-10-22 11:04:00
categories:
- DataScience
tags:
- DataScience
- MachineLearning
- Kaggle
---

# Coursera Kaggle 강의(How to win a data science competition) week 3-1 Metrics 요약

## Metrics

어떤 metric을 사용하느냐에 따라 모델이 학습하는 방향이 다르다. 우리가 풀고자하는 문제에 최적화된 metric을 선택하는 것이 중요하다.

### 1. Regression metrics

#### 4.1 MSE, RMSE, R-squared

- **MSE** (Mean Square Error) : target과 predict의 차이값의 제곱의 평균
  - 최적의 Constant 값 : target mean

![](https://raw.githubusercontent.com/DevStarSJ/Study/master/Blog/Kaggle/Coursera.competition/image/coursera.competition.03.01.png)

![](https://raw.githubusercontent.com/DevStarSJ/Study/master/Blog/Kaggle/Coursera.competition/image/coursera.competition.03.02.png)

- **RMSE** (Root Mean Square Error): MSE에 root취한 값

![](https://raw.githubusercontent.com/DevStarSJ/Study/master/Blog/Kaggle/Coursera.competition/image/coursera.competition.03.03.png)

MSE의 최소값이 RMSE에서도 최소값이므로 최적화 결과가 같다. 그래서 비교적 구현이 간단한 MSE를 사용하는 경우가 많지만, **learning rate** 같은 몇몇의 hyperparameter 값에 따라 다르게 동작 할 수 있다.  
MSE와 RMSE 값이 32라고 성능이 좋은지 나쁜지 판단이 힘들다. 그래서 상대적인 값으로 평가가 필요할 수 있다.

- **R2** (R Squared)
  - `sklearn.metrics.r2_score`
  - P-Value와 같이 0 ~ 1 사이의 값을 나타내는데, MSE가 0 이면 R2는 1이며, MSE가 constant 모델보다 클 때 R2는 0이다.

![](https://raw.githubusercontent.com/DevStarSJ/Study/master/Blog/Kaggle/Coursera.competition/image/coursera.competition.03.04.png)

#### 4.2 MAE, RMAE

- **MAE** (Mean Absolute Error): target과 predict의 차이 절대값

  - 최적의 Constant 값 : target median

![](https://raw.githubusercontent.com/DevStarSJ/Study/master/Blog/Kaggle/Coursera.competition/image/coursera.competition.03.05.png)

- **RMAE** (Root Mean Absolute Error): MAE에 root취한 값

#### 4.3 MSE와 MAE의 차이
- MSE의 경우 차이가 2배이면 error가 4배가 되는데, MAE는 차이가 2배이면 error도 2배  
- MSE와 RMSE는 최적해를 찾기위해 gradient하게 접근시 각 지점마다 기울기(미분값)이 다르지만, MAE는 왼쪽은 -1, 오른쪽은 1이다.
- MAE는 outlier에 덜 민감하게 동작한다. (MSE는 제곱을 해서 크게 민감하다.)
- outlier가 없다고 확신이 드는 경우에는 MSE가 더 좋은 경우가 많다.

