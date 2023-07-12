# 💻 지도 경로 시각화 By Python 

### 1. routing visualization 패키지 다운로드

```shell
pip install mapsrouting==0.1.11
```

[최신 버전 (0.1.11)](https://pypi.org/project/mapsrouting/0.1.11/) (latest updated 23.07.12)

<br>

### 2. 파이썬 버전과 맞는 GDAL 패키지 다운로드
[GDAL 패키지 설치](https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal) 후 하단 명령어 터미널에 입력

```shell
pip install “상단 Gdal 다운 패키지 경로”
# pip install "C:\Users\...\GDAL-3.4.3-cp310-cp310-win_amd64.whl"
```

<br>

### 3. osrm 패키지 다운로드 및 파일 수정
1️⃣ **하단 명령어 터미널에 입력**

```shell
pip install osrm 
```

프로그램 실행시 오류 발생하여 다음 단계와 같이 주석 처리 진행 (프로그램 실행시 오류 발생)

<br>

2️⃣ **osrm/core.py 주석 처리**

```python
# from polyline.codec import PolylineCodec
```

<br>

3️⃣ **osrm/extra.py 주석 처리**

```python
# from matplotlib.mlab import griddata
```

<br> 

### 4. 패키지 사용
```python
from maps.visualR import visualize
```

다운로드한 패키지와 메서드에 적용할 csv 파일, 색상 변수를 바탕으로 메서드 실행

<br>

```python
# 예시
visualize('*.csv', color)
```

<br>

### 출력 화면
![image](https://github.com/Dongguk-MAPS/Routing-Visualization/assets/77263479/578d41be-48ca-446c-91af-62927c07f8f2)