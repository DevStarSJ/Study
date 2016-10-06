# macOS에 TensorFlow설치

### 1. Virtual Environment 설정

- 필요없는 경우 생략
- 아래 명령어는  Anaconda 상에서의 예제

```
conda create -n tensorflow scikit-learn
source activate tensorflow
```

### 2. Download wheel file

- 자신의 파이썬 버전에 맞는 `.whl` 파일을 다운로드
- 아래 예제는 0.6.0 버전 기준이므로 설치할 버전정보에 대한 wheel파일 정보를 확인해야 함

- Python2
```
curl https://storage.googleapis.com/tensorflow/mac/tensorflow-0.6.0-py2-none-any.whl --output tensorflow-0.6.0-py2-none-any.whl
```

- Python 3
```
curl https://storage.googleapis.com/tensorflow/mac/tensorflow-0.6.0-py3-none-any.whl --output tensorflow-0.6.0-py3-none-any.whl
```

### 3. Install

자신의 파이썬 버전에 맞는 `.whl` 파일을 이용해서 설치


```
pip install tensorflow-0.6.0-py3-none-any.whl
```

### 4. 제대로 설치되었는지 Test

```Python
import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

a = tf.constant(10)
b = tf.constant(32)
print(sess.run(a+b))
```

```
Hello, TensorFlow!
42
```
