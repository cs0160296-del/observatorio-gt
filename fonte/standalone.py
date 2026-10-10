# -*- coding: utf-8 -*-
"""Embrulha o index.html do Artifact num documento HTML completo, para alojamento
próprio (GitHub Pages ou qualquer servidor estático).

O runtime dos Artifacts injecta <!doctype>, <head> e um reset mínimo; um servidor
estático não injecta nada, pelo que isso tem de ir no ficheiro.
"""
import re, sys

SRC = "pagina.html"   # corpo da página, sem <head>
DST = sys.argv[1] if len(sys.argv) > 1 else "../index.html"
# Substituir pelo URL final depois de ativar o GitHub Pages.
URL = sys.argv[2] if len(sys.argv) > 2 else "https://EXEMPLO.github.io/observatorio-gt/"

body = open(SRC, encoding="utf-8").read()
title = re.search(r"<title>(.*?)</title>", body).group(1)
body = body.replace(f"<title>{title}</title>\n", "", 1)

DESC = ("Rastreador de todos os grupos de trabalho criados por despacho do Governo "
        "português desde 2 de abril de 2024: prazos, estado de execução e evidência, "
        "com ligação ao Diário da República.")

HEAD = f"""<!doctype html>
<html lang="pt-PT">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{DESC}">
<meta name="author" content="">
<link rel="canonical" href="{URL}">

<meta property="og:type" content="website">
<meta property="og:locale" content="pt_PT">
<meta property="og:site_name" content="{title}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{DESC}">
<meta property="og:url" content="{URL}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{DESC}">

<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>%F0%9F%8F%9B%EF%B8%8F</text></svg>">
<style>
  *{{box-sizing:border-box}}
  html{{color-scheme:light dark}}
  body{{margin:0}}
  img{{max-width:100%}}
  [hidden]{{display:none!important}}
</style>
</head>
<body>
"""

open(DST, "w", encoding="utf-8").write(HEAD + body + "\n</body>\n</html>\n")
print("escrito:", DST)
print("título :", title)
print("URL    :", URL, "(editar depois de ativar o Pages)")
