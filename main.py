from fastapi import FastAPI,Form, Response
import uvicorn

from reportlab.pdfgen.canvas import Canvas
from reportlab.graphics import renderPDF
from PyPDF2 import PdfFileReader


import qrcode
import qrcode.image.svg
from svglib.svglib import svg2rlg
import tempfile

import datetime
import time

def make_qr_code_drawing(data, size):
    qr = qrcode.QRCode(
        version=2,  # QR code version a.k.a size, None == automatic
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # lots of error correction
        box_size=size,  # size of each 'pixel' of the QR code
        border=4  # minimum size according to spec
        )
    qr.add_data(data)
    qrcode_svg = qr.make_image(image_factory=qrcode.image.svg.SvgPathFillImage)
    svg_file = tempfile.NamedTemporaryFile()
    qrcode_svg.save(svg_file)  # store as an SVG file
    svg_file.flush()
    qrcode_rl = svg2rlg(svg_file.name)  # load SVG file as reportlab graphics
    svg_file.close()
    return qrcode_rl

app = FastAPI()

@app.route("/")
@app.get("/")
async def root():
    return {"Attestion de deplacement"}



@app.get("/generate_certificate_acheq14/")
async def generate_pdf_certificate():
    canvas = Canvas("Attestation_deplacement.pdf")
    canvas.setFont("Times-Roman", 16)
    canvas.drawString(120, 800, "ATTESTATION DE DÉPLACEMENT DÉROGATOIRE")
    canvas.setFont("Times-Roman", 10)
    canvas.drawString(100,775,"En application de l'article 51 du décret n° 2020-1262 du 16 octobre 2020 prescrivant les mesures générales")
    canvas.drawString(125,765,"nécessaires pour faire face à l'épidémie de covid-19 dans le cadre de l'état d'urgence sanitaire")
    canvas.setFont("Times-Roman", 12)
    canvas.drawString(70,700,"Je soussigné(e),")
    canvas.drawString(70,675,"Mme/M. : acheq rhermini")
    canvas.drawString(70,650,"Né le : 07/02/1997")
    canvas.drawString(300,650,"à : Sefrou, Maroc")
    canvas.drawString(70,625,"Demerant : 172 rue Raymond Losserand, Paris, 75014")
    canvas.drawString(70,600,"certifie que mon déplacement est lié au motif suivant (cocher la case) autorisé en application des")
    canvas.drawString(70,585,"mesures générales nécessaires pour faire face à l'épidémie de Covid19 dans le cadre de l'état")
    canvas.drawString(70,570,"d'urgence sanitaire :")
    canvas.drawString(70,530,"[  ]  Déplacements entre le domicile et le lieu d'exercice de l'activité professionnelle ou le lieu")
    canvas.drawString(70,515,"       d'enseignement et de formation")
    canvas.drawString(70,475,"[  ]  Déplacements pour des consultations et soins ne pouvant être assurés à distance et ne")
    canvas.drawString(70,460,"       pouvant être différés ou pour l'achat de produits de santé")
    canvas.drawString(70,420,"[  ]  Déplacements pour motif familial impérieux, pour l'assistance aux personnes vulnérables")
    canvas.drawString(70,405,"       ou précaires ou pour la garde d'enfants")
    canvas.drawString(70,365,"[  ]  Déplacements des personnes en situation de handicap et de leur accompagnant")
    canvas.drawString(70,325,"[  ]  Déplacements pour répondre à une convocation judiciaire ou administrative")
    canvas.drawString(70,285,"[  ]  Déplacements pour participer à des missions d'intérêt général sur demande de l'autorité")
    canvas.drawString(70,270,"       administrative")
    canvas.drawString(70,230,"[  ]  Déplacements liés à des transits pour des déplacements de longues distances")
    canvas.drawString(70,190,"[ X ]  Déplacements brefs, dans un rayon maximal d'un kilomètre autour du domicile pour les")
    canvas.drawString(70,175,"       besoins des animaux de compagnie")
    canvas.drawString(70,135,"Fait à : Paris")
    #canvas.drawString(250,145,url)
    canvas.drawString(70,115,"Le : {} ".format(datetime.date.today()))
    time=str(datetime.datetime.now().time()).split(':')[0]+':'+str(datetime.datetime.now().time()).split(':')[1]
    canvas.drawString(300,115,"à : {} ".format(time))
    canvas.drawString(70,95,"Signature:")
    qrcode_rl = make_qr_code_drawing('https://www.gouvernement.fr/info-coronavirus', 10)
    renderPDF.draw(qrcode_rl,canvas, 400,30)

    canvas.save()
    with open("Attestation_deplacement.pdf", "rb") as f: 
        pdf= f.read() 
    reponse= Response(content=pdf, media_type="application/pdf") 
    return reponse
