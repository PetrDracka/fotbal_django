# ⚽ Fotbalové Statistiky & Síň slávy

Webová aplikace postavená na frameworku **Django (Python)**, která slouží k evidenci fotbalových střelců a prohlížení fotbalových legend.

## 🚀 Klíčové funkce
- **Dynamická tabulka střelců:** Možnost přidávat hráče přes formulář přímo do databáze.
- **Automatické řazení:** Hráči jsou v tabulce automaticky řazeni od nejvyššího počtu gólů po nejnižší.
- **Interaktivní Síň slávy:** JavaScriptová sekce, která po kliknutí na legendu (Messi, Ronaldo...) zobrazí jejich největší kariérní úspěchy.
- **Moderní UI:** Vzhled využívá moderní styl *Glassmorphism* (skleněný efekt) s tmavým pozadím a zlatými detaily.

## 🛠️ Použité technologie
- **Backend:** Python 3, Django Framework
- ** Relační databáze:** SQLite 3
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla JS)

## 📦 Jak projekt spustit lokálně
1. Aktivujte virtuální prostředí: `source venv/bin/activate`
2. Nainstalujte Django: `pip install django`
3. Spusťte vestavěný server: `python3 manage.py runserver`
4. Otevřete v prohlížeči adresu: `http://127.0.0.1:8000/`