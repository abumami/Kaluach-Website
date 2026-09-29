function hebrewNumber(value) {
  const thousands = value >= 5000 ? 'ה׳' : '';
  let number = value >= 5000 ? value % 1000 : value;
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

  const formatted = result.length === 1
    ? `${result}׳`
    : `${result.slice(0, -1)}״${result.slice(-1)}`;
  return `${thousands}${formatted}`;
}

function updateHebrewDate() {
  const now = new Date();
  const locale = 'he-IL-u-ca-hebrew';
  const format = (options) => new Intl.DateTimeFormat(locale, options).format(now);

  document.querySelector('#hebrew-day').textContent = hebrewNumber(Number(format({ day: 'numeric' })));
  document.querySelector('#hebrew-month').textContent = format({ month: 'long' });
  document.querySelector('#hebrew-weekday').textContent = format({ weekday: 'long' });
  document.querySelector('#hebrew-year').textContent = hebrewNumber(Number(format({ year: 'numeric' })));
  document.querySelector('#english-hebrew-date').textContent = new Intl.DateTimeFormat('en-US-u-ca-hebrew', {
    day: 'numeric', month: 'long', weekday: 'long', year: 'numeric',
  }).format(now);
}

updateHebrewDate();
window.setInterval(updateHebrewDate, 60 * 60 * 1000);