@app.get("/generate_certificate_acheq14_soins/")
async def generate_pdf_certificate():
    canvas = Canvas("Attestation_deplacement.pdf")
    canvas.setFont("Times-Roman", 16)
    canvas.drawString(120, 800, "ATTESTATION DE DÉPLACEMENT DÉROGATOIRE")
    canvas.setFont("Times-Roman", 10)
    canvas.drawString(100,775,"En application de l'article 51 du décret n° 2020-1262 du 16 octobre 2020 prescrivant les mesures générales")
    canvas.drawString(125,765,"nécessaires pour faire face à l'épidémie de covid-19 dans le cadre de l'état d'urgence sanitaire")
    canvas.setFont("Times-Roman", 12)
    canvas.drawString(70,700,"Je soussigné(e),")
    canvas.drawString(70,675,"Mme/M. : acheq rhermini")
    canvas.drawString(70,650,"Né le : 07/02/1997")
    canvas.drawString(300,650,"à : Sefrou, Maroc")
    canvas.drawString(70,625,"Demerant : 172 rue Raymond Losserand, Paris, 75014")
    canvas.drawString(70,600,"certifie que mon déplacement est lié au motif suivant (cocher la case) autorisé en application des")
    canvas.drawString(70,585,"mesures générales nécessaires pour faire face à l'épidémie de Covid19 dans le cadre de l'état")
    canvas.drawString(70,570,"d'urgence sanitaire :")
    canvas.drawString(70,530,"[  ]  Déplacements entre le domicile et le lieu d'exercice de l'activité professionnelle ou le lieu")
    canvas.drawString(70,515,"       d'enseignement et de formation")
    canvas.drawString(70,475,"[ X ]  Déplacements pour des consultations et soins ne pouvant être assurés à distance et ne")
    canvas.drawString(70,460,"       pouvant être différés ou pour l'achat de produits de santé")
    canvas.drawString(70,420,"[  ]  Déplacements pour motif familial impérieux, pour l'assistance aux personnes vulnérables")
    canvas.drawString(70,405,"       ou précaires ou pour la garde d'enfants")
    canvas.drawString(70,365,"[  ]  Déplacements des personnes en situation de handicap et de leur accompagnant")
    canvas.drawString(70,325,"[  ]  Déplacements pour répondre à une convocation judiciaire ou administrative")
    canvas.drawString(70,285,"[  ]  Déplacements pour participer à des missions d'intérêt général sur demande de l'autorité")
    canvas.drawString(70,270,"       administrative")
    canvas.drawString(70,230,"[  ]  Déplacements liés à des transits pour des déplacements de longues distances")
    canvas.drawString(70,190,"[  ]  Déplacements brefs, dans un rayon maximal d'un kilomètre autour du domicile pour les")
    canvas.drawString(70,175,"       besoins des animaux de compagnie")
    canvas.drawString(70,135,"Fait à : Paris")
    #canvas.drawString(250,145,url)
    canvas.drawString(70,115,"Le : {} ".format(datetime.date.today()))
    time=str(datetime.datetime.now().time()).split(':')[0]+':'+str(datetime.datetime.now().time()).split(':')[1]
    canvas.drawString(300,115,"à : {} ".format(time))
    canvas.drawString(70,95,"Signature:")
    qrcode_rl = make_qr_code_drawing('https://www.gouvernement.fr/info-coronavirus', 10)
    renderPDF.draw(qrcode_rl,canvas, 400,30)

    canvas.save()
    with open("Attestation_deplacement.pdf", "rb") as f: 
        pdf= f.read() 
    reponse= Response(content=pdf, media_type="application/pdf") 
    return reponse
