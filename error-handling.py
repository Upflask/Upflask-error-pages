# Error handling
def error_page(error, code):
  return render_template('error.html', page=config["SITE_DATA"], error=error, code=code)

@app.errorhandler(404)
def page_not_found(e):
    return error_page(error="404 dude. Check the URL.<br>え、何探した？<br>Donde estas buscando?<br>404, ziom. Sprawdź link.<br>404 grabben. Kolla url.<br>404 junge. Überprüfe die url.<br>404 dude. Controleer de URL.<br>ﺦﻃﺃ 404 - ﺕﺄﻛﺩ ﻢﻧ ﺎﻟﺭﺎﺒﻃ ﻱﺍ ﻉﺰﻳﺰﻳ<br>404. Katso nettisivun osoite.", code=404), 404

@app.errorhandler(500)
def internal_error(e):
    return error_page(error="Even I don't know what happened<br>全然わからない<br>Que paso?<br>Nawet ja nie wiem o co chodzi<br>Inte ens jag har en anning om vad som hänt<br>Sogar ich weißt nicht was passiert ist<br>Zelfs ik heb geen idee wat er gebeurt is<br>ﺢﺗﻯ ﺄﻧﺍ ﻻ ﺄﻌﻠﻣ ﻡﺍ ﺎﻟﺬﻳ ﺡﺪﺛ<br>En edes minäkään tiedä mitä tapahtui", code=500), 500

@app.errorhandler(403)
def no_permission(e):
    return error_page(error="No no<br>ダメ<br>Que estas haciendo?<br>No chyba nie<br>Ajabaja<br>Nein nein<br>Nee nee<br>ﻊﻴﺑ ﻊﻠﻴﻛ!<br>Ei ei", code=403), 403

@app.errorhandler(413)
def too_big(e):
    return error_page(error="Did you even check the Terms dude?<br>馬鹿、用語をチェック<br>Usted incluso comprobar los terminos?<br>Najpierw przeczytaj regulamin, ok?<br>Kollade du ens användarvilkoren???<br>Hast du übehaupt die Nutzungsbedingungen gelesen?<br>Heb je de voorwaarden wel gelezen of niet?<br>ﻪﻟ ﻕﺭﺄﺗ ﺵﺭﻮﻃ ﺎﻟﺮﻔﻋ ﻱﺍ ﺮﺠﻟ؟<br>Katsoitko sidä edes ehdot?", code=413)
