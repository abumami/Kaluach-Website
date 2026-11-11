function hebrewNumber(value) {
  let number = value % 1000;           // years without the thousands (תשפ״ז, not ה׳תשפ״ז)
  const letters = [
    [400, 'ת'], [300, 'ש'], [200, 'ר'], [100, 'ק'], [90, 'צ'], [80, 'פ'],
    [70, 'ע'], [60, 'ס'], [50, 'נ'], [40, 'מ'], [30, 'ל'], [20, 'כ'],
    [10, 'י'], [9, 'ט'], [8, 'ח'], [7, 'ז'], [6, 'ו'], [5, 'ה'],
    [4, 'ד'], [3, 'ג'], [2, 'ב'], [1, 'א'],
  ];
  let result = '';

  while (number > 0) {
    if (number === 15) { result += 'טו'; break; }
    if (number === 16) { result += 'טז'; break; }
    const pair = letters.find(([amount]) => amount <= number);
    if (!pair) break;
    result += pair[1];
    number -= pair[0];
  }

  return result.length === 1 ? `${result}׳` : `${result.slice(0, -1)}״${result.slice(-1)}`;
}

// Today's Hebrew date under the hero heading, e.g.
//   יום רביעי · כ׳ בחשוון תשפ״ז
//   Wednesday · 20 Heshvan 5787
function updateHebrewDate() {
  const now = new Date();
  const he = (options) => new Intl.DateTimeFormat('he-IL-u-ca-hebrew', options).format(now);
  const en = new Intl.DateTimeFormat('en-US-u-ca-hebrew', { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' })
    .formatToParts(now).reduce((parts, p) => { parts[p.type] = p.value; return parts; }, {});

  const heDate = document.querySelector('#hebrew-date-he');
  const enDate = document.querySelector('#hebrew-date-en');
  if (heDate) {
    heDate.textContent = `${he({ weekday: 'long' })} · ${hebrewNumber(Number(he({ day: 'numeric' })))} ב${he({ month: 'long' })} ${hebrewNumber(Number(he({ year: 'numeric' })))}`;
  }
  if (enDate) {
    enDate.textContent = `${en.weekday} · ${en.day} ${en.month} ${en.year}`;
  }
}

updateHebrewDate();
window.setInterval(updateHebrewDate, 60 * 60 * 1000);