@app.get("/generate_certificate_acheq95/")
async def generate_pdf_certificate():
    canvas = Canvas("Attestation_deplacement.pdf")
    canvas.setFont("Times-Roman", 16)
    canvas.drawString(120, 800, "ATTESTATION DE DÉPLACEMENT DÉROGATOIRE")
    canvas.setFont("Times-Roman", 10)
    canvas.drawString(100,775,"En application de l'article 51 du décret n° 2020-1262 du 16 octobre 2020 prescrivant les mesures générales")
    canvas.drawString(125,765,"nécessaires pour faire face à l'épidémie de covid-19 dans le cadre de l'état d'urgence sanitaire")
    canvas.setFont("Times-Roman", 12)
    canvas.drawString(70,700,"Je soussigné(e),")
    canvas.drawString(70,675,"Mme/M. : acheq rhermini")
    canvas.drawString(70,650,"Né le : 07/02/1997")
    canvas.drawString(300,650,"à : Sefrou, Maroc")
    canvas.drawString(70,625,"Demerant : 27 rue Emile Zola, Bezons, 95870")
    canvas.drawString(70,600,"certifie que mon déplacement est lié au motif suivant (cocher la case) autorisé en application des")
    canvas.drawString(70,585,"mesures générales nécessaires pour faire face à l'épidémie de Covid19 dans le cadre de l'état")
    canvas.drawString(70,570,"d'urgence sanitaire :")
    canvas.drawString(70,530,"[  ]  Déplacements entre le domicile et le lieu d'exercice de l'activité professionnelle ou le lieu")
    canvas.drawString(70,515,"       d'enseignement et de formation")
    canvas.drawString(70,475,"[  ]  Déplacements pour des consultations et soins ne pouvant être assurés à distance et ne")
    canvas.drawString(70,460,"       pouvant être différés ou pour l'achat de produits de santé")
    canvas.drawString(70,420,"[  ]  Déplacements pour motif familial impérieux, pour l'assistance aux personnes vulnérables")
    canvas.drawString(70,405,"       ou précaires ou pour la garde d'enfants")
    canvas.drawString(70,365,"[  ]  Déplacements des personnes en situation de handicap et de leur accompagnant")
    canvas.drawString(70,325,"[  ]  Déplacements pour répondre à une convocation judiciaire ou administrative")
    canvas.drawString(70,285,"[  ]  Déplacements pour participer à des missions d'intérêt général sur demande de l'autorité")
    canvas.drawString(70,270,"       administrative")
    canvas.drawString(70,230,"[  ]  Déplacements liés à des transits pour des déplacements de longues distances")
    canvas.drawString(70,190,"[ X ]  Déplacements brefs, dans un rayon maximal d'un kilomètre autour du domicile pour les")
    canvas.drawString(70,175,"       besoins des animaux de compagnie")
    canvas.drawString(70,135,"Fait à : Bezons")
    #canvas.drawString(250,145,url)
    canvas.drawString(70,115,"Le : {} ".format(datetime.date.today()))
    time=str(datetime.datetime.now().time()).split(':')[0]+':'+str(datetime.datetime.now().time()).split(':')[1]
    canvas.drawString(300,115,"à : {} ".format(time))
    canvas.drawString(70,95,"Signature:")
    qrcode_rl = make_qr_code_drawing('https://www.gouvernement.fr/info-coronavirus', 10)
    renderPDF.draw(qrcode_rl,canvas, 400,30)

    canvas.save()
    with open("Attestation_deplacement.pdf", "rb") as f: 
        pdf= f.read() 
    reponse= Response(content=pdf, media_type="application/pdf") 
    return reponse
