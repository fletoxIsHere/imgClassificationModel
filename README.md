# imgClassificationModel

1.installer les dependances python pour le machine learning
pip install -r requirements.txt

2.generer le fichier my_model.h5 en executant tous les blocks de code dans le fichier Untitled.ipynb

3.lancer l'application flask par la commande:
python app.py

endpoint exposed:
POST:http://127.0.0.1:5000/predict :: payload = {"url":"<img link>"}

test de l'endpoint:
<br>
![image](https://github.com/fletoxIsHere/imgClassificationModel/assets/106785467/2c300fa7-aa32-4f4e-b7a3-d6ed84b14e2c)

