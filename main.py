import requests

"""
Constraints:
1. 0 < surah < 144
2. 0 < aya < ...

For the surah that is being accessed,
we need to know the upper bound on the aya 
so that this is not exceeded
"""
surah = 2
verse = 1
print(getText(surah,verse))


api = f'https://quranenc.com/api/v1/translation/aya/english_saheeh/{surah}/{verse}'

quranenc = requests.get(api)
quranenc_json = ''

if quranenc.status_code == 200:
  quranenc_json = quranenc.json()



'''
Return: The specified surah verse
Constraints: 1 <= surah <= 114 && 
'''
def getText(surah: int, verse: int) -> str:
  text = ''
  if verseInBounds(surah, verse):
      text = surahJson["result"][verse]["arabic_text"]
  return text

def verseInBounds(surah: int, verse: int) -> bool:
  if (1 <= surah and surah <= 114):
    surahJson = quranenc.json()
    surahVerseLimit = surahJson["result"]
    if (1 <= verse and verse <= surahVerseLimit):
      return True
  else:
    return False





   