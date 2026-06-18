/* 허브 검색 — 외부 라이브러리 0.
   window.ISSUES_INDEX (index-data.js) 위에서 키워드 substring 매칭 + 날짜 정렬. */
(function () {
  var DATA = window.ISSUES_INDEX || [];
  var VERDICT_COLOR = {
    "사실": "#137A47", "대체로 사실": "#3F8F5E", "논쟁": "#B7860B",
    "대체로 거짓": "#CF6A2B", "거짓": "#B5392C"
  };

  var grid = document.getElementById("grid");
  var countEl = document.getElementById("count");
  var qEl = document.getElementById("q");
  var btnUpdated = document.getElementById("sort-updated");
  var btnOccurred = document.getElementById("sort-occurred");

  var state = { q: "", sort: "updated" };

  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  function spectrum(claims) {
    return (claims || []).map(function (c) {
      var col = VERDICT_COLOR[c.verdict] || "#9aa3b2";
      return '<i style="background:' + col + '" title="' + esc(c.verdict) + '"></i>';
    }).join("");
  }

  function card(e) {
    return '<a class="card" href="' + esc(e.url) + '">'
      + '<div class="meta">' + esc(e.date_updated) + ' · ' + esc(e.category || "-") + '</div>'
      + '<h2>' + esc(e.title) + '</h2>'
      + '<p>' + esc(e.summary) + '</p>'
      + '<div class="card-spectrum">' + spectrum(e.claims) + '</div>'
      + '</a>';
  }

  function render() {
    var q = state.q.trim().toLowerCase();
    var rows = DATA.filter(function (e) {
      return q === "" || (e.search_blob || "").indexOf(q) !== -1;
    });
    var key = state.sort === "occurred" ? "date_occurred" : "date_updated";
    rows.sort(function (a, b) { return (b[key] || "").localeCompare(a[key] || ""); });

    countEl.textContent = rows.length + " / " + DATA.length + " 건";
    grid.innerHTML = rows.length
      ? rows.map(card).join("")
      : '<p class="empty">검색 결과가 없습니다. 다른 키워드로 찾아보세요.</p>';
  }

  qEl.addEventListener("input", function () { state.q = qEl.value; render(); });
  btnUpdated.addEventListener("click", function () {
    state.sort = "updated"; btnUpdated.setAttribute("aria-pressed", "true");
    btnOccurred.setAttribute("aria-pressed", "false"); render();
  });
  btnOccurred.addEventListener("click", function () {
    state.sort = "occurred"; btnOccurred.setAttribute("aria-pressed", "true");
    btnUpdated.setAttribute("aria-pressed", "false"); render();
  });

  render();
})();
