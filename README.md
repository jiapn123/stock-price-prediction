# 주가 예측 프로젝트 [전체 PPT 보기](https://www.canva.com/design/DAF6GWctPqM/2rxSDv_N5awC5rho7NgYcQ/edit)

### 1. 수행 절차: 
1) DB 구축 -> 시세 조회 -> RNN 예측 
2) DBupdater.ipynb -> Analyzer.py -> RNN_stock.py
<img width="956" alt="Screenshot 2024-04-12 at 4 20 35 PM" src="https://github.com/jiapn123/stock-price-prediction/assets/155503641/5132ea5e-f627-467e-ba8f-559c7cba4f6a">

### 2.서비스 배포: Django
1) 가성 환경 생성
- conda create -n envDjango python=3.10
- conda env list
- conda activate 
- pip install requirements.txt
- cd Investar3
- python manage.py runserver localhost:8000
- http://localhost:8000/Django

2) 배포 결과 시연(삼성전자)
<img width="446" alt="Screenshot 2024-04-12 at 4 22 32 PM" src="https://github.com/jiapn123/stock-price-prediction/assets/155503641/ed160165-6ea6-4fd0-94f2-e20117a88940">
