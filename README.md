
Virtuális környezet létrehozása

**Ellenőrizzétek hogy CMD-ben vagytok-e, mert a PowerShell sok helyen tiltja a scriptek futtatását!**

```cmd
python -m venv .venv
```

Virtuális környezet aktiválása. A sor elején megjelenik hogy **(.venv)**
```cmd
.venv\Scripts\activate
```

Django telepítése (csak akkor ha ott van a zárójelben hogy .venv!)
```cmd
pip install -r requirements.txt
```

Django fejlesztői szerver elindítása
```cmd
python manage.py runserver
```