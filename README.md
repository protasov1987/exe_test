# exe_test

Небольшое окно на Python/Tkinter с кнопкой «Привет». После нажатия появляется надпись «Сам дурак» и рисуется простая смешная рожица на Canvas.

## Запуск

```bash
python app.py
```

## Сборка `.exe` для Windows

1. Установите зависимости (требуется установленный Python 3.9+):
   ```bash
   python -m pip install --upgrade pip
   python -m pip install pyinstaller
   ```
2. Соберите исполняемый файл:
   ```bash
   pyinstaller --noconfirm --onefile --windowed app.py
   ```
3. Готовый `app.exe` появится в папке `dist`.

> Tkinter входит в стандартную библиотеку Python, поэтому дополнительных пакетов, кроме PyInstaller для сборки, не требуется.