@app.get("/generate_certificate_mehdi/")
async def generate_pdf_certificate():
    canvas = Canvas("Attestation_deplacement.pdf")
    canvas.setFont("Times-Roman", 16)
    canvas.drawString(120, 800, "ATTESTATION DE DÉPLACEMENT DÉROGATOIRE")
    canvas.setFont("Times-Roman", 10)
    canvas.drawString(100,775,"En application de l'article 51 du décret n° 2020-1262 du 16 octobre 2020 prescrivant les mesures générales")
    canvas.drawString(125,765,"nécessaires pour faire face à l'épidémie de covid-19 dans le cadre de l'état d'urgence sanitaire")
    canvas.setFont("Times-Roman", 12)
    canvas.drawString(70,700,"Je soussigné(e),")
    canvas.drawString(70,675,"Mme/M. : mehdi diouri")
    canvas.drawString(70,650,"Né le : 11/11/1996")
    canvas.drawString(300,650,"à : Fès, Maroc")
    canvas.drawString(70,625,"Demerant : 12 rue des Frères Caudron, Vélizy-Villacoublay, 78140")
    canvas.drawString(70,600,"certifie que mon déplacement est lié au motif suivant (cocher la case) autorisé en application des")
    canvas.drawString(70,585,"mesures générales nécessaires pour faire face à l'épidémie de Covid19 dans le cadre de l'état")
    canvas.drawString(70,570,"d'urgence sanitaire :")
    canvas.drawString(70,530,"[  ]  Déplacements entre le domicile et le lieu d'exercice de l'activité professionnelle ou le lieu")
    canvas.drawString(70,515,"       d'enseignement et de formation")
    canvas.drawString(70,475,"[  ]  Déplacements pour des consultations et soins ne pouvant être assurés à distance et ne")
    canvas.drawString(70,460,"       pouvant être différés ou pour l'achat de produits de santé")
    canvas.drawString(70,420,"[  ]  Déplacements pour motif familial impérieux, pour l'assistance aux personnes vulnérables")
    canvas.drawString(70,405,"       ou précaires ou pour la garde d'enfants")
    canvas.drawString(70,365,"[  ]  Déplacements des personnes en situation de handicap et de leur accompagnant")
    canvas.drawString(70,325,"[  ]  Déplacements pour répondre à une convocation judiciaire ou administrative")
    canvas.drawString(70,285,"[  ]  Déplacements pour participer à des missions d'intérêt général sur demande de l'autorité")
    canvas.drawString(70,270,"       administrative")
    canvas.drawString(70,230,"[  ]  Déplacements liés à des transits pour des déplacements de longues distances")
    canvas.drawString(70,190,"[ X ]  Déplacements brefs, dans un rayon maximal d'un kilomètre autour du domicile pour les")
    canvas.drawString(70,175,"       besoins des animaux de compagnie")
    canvas.drawString(70,135,"Fait à : Paris")
    #canvas.drawString(250,145,url)
    canvas.drawString(70,115,"Le : {} ".format(datetime.date.today()))
    time=str(datetime.datetime.now().time()).split(':')[0]+':'+str(datetime.datetime.now().time()).split(':')[1]
    canvas.drawString(300,115,"à : {} ".format(time))
    canvas.drawString(70,95,"Signature:")
    qrcode_rl = make_qr_code_drawing('https://www.gouvernement.fr/info-coronavirus', 10)
    renderPDF.draw(qrcode_rl,canvas, 400,30)

    canvas.save()
    with open("Attestation_deplacement.pdf", "rb") as f: 
        pdf= f.read() 
    reponse= Response(content=pdf, media_type="application/pdf") 
    return reponse
