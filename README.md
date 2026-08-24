# Wytyczne SOiA

Publiczne repozytorium wytycznych dotyczących systemu ostrzegania i alarmowania (SOiA). Będą w nim publikowane materiały organizacyjne, techniczne i sprzętowe związane z systemem.

## Zawartość

1. **[Podręcznik SOiA](PODRECZNIK_v2.md)** — strona główna, sposób korzystania z dokumentu i spis treści.
2. **[Dwanaście załączników](zalaczniki/)** — każdy załącznik jest osobnym plikiem Markdown, dzięki czemu można go bezpośrednio otworzyć, zacytować i udostępnić.
3. **[Dokumentacja GitHub Pages](docs/)** — osobne strony załączników generowane z tych samych źródeł dla serwisu MkDocs.

Kolejne wytyczne techniczne i sprzętowe będą dodawane jako odrębne, jednoznacznie oznaczone dokumenty.

## Strona

[Otwórz Wytyczne SOiA w GitHub Pages](https://kgpsp.github.io/WYTYCZNE_SOIA/). Załączniki są dostępne w bocznej nawigacji, pogrupowane według siedmiu części podręcznika.

Pliki w `docs/` powstają deterministycznie po uruchomieniu:

```bash
python scripts/build_docs.py
```

Workflow GitHub Pages sprawdza testy generatora, zgodność wygenerowanych stron ze źródłami oraz ścisły build MkDocs.
