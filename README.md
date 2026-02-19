
Virtuális környezet létrehozása
```cmd
python -m venv myvenv
```

Virtuális környezet aktiválása. A sor elején megjelenik hogy **(myvenv)**
```cmd
myvenv\Scripts\activate
```

Django telepítése (csak akkor ha ott van a zárójelben hogy myvenv!)
```cmd
pip install django
```

Django fejlesztői szerver elindítása
```cmd
python manage.py runserver
```