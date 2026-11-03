# Site generator

Builds kaluach.com's app pages (/mac, /iKaluach, /win, /android: about, privacy and support,
in English and Hebrew) and 404.html.

- `content.py` holds the text; `build.py` turns it into pages.
- Run from the Kaluach-Website folder: `python3 _tools/site/build.py .`
- Rebuild into a copy first and compare it with the live pages before overwriting them.
- When you hand-edit a generated page, make the same change in `content.py`, or the next
  rebuild will undo it.

This folder isn't published: GitHub Pages skips folders whose names start with "_".

Moved here from the Kaluach Win source (Finnmark v74, tools/site) on 3 Nov 2026.
