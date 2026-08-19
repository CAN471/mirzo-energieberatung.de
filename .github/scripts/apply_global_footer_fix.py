from pathlib import Path
import re

PAGES = [
    Path("index.html"),
    Path("about/index.html"),
    Path("privacy-policy/index.html"),
    Path("terms-conditions/index.html"),
]

STYLE = r'''<style id="mirzo-global-footer-v2-css">
/* Shared MIRZO export fixes. */
.framer-1jsse1n-container,
[id="1jsse1n"] {
  display: none !important;
  visibility: hidden !important;
  pointer-events: none !important;
}

/* Same cleaned footer on every route. */
footer[data-framer-name="Footer"] form,
footer[data-framer-name="Footer"] [data-framer-name="Social"],
footer[data-framer-name="Footer"] [data-framer-name="About"],
footer[data-framer-name="Footer"] [data-framer-name="Bottom"] > [data-framer-name="Content"] > [data-framer-name="Right"] {
  display: none !important;
}

.lunavo-footer-brand {
  position: relative;
  isolation: isolate;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  min-height: 42px;
  padding: 6px 12px 6px 7px;
  border: 1px solid rgba(255,255,255,.09);
  border-radius: 999px;
  background: linear-gradient(180deg, rgba(255,255,255,.06) 0%, rgba(255,255,255,.025) 100%);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.07), 0 10px 32px rgba(0,0,0,.22);
  color: #fff;
  font-family: "DM Sans", "DM Sans Placeholder", sans-serif;
  text-decoration: none;
  overflow: hidden;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  transition: transform 220ms ease, border-color 220ms ease, box-shadow 220ms ease, background 220ms ease;
}
.lunavo-footer-brand::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  background: linear-gradient(105deg, transparent 30%, rgba(255,255,255,.12) 48%, transparent 66%);
  transform: translateX(-125%);
  transition: transform 650ms cubic-bezier(.2,.8,.2,1);
}
.lunavo-footer-brand:hover {
  transform: translateY(-2px);
  border-color: rgba(77,140,255,.34);
  background: linear-gradient(180deg, rgba(0,85,255,.11) 0%, rgba(255,255,255,.03) 100%);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.10), 0 12px 34px rgba(0,85,255,.16);
}
.lunavo-footer-brand:hover::before { transform: translateX(125%); }
.lunavo-footer-brand .lunavo-mark {
  position: relative;
  display: grid;
  place-items: center;
  width: 28px;
  height: 28px;
  flex: 0 0 28px;
  border: 1px solid rgba(255,255,255,.16);
  border-radius: 50%;
  background: radial-gradient(circle at 30% 22%, rgb(99,157,255) 0%, rgb(0,85,255) 52%, rgb(0,45,145) 100%);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.32), 0 0 20px rgba(0,85,255,.30);
  color: #fff;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: -.5px;
}
.lunavo-footer-brand .lunavo-mark::after {
  content: "";
  position: absolute;
  width: 5px;
  height: 5px;
  right: -1px;
  top: -1px;
  border: 2px solid rgb(8,8,8);
  border-radius: 50%;
  background: rgb(104,255,178);
  box-shadow: 0 0 9px rgba(104,255,178,.65);
}
.lunavo-footer-brand .lunavo-copy {
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 1px;
  min-width: 0;
}
.lunavo-footer-brand .lunavo-kicker {
  color: rgba(255,255,255,.38);
  font-size: 8px;
  line-height: 10px;
  font-weight: 600;
  letter-spacing: .95px;
  white-space: nowrap;
}
.lunavo-footer-brand .lunavo-name {
  color: rgba(255,255,255,.88);
  font-size: 11px;
  line-height: 14px;
  font-weight: 700;
  letter-spacing: .72px;
  white-space: nowrap;
  transition: color 220ms ease;
}
.lunavo-footer-brand .lunavo-arrow {
  color: rgba(255,255,255,.34);
  font-size: 13px;
  line-height: 1;
  transition: color 220ms ease, transform 220ms ease;
}
.lunavo-footer-brand:hover .lunavo-name { color: #fff; }
.lunavo-footer-brand:hover .lunavo-arrow {
  color: rgb(126,169,255);
  transform: translate(2px,-2px);
}
@media (max-width: 809.98px) {
  .lunavo-footer-brand { min-height: 38px; gap: 8px; padding: 5px 10px 5px 6px; }
  .lunavo-footer-brand .lunavo-mark { width: 25px; height: 25px; flex-basis: 25px; font-size: 11px; }
  .lunavo-footer-brand .lunavo-kicker { display: none; }
  .lunavo-footer-brand .lunavo-name { font-size: 10px; letter-spacing: .62px; }
}
</style>'''