@app.get("/generate_certificate_ahmed/")
async def generate_pdf_certificate():
    canvas = Canvas("Attestation_deplacement.pdf")
    canvas.setFont("Times-Roman", 16)
    canvas.drawString(120, 800, "ATTESTATION DE DÉPLACEMENT DÉROGATOIRE")
    canvas.setFont("Times-Roman", 10)
    canvas.drawString(100,775,"En application de l'article 51 du décret n° 2020-1262 du 16 octobre 2020 prescrivant les mesures générales")
    canvas.drawString(125,765,"nécessaires pour faire face à l'épidémie de covid-19 dans le cadre de l'état d'urgence sanitaire")
    canvas.setFont("Times-Roman", 12)
    canvas.drawString(70,700,"Je soussigné(e),")
    canvas.drawString(70,675,"Mme/M. : ahmed Tazi")
    canvas.drawString(70,650,"Né le : 26/11/1996")
    canvas.drawString(300,650,"à : Fès, Maroc")
    canvas.drawString(70,625,"Demerant : 16 rue André Blanc Lapierre, Gif-sur-Yvette, 91190")
    canvas.drawString(70,600,"certifie que mon déplacement est lié au motif suivant (cocher la case) autorisé en application des")
    canvas.drawString(70,585,"mesures générales nécessaires pour faire face à l'épidémie de Covid19 dans le cadre de l'état")
    canvas.drawString(70,570,"d'urgence sanitaire :")
    canvas.drawString(70,530,"[  ]  Déplacements entre le domicile et le lieu d'exercice de l'activité professionnelle ou le lieu")
    canvas.drawString(70,515,"       d'enseignement et de formation")
    canvas.drawString(70,475,"[  ]  Déplacements pour des consultations et soins ne pouvant être assurés à distance et ne")
    canvas.drawString(70,460,"       pouvant être différés ou pour l'achat de produits de santé")
    canvas.drawString(70,420,"[  ]  Déplacements pour motif familial impérieux, pour l'assistance aux personnes vulnérables")
    canvas.drawString(70,405,"       ou précaires ou pour la garde d'enfants")
    canvas.drawString(70,365,"[  ]  Déplacements des personnes en situation de handicap et de leur accompagnant")
    canvas.drawString(70,325,"[  ]  Déplacements pour répondre à une convocation judiciaire ou administrative")
    canvas.drawString(70,285,"[  ]  Déplacements pour participer à des missions d'intérêt général sur demande de l'autorité")
    canvas.drawString(70,270,"       administrative")
    canvas.drawString(70,230,"[  ]  Déplacements liés à des transits pour des déplacements de longues distances")
    canvas.drawString(70,190,"[ X ]  Déplacements brefs, dans un rayon maximal d'un kilomètre autour du domicile pour les")
    canvas.drawString(70,175,"       besoins des animaux de compagnie")
    canvas.drawString(70,135,"Fait à : Gif-sur-Yvette")
    #canvas.drawString(250,145,url)
    canvas.drawString(70,115,"Le : {} ".format(datetime.date.today()))
    time=str(datetime.datetime.now().time()).split(':')[0]+':'+str(datetime.datetime.now().time(timezone.utc)).split(':')[1]
    canvas.drawString(300,115,"à : {} ".format(time))
    canvas.drawString(70,95,"Signature:")
    qrcode_rl = make_qr_code_drawing('https://www.gouvernement.fr/info-coronavirus', 10)
    renderPDF.draw(qrcode_rl,canvas, 400,30)

    canvas.save()
    with open("Attestation_deplacement.pdf", "rb") as f: 
        pdf= f.read() 
    reponse= Response(content=pdf, media_type="application/pdf") 
    return reponse



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info")