SCRIPT = r'''<script id="mirzo-global-footer-v2-js">
(function () {
  var markup = '<span class="lunavo-mark" aria-hidden="true">L</span><span class="lunavo-copy"><span class="lunavo-kicker">DIGITAL EXPERIENCE BY</span><strong class="lunavo-name">LUNAVO MEDIA</strong></span><span class="lunavo-arrow" aria-hidden="true">↗</span>';

  function applyOverrides() {
    document.querySelectorAll('.framer-1jsse1n-container, [id="1jsse1n"]').forEach(function (preview) {
      preview.style.setProperty('display', 'none', 'important');
      preview.style.setProperty('visibility', 'hidden', 'important');
      preview.style.setProperty('pointer-events', 'none', 'important');
      preview.setAttribute('aria-hidden', 'true');
      preview.querySelectorAll('[tabindex]').forEach(function (el) { el.removeAttribute('tabindex'); });
    });

    document.querySelectorAll('footer[data-framer-name="Footer"] form, footer[data-framer-name="Footer"] [data-framer-name="Social"], footer[data-framer-name="Footer"] [data-framer-name="About"], footer[data-framer-name="Footer"] [data-framer-name="Bottom"] > [data-framer-name="Content"] > [data-framer-name="Right"]').forEach(function (el) {
      el.style.setProperty('display', 'none', 'important');
    });

    document.querySelectorAll('footer[data-framer-name="Footer"] [data-framer-name="Bottom"] [data-framer-name="Content"]').forEach(function (row) {
      if (row.querySelector('.lunavo-footer-brand')) return;
      var brand = document.createElement('a');
      brand.className = 'lunavo-footer-brand';
      brand.href = 'https://lunavo.media';
      brand.target = '_blank';
      brand.rel = 'noopener noreferrer';
      brand.setAttribute('aria-label', 'Digital experience by Lunavo Media');
      brand.innerHTML = markup;
      row.appendChild(brand);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', applyOverrides);
  } else {
    applyOverrides();
  }

  var root = document.getElementById('main') || document.body;
  var observer = new MutationObserver(applyOverrides);
  observer.observe(root, { childList: true, subtree: true });
  window.setTimeout(function () { applyOverrides(); observer.disconnect(); }, 20000);
})();
</script>'''


def strip_tag(text: str, tag: str, id_value: str) -> str:
    pattern = rf'<{tag}\s+id=["\']{re.escape(id_value)}["\'][^>]*>.*?</{tag}>'
    return re.sub(pattern, '', text, flags=re.S | re.I)


for page in PAGES:
    if not page.exists():
        raise SystemExit(f"Missing expected page: {page}")

    text = page.read_text(encoding="utf-8")

    for old_id in ("mirzo-preview-footer-overrides-css", "mirzo-global-footer-v2-css"):
        text = strip_tag(text, "style", old_id)
    for old_id in ("mirzo-preview-footer-overrides-js", "mirzo-global-footer-v2-js"):
        text = strip_tag(text, "script", old_id)

    if "</head>" not in text or "</body>" not in text:
        raise SystemExit(f"Unexpected HTML structure in {page}")

    text = text.replace("</head>", STYLE + "</head>", 1)
    text = text.replace("</body>", SCRIPT + "</body>", 1)
    page.write_text(text, encoding="utf-8")

    final = page.read_text(encoding="utf-8")
    assert final.count('id="mirzo-global-footer-v2-css"') == 1, page
    assert final.count('id="mirzo-global-footer-v2-js"') == 1, page

homepage = Path("index.html").read_text(encoding="utf-8")
if "framer-1jsse1n-container" not in homepage or 'id="1jsse1n"' not in homepage:
    raise SystemExit("Homepage preview marker not found")

print("Updated all four HTML pages")